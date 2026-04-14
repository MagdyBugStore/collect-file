"""
دوال للتفاعل مع المستخدم
"""

from pathlib import Path

def ask_project_name() -> str:
    """سؤال المستخدم عن اسم المشروع"""
    name = input("Project name (default: express-ts-mongo): ").strip()
    return name if name else "express-ts-mongo"

def ask_overwrite(project_path: Path) -> bool:
    """السؤال عن إمكانية الكتابة فوق مجلد موجود"""
    if project_path.exists():
        ans = input(f"Directory '{project_path.name}' already exists. Overwrite? (y/N): ").strip().lower()
        return ans == 'y'
    return True

def ask_install_deps() -> bool:
    """السؤال عن تثبيت dependencies"""
    ans = input("\n✨ Do you want to run 'npm install' now? (Y/n): ").strip().lower()
    return ans != 'n'