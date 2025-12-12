# 📊 snap-analog

### Advanced Log Analysis & Visualization Toolkit

**Developer:** Batuhan Erkoc
**Version:** 2.0

snap-analog is a powerful command-line toolkit designed for parsing, analyzing, optimizing, and visualizing large-scale log files.
It supports Apache, Nginx, JSON-based logs, and even system logs.
Featuring memory-optimized analysis, advanced error-rate detection, traffic insights, and rich visual dashboards.

---

## 🚀 Features

* 🔍 **High-performance log analysis** (supports millions of lines)
* 💾 **Multiple memory modes:** `auto`, `balanced`, `full`, `aggressive`
* 📊 **Beautiful visual dashboards** using Matplotlib & Seaborn
* 🧠 **Traffic analysis:** top IPs, URLs, status groups, HTTP methods
* ⚠️ **Error-rate warnings** with threshold detection
* 🕒 **Time-series request charts**
* 🧪 **Built-in random test log generator**
* 🛠 **CLI interface with dynamic terminal UI**
* 🌈 **Colorful and readable terminal output**

---

## 📦 Installation

### ✔ Option 1 — Using virtual environment (recommended)

```bash
git clone https://github.com/<your-username>/snap-analog.git
cd snap-analog

python3 -m venv venv
source venv/bin/activate   # Mac/Linux
# .\venv\Scripts\activate  # Windows

pip install -r requirements.txt
pip install .
```

Now the command is available:

```bash
snap-analog --help
```

---

### ✔ Option 2 — Install directly (not recommended on macOS system Python)

```bash
pip install .
```

If you get “externally managed environment” error, use:

```bash
pip install --user .
```

---

## 🧪 Generating Test Logs

```bash
snap-analog generate-test --lines 5000 --output logs/test.log --format apache
```

or:

```bash
snap-analog generate-test --format json --lines 3000 --output logs/sample.json
```

---

## 🔍 Analyzing Logs

Basic usage:

```bash
snap-analog analyze access.log
```

With visualization:

```bash
snap-analog analyze access.log --visualize
```

Aggressive memory mode:

```bash
snap-analog analyze access.log --mode aggressive
```

Custom report filename:

```bash
snap-analog analyze access.log --output results/report.json
```

---

## 📊 Visualizing Existing JSON Report

```bash
snap-analog visualize reports/log_analysis_20250101_120000.json
```

Custom theme/size:

```bash
snap-analog visualize report.json --theme darkgrid --size large --dpi 200
```

---

## 📂 Project Structure

```
snap-analog/
│
├── src/
│   ├── cli.py                # Main CLI entry point
│   ├── log_analyzer.py       # Memory-optimized analyzer
│   ├── log_visualizer.py     # Dashboard generator
│
├── reports/                  # Auto-saved dashboards
├── logs/                     # User log files
├── setup.py
├── requirements.txt
└── README.md
```

---

## 💡 Example Visuals

The visualizer generates a dashboard containing:

* Pie chart of status groups
* Top IPs bar chart
* Top URLs bar chart
* Time-series traffic chart
* HTTP method distribution
* Error-rate heatbars

Output is saved to:

```
reports/dashboard_YYYYMMDD_HHMMSS.png
```

---

## ⚙ Requirements

```
matplotlib
seaborn
pandas
numpy
psutil (optional, for system info)
```

Install:

```bash
pip install -r requirements.txt
```

---

## 🧑‍💻 Development

Editable install:

```bash
pip install -e .
```

Run CLI directly:

```bash
python3 src/cli.py analyze logs/test.log
```

---

## 🤝 Contributing

Pull requests are welcome!
If you find a bug or want a feature added, open an issue.

---

## 📜 License

MIT License — free for personal and commercial use.

---

## ⭐ Support

If you like the project, consider leaving a ⭐ on GitHub — it helps a lot!
Developed with ❤️ by **Batuhan Erkoc**.

