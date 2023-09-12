from PIL import Image

def open_image(image_path):
    try:
        image = Image.open(image_path)
        return image
    except Exception as e:
        print(f"Error: {e}")
        return None

def process_image(image, threshold):
    if image is None:
        return None

    new_image = Image.new(image.mode, image.size)
    width, height = image.size

    for x in range(1, width - 1):
        for y in range(1, height - 1):
            pixel_color = image.getpixel((x, y))
            left_color = image.getpixel((x - 1, y))
            right_color = image.getpixel((x + 1, y))
            top_color = image.getpixel((x, y - 1))
            bottom_color = image.getpixel((x, y + 1))

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
                new_image.putpixel((x, y), (0, 0, 0))  # Set edge pixels to black
            else:
                new_image.putpixel((x, y), (255, 255, 255))  # Set non-edge pixels to white

    return new_image

def main():
    image_path = input("Enter path to your image: ")
    threshold = int(input("Enter the threshold value: "))

    outputImage = open_image(image_path)
    if outputImage:
        processed_image = process_image(outputImage, threshold)
        if processed_image:
            output_path = "modified_image.jpg"
            processed_image.save(output_path)
            print(f"Modified image saved as {output_path}")
            original_image.close()
            processed_image.close()
            print("-> DONE <-")

if __name__ == "__main__":
    main()
