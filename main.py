from PIL import Image, ImageFilter, ImageEnhance
# with Image.open("jpg.6.jpg")as file:
#     #file.show()
#     print("Розмір фото:", file.size)
#     print("Формат файлу:",file.format)
#     print("Колірний формат:", file.mode)
#     gray=file.convert("L")
#     gray.save("gray.jpg")
#     blured=file.filter(ImageFilter.BLUR)
#     blured.save("blured.jpg")
#     up = file.transpose(Image.ROTATE_180)
#     up.save("up.jpg")    
#     mirror=file.transpose(Image.FLIP_LEFT_RIGHT)
#     mirror.save("mirror.jpg")
#     pic_contrast = ImageEnhance.Contrast(file)
#     pic_contrast = pic_contrast.enhance (1.5)
#     pic_contrast.save("pic_contrast.jpg")
class ImageEditor:
    def __init__(self,name):
        self.name=name
        self.original=""
        self.files=[]
        self.counter=1
    def open(self):
        try:
            self.original=Image.open(self.name)
            self.files.append(self.original)
        except:
            print("Назва вказана не вірно!")
    def do_left(self):
        left=self.original.transpose(Image.ROTATE_90)
        self.files.append(left)
        new=self.name.split(".")
        left.save(new[0]+str(self.counter)+"."+new[1])
        self.counter+=1

    def do_cropped(self):
        box=(20,20,20,20)
        cropped=self.original.crop(box)
        self.files.append(cropped)
        new=self.name.split(".")
        cropped.save(new[0]+str(self.counter)+"."+new[1])
        self.counter+=1

image=ImageEditor("6.jpg")
image.open()
image.do_left()
image.do_cropped()
for file in image.files:
    file.show()
