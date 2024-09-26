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

    #
    # Converting image to ASCII art
    #
    image_to_ascii(resized_grayscale)
    
    # ASCII Chars from darkest to lightest: $@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,"^`'.
    
def resize(image, new_width = 150):
    width, height = image.size
    ratio = height / width
    
    new_height = int(ratio * new_width)
    resized_image = image.resize((new_width, new_height))
    
    return resized_image

def image_to_ascii(image):
    ascii_chars = ['@', '#', 'S', '%', '?', '*', '+', ';', ':', '.']
    pixels = image.load()
    print(pixels)
    
    for y in range(image.size[1]):
        for x in range(image.size[0]):
            brightness = pixels[x, y]
            
            if brightness <= 255 and brightness > 230:
                print('@', end = "")
            elif brightness <= 230 and brightness > 205:
                print('#', end = "")
            elif brightness <= 205 and brightness > 180:
                print('S', end = "")
            elif brightness <= 180 and brightness > 155:
                print('%', end = "")
            elif brightness <= 155 and brightness > 130:
                print('?', end = "")
            elif brightness <= 130 and brightness > 105:
                print('*', end = "")
            elif brightness <= 105 and brightness > 80:
                print('+', end = "")
            elif brightness <= 80 and brightness > 55:
                print(';', end = "")
            elif brightness <= 55 and brightness > 30:
                print(':', end = "")
            else:
                print('.', end = "")

        print("\n")
            
main()