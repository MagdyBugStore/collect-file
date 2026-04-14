#!/usr/bin/env python3
"""
الملف الرئيسي لتهيئة مشروع Node.js + Express + TypeScript + MongoDB
"""

import os
import sys
import json
import shutil
from pathlib import Path
from typing import Dict, List

# استيراد الوحدات المحلية
try:
    from utils import create_directories, write_file, run_npm_install
    from prompts import ask_project_name, ask_overwrite, ask_install_deps
except ImportError as e:
    print(f"Error importing modules: {e}")
    print("Please ensure utils.py and prompts.py exist in the same directory")
    sys.exit(1)

def load_structure_from_json(json_path: Path) -> Dict:
    """تحميل ملف structure.json"""
    with open(json_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def generate_project(structure: Dict, project_path: Path, templates_dir: Path):
    """إنشاء المشروع بناءً على الهيكل والقوالب"""
    # إنشاء المجلدات
    dirs = structure.get("directories", [])
    create_directories(project_path, dirs)
    
    # إنشاء الملفات
    files = structure.get("files", [])
    for file_info in files:
        file_path = project_path / file_info["path"]
        template_name = file_info.get("template")
        content = file_info.get("content", "")
        
        if template_name:
            template_file = templates_dir / template_name
            if template_file.exists():
                with open(template_file, 'r', encoding='utf-8') as tf:
                    content = tf.read()
            else:
                print(f"⚠️ Template '{template_name}' not found for {file_info['path']}")
        
        write_file(file_path, content)
    
    # نسخ الملفات الثابتة إن وجدت
    static = structure.get("static", [])
    for static_item in static:
        src = templates_dir / static_item["src"]
        dest = project_path / static_item["dest"]
        if src.is_file():
            shutil.copy2(src, dest)
            print(f"📄 Copied static file: {static_item['dest']}")
        elif src.is_dir():
            shutil.copytree(src, dest, dirs_exist_ok=True)
            print(f"📁 Copied static dir: {static_item['dest']}")

def main():
    print("🚀 Express TypeScript MongoDB Backend Initializer (Modular)\n")
    
    # تحديد المسارات
    script_dir = Path(__file__).parent.resolve()
    structure_file = script_dir / "structure.json"
    templates_dir = script_dir / "templates"
    
    if not structure_file.exists():
        print(f"❌ structure.json not found in {script_dir}")
        sys.exit(1)
    
    if not templates_dir.exists():
        print("⚠️ templates directory not found. Creating default empty one.")
        templates_dir.mkdir(parents=True, exist_ok=True)
    
    # تحميل الهيكل
    structure = load_structure_from_json(structure_file)
    
    # الحصول على اسم المشروع
    project_name = ask_project_name()
    project_path = Path.cwd() / project_name
    
    # التحقق من وجود المشروع
    if not ask_overwrite(project_path):
        print("❌ Aborted.")
        sys.exit(1)
    
    # إنشاء المشروع
    print(f"\n📂 Generating project in: {project_path}")
    project_path.mkdir(parents=True, exist_ok=True)
    generate_project(structure, project_path, templates_dir)
    
    # تثبيت dependencies
    if ask_install_deps():
        run_npm_install(project_path)
    else:
        print("⚠️ Skipped npm install. Run manually later.")
    
    print("\n🎉 Project initialization complete!")
    print(f"👉 cd {project_name}")
    print("👉 cp .env.example .env")
    print("👉 npm run dev")

if __name__ == "__main__":
    main()