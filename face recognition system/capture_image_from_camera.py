import cv2

cam_port = 1
cam = cv2.VideoCapture(cam_port)

# Ensure the camera is opened successfully
if not cam.isOpened():
    print("Error: Could not open camera.")
else:
    # Reading the input using the camera
    inp = input('Enter person name: ')
    
    while True:
        result, image = cam.read()
        if result:
            cv2.imshow("Camera Feed", image)
            # Wait for 's' key to save the image
            if cv2.waitKey(1) & 0xFF == ord('s'):
                cv2.imwrite(f"{inp}.png", image)
                print("Image taken")
                break
        else:
            print("No image detected. Please try again.")
            break

    # Release the camera and close all windows
    cam.release()
    cv2.destroyAllWindows()
