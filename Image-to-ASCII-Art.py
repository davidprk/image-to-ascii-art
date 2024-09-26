# Importing Pillow (image library)
from PIL import Image, ImageEnhance
   
def main(new_width = 150):
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

    #
    # Converting image to ASCII art
    #
    
    # Receives the ASCII art as one line
    line_image = image_to_ascii(resized_grayscale)
    for i in range(0, len(line_image), new_width):
        print(line_image[i:i+new_width])
    
def resize(image, new_width = 150):
    width, height = image.size
    ratio = height / width / 1.65
    
    new_height = int(ratio * new_width)
    resized_image = image.resize((new_width, new_height))
    
    return resized_image

def image_to_ascii(image):
    ascii_chars = ['@', '#', '%', '*', '+', '-', '.', ' ', '`', '"']

    pixels = image.getdata()
    
    characters = []
    for pixel in pixels:
        characters.append(ascii_chars[pixel // 26])
        
    return "".join(characters)
            
main()