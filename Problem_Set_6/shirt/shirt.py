import sys
from PIL import Image, ImageOps

extensions = ['.jpg', '.jpeg', '.png']
if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
else:
    try:
        if (sys.argv[1][-4:] not in extensions) or (sys.argv[2][-4:] not in extensions):
            sys.exit("Invalid Input")
        elif sys.argv[1][-4:] != sys.argv[2][-4:]:
            sys.exit("Input and output have different extensions")
        else:
            #Open Images
            image1 = Image.open(sys.argv[1])
            shirt = Image.open('shirt.png')
            #Resize and crop them into the shirt's size
            width, height = shirt.size 
            image1 = ImageOps.fit(image1, size= (width, height))
            #Paste shirt onto image (mask= shirt, to make the background transparrent)
            image1.paste(shirt, mask= shirt)
            #Save merged images onto the output file in the 2nd command line argument
            image1.save(sys.argv[2])

    except FileNotFoundError:
        sys.exit("File does not exist")