import PIL.Image

#setup the ASCII used to build the output text
ascii_chars = ['@','#','S','%','?','*','+',';',':',',','.']

#resize image based on a new width
def resize_image(image, new_width = 100):
    width, height = image.size
    ratio = height / width
    new_height = int(new_width * ratio)
    resized_image = image.resize((new_width, new_height))
    return(resized_image)

#converting pixels into grascale
def gray_scale(image):
    grayscale_image = image.convert("L")
    return(grayscale_image)

# converting pixels to a string of ASCII characters
def pixels_to_ascii(image):
    pixels = image.getdata()
    characters = "".join([ascii_chars[pixel//25] for pixel in pixels])
    return(characters)


def main(new_width):
    # attempting to open the image
    path = input("Enter a valid pathname to an image: \n")
    try:
        image = PIL.Image.open(path)
    except:
        print(path, " is not a valid pathname")
    
    # converting image to ASCII
    new_image_data = pixels_to_ascii(gray_scale(resize_image(image)))

    #format
    pixel_count = len(new_image_data)
    ascii_image = "\n".join(new_image_data[i : (i+new_width)] for i in range(0, pixel_count, new_width))

    #printing the result

    print(ascii_image)

    #save the result to a text file
    with open("ascii_image.txt","w") as f:
        f.write(ascii_image)
main(100)