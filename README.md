
# 🔐 Paillier Cryptosystem – Homomorphic Encryption in Python

A clean implementation of the **Paillier cryptosystem**, a public-key encryption algorithm that supports **homomorphic addition** on encrypted data. Built in Python, this project demonstrates secure communication and computation between a client and server using Paillier's properties.

> 📘 Based on Pascal Paillier's 1999 paper on probabilistic public-key cryptosystems.

---

## 📌 Features

- 🔑 Key generation using large primes and modular arithmetic
- 🔒 Probabilistic encryption with randomization
- 🔓 Decryption with Chinese Remainder Theorem
- ➕ Homomorphic addition: `E(m1) * E(m2) = E(m1 + m2)`
- 🧪 Simple demo of client-server communication over sockets

---

## 🛠️ Tech Stack

- **Language:** Python 3
- **Core Libraries:** `pycryptodome`, `sympy`, `socket`, `pickle`
- **Architecture:** Modular OOP classes with client/server communication

---

## 📂 Project Structure

```
PaillierCryptosystemAlgo/
├── paillier.py         # Core Paillier algorithm implementation
├── client.py           # Encrypts data and handles decryption
├── server.py           # Performs operations on ciphertexts
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the Repo

```bash
git clone https://github.com/rahules24/PaillierCryptosystemAlgo.git
cd PaillierCryptosystemAlgo
```

### 2. Set Up Environment & Install Dependencies

```bash
python -m venv venv
source venv/bin/activate   # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

---

## 🚀 How to Run the Demo

### Step-by-step:

1. Start the server:
```bash
python server.py
```

2. In a separate terminal, run the client:
```bash
python client.py
```

3. Observe:
   - Key generation
   - Encryption of `m1 = 1000` and `m2 = 2000`
   - Homomorphic addition on the server
   - Decryption of the result → `m1 + m2 = 3000`

---

## 🔍 Example Use Case

> Use this as a **proof-of-concept** for privacy-preserving computation — adding two encrypted salaries without revealing them.

---

## 📄 Theory

- Based on **Composite Residuosity Class** problem (DCRA)
- Secure due to the difficulty of factoring large composites
- Randomized encryption: same message, different ciphertexts
- Allows basic computations directly on encrypted data

---

## 🧠 What I Learned

- How to implement a public-key cryptosystem from scratch
- Working with large integer arithmetic in Python
- Real-time socket-based client-server communication
- Practical demonstration of homomorphic encryption

---

_Refer to Report for precise details!_
