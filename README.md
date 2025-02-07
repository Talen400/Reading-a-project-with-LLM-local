# Project Overview

## 📌 Introduction
This project provides a means for your LLM and your project to be studied locally.

## 📂 Project Structure
- `requirements.txt` - Lists the required dependencies for the project.
- `GenerateClass.py` - This is the script that will read and generate a tree so that LLM can understand your project.
- `.gitignore` - Specifies which files Git should ignore.
- `main.py` - File where LLM will be called and what to do, which files to ignore and which to read

## 🚀 Getting Started
### Prerequisites
Ensure you have Python and OLLAMA installed. You can install the dependencies by running:
```bash
pip install -r requirements.txt
```

### Installing OLLAMA
Follow the official site to install OLLAMA: [OLLAMA Installation](https://ollama.com)

### Configuring Environment Variables
Before running the project, ensure the necessary variables are set up. Below are the required variables and how to configure them in `__main__`:
- `ai_model`: Which model will you use
- `directory_path`: The directory of the project to be read
- `ignore_dirs_list`: Which subdirectories will be ignored by LLM. Example: __pycache__
- `ignore_files_list`: Which files will be ignored by LLM
- `msg`: The prompt for what LLM will answer after reading the project
- 
### Running the Project
To execute, use:
```bash
python main.py
```

## 🛠 Troubleshooting
- Ensure all dependencies are installed.
- Verify that OLLAMA is installed, configured correctly and running.

## 📌 Additional Notes
- Modify `.gitignore` as needed to include/exclude files.
- Contributions and improvements are welcome!

## 📜 License
This project is licensed under [MIT License](LICENSE).
