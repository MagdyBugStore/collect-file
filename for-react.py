import os

# 1. Project directory (React usually puts source code in 'src')
project_path = './src'  
output_file = 'react_code.md'          # Markdown output

# 2. Define extensions to include
valid_extensions = ('.js', '.jsx', '.ts', '.tsx', '.css', '.json')

# 3. Directories to skip
excluded_dirs = {'node_modules', 'dist', 'build', '.git'}

# Helper to get language for code fence
def get_language(ext):
    lang_map = {
        '.js': 'javascript', '.jsx': 'jsx',
        '.ts': 'typescript', '.tsx': 'tsx',
        '.css': 'css', '.json': 'json'
    }
    return lang_map.get(ext, 'text')

with open(output_file, 'w', encoding='utf-8') as out_file:
    for root, dirs, files in os.walk(project_path):
        # Skip excluded directories
        dirs[:] = [d for d in dirs if d not in excluded_dirs]
        
        for file in files:
            if file.endswith(valid_extensions):
                file_path = os.path.join(root, file)
                rel_path = os.path.relpath(file_path, start='.')
                ext = os.path.splitext(file)[1]
                lang = get_language(ext)

                # Write Markdown heading
                out_file.write(f"## File: `{rel_path}`\n\n")
                out_file.write(f"```{lang}\n")

                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        # Write line numbers
                        for i, line in enumerate(f, start=1):
                            out_file.write(f"{i} {line.rstrip(chr(10))}\n")
                except Exception as e:
                    out_file.write(f"// Error reading file: {e}\n")

                out_file.write("```\n\n")

print(f"Done! Created {output_file} (Markdown with line numbers)")