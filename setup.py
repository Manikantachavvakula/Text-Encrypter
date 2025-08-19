#!/usr/bin/env python3
"""
Python Text Encrypter - Quick Setup Script
Automated setup for Flask encryption application
"""

import os
import subprocess
import sys
import platform

def print_header():
    """Display setup header"""
    print("\n" + "="*50)
    print("🔐 PYTHON TEXT ENCRYPTER SETUP")
    print("="*50)
    print("Setting up your encryption application...")
    print()

def check_python_version():
    """Verify Python version compatibility"""
    print("🐍 Checking Python version...")
    
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 7):
        print("❌ Python 3.7+ required")
        print(f"   Current version: {version.major}.{version.minor}")
        return False
    
    print(f"✅ Python {version.major}.{version.minor} detected")
    return True

def install_requirements():
    """Install required packages"""
    print("\n📦 Installing dependencies...")
    
    packages = [
        'Flask==2.3.3',
        'cryptography==41.0.4', 
        'selenium==4.15.0',
        'gunicorn==21.2.0'
    ]
    
    try:
        # Try requirements.txt first
        if os.path.exists('requirements.txt'):
            subprocess.check_call([
                sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'
            ])
            print("✅ Requirements installed from requirements.txt")
        else:
            # Install packages individually
            for package in packages:
                print(f"   Installing {package}...")
                subprocess.check_call([
                    sys.executable, '-m', 'pip', 'install', package
                ])
            print("✅ All packages installed successfully")
        
        return True
        
    except subprocess.CalledProcessError as e:
        print(f"❌ Installation failed: {e}")
        print("   Try installing packages manually:")
        for pkg in packages:
            print(f"   pip install {pkg}")
        return False

def create_project_structure():
    """Create necessary directories"""
    print("\n📁 Creating project structure...")
    
    directories = ['templates', 'static']
    created = []
    
    for directory in directories:
        if not os.path.exists(directory):
            os.makedirs(directory)
            created.append(directory)
    
    if created:
        print(f"✅ Created directories: {', '.join(created)}")
    else:
        print("✅ Project structure already exists")
    
    return True

def verify_files():
    """Check for required project files"""
    print("\n📄 Verifying project files...")
    
    required_files = {
        'app.py': 'Main Flask application',
        'templates/index.html': 'Web interface template',
        'static/style.css': 'Stylesheet',
        'DSA_concepts.py': 'Educational DSA demos'
    }
    
    missing = []
    
    for file_path, description in required_files.items():
        if os.path.exists(file_path):
            print(f"✅ {description}: {file_path}")
        else:
            print(f"❌ Missing: {file_path}")
            missing.append(file_path)
    
    if missing:
        print(f"\n⚠️  Missing files: {', '.join(missing)}")
        print("   Please ensure all project files are present")
        return False
    
    return True

def test_import():
    """Test if Flask can be imported"""
    print("\n🧪 Testing Flask import...")
    
    try:
        import flask
        print(f"✅ Flask {flask.__version__} imported successfully")
        return True
    except ImportError:
        print("❌ Flask import failed")
        return False

def display_next_steps():
    """Show user what to do next"""
    print("\n🚀 SETUP COMPLETE!")
    print("-" * 30)
    print("Next steps:")
    print("1. Start the application:")
    print("   python app.py")
    print()
    print("2. Open your browser:")
    print("   http://localhost:5000")
    print()
    print("3. Run DSA demonstrations:")
    print("   python DSA_concepts.py")
    print()
    print("4. Run tests:")
    print("   python test.py")
    print()

def run_application():
    """Start the Flask application"""
    print("🌐 Starting Flask application...")
    print("   URL: http://localhost:5000")
    print("   Press Ctrl+C to stop")
    print()
    
    try:
        # Import and run
        import app
        app.app.run(debug=True, host='0.0.0.0', port=5000)
    except ImportError:
        print("❌ Cannot import app.py")
        print("   Please check that app.py exists and is valid")
    except KeyboardInterrupt:
        print("\n👋 Application stopped by user")
    except Exception as e:
        print(f"❌ Failed to start application: {e}")

def main():
    """Main setup process"""
    print_header()
    
    # Step 1: Check Python version
    if not check_python_version():
        return False
    
    # Step 2: Create directories
    if not create_project_structure():
        return False
    
    # Step 3: Install packages
    if not install_requirements():
        return False
    
    # Step 4: Test imports
    if not test_import():
        return False
    
    # Step 5: Verify files
    if not verify_files():
        print("\n⚠️  Some files are missing but setup will continue")
    
    # Step 6: Show next steps
    display_next_steps()
    
    # Step 7: Ask to start app
    while True:
        try:
            choice = input("🚀 Start the application now? (y/n): ").lower().strip()
            
            if choice in ['y', 'yes']:
                run_application()
                break
            elif choice in ['n', 'no']:
                print("\n📋 Setup complete! Start manually with: python app.py")
                break
            else:
                print("Please enter 'y' or 'n'")
                
        except KeyboardInterrupt:
            print("\n👋 Setup cancelled")
            break
    
    return True

if __name__ == "__main__":
    try:
        success = main()
        sys.exit(0 if success else 1)
    except KeyboardInterrupt:
        print("\n👋 Setup interrupted")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Setup failed: {e}")
        sys.exit(1)