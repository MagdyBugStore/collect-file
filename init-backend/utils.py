"""
دوال مساعدة لإنشاء الملفات والمجلدات وتثبيت dependencies
"""

from pathlib import Path
from typing import List
import subprocess

def create_directories(base_path: Path, dirs: List[str]):
    """إنشاء المجلدات المطلوبة"""
    for d in dirs:
        (base_path / d).mkdir(parents=True, exist_ok=True)
        print(f"📁 Created: {d}")

def write_file(path: Path, content: str):
    """كتابة محتوى إلى ملف"""
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content.strip())
    print(f"📄 Created: {path}")

def run_npm_install(project_path: Path):
    """تشغيل npm install في مجلد المشروع"""
    try:
        subprocess.run(["npm", "install"], cwd=str(project_path), check=True)
        print("✅ Dependencies installed successfully!")
    except subprocess.CalledProcessError:
        print("❌ npm install failed. Please run 'npm install' manually.")
    except FileNotFoundError:
        print("⚠️ npm not found. Please install Node.js first.")