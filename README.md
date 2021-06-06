# Code Image to Text Converter

Convert code image into text.

For example, if you want to extract code from the image named `images/carbon.png`.
![image](https://github.com/khuyentran1401/code_image_to_text/blob/master/images/carbon.png?raw=True)

Type:
```bash
python -m image_converter images/carbon.png .py
```
will convert the image to text like below and save the code to the file named `carbon.py`.

```python
class DataLoader:

	 def __init__(self, data_dir: str):
		 self.data_dir = data_dir

		 print("Instance is created")
	 def __call__(self):

		 print("Instance is called")

data_loader = DataLoader('my_data_dir')

data_loader()

```

# Installation
## Intall Tesseract
* Linux
```bash
sudo apt-get update
sudo apt-get install tesseract-ocr
sudo apt-get install libtesseract-dev
```

* Windows
Install from [here](https://github.com/UB-Mannheim/tesseract/wiki)
## Install code-image-to-text
```bash
pip install code-image-to-text
```



