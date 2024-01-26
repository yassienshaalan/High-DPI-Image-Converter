import os
from PIL import Image
import time

# Sensibly increase the maximum number of pixels allowed
Image.MAX_IMAGE_PIXELS = 250000000  # Adjust based on your requirements, but keep it reasonable

def resize_image_to_increase_dpi(image, target_dpi):
    original_dpi = max(image.info.get('dpi', (72, 72)))  # Use the higher DPI if available, or default to 72
    scaling_factor = min(target_dpi / original_dpi, 2)  # Limit scaling to prevent excessively large images, adjust as needed

    new_width = int(image.width * scaling_factor)
    new_height = int(image.height * scaling_factor)
    resized_image = image.resize((new_width, new_height), Image.Resampling.LANCZOS)

    return resized_image

def get_dpi(image):
    dpi = image.info.get('dpi', (72, 72))  # Default DPI if not specified in the image
    return dpi

def get_user_input_dpi():
    while True:
        try:
            target_dpi = int(input("Enter the target DPI (e.g., 300): "))
            if target_dpi <= 0:
                print("DPI must be a positive integer. Please try again.")
            elif target_dpi > 1200:  # Setting an upper limit for practical purposes
                print("The entered DPI is unusually high. Please enter a value less than or equal to 1200.")
            else:
                return target_dpi
        except ValueError:
            print("Invalid input. Please enter an integer value for DPI.")



print("Starting the image DPI conversion and resizing process...")
print("This program will increase the DPI of each image to target dpi e.g. 300, resizing the pixel dimensions to maintain the physical size.")
print("Converted images will be saved in a 'Converted' directory with their size and DPI information updated.")

# Prompt the user for the target DPI with input validation
target_dpi = get_user_input_dpi()

parent_path = os.path.join(os.getcwd(), 'example')

directory = "Converted"
convert_path = os.path.join(parent_path, directory)

if not os.path.exists(convert_path):
    os.mkdir(convert_path)

i = 1
for filename in os.scandir(parent_path):
    if filename.is_file() and filename.path.endswith(('.png', '.jpg', '.jpeg')):
        try:
            start_time = time.time()
            im = Image.open(filename.path)
            original_size = im.size
            original_dpi = get_dpi(im)

            print(f"\nProcessing {filename.name}...")
            print(f"Original size: {original_size} pixels, DPI: {original_dpi}")

            im_resized = resize_image_to_increase_dpi(im, target_dpi)
            new_size = im_resized.size

            new_file = os.path.join(convert_path, f"Image{i}.png")
            i += 1

            im_resized.save(new_file, "PNG", dpi=(target_dpi, target_dpi))
            end_time = time.time()

            # Re-open the saved image to accurately check the new DPI
            with Image.open(new_file) as im_check:
                new_dpi = get_dpi(im_check)

            print(f"New size: {new_size} pixels, New DPI: {new_dpi}")
            print(f"Converted and resized {filename.name} and saved as {new_file}.")
            print(f"Time taken: {end_time - start_time:.2f} seconds.")

        except Exception as e:
            print(f"Error converting {filename.path}: {e}")
            continue
