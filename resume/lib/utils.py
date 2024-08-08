import os
import markdown2

def read_file(file_path):
    """
    Reads the content of a file and returns it. Handles file not found and other exceptions.
    
    :param file_path: Path to the file.
    :return: Content of the file.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        exit(1)
    except Exception as e:
        print(f"Error: {e}")
        exit(1)

def convert_markdown_to_html(markdown_content):
    """
    Converts Markdown content to HTML using markdown2.

    :param markdown_content: Content in Markdown format.
    :return: HTML content as a string.
    """
    return markdown2.markdown(markdown_content)

def save_temp_html(html_content, folder_path, file_name):
    """
    Saves the HTML content to a specified folder and file.

    :param html_content: HTML content to save.
    :param folder_path: Path to the folder where the file will be saved.
    :param file_name: Name of the HTML file.
    """
    try:
        os.makedirs(folder_path, exist_ok=True)
        file_path = os.path.join(folder_path, file_name)
        with open(file_path, 'w', encoding='utf-8') as temp_file:
            temp_file.write(html_content)
        print(f"Temporary HTML saved to: {file_path}")
    except Exception as e:
        print(f"Error saving temporary HTML: {e}")
        exit(1)
