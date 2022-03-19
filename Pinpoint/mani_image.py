from PIL import Image
def resizeImage(size, image_file):
    image = Image.open(image_file)
    resized_image = image.resize((size, size))
    print(str(size) + "_" +image_file)
    resized_image.save(str(size) + "_" +image_file)
def makeImageTransparent(image_file):
    image = Image.open(image_file)
    rgba = image.convert("RGBA")
    datas = rgba.getdata()
    newData = []
    for item in datas:
        if item[0] == 0 and item[1] == 0 and item[2] == 0:
            newData.append((255, 255, 255, 0))
        else:
            newData.append(item)
    rgba.putdata(newData)
    rgba.save("50_" + image_file, "PNG")
resizeImage(50, "friend.png")