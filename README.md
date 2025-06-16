# txt_to_json_converter

A simple Python script to convert old Sonic Tracker V1 text-based user data (`users.txt` and `data_<username>.txt`) into the new JSON-based format (`users.json` and `data/<username>.txt`) used in Sonic Tracker V2.

---

## 📁 Project Structure

```
txt_to_json_converter/
├── users.txt                # Old user data (comma-separated)
├── users.json               # Converted JSON format user data
├── data_<username>.txt      # Old individual data files (per user)
├── data/<username>.txt      # New data folder with individual files
├── txt_to_json_converter.py # Main conversion script
├── README.md                # Project documentation
├── LICENSE                  # MIT License
└── .gitignore               # Git ignore file
```

---

## 🚀 How to Use

1. Place `users.txt` and `data_<username>.txt` files in the same directory as the script.
2. Run the script:

```bash
python txt_to_json_converter.py
```

3. The script will:
   - Convert `users.txt` → `users.json`
   - Move `data_<username>.txt` → `data/<username>.txt`

---

## 🔧 Requirements

- Python 3.x
- No external libraries required (uses built-in modules)

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🤝 Author

Made with ❤️ by Jisan & Sonic (ChatGPT)
