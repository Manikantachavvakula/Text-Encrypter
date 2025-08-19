# 🔐 Python Text Encrypter

A modern web-based encryption tool built with Flask that demonstrates **Data Structures & Algorithms (DSA)** concepts while providing secure text encryption capabilities. This project combines educational DSA implementations with practical cryptography for learning and real-world applications.

## 🌟 **Project Highlights**

- **Full-Stack Web Application**: Flask backend with responsive HTML/CSS/JS frontend
- **Multiple Encryption Methods**: Caesar Cipher, AES-256 Fernet, SHA-256 Hashing
- **DSA Implementation**: Stack, Queue, Hash Tables, Sorting & Search algorithms
- **Real-time Statistics**: Track encryption usage and performance metrics
- **Modern UI/UX**: Animated gradients, responsive design, mobile-friendly
- **Educational Focus**: Code demonstrates Big O notation and algorithm complexity

## 🚀 **Live Demo**

```bash
# Quick Start
git clone https://github.com/yourusername/text-encrypter
cd text-encrypter
python setup.py
```

**🌐 Demo URL**: `http://localhost:5000` (runs locally)

> **Note**: This project runs as a local web server. For portfolio showcasing, you can deploy to platforms like Heroku, Railway, or Vercel for a live demo.

## 📋 **Features**

### 🔒 **Encryption Algorithms**
- **Caesar Cipher**: Educational implementation with shift-based encryption
- **AES Fernet**: Industry-standard symmetric encryption with password protection
- **SHA-256 Hash**: One-way cryptographic hashing for data integrity

### 📊 **DSA Demonstrations**
- **Stack Operations**: LIFO encryption history management
- **Queue Processing**: FIFO request handling system
- **Hash Tables**: O(1) algorithm lookup performance
- **Time Complexity**: Real-time Big O analysis and comparison
- **Sorting Algorithms**: Bubble sort vs built-in sort comparison
- **Search Methods**: Linear vs Binary search implementation

### 🎨 **User Experience**
- **Responsive Design**: Works on desktop, tablet, and mobile devices
- **Real-time Processing**: Instant encryption/decryption feedback
- **Usage Statistics**: Track encryption methods and character counts
- **Password Generation**: Secure random key generator
- **Error Handling**: User-friendly error messages and validation

## 🛠️ **Technology Stack**

| Component | Technology | Purpose |
|-----------|------------|---------|
| **Backend** | Python Flask | Web framework and API endpoints |
| **Cryptography** | `cryptography` library | AES encryption implementation |
| **Frontend** | HTML5, CSS3, JavaScript | Responsive user interface |
| **Data Structures** | Python collections | Queue, Stack, and Hash table demos |
| **Testing** | Selenium WebDriver | Automated UI testing |
| **Security** | PBKDF2, Fernet | Key derivation and encryption |

## 📁 **Project Structure**

```
text-encrypter/
├── app.py                 # Flask application and API routes
├── DSA_concepts.py        # Educational DSA demonstrations
├── setup.py              # Automated project setup script
├── test.py               # Selenium automated tests
├── requirements.txt      # Python dependencies
├── templates/
│   └── index.html        # Modern responsive web interface
├── static/
│   └── style.css         # Advanced CSS animations
└── README.md             # Project documentation
```

## 🔧 **Installation & Setup**

### **Method 1: Automated Setup**
```bash
# Clone the repository
git clone https://github.com/yourusername/text-encrypter
cd text-encrypter

# Run automated setup
python setup.py
```

### **Method 2: Manual Setup**
```bash
# Install dependencies
pip install -r requirements.txt

# Run the application
python app.py

# Visit in browser
open http://localhost:5000
```

### **Run DSA Demonstrations**
```bash
# See educational algorithm examples
python DSA_concepts.py
```

### **Run Automated Tests**
```bash
# Selenium UI testing
python test.py
```

## 📈 **Algorithm Complexity Analysis**

