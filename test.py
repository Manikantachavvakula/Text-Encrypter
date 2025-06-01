from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

def test_encrypter():
    driver = webdriver.Chrome()
    
    try:
        print("🧪 Testing Python Text Encrypter...")
        
        # Navigate to app
        driver.get("http://localhost:5000")
        time.sleep(2)
        
        # Test Caesar encryption
        input_field = driver.find_element(By.ID, "inputText")
        input_field.send_keys("Hello World!")
        
        method = Select(driver.find_element(By.ID, "method"))
        method.select_by_value("caesar")
        
        process_btn = driver.find_element(By.ID, "processBtn")
        process_btn.click()
        time.sleep(1)
        
        result = driver.find_element(By.ID, "result").get_attribute("value")
        print(f"✅ Caesar encryption: {result}")
        
        # Switch to decrypt mode
        decrypt_btn = driver.find_element(By.XPATH, "//button[contains(text(), 'Decrypt')]")
        decrypt_btn.click()
        time.sleep(1)
        
        # Test decryption
        input_field = driver.find_element(By.ID, "inputText")
        input_field.clear()
        input_field.send_keys(result)
        
        process_btn = driver.find_element(By.ID, "processBtn")
        process_btn.click()
        time.sleep(1)
        
        decrypted = driver.find_element(By.ID, "result").get_attribute("value")
        print(f"✅ Caesar decryption: {decrypted}")
        
        assert "Hello World!" == decrypted, "Decryption failed!"
        print("🎉 All tests passed!")
        
    except Exception as e:
        print(f"❌ Test failed: {e}")
    
    finally:
        driver.quit()

if __name__ == "__main__":
    test_encrypter()