# Sub-Domain-Enumeration
A multi-threaded Python-based CLI tool to perform subdomain enumeration by brute-forcing a wordlist and checking for live subdomains via HTTP GET requests.
---


## 🚀 Features

- 🧵 Multi-threaded for fast performance.
- 📄 Wordlist-based brute force.
- ✅ Identifies live subdomains with HTTP 200 status code.
- 🖥️ Beautiful ASCII banner for branding.
- 📦 Simple and lightweight – only requires `requests`.

---

## 📁 File Structure

- `subdomain.py` – Main script for subdomain enumeration.
- `small.txt` – (You need to provide) A wordlist containing subdomain names to test.

---

## ⚙️ Requirements

- Python 3.x


## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/JoshuaFerando/Sub-Domain-Enumeration
   cd Sub-Domain-Enumeration
   ```


2.Install the required module using:
```bash
pip install -r requirements.txt
```

---

## 🛠️ Usage
1. **Prepare your wordlist** (e.g., `small.txt`) – one subdomain per line.
2. **Edit script variables** in `subdomain.py`:
```python
url = "https://www.google.com"
wordlist_path = "small.txt"
total_threads = 72
```
3. **Run the tool**:
```bash
python3 subdomain.py
```

---

## 🔧 Configuration Tips

- If you encounter `ConnectionResetError`, reduce the `total_threads` value.
- Make sure your target URL does not block too many requests in a short span (may trigger rate-limiting or firewall rules).

---

## 📝 Example Output

```
***********************************
Target URL: https://www.google.com
Wordlist Used: small.txt
Total Sub-Domain To check: 500
***********************************

The Various Sub-Domains found are...

https://www.google.com/mail
https://www.google.com/maps
...
```

---

## Disclaimer

This script is intended for educational and ethical penetration testing purposes only. Unauthorized usage against systems you do not own or have explicit permission to test is illegal.

## Contribution

Pull requests are welcome! Feel free to improve the script by optimizing performance or adding new features.

## Author

Joshua Fernando

