import os

class GenerateOutput:
    def __init__(self, directory, ignore_dirs=None, ignore_files=None, output_filename="output.txt"):
        self.directory = directory
        self.ignore_dirs = ignore_dirs if ignore_dirs else []
        self.ignore_files = ignore_files if ignore_files else []
        self.output_filename = output_filename

    def read_file_content(self, file_path):
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                return file.read()
        except Exception as e:
            return f"Error reading file {file_path}: {e}"

    def read_directory_structure(self):
        structure = ""
        for root, dirs, files in os.walk(self.directory):
            dirs[:] = [d for d in dirs if d not in self.ignore_dirs]
            files = [f for f in files if f not in self.ignore_files]

            level = root.replace(self.directory, "").count(os.sep)
            indentation = " " * 4 * level
            structure += f"{indentation}- {os.path.basename(root)}/\n"
            sub_indentation = " " * 4 * (level + 1)
            for file in files:
                structure += f"{sub_indentation}- {file}\n"
        return structure

    def list_contents(self):
        content_list = []
        for root, dirs, files in os.walk(self.directory):
            dirs[:] = [d for d in dirs if d not in self.ignore_dirs]
            for file in files:
                if file not in self.ignore_files:
                    full_path = os.path.join(root, file)
                    content = self.read_file_content(full_path)
                    content_list.append((full_path, content))
        return content_list

    def save_to_file(self):
        structure = self.read_directory_structure()
        contents = self.list_contents()
        with open(self.output_filename, "w", encoding="utf-8") as output_file:
            output_file.write("Directory structure:\n")
            output_file.write(structure + "\n\n")
            output_file.write("List of file contents:\n")
            for i, (path, content) in enumerate(contents, start=1):
                output_file.write(f"\n--- File {i} content: {path} ---\n")
                output_file.write(content + "\n")
        print(f"Output saved to '{self.output_filename}'.")

"""
Example to test:

if __name__ == "__main__":
    directory_path = "C:/Users/ricar/OneDrive/Desktop/readmeGenerator"
    ignore_dirs_list = [".git", "__pycache__", ".venv"]
    ignore_files_list = ["README.md", ".env"]  

    generator = GenerateOutput(directory_path, ignore_dirs_list, ignore_files_list)
    generator.save_to_file()
"""