| Algorithm | Time Complexity | Space Complexity | Use Case |
|-----------|----------------|------------------|----------|
| Caesar Cipher | O(n) | O(1) | Educational learning |
| AES Fernet | O(n) | O(1) | Secure encryption |
| SHA-256 Hash | O(n) | O(1) | Data integrity |
| Hash Table Lookup | O(1) | O(n) | Algorithm selection |
| Stack Operations | O(1) | O(n) | History management |
| Queue Operations | O(1) | O(n) | Request processing |

## 🎯 **Learning Outcomes**

This project demonstrates:

1. **Web Development**: Full-stack application with Flask
2. **Cryptography**: Modern encryption standards and implementations
3. **Data Structures**: Practical use of stacks, queues, and hash tables
4. **Algorithm Analysis**: Big O notation and performance measurement
5. **Software Testing**: Automated testing with Selenium
6. **UI/UX Design**: Responsive design and user experience principles
7. **Security Practices**: Password handling and secure key generation

## 🧪 **Testing**

The project includes comprehensive testing:

- **Unit Tests**: Algorithm correctness verification
- **Integration Tests**: Flask API endpoint testing
- **UI Tests**: Selenium automated browser testing
- **Performance Tests**: Time complexity validation

```bash
# Run all tests
python test.py
```

## 🚀 **Deployment Options**

### **For Portfolio Live Demo:**

1. **Heroku** (Free tier available)
```bash
# Add Procfile: web: python app.py
heroku create your-text-encrypter
git push heroku main
```

2. **Railway** (Modern deployment)
```bash
# Connect GitHub repo
# Deploy automatically on push
```

3. **Vercel** (Frontend focus)
```bash
# Configure for Python
vercel --prod
```

## 📸 **Screenshots**

### Main Interface
- Modern animated gradient border
- Dual-mode encryption/decryption
- Algorithm selection dropdown
- Real-time result display

### Statistics Dashboard
- Usage tracking
- Performance metrics
- Algorithm comparison

## 🔐 **Security Features**

- **PBKDF2 Key Derivation**: 100,000 iterations for password security
- **Fernet Encryption**: AES 128 with authentication
- **Secure Random Generation**: Cryptographically secure key generation
- **Input Validation**: Comprehensive error handling and sanitization

## 🎨 **UI/UX Features**

- **Responsive Design**: Mobile-first approach
- **Animated Gradients**: CSS keyframe animations
- **Interactive Elements**: Hover effects and transitions
- **Dark Theme**: Modern aesthetic with purple accent colors
- **Accessibility**: Proper contrast ratios and semantic HTML

## 📝 **Portfolio Description**

**For your portfolio, use this concise description:**

> **Python Text Encrypter** - A full-stack web application demonstrating advanced Data Structures & Algorithms concepts through practical cryptography implementation. Built with Flask backend and modern responsive frontend, featuring Caesar Cipher, AES-256 encryption, and SHA-256 hashing. Includes real-time algorithm complexity analysis, automated testing with Selenium, and educational DSA demonstrations including Stack, Queue, and Hash Table operations. Perfect showcase of web development, security practices, and computer science fundamentals.

## 🤝 **Contributing**

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 **License**

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 **Author**

**Manikanta Chavvakula**
- **Portfolio**: [Your Portfolio URL]
- **LinkedIn**: [https://www.linkedin.com/in/manikanta-chavvakula-43b308189](https://www.linkedin.com/in/manikanta-chavvakula-43b308189)
- **GitHub**: [Your GitHub Profile]

## 🎯 **Next Steps**

- [ ] Add database persistence for user sessions
- [ ] Implement JWT authentication
- [ ] Add more encryption algorithms (RSA, Blowfish)
- [ ] Create API documentation with Swagger
- [ ] Add Docker containerization
- [ ] Implement real-time collaboration features

---

⭐ **Star this repository if you found it helpful!**