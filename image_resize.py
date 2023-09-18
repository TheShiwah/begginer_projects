# install pillow
# import pillow
# open up the image we want to resize
# print the current size of that image
# specify the size we want change it to
# save the new resized image

from PIL import Image


def resize_image(size1, size2):
    image = Image.open('test.jpg')

    print(f"Current size : {image.size}")

    resized_image = image.resize((size1, size2))

    resized_image.save('test2-' + str(size1) + str(size2)+'.jpeg')


size1 = int(input('Enter width: '))
size2 = int(input('Enter length: '))
resize_image(size1, size2)

