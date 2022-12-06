from PIL import Image, ImageDraw, ImageFont
import os

# Path to the folder containing the images
IMAGES_FOLDER = "path/to/folder/with/images"

# Path to the watermark image
WATERMARK_IMAGE = "path/to/watermark/image.png"

# Folder where the watermarked images will be saved
WATERMARKED_IMAGES_FOLDER = "path/to/folder/for/watermarked/images"

# Desired width of the watermark image in pixels
WATERMARK_WIDTH = 150

# Load the watermark image and get its size
watermark = Image.open(WATERMARK_IMAGE)
watermark_width, watermark_height = watermark.size

# Calculate the new height of the watermark image, preserving the aspect ratio
watermark_height_new = int(watermark_height * WATERMARK_WIDTH / watermark_width)

# Resize the watermark image to the desired width and height
watermark_resized = watermark.resize((WATERMARK_WIDTH, watermark_height_new), Image.ANTIALIAS)

# Iterate over the images in the folder
for filename in os.listdir(IMAGES_FOLDER):
    # Open the image
    image = Image.open(os.path.join(IMAGES_FOLDER, filename))

    # Calculate the position of the watermark in the bottom left corner of the image
    x = 0
    y = image.height - watermark_height_new
    position = (x, y)

    # Create an ImageDraw object
    draw = ImageDraw.Draw(image)

    # Paste the resized watermark image onto the main image
    image.paste(watermark_resized, position, watermark_resized)

    # Save the watermarked image with a new name in the specified folder
    watermarked_filename = "watermarked_" + filename
    watermarked_filepath = os.path.join(WATERMARKED_IMAGES_FOLDER, watermarked_filename)
    image.save(watermarked_filepath)
