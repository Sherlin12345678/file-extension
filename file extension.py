Python 3.10.5 (tags/v3.10.5:f377153, Jun  6 2022, 16:14:13) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
filename = input("Input Filename: ")
Input Filename: abc.python
f_extns = filename.split(".")
print("The extension of the file is : " + repr(f_extns[-1]))
The extension of the file is : 'python'
