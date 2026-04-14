import os

# المسار الأساسي للمشروع (يفترض أن السكريبت يُشغّل من جذر المشروع)
project_root = './'

# مجلد الكود الرئيسي
lib_folder = os.path.join(project_root, 'lib')

# ملف pubspec.yaml
pubspec_file = os.path.join(project_root, 'pubspec.yaml')

# ملف المخرجات (Markdown)
output_file = 'mobile-code.md'

# المجلدات المستثناة
excluded_dirs = {'build', '.dart_tool', '.idea', '.vscode', 'test'}

# دالة لكتابة ملف مع أرقام الأسطر
def write_file_with_lines(out_file, file_path, rel_path, lang):
    out_file.write(f"## File: `{rel_path}`\n\n")
    out_file.write(f"```{lang}\n")
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for i, line in enumerate(f, start=1):
                out_file.write(f"{i} {line.rstrip(chr(10))}\n")
    except Exception as e:
        out_file.write(f"// Error reading file: {e}\n")
    out_file.write("```\n\n")

with open(output_file, 'w', encoding='utf-8') as out_file:
    # 1. معالجة pubspec.yaml إذا كان موجوداً
    if os.path.isfile(pubspec_file):
        write_file_with_lines(out_file, pubspec_file, 'pubspec.yaml', 'yaml')
    else:
        out_file.write(f"## Warning: `pubspec.yaml` not found at {pubspec_file}\n\n")
    
    # 2. معالجة مجلد lib
    if os.path.isdir(lib_folder):
        for root, dirs, files in os.walk(lib_folder):
            # استبعاد المجلدات غير المرغوب فيها
            dirs[:] = [d for d in dirs if d not in excluded_dirs]
            
            for file in files:
                if file.endswith('.dart'):
                    file_path = os.path.join(root, file)
                    rel_path = os.path.relpath(file_path, start=project_root)
                    write_file_with_lines(out_file, file_path, rel_path, 'dart')
    else:
        out_file.write(f"## Warning: `lib` folder not found at {lib_folder}\n\n")

print(f"Done! Created {output_file} (Markdown with line numbers including pubspec.yaml)")