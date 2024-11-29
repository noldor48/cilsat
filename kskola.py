from PIL import Image, ImageFilter

try:  
    original = Image.open("images.png")  
    print("file exist")
    print("Размер изображения:")  
    print(original.format, original.size, original.mode)
    original.show()
except FileNotFoundError:  
    print("Файл не найден")
