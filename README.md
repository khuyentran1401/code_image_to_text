# Code Image to Text Converter

Convert code in image to text and save it to a file.

For example, if you want to extract code from this image.
![image](images/carbon_2.png)

Typing
```bash
python code_recognizer.py -f name_of_your_image_file -e .py
```
will generate this output
![image](images/output.png)

and save the code to `name_of_your_image_file.py` in your current directory.

Note that there is no tab in the output code so you will need to add indentation to make it look like the original code.

# Install dependencies
## Intall Tesseract
* Linux
```bash
sudo apt-get update
sudo apt-get install tesseract-ocr
sudo apt-get install libtesseract-dev
```

* Windows
Install from [here](https://github.com/UB-Mannheim/tesseract/wiki)



