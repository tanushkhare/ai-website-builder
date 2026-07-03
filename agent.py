import os
import re
import time
import zipfile
import argparse
import webbrowser
from groq import Groq
from dotenv import load_dotenv

# ============================================
# CONFIG
# ============================================
MODEL_NAME = "llama-3.1-8b-instant"

# ============================================
# LOAD ENV
# ============================================
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    print("❌ GROQ_API_KEY not found in .env file")
    exit()

client = Groq(api_key=api_key)

# ============================================
# CLI ARGUMENTS
# ============================================
parser = argparse.ArgumentParser(description="🚀 AI Website Generator v1.0")

parser.add_argument("--desc", help="Website description")
parser.add_argument("--mode", choices=["single", "multi"], default="multi")
parser.add_argument("--theme", choices=["dark", "luxury", "minimal"], default="dark")
parser.add_argument("--preview", action="store_true")

args = parser.parse_args()
start_time = time.time()

print("=" * 65)
print("🚀 AI WEBSITE GENERATOR")
print("=" * 65)
print("Generate modern websites using AI (Groq + Llama 3.1)")
print()

description = args.desc.strip() if args.desc else input("📝 Enter website description: ").strip()
mode = args.mode
theme = args.theme

if not description:
    print("❌ Description cannot be empty.")
    exit()

# ============================================
# THEME ENGINE
# ============================================
theme_styles = {
    "dark": "Dark modern UI with deep navy background and subtle animations.",
    "luxury": "Premium black and gold theme with glassmorphism and smooth transitions.",
    "minimal": "Clean white minimal layout with soft spacing and elegant typography."
}

theme_instruction = theme_styles.get(theme, theme_styles["dark"])

# ============================================
# PROJECT FOLDER SETUP
# ============================================
folder_name = re.sub(r'[^a-zA-Z0-9]+', '-', description.lower()).strip('-')
folder_name = folder_name[:50]  # Windows-safe length

project_path = os.path.join("projects", folder_name)

if os.path.exists(project_path):
    folder_name += "-" + str(int(time.time()))
    project_path = os.path.join("projects", folder_name)

os.makedirs(project_path, exist_ok=True)

# ============================================
# PROMPT BUILDER
# ============================================
if mode == "single":
    file_instruction = """
Return code EXACTLY separated like this:

---index.html---
<html code>

---style.css---
css code
"""
else:
    file_instruction = """
Return code EXACTLY separated like this:

---index.html---
<html code>

---about.html---
<html code>

---contact.html---
<html code>

---style.css---
css code
"""

prompt = f"""
You are a senior professional web developer.

Theme:
{theme_instruction}

Generate a complete modern website.

Requirements:
- Fully responsive
- Smooth animations
- Professional layout
- Navigation bar
- Footer included
- Clean, production-ready code
- Use semantic HTML5
- Modern UI design

Website description:
{description}

IMPORTANT:
{file_instruction}

No explanations.
"""
print("\n⚡ Connecting to Groq AI...")
print(f"🧠 AI Model : {MODEL_NAME}")
print("🤖 Generating website...")

# ============================================
# CALL GROQ API
# ============================================
try:
    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
    )
except Exception as e:
    print("\n❌ API Error occurred.")
    print("Details:", str(e))
    print("Check your model name or API key.")
    exit()

content = response.choices[0].message.content

print("✅ AI response received.")

if not content:
    print("❌ Empty response from model.")
    exit()

# ============================================
# FILE EXTRACTION
# ============================================
sections = re.split(r'---(.*?)---', content, flags=re.DOTALL)

if len(sections) < 3:
    print("❌ Could not parse files correctly.")
    exit()

for i in range(1, len(sections), 2):
    filename = sections[i].strip()
    filecontent = sections[i + 1].strip()

    if not filename or not filecontent:
        continue

    # 🔥 Safety: Fix wrong CSS paths if model generates them
    if filename.endswith(".html"):
        filecontent = filecontent.replace(
            'href="assets/style.css"',
            'href="style.css"'
        )

    save_path = os.path.join(project_path, filename)
    print(f"📄 Creating {filename}")

    with open(save_path, "w", encoding="utf-8") as f:
        f.write(filecontent)

# ============================================
# ZIP EXPORT
# ============================================
zip_path = os.path.join(project_path, "website.zip")

with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
    for root, dirs, files in os.walk(project_path):
        for file in files:
            full_path = os.path.join(root, file)
            relative_path = os.path.relpath(full_path, project_path)
            zipf.write(full_path, relative_path)

# ============================================
# SUCCESS MESSAGE
# ============================================
print("\n" + "=" * 65)
print("🎉 WEBSITE GENERATED SUCCESSFULLY!")
print("=" * 65)
print(f"\n🎨 Theme Selected : {theme.capitalize()}")
print(f"📄 Mode           : {mode.capitalize()} Page")

print("\n📁 Output Folder")
print(f"   {project_path}")

print("\n📦 ZIP Archive")
print(f"   {zip_path}")

generated_files = [
    f for f in os.listdir(project_path)
    if f.endswith((".html", ".css", ".js"))
]

print(f"\n📄 Generated Files ({len(generated_files)})")

for file in generated_files:
    print(f"   ✔ {file}")

elapsed = time.time() - start_time

print(f"\n⏱ Generation Time : {elapsed:.2f} seconds")

print("\n🚀 Thank you for using AI Website Generator!")
print("=" * 65)

# ============================================
# PREVIEW MODE
# ============================================
if args.preview:
    index_file = os.path.join(project_path, "index.html")
    print("\n🌐 Opening website preview...")
    webbrowser.open(index_file)
