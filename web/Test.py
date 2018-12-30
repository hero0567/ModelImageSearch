import os

if __name__ == '__main__':
    amazon_path = "images\\Reference images\\Amazom"
    imageName = amazon_path.split(os.path.sep)[-1]
    dotIndex = imageName.find(".");
    print(dotIndex)
    print(imageName[0:dotIndex])
    print(os.path.sep)