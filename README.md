# 🏦 SecureBank — Secure Multi-Account Banking Application

A web-based banking application built with Python and Flask, designed to simulate everyday banking operations through a secure, user-friendly interface.

SecureBank allows users to register, authenticate, manage bank accounts, view account balances and perform transactions through a centralised banking dashboard.

The project focuses on backend development, database management, authentication, transaction processing and practical application security.

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-Web_Framework-black?logo=flask)
![SQLite](https://img.shields.io/badge/SQLite-Database-003B57?logo=sqlite)
![HTML5](https://img.shields.io/badge/HTML5-Markup-E34F26?logo=html5)
![CSS3](https://img.shields.io/badge/CSS3-Styling-1572B6?logo=css3)
![JavaScript](https://img.shields.io/badge/JavaScript-Frontend-F7DF1E?logo=javascript)
![Status](https://img.shields.io/badge/Status-In_Development-orange)

---

## 📌 Project Overview

SecureBank is a simulated digital banking platform developed to demonstrate how a banking application can manage users, accounts and financial transactions.

The application uses Flask to handle backend operations, SQLite for persistent data storage and HTML, CSS and JavaScript for the user interface.

The system is being developed with a multi-account structure, allowing users to manage multiple accounts under one login.

## 🏗️ System Architecture

```text
                  SECUREBANK
                      |
          +-----------+-----------+
          |                       |
     User Interface          Authentication
    HTML / CSS / JS           Flask Backend
          |                       |
          +-----------+-----------+
                      |
                Application Logic
                      |
          +-----------+-----------+
          |                       |
     Account Management     Transaction Engine
          |                       |
          +-----------+-----------+
                      |
                 SQLite Database
                      |
          +-----------+-----------+
          |                       |
        Users                  Accounts
                                  |
                             Transactions
```

## ✨ Features

### Implemented

- **User Registration:** Create a banking account with securely hashed passwords.
- **User Authentication:** Login and session-based access control.
- **Banking Dashboard:** View account information and recent transactions.
- **Account Management Foundation:** Database structure supports multiple accounts per user.
- **Money Transfers:** Transfer funds between bank accounts.
- **Recipient Verification:** Verify recipient account details before transferring.
- **Transaction History:** Retrieve transactions associated with a user's accounts.
- **Account Number Protection:** Mask account details and provide a copy-account-number function.
- **Input Validation:** Validate transaction amounts and account information.

### In Development

- Multiple account creation and management interface.
- Merchant deposit and internal transfer-to-self options.
- ATM/cash withdrawal simulation.
- Improved transaction statements.
- Expanded account settings and security controls.
- Enhanced transaction notifications.

## ⚙️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| Flask | Web application framework |
| SQLite | Relational database |
| HTML5 | Page structure |
| CSS3 | User interface styling |
| JavaScript | Frontend interactions |
| Git & GitHub | Version control |

## 🗄️ Database Structure

SecureBank uses SQLite to store application data.

The current database design includes:

**Users**
- User ID
- Full name
- Email address
- Password hash
- Account creation date

**Accounts**
- Account ID
- User ID
- Account number
- Account balance

**Transactions**
- Sender account
- Receiver account
- Transaction amount
- Transaction type
- Transaction status
- Transaction date
- Description

## 🔐 Security Considerations

Security is an important part of the development process.

Current security-related implementations include:

- Password hashing using Werkzeug security utilities.
- Session-based authentication.
- User-specific account queries.
- Recipient account verification.
- Transaction amount validation.
- Protection against unauthorised access to authenticated routes.

Further security improvements will be introduced as development progresses.

## 🚀 Getting Started

### Prerequisites

- Python 3.x
- pip
- Git

### Installation

**1. Clone the repository**

```bash
git clone https://github.com/YOUR-USERNAME/Secure-Banking-App.git
```

**2. Navigate into the project directory**

```bash
cd Secure-Banking-App
```

**3. Create a virtual environment**

```bash
python -m venv venv
```

**4. Activate the virtual environment**

Windows:

```bash
venv\Scripts\activate
```

**5. Install dependencies**

```bash
pip install flask werkzeug
```

Install any additional dependencies listed in `requirements.txt` if available.

**6. Initialise the database**

Run the database initialisation script:

```bash
python database/init_db.py
```

**7. Start the application**

```bash
python app.py
```

Open your browser and navigate to:

```text
http://127.0.0.1:5000
```

## 📂 Project Structure

```text
Secure-Banking-App/
│
├── app.py
├── database/
│   ├── init_db.py
│   └── Securebank.db
│
├── templates/
│   ├── index.html
│   ├── login.html
│   ├── register.html
│   ├── deposit.html
│   └── transfer.html
│
├── static/
│   └── style.css
│
├── README.md
└── .gitignore
```

*The project structure may evolve as additional modules and features are introduced.*

## 🛣️ Development Roadmap

- [x] User registration and authentication
- [x] Password hashing
- [x] Banking dashboard
- [x] Account database structure
- [x] Fund transfer functionality
- [x] Recipient verification
- [x] Transaction history retrieval
- [ ] Complete multiple-account management
- [ ] Merchant deposit simulation
- [ ] Internal transfer-to-self
- [ ] ATM/cash withdrawal simulation
- [ ] Detailed transaction statements
- [ ] Automated testing expansion
- [ ] Deployment

## ⚠️ Disclaimer

SecureBank is an educational software development project.

It is a simulated banking application and is not connected to real financial institutions or payment networks. It must not be used to store or process real financial funds.

## 👩‍💻 Author

**Miracle Nmesoma Ndubuisi**

Computer Science Student | Software Development

GitHub: https://github.com/mndubuisi54-debug

---

*Built as a practical exploration of backend engineering, database management, web development and application security.*
