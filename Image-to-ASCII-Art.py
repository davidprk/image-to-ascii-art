# Importing Pillow (image library)
from PIL import Image, ImageEnhance
   
#
# Receiving user input
#
valid_pathname = False
while not valid_pathname:
    
    try:
        print("Enter a valid pathname to an image: ")
        
        pathname = input()
        
        image = Image.open(pathname)
    except:
        print("Given invalid pathname. Please try again.")
    else:
        valid_pathname = True

# ASCII Chars from darkest to lightest: $@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,"^`'.
