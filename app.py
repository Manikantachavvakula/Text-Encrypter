from flask import Flask, render_template, request, jsonify
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import base64, hashlib, secrets, string
from collections import deque
import time
import os

app = Flask(__name__)

class CryptoEngine:
    def __init__(self):
        self.history = deque(maxlen=10)
    
    def caesar_cipher(self, text, shift=3, decrypt=False):
        if decrypt: 
            shift = -shift
        result = ""
        for char in text:
            if char.isalpha():
                base = 65 if char.isupper() else 97
                result += chr((ord(char) - base + shift) % 26 + base)
            else:
                result += char
        self._add_history('Caesar', len(text))
        return result
    
    def fernet_encrypt(self, text, password="defaultpass"):
        try:
            key = self._gen_key(password)
            f = Fernet(key)
            encrypted = f.encrypt(text.encode())
            result = base64.urlsafe_b64encode(encrypted).decode()
            self._add_history('AES', len(text))
            return result
        except Exception as e:
            return f"Error: {str(e)}"
    
    def fernet_decrypt(self, encrypted_text, password="defaultpass"):
        try:
            key = self._gen_key(password)
            f = Fernet(key)
            encrypted_data = base64.urlsafe_b64decode(encrypted_text.encode())
            decrypted = f.decrypt(encrypted_data)
            return decrypted.decode()
        except:
            return "Wrong password entered"
    
    def hash_encrypt(self, text):
        result = hashlib.sha256(text.encode()).hexdigest()
        self._add_history('Hash', len(text))
        return result
    
    def generate_key(self, length=16):
        chars = string.ascii_letters + string.digits + "!@#$%^&*"
        return ''.join(secrets.choice(chars) for _ in range(length))
    
    def get_stats(self):
        if not self.history:
            return {"message": "No encryption history available"}
        
        methods = {}
        total_chars = 0
        
        for entry in self.history:
            method = entry['method']
            methods[method] = methods.get(method, 0) + 1
            total_chars += entry['length']
        
        return {
            'total': len(self.history),
            'methods': methods,
            'chars': total_chars,
            'avg': round(total_chars / len(self.history), 1)
        }
    
    def _gen_key(self, password):
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(), 
            length=32, 
            salt=b'salt123', 
            iterations=100000
        )
        return base64.urlsafe_b64encode(kdf.derive(password.encode()))
    
    def _add_history(self, method, length):
        self.history.append({
            'method': method, 
            'length': length, 
            'time': time.time()
        })

# Initialize crypto engine
crypto = CryptoEngine()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    data = request.json
    text = data.get('text', '').strip()
    method = data.get('method', 'caesar')
    password = data.get('password', 'defaultpass')
    action = data.get('action', 'encrypt')
    
    if not text:
        return jsonify({'error': 'Please enter some text to process'})
    
    try:
        if action == 'encrypt':
            if method == 'caesar':
                result = crypto.caesar_cipher(text)
            elif method == 'fernet':
                result = crypto.fernet_encrypt(text, password)
            elif method == 'hash':
                result = crypto.hash_encrypt(text)
            else:
                return jsonify({'error': 'Invalid encryption method'})
        else:  # decrypt
            if method == 'caesar':
                result = crypto.caesar_cipher(text, decrypt=True)
            elif method == 'fernet':
                result = crypto.fernet_decrypt(text, password)
            else:
                return jsonify({'error': 'Hash values cannot be decrypted'})
        
        return jsonify({
            'result': result,
            'method': method,
            'action': action,
            'length': len(result)
        })
        
    except Exception as e:
        return jsonify({'error': f'Processing failed: {str(e)}'})

@app.route('/generate-key')
def generate_key():
    try:
        key = crypto.generate_key()
        return jsonify({'key': key})
    except Exception as e:
        return jsonify({'error': f'Key generation failed: {str(e)}'})

@app.route('/stats')
def stats():
    try:
        return jsonify(crypto.get_stats())
    except Exception as e:
        return jsonify({'error': f'Stats unavailable: {str(e)}'})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=False, host='0.0.0.0', port=port)