from PIL import Image
from PIL import ImageOps
import sys

def main():
    if len(sys.argv) == 3:
        firstarg = sys.argv[1].split('.')[1]
        secondarg = sys.argv[2].split('.')[1]
        if firstarg == secondarg:
            if secondarg in ['jpg','jpeg','png']:
                try:
                    image = Image.open(sys.argv[1])
                except FileNotFoundError:
                    sys.exit('Input does not exist')
                tshirt = Image.open('shirt.png')
                size = tshirt.size
                muppet = ImageOps.fit(image, size)
                muppet.paste(tshirt,tshirt)
                muppet.save(sys.argv[2])
            else:
                sys.exit('Invalid Output')
        else:
            sys.exit('Input and output have different extensions')
    elif len(sys.argv) <= 2:
        sys.exit('Too few command-line arguments')
    elif len(sys.argv) > 3:
        sys.exit('Too many command-line arguments')

if __name__ == "__main__":
    main()

