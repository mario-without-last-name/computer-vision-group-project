from PIL import Image

# Open the image
img = Image.open("penjelasan color space yang cukup merah.png")

# Get the width and height of the image
width, height = img.size

# Convert the image to RGB format
rgb_img = img.convert("RGB")

# Iterate over every pixel in the image
for x in range(width):
    for y in range(height):
        # Get the RGB values of the pixel
        r, g, b = rgb_img.getpixel((x, y))
        
        # Check if Red value is less than the Green + Blue value
        if r <= g + b:
            # Set the pixel to black
            rgb_img.putpixel((x, y), (0, 0, 0))

# Save the modified image
rgb_img.save("modified_image.jpg")