from PIL import Image,ImageFilter

img = Image.open('./pocedek/pikachu.jpg') #open image in python
img1 = Image.open('./pocedek/bulbasaur.jpg') 
img2 = Image.open('./pocedek/charmander.jpg')
img3 = Image.open('./pocedek/charmander.jpg')
img4 = Image.open('./pocedek/squirtle.jpg')
box =(100,100,400,400)
region = img4.crop(box)


filtered_img = img.filter(ImageFilter.BLUR)   #using filter on image for blur the image
filtered_img1 = img1.filter(ImageFilter.SHARPEN) #using filter for sharpen the image
filtered_img2 = img2.convert('L')   #to convert image in grey (black and white)
filtered_img2 = img2.convert('1')  #to convert image in grey dotted format
filtered_img3 = img3.convert('P') #to convert image in colour dotted format
resize= img3.resize((100,100))
img4.thumbnail((400,100)) # when use thumbnail it didn't give exact ration which you has written it return in an aspct set 
                        #  set by itself best aspect for thumbnail

print(img.format)  # to check format of image
print(img.size)  #to check size of image
print(img.mode)  #to check mode of image
filtered_img.save("blur.png",'png')  #to save image by its name and format
filtered_img1.save("sharpen.jpg",'jpeg')
filtered_img2.save("grey.jpg",'jpeg')
filtered_img3.save("grey.png",'png')
# filtered_img2.show() # showing converted image in new pop-window
resize.save('resize.png','png')
region.save('crop.png','png')
img4.save('thumbnail.jpg','jpeg')
print(img)


