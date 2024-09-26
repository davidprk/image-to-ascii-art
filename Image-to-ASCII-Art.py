# Importing Pillow (image library)
from PIL import Image, ImageEnhance
   
def main():
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

    #
    # Image reformatting (change to grayscale image of a given size)
    #

    # Resizing image
    resized_image = resize(image)

    # Creating enhancer for given image
    resized_grayscale = resized_image.convert("L")
    resized_grayscale.show()

    #
    # Converting image to ASCII art
    #

    # ASCII Chars from darkest to lightest: $@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,"^`'.
    
def resize(image, new_width = 300):
    width, height = image.size
    ratio = height / width
    
    new_height = int(ratio * new_width)
    resized_image = image.resize((new_width, new_height))
    
    return resized_image

main()