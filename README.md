# 🔉 Vākyantrā – Sanskrit Programming Language Interpreter (Python)

**Vākyantrā** is a simple interpreter written in Python for a custom programming language inspired by Sanskrit. It allows you to write and execute Sanskrit-like code that feels natural and readable, yet maps to real logical operations.

> 🧠 Powered by: Python 3.7+
> 📁 File extension: `.ved`

---

## 📦 Features

* ✅ Simple syntax for print, variables, and conditionals
* ✅ Read `.ved` code from files or input
* ✅ Modular design for future expansion
* ⚧️ (Planned): Loops (`यावत्`), functions (`कार्य️`), imports, math expressions

---

## 🧱 Syntax (VedLang)

| Concept      | VedLang Syntax                    | Meaning             |
| ------------ | --------------------------------- | ------------------- |
| Print        | `वद(" नमस्ते जगत् ")`             | Print to console    |
| Assignment   | `संख्या = 10`                     | Variable assignment |
| Conditionals | `यदि संख्या > 5 तर्हि` / `अन्यथा` | If / else           |

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/Lucky-Joshi/Vakyantra.git
cd vakyantra
```

### 2. Run the Interpreter

```bash
python main.py path/to/file.ved
```

Or start in REPL mode:

```bash
python main.py
```

---

## 🧪 Example `.ved` File

```ved
वद(" प्रारम्भः ")
संख्या = 7
यदि संख्या % 2 == 0 तर्हि
  वद(" एषा संख्या समा अस्ति। ")
अन्यथा
  वद(" एषा संख्या विषमा अस्ति। ")
```

---

## 🔧 Roadmap

* [ ] Loops (e.g., `यावत्`)
* [ ] Functions (e.g., `कार्य️`)
* [ ] Data structures
* [ ] File import/export
* [ ] Browser-based runner using Pyodide

---

## 💡 How It Works

The interpreter:

1. Tokenizes Sanskrit code
2. Matches keywords like `वद`, `यदि`, `अन्यथा`
3. Uses `eval()` safely for arithmetic
4. Handles context and variable storage in memory

---

## 📜 License

MIT License — use it, fork it, modify it, teach with it.

---

## 🙏 Inspired By

* Sanskrit grammar & structure (Panini vibes)
* Basic Python/JS interpreters
* Educational languages like Logo, Scratch, and LISP

---

## 🧙‍♂️ Author

Lucky Joshi
[GitHub](https://github.com/Lucky-Joshi) 

---

🔉 *Let the code speak in Sanskrit.*
