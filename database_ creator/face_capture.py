import cv2
import os

# Define the parent folder where images will be saved
parent_folder = "captured_images"

# Create the parent folder if it does not exist
if not os.path.exists(parent_folder):
    os.makedirs(parent_folder)

# Prompt user for a folder name to save the images inside the parent folder
folder_name = input("Enter a name for the folder to save images: ")

# Create the path for the user-specified folder inside the parent folder
save_folder = os.path.join(parent_folder, folder_name)
if not os.path.exists(save_folder):
    os.makedirs(save_folder)

# Open the camera
cap = cv2.VideoCapture(0)  # 0 is the default camera

# Check if the camera opened successfully
if not cap.isOpened():
    print("Error: Could not open the camera.")
    exit()

# Number of images to capture
num_images = 200

print("Press 'q' to quit early...")

for i in range(num_images):
    ret, frame = cap.read()

    if not ret:
        print(f"Failed to grab frame {i+1}")
        break

    # Show the frame on screen
    cv2.imshow("Capturing", frame)

    # Save the frame in color with the folder name as part of the image name
    image_path = os.path.join(save_folder, f"{folder_name}_{i+1}.jpg")
    cv2.imwrite(image_path, frame)
    print(f"Saved {image_path}")

    # Wait for a short period before capturing the next frame
    key = cv2.waitKey(100)  # 100 ms delay between captures
    if key & 0xFF == ord('q'):
        print("Early exit requested.")
        break

# Release the camera and close windows
cap.release()
cv2.destroyAllWindows()

print("Finished capturing images.")
