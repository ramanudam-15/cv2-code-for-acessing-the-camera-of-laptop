import cv2

# Get the index of the front camera (usually 0 or 1)
front_camera_index = 0  # You may need to change this based on your system

# Create a VideoCapture object
cap = cv2.VideoCapture(front_camera_index)

# Check if the camera is opened successfully
if not cap.isOpened():
    print("Error: Could not open front camera.")
    exit()

# Set the window name
window_name = "Front Camera"

while True:
    # Read a frame from the camera
    ret, frame = cap.read()

    # Check if the frame is successfully read
    if not ret:
        print("Error: Failed to grab frame.")
        break

    # Display the frame in a window
    cv2.imshow(window_name, frame)

    # Break the loop if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('x'):
        break
    cv2.imshow(window_name, frame)

    # Break the loop if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('x'):
        break

# Release the VideoCapture and close the window
cap.release()
cv2.destroyAllWindows()