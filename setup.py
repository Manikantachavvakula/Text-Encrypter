#!/usr/bin/env python3
"""
Quick setup script for Python Text Encrypter
Run this to set up the project automatically
"""

import os
import subprocess
import sys

def install_requirements():
    """Install required packages"""
    print("📦 Installing requirements...")
    try:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'])
        print("✅ Requirements installed successfully!")
    except subprocess.CalledProcessError:
        print("❌ Failed to install requirements. Installing individually...")
        packages = ['Flask==2.3.3', 'cryptography==41.0.4', 'selenium==4.15.0']
        for package in packages:
            try:
                subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])
                print(f"✅ Installed {package}")
            except subprocess.CalledProcessError:
                print(f"❌ Failed to install {package}")

def create_directories():
    """Create necessary directories"""
    print("📁 Creating project structure...")
    
    if not os.path.exists('templates'):
        os.makedirs('templates')
        print("✅ Created templates/ directory")
    
    if not os.path.exists('static'):
        os.makedirs('static')
        print("✅ Created static/ directory")

def check_files():
    """Check if all necessary files exist"""
    required_files = ['app.py', 'templates/index.html']
    missing_files = []
    
    for file in required_files:
        if not os.path.exists(file):
            missing_files.append(file)
    
    if missing_files:
        print("⚠️  Missing files:")
        for file in missing_files:
            print(f"   - {file}")
        print("\nPlease create these files from the provided code.")
        return False
    
    print("✅ All required files present!")
    return True

def run_application():
    """Start the Flask application"""
    print("\n🚀 Starting the application...")
    print("📍 URL: http://localhost:5000")
    print("🛑 Press Ctrl+C to stop the server")
    
    try:
        # Import and run the app
        import app
        app.app.run(debug=True, host='0.0.0.0', port=5000)
    except ImportError:
        print("❌ Could not import app.py. Make sure it exists and is properly formatted.")
    except KeyboardInterrupt:
        print("\n👋 Application stopped.")

def main():
    """Main setup function"""
    print("🐍 Python Text Encrypter Setup")
    print("=" * 40)
    
    # Create directories
    create_directories()
    
    # Install requirements
    install_requirements()
    
    # Check files
    if not check_files():
        return
    
    # Ask user if they want to start the app
    while True:
        choice = input("\n🚀 Start the application now? (y/n): ").lower().strip()
        if choice in ['y', 'yes']:
            run_application()
            break
        elif choice in ['n', 'no']:
            print("\n📋 To start later, run: python app.py")
            print("🧪 To run tests, run: python test_selenium.py")
            print("🎓 To see DSA demos, run: python dsa_concepts.py")
            break
        else:
            print("Please enter 'y' or 'n'")

if __name__ == "__main__":
    main()