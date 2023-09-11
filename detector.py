from PIL import Image

imagePath = input("Enter path to your image: ")
try:
    image = Image.open(imagePath)
except:
    print("Enter a valid image path")

newImage = Image.new(image.mode, image.size)

width, height = image.size
threshold = int(input("Enter the threshold value: "))
print(f"\n------\nWorking on your image:\n\tPath: {imagePath}\n\tSize: {width}x{height}\n\nPlease wait...")

# Define a threshold for color difference (you can adjust this value)


for x in range(1, width - 1):
    for y in range(1, height - 1):
        pixel_color = image.getpixel((x, y))
        left_color = image.getpixel((x - 1, y))
        right_color = image.getpixel((x + 1, y))
        top_color = image.getpixel((x, y - 1))
        bottom_color = image.getpixel((x, y + 1))

        # Calculate the color difference between the pixel and its surroundings
        diff_left = sum(abs(pixel_color[i] - left_color[i]) for i in range(3))
        diff_right = sum(abs(pixel_color[i] - right_color[i]) for i in range(3))
        diff_top = sum(abs(pixel_color[i] - top_color[i]) for i in range(3))
        diff_bottom = sum(abs(pixel_color[i] - bottom_color[i]) for i in range(3))

        if (
            diff_left > threshold
            or diff_right > threshold
            or diff_top > threshold
            or diff_bottom > threshold
        ):
            newImage.putpixel((x, y), (0, 0, 0))  # Set edge pixels to black
        else:
            newImage.putpixel((x, y), (255, 255, 255))  # Set non-edge pixels to white

newImage.save("modified_image.jpg")
print("-> DONE <-")
image.close()
newImage.close()
