"""
Automated Test Suite for Python Text Encrypter
Selenium-based UI testing for encryption functionality
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import sys

class EncrypterTests:
    def __init__(self):
        self.driver = None
        self.base_url = "http://localhost:5000"
        self.test_results = []
    
    def setup_driver(self):
        """Initialize Chrome WebDriver with options"""
        print("🌐 Setting up browser...")
        
        try:
            chrome_options = Options()
            chrome_options.add_argument("--headless")  # Run in background
            chrome_options.add_argument("--no-sandbox")
            chrome_options.add_argument("--disable-dev-shm-usage")
            
            self.driver = webdriver.Chrome(options=chrome_options)
            self.driver.implicitly_wait(10)
            print("✅ Browser setup complete")
            return True
            
        except Exception as e:
            print(f"❌ Browser setup failed: {e}")
            print("   Make sure Chrome and ChromeDriver are installed")
            return False
    
    def navigate_to_app(self):
        """Navigate to the application"""
        print(f"🔗 Navigating to {self.base_url}...")
        
        try:
            self.driver.get(self.base_url)
            
            # Wait for page to load
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "inputText"))
            )
            
            title = self.driver.title
            print(f"✅ Page loaded: {title}")
            return True
            
        except Exception as e:
            print(f"❌ Navigation failed: {e}")
            print("   Make sure the Flask app is running on localhost:5000")
            return False
    
    def test_caesar_encryption(self):
        """Test Caesar cipher encryption and decryption"""
        print("\n🔒 Testing Caesar cipher...")
        
        try:
            # Clear any existing content
            input_field = self.driver.find_element(By.ID, "inputText")
            input_field.clear()
            
            # Enter test text
            test_text = "Hello World Test!"
            input_field.send_keys(test_text)
            
            # Select Caesar cipher
            method_select = Select(self.driver.find_element(By.ID, "method"))
            method_select.select_by_value("caesar")
            
            # Click encrypt button
            encrypt_btn = self.driver.find_element(By.ID, "processBtn")
            encrypt_btn.click()
            
            # Wait for result
            time.sleep(2)
            
            # Get encrypted result
            result_field = self.driver.find_element(By.ID, "result")
            encrypted_text = result_field.get_attribute("value")
            
            if encrypted_text and encrypted_text != test_text:
                print(f"✅ Encryption successful: {encrypted_text}")
                
                # Test decryption
                return self.test_caesar_decryption(encrypted_text, test_text)
            else:
                print("❌ Encryption failed - no result")
                return False
                
        except Exception as e:
            print(f"❌ Caesar encryption test failed: {e}")
            return False
    
    def test_caesar_decryption(self, encrypted_text, original_text):
        """Test Caesar cipher decryption"""
        try:
            # Switch to decrypt mode
            decrypt_btn = self.driver.find_element(
                By.XPATH, "//button[contains(text(), 'Decrypt')]"
            )
            decrypt_btn.click()
            time.sleep(1)
            
            # Clear input and enter encrypted text
            input_field = self.driver.find_element(By.ID, "inputText")
            input_field.clear()
            input_field.send_keys(encrypted_text)
            
            # Click decrypt button
            process_btn = self.driver.find_element(By.ID, "processBtn")
            process_btn.click()
            time.sleep(2)
            
            # Check decrypted result
            result_field = self.driver.find_element(By.ID, "result")
            decrypted_text = result_field.get_attribute("value")
            
            if decrypted_text == original_text:
                print(f"✅ Decryption successful: {decrypted_text}")
                return True
            else:
                print(f"❌ Decryption failed: expected '{original_text}', got '{decrypted_text}'")
                return False
                
        except Exception as e:
            print(f"❌ Caesar decryption test failed: {e}")
            return False
    
    def test_fernet_encryption(self):
        """Test AES Fernet encryption"""
        print("\n🔐 Testing AES Fernet encryption...")
        
        try:
            # Switch back to encrypt mode
            encrypt_btn = self.driver.find_element(
                By.XPATH, "//button[contains(text(), 'Encrypt')]"
            )
            encrypt_btn.click()
            time.sleep(1)
            
            # Clear input
            input_field = self.driver.find_element(By.ID, "inputText")
            input_field.clear()
            
            # Enter test text
            test_text = "Secret Message 123!"
            input_field.send_keys(test_text)
            
            # Select Fernet method
            method_select = Select(self.driver.find_element(By.ID, "method"))
            method_select.select_by_value("fernet")
            time.sleep(1)
            
            # Enter password
            password_field = self.driver.find_element(By.ID, "password")
            password_field.clear()
            password_field.send_keys("testpassword123")
            
            # Click encrypt
            process_btn = self.driver.find_element(By.ID, "processBtn")
            process_btn.click()
            time.sleep(2)
            
            # Check result
            result_field = self.driver.find_element(By.ID, "result")
            encrypted_text = result_field.get_attribute("value")
            
            if encrypted_text and encrypted_text != test_text and "Error" not in encrypted_text:
                print(f"✅ Fernet encryption successful (length: {len(encrypted_text)})")
                return True
            else:
                print(f"❌ Fernet encryption failed: {encrypted_text}")
                return False
                
        except Exception as e:
            print(f"❌ Fernet encryption test failed: {e}")
            return False
    
    def test_hash_function(self):
        """Test SHA-256 hash function"""
        print("\n🗝️ Testing SHA-256 hash...")
        
        try:
            # Clear input
            input_field = self.driver.find_element(By.ID, "inputText")
            input_field.clear()
            
            # Enter test text
            test_text = "Hash Me Please!"
            input_field.send_keys(test_text)
            
            # Select hash method
            method_select = Select(self.driver.find_element(By.ID, "method"))
            method_select.select_by_value("hash")
            time.sleep(1)
            
            # Click process
            process_btn = self.driver.find_element(By.ID, "processBtn")
            process_btn.click()
            time.sleep(2)
            
            # Check result
            result_field = self.driver.find_element(By.ID, "result")
            hash_result = result_field.get_attribute("value")
            
            # SHA-256 should produce 64 character hex string
            if hash_result and len(hash_result) == 64 and hash_result.isalnum():
                print(f"✅ Hash generation successful: {hash_result[:20]}...")
                return True
            else:
                print(f"❌ Hash generation failed: {hash_result}")
                return False
                
        except Exception as e:
            print(f"❌ Hash test failed: {e}")
            return False
    
    def test_key_generation(self):
        """Test random key generation"""
        print("\n🔑 Testing key generation...")
        
        try:
            # Click generate key button
            generate_btn = self.driver.find_element(
                By.XPATH, "//button[contains(text(), 'Generate Key')]"
            )
            generate_btn.click()
            time.sleep(1)
            
            # Check if password field is filled
            password_field = self.driver.find_element(By.ID, "password")
            generated_key = password_field.get_attribute("value")
            
            if generated_key and len(generated_key) >= 10:
                print(f"✅ Key generation successful: {generated_key}")
                return True
            else:
                print("❌ Key generation failed")
                return False
                
        except Exception as e:
            print(f"❌ Key generation test failed: {e}")
            return False
    
    def test_statistics(self):
        """Test statistics functionality"""
        print("\n📊 Testing statistics...")
        
        try:
            # Click stats button
            stats_btn = self.driver.find_element(
                By.XPATH, "//button[contains(text(), 'View Statistics')]"
            )
            stats_btn.click()
            time.sleep(2)
            
            # Check if stats content appears
            stats_content = self.driver.find_element(By.ID, "statsContent")
            content_text = stats_content.text
            
            if content_text and ("Total" in content_text or "No history" in content_text):
                print("✅ Statistics loaded successfully")
                return True
            else:
                print("❌ Statistics loading failed")
                return False
                
        except Exception as e:
            print(f"❌ Statistics test failed: {e}")
            return False
    
    def run_all_tests(self):
        """Execute complete test suite"""
        print("🧪 STARTING TEST SUITE")
        print("="*50)
        
        # Setup
        if not self.setup_driver():
            return False
        
        if not self.navigate_to_app():
            self.cleanup()
            return False
        
        # Run tests
        tests = [
            ("Caesar Encryption", self.test_caesar_encryption),
            ("Fernet Encryption", self.test_fernet_encryption),
            ("Hash Function", self.test_hash_function),
            ("Key Generation", self.test_key_generation),
            ("Statistics", self.test_statistics)
        ]
        
        passed = 0
        total = len(tests)
        
        for test_name, test_func in tests:
            try:
                if test_func():
                    self.test_results.append(f"✅ {test_name}")
                    passed += 1
                else:
                    self.test_results.append(f"❌ {test_name}")
            except Exception as e:
                print(f"❌ {test_name} crashed: {e}")
                self.test_results.append(f"💥 {test_name} (crashed)")
        
        # Results summary
        self.print_results(passed, total)
        self.cleanup()
        
        return passed == total
    
    def print_results(self, passed, total):
        """Display test results summary"""
        print("\n" + "="*50)
        print("🎯 TEST RESULTS SUMMARY")
        print("="*50)
        
        for result in self.test_results:
            print(result)
        
        print(f"\nScore: {passed}/{total} tests passed")
        
        if passed == total:
            print("🎉 ALL TESTS PASSED! 🎉")
        elif passed > total // 2:
            print("⚡ Most tests passed - minor issues detected")
        else:
            print("⚠️ Multiple test failures - check application")
        
        print("="*50)
    
    def cleanup(self):
        """Clean up browser resources"""
        if self.driver:
            self.driver.quit()
            print("🧹 Browser cleanup complete")

def main():
    """Main test execution"""
    print("🔐 Python Text Encrypter - Test Suite")
    print("Automated UI testing with Selenium\n")
    
    # Check if app is likely running
    try:
        import requests
        response = requests.get("http://localhost:5000", timeout=5)
        if response.status_code != 200:
            print("⚠️ Warning: App may not be running properly")
    except:
        print("⚠️ Warning: Cannot connect to localhost:5000")
        print("   Make sure to run 'python app.py' first")
        
        choice = input("\nContinue with tests anyway? (y/n): ")
        if choice.lower() not in ['y', 'yes']:
            return
    
    # Run tests
    tester = EncrypterTests()
    success = tester.run_all_tests()
    
    # Exit with appropriate code
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n👋 Tests interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Test suite failed: {e}")
        sys.exit(1)