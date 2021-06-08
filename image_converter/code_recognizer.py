import cv2
import pytesseract
from rich.console import Console
from rich.syntax import Syntax
from pathlib import Path
import typer

app = typer.Typer(name="code-image-to-text",
                  add_completion=True, help="Convert code image to text")


class CodeCleaner:
    def __init__(self, code=None):
        self.code = code

    @staticmethod
    def _remove_outputs(code: str):
        lines = code.split("\n")
        inputs = []
        for line in lines:
            if line.startswith('>>>'):
                line = line.replace('>>> ', '')
                inputs.append(line)
            elif line.startswith('see'):
                line = line.replace('see', '\t')
                inputs.append(line)
            elif line.startswith('wee'):
                line = line.replace('wee', '\t\t')
                inputs.append(line)
            elif line == '':
                inputs.append(line)
        if inputs == []:
            inputs = lines
        return '\n'.join(inputs)

    @classmethod
    def replace_bad_characters(cls, code):
        if '>>>' in code:
            code = cls. _remove_outputs(code)
        code = code.replace("( ", "(")
        code = code.replace(" )", ")")
        return code

    @staticmethod
    def is_empty_line(sent):
        return len(sent) == 0

    @staticmethod
    def detect_print_code(self, sentences):
        for sent in sentences:
            exec(sent)

    def clean(self):
        code = self.replace_bad_characters(self.code)
        return code


def convert_image_to_text(image_dir: str):
    """Turn image code into text"""

    img = cv2.imread(image_dir)
    custom_oem_psm_config = (r"--psm 6")

    return pytesseract.image_to_string(img, config=custom_oem_psm_config)


def print_code_with_syntax(file: str):
    syntax = Syntax.from_path(file, theme='monokai', line_numbers=True)
    console = Console()
    console.print(syntax)


def get_file_name(dir_name: str):
    image_file = dir_name.split("/")[-1]
    return image_file.split(".")[0]


def save_code(filename: str, output: str, extension: str, clean_code: str):
    if not output:
        output = get_file_name(filename)

    file = Path(output + extension)
    file.write_text(clean_code)
    return file


@app.command()
def main(filename: str = typer.Argument(..., help='Image file'),
         extension: str = typer.Argument(
             ..., help="File extension for your output file, .i.e .py"),
         output: str = typer.Argument(None, help="Output file's name")):

    code = convert_image_to_text(filename)
    clean_code = CodeCleaner(code).clean()
    save_file = save_code(filename, output, extension, clean_code)
    print_code_with_syntax(save_file)


if __name__ == '__main__':

    app()
