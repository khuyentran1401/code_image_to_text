import cv2
import pytesseract
from rich.console import Console
from rich.syntax import Syntax
import argparse
from pathlib import Path


class CodeCleaner:
    def __init__(self, code=None):
        self.code = code 

    @staticmethod
    def replace_bad_characters(code):
        code = code.replace(">>>", "")
        code = code.replace("( )", "()")
        return code
    
    @staticmethod
    def remove_whitespace_one_sentence(code):
        return code.strip()

    def remove_whitespace_multiple_sentences(self, code):
        sentences = code.split("\n")
        return [self.remove_whitespace_one_sentence(sent) for sent in sentences]

    @staticmethod
    def is_empty_line(sent):
        return len(sent) == 0

    @staticmethod
    def sentences_list_to_string(sentences: list):
        return '\n'.join(sentences)
        
    # def add_tab(self, sentences: list) -> list:
    #     num_tabs = 0
    #     for i, sent in enumerate(sentences):
    #         if not self.is_empty_line(sent):
    #             if sent[-1]==":":
    #                 num_tabs += 1
    #                 sentences[i+1] = "\t"* num_tabs + sentences[i+1]
    #             else:
                    
    #     return sentences
            
    @staticmethod
    def detect_print_code(self, sentences):

        for sent in sentences:
            exec(sent)

    def clean(self):
        code = self.replace_bad_characters(self.code)
        sentences = self.remove_whitespace_multiple_sentences(code)
        # sentences = self.add_tab(sentences)
        code = self.sentences_list_to_string(sentences)
        return code

def convert_image_to_text(image_dir: str):
    img = cv2.imread(image_dir)
    return pytesseract.image_to_string(img)

def print_code_with_syntax(code: str, language: str, line_numbers=True):
    syntax = Syntax(code, language, theme='monokai', line_numbers=line_numbers)
    console = Console()
    console.print(syntax)

def get_file_name(dir_name: str):
    image_file = dir_name.split("/")[-1]
    return image_file.split(".")[0]

def save_code(args):
    if args.Output:
        filename = args.Output
    else:
        file_name = get_file_name(args.File)

    end_file_name = args.Extension
    file = Path(file_name + end_file_name)
    file.write_text(clean_code)

if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--File", help="Image file")
    parser.add_argument("-o", "--Output", help="Output file's name")
    parser.add_argument("-e", "--Extension", help="File extension for your output file, .i.e .py", default="")
    args = parser.parse_args()

    console = Console()

    if args.File:
        code = convert_image_to_text(args.File)
        clean_code = CodeCleaner(code).clean()

        print_code_with_syntax(clean_code, "python")

        save_code(args)
    else:
        console.print("Please insert your image file path using [bold green]`python code_recognizer.py -f your_image_file_name`[/bold green]")