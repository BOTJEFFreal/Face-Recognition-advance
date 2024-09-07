import os
import cv2

# Specify the directory containing PNG images
input_folder = "./pngPics"
output_folder = "./jpgPics"

# Create the output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Iterate over all files in the input folder
for filename in os.listdir(input_folder):
    if filename.endswith(".png"):  # Check if the file is a PNG
        # Construct full file path
        png_path = os.path.join(input_folder, filename)
        
        # Read the PNG image
        image = cv2.imread(png_path)
        
        if image is not None:  # Ensure the image was successfully loaded
            # Change the file extension to .jpg
            jpg_filename = filename.rsplit(".", 1)[0] + ".jpg"
            jpg_path = os.path.join(output_folder, jpg_filename)
            
            # Save the image in JPG format
            cv2.imwrite(jpg_path, image)
            print(f"Converted {filename} to {jpg_filename}.")
        else:
            print(f"Failed to read {filename}. Skipping.")

print("Conversion complete.")
