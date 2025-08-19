# 🔐 Python Text Encrypter

A modern, responsive web application that demonstrates **Data Structures & Algorithms (DSA)** concepts through practical cryptography implementation. Built with Flask backend and modern responsive frontend.

## ✨ Features

### 🔒 Encryption Methods
- **Caesar Cipher** - Educational shift-based encryption
- **AES Fernet** - Industry-standard symmetric encryption
- **SHA-256 Hash** - One-way cryptographic hashing

### 📱 Responsive Design
- **Mobile-First** - Optimized for all screen sizes
- **Modern UI** - Animated gradient borders and smooth transitions
- **Touch-Friendly** - Large buttons and intuitive gestures
- **Dark Theme** - Easy on the eyes with purple accent colors

### 📊 DSA Demonstrations
- **Stack Operations** - LIFO encryption history
- **Queue Processing** - FIFO request handling
- **Hash Tables** - O(1) algorithm lookup
- **Time Complexity** - Real-time performance analysis
- **Search & Sort** - Algorithm comparison demos

## 🚀 Quick Start

### Option 1: Automated Setup
```bash
git clone <your-repo-url>
cd text-encrypter
python setup.py
```

### Option 2: Manual Setup
```bash
# Install dependencies
pip install -r requirements.txt

# Run application
python app.py

# Visit in browser
http://localhost:5000
```

## 📱 Mobile Optimization

The application is fully responsive and optimized for:
- **Mobile Phones** (320px - 768px)
- **Tablets** (768px - 1024px) 
- **Desktop** (1024px+)

Key mobile features:
- Touch-optimized buttons
- Responsive typography using `clamp()`
- Flexible layouts with CSS Grid/Flexbox
- Optimized animations and transitions

## 🛠️ Technology Stack

| Component | Technology | Purpose |
|-----------|------------|---------|
| **Backend** | Flask | Web framework & API |
| **Frontend** | HTML5/CSS3/JS | Responsive interface |
| **Crypto** | Cryptography library | Secure encryption |
| **Testing** | Selenium | Automated UI tests |
| **Deployment** | Gunicorn | Production server |

## 📁 Project Structure

```
text-encrypter/
├── app.py                 # Flask application
├── requirements.txt       # Dependencies
├── setup.py              # Automated setup
├── test.py               # Test suite
├── DSA_concepts.py       # Educational demos
├── Procfile              # Deployment config
├── templates/
│   └── index.html        # Main interface
└── static/
    └── style.css         # Responsive styles
```

## 🧪 Testing

Run automated tests:
```bash
python test.py
```

Test coverage includes:
- ✅ Caesar cipher encryption/decryption
- ✅ AES Fernet encryption
- ✅ SHA-256 hashing
- ✅ Key generation
- ✅ Statistics tracking
- ✅ UI responsiveness

## 📈 Algorithm Complexity

| Algorithm | Time | Space | Use Case |
|-----------|------|-------|----------|
| Caesar Cipher | O(n) | O(1) | Education |
| AES Fernet | O(n) | O(1) | Security |
| SHA-256 | O(n) | O(1) | Integrity |
| Hash Lookup | O(1) | O(n) | Performance |

## 🎨 Responsive Design Features

### CSS Techniques Used:
- **CSS Grid & Flexbox** for flexible layouts
- **clamp()** for responsive typography
- **CSS Custom Properties** for theming
- **Container Queries** for component responsiveness
- **CSS Animation** with `@keyframes`
- **Media Queries** for breakpoint optimization

### Mobile Optimizations:
- **Touch targets** minimum 44px
- **Readable fonts** with proper contrast
- **Fast loading** with optimized assets
- **Offline support** capabilities
- **PWA ready** structure

## 🌐 Deployment Options

### Heroku
```bash
# Create app
heroku create your-app-name

# Deploy
git push heroku main
```

### Railway
```bash
# Connect GitHub repo
# Auto-deploy on push
```

### Local Development
```bash
# Development server
python app.py

# Production server
gunicorn app:app
```

## 🔐 Security Features

- **PBKDF2** key derivation (100,000 iterations)
- **Fernet encryption** (AES-128 + authentication)
- **Secure random** key generation
- **Input validation** and sanitization
- **CSRF protection** ready
- **XSS prevention** with proper escaping

## 📚 Educational Value

This project demonstrates:

1. **Web Development**
   - Flask framework usage
   - RESTful API design
   - Frontend/backend communication

2. **Cryptography**
   - Symmetric encryption
   - Hash functions
   - Key derivation

3. **Data Structures**
   - Stack (LIFO) operations
   - Queue (FIFO) processing
   - Hash table lookups

4. **Responsive Design**
   - Mobile-first approach
   - CSS Grid/Flexbox
   - Modern web standards

5. **Software Testing**
   - Automated UI testing
   - Test-driven development

## 🎯 Learning Outcomes

Students will learn:
- Modern web development practices
- Cryptographic principles and implementation
- Data structure applications in real projects
- Responsive design techniques
- Testing and deployment strategies
- Software engineering best practices

## 👨‍💻 Author

**Manikanta Chavvakula**
- 💼 [LinkedIn](https://www.linkedin.com/in/manikanta-chavvakula-43b308189)
- 📱 [Instagram](https://instagram.com/___iam_mk___)
- 📘 [Facebook](https://www.facebook.com/manikanta.rockzzz.5)

## 📄 License

MIT License - feel free to use for educational purposes

## 🤝 Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📞 Support

For issues or questions:
- 🐛 Open an issue on GitHub
- 📧 Contact via LinkedIn
- 💬 Join the discussion

---

⭐ **Star this repository if you found it helpful!**

Made with ❤️ for educational purposes