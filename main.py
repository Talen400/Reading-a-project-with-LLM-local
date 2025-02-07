import ollama
from generateOut import GenerateOutput

def generate_ai(content, msg, model):
    print("-----------------------------")
    prompt = f"{msg}: \n {content} "
    response = ollama.generate(model=model, prompt=prompt)
    print(f"{response['response']}\n")
    
    with open("README.md", "w", encoding="utf-8") as output_file:
        output_file.write(response['response'])

def read_txt_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        return content
    except Exception as e:
        return f"Error reading the file: {e}"

if __name__ == "__main__":
    ai_model = " model " # Example: deepseek-r1:1.5b
    intermediate_file = "Out.txt"
    directory_path = "Your project directory"
    ignore_dirs_list = [".git", "__pycache__", ".venv"]
    ignore_files_list = ["README.md", ".env", ".git"] 
    msg = """
    You are an assistant who creates README files for software projects.
    From the directory structure and scripts below, generate a short README that describes the project in a general way.
    """

    generator = GenerateOutput(directory_path, ignore_dirs_list, ignore_files_list, intermediate_file)
    generator.save_to_file()

    content = read_txt_file(intermediate_file)

    generate_ai(content, msg, ai_model)