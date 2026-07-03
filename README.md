# 🚀 AI Website Generator

Generate complete, production-ready multi-page websites from a single description using **Groq + LLaMA**.

![Demo](projects/fintech-demo/screenshot-preview.png)

---

## ✨ Features

- **One-command generation** — describe your site, get full HTML/CSS in seconds
- **3 visual themes** — `dark`, `luxury`, `minimal`
- **Multi-page output** — index, about, contact + shared CSS
- **Responsive by default** — mobile-first with proper breakpoints
- **Auto ZIP export** — ready to deploy immediately
- **Browser preview** — `--preview` flag opens the site instantly
- **Powered by Groq** — blazing fast inference with LLaMA 3.3 70B

---

## 📁 Project Structure

```
ai-website-generator/
├── agent.py                  # Main generator script
├── requirements.txt          # Python dependencies
├── .env.example              # API key template
├── .gitignore
├── README.md
│
└── projects/                 # All generated sites live here
    └── fintech-demo/         # Example: Modern Fintech Dashboard
        ├── index.html
        ├── about.html
        ├── contact.html
        ├── style.css
        └── website.zip
```

---

## ⚡ Quick Start

### 1. Clone the repo

```bash
git clone https://github.com/YOUR_USERNAME/ai-website-generator.git
cd ai-website-generator
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Add your Groq API key

```bash
cp .env.example .env
# Edit .env and paste your key from https://console.groq.com
```

### 4. Generate a website

```bash
python agent.py --desc "SaaS landing page for a project management tool" --theme dark --preview
```

---

## 🎛️ CLI Options

| Flag | Values | Default | Description |
|------|--------|---------|-------------|
| `--desc` | any string | *(prompted)* | Website description |
| `--mode` | `single` `multi` | `multi` | Single page or multi-page |
| `--theme` | `dark` `luxury` `minimal` | `dark` | Visual theme |
| `--preview` | flag | off | Open in browser after generation |
| `--model` | any Groq model | `llama-3.3-70b-versatile` | Override the model |

### Examples

```bash
# Minimal single-page portfolio
python agent.py --desc "Personal portfolio for a UX designer" --mode single --theme minimal

# Luxury e-commerce landing page
python agent.py --desc "High-end watch brand e-commerce site" --theme luxury --preview

# Dark SaaS dashboard
python agent.py --desc "Analytics dashboard for a social media tool" --theme dark
```

---

## 🗂️ Demo Output

The `projects/fintech-demo/` folder contains a live example generated for:

> *"Modern fintech dashboard for payment processing and analytics"*

**Pages:** Home · About · Contact  
**Theme:** Dark  
**Features:** animated hero, floating stat cards, feature grid, testimonial, contact form

---

## 🔧 Requirements

- Python 3.9+
- [Groq API key](https://console.groq.com) (free tier available)

---

## 🤝 Contributing

Pull requests are welcome! Please open an issue first to discuss what you'd like to change.

---

## 📄 License

MIT — free to use, fork, and build upon.
