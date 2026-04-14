import os

# Configuration
project_root = './'
output_file = 'node_code.md'            # Markdown output
valid_extensions = ('.ts', '.js', '.json', '.mjs', '.env.example')
excluded_dirs = {
    'node_modules', 'dist', 'build', 'coverage',
    '.git', '.husky', '.vscode', 'out'
}
excluded_files = {'package-lock.json', 'yarn.lock', 'pnpm-lock.yaml'}

def get_language(ext):
    lang_map = {
        '.js': 'javascript', '.mjs': 'javascript',
        '.ts': 'typescript', '.json': 'json',
        '.env.example': 'text'
    }
    return lang_map.get(ext, 'text')

with open(output_file, 'w', encoding='utf-8') as out_file:
    for root, dirs, files in os.walk(project_root):
        dirs[:] = [d for d in dirs if d not in excluded_dirs]

        for file in files:
            if file.endswith(valid_extensions) and file not in excluded_files:
                file_path = os.path.join(root, file)
                rel_path = os.path.relpath(file_path, start=project_root)
                ext = os.path.splitext(file)[1]
                lang = get_language(ext)

                out_file.write(f"## File: `{rel_path}`\n\n")
                out_file.write(f"```{lang}\n")

                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        for i, line in enumerate(f, start=1):
                            out_file.write(f"{i} {line.rstrip(chr(10))}\n")
                except Exception as e:
                    out_file.write(f"// Error reading file: {e}\n")

                out_file.write("```\n\n")

print(f"Successfully compiled project into {output_file} (Markdown with line numbers)")