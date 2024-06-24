import cv2
cap = cv2.VideoCapture(0)  
if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Could not read frame from camera.")
        break

    
    img = cv2.GaussianBlur(frame, (15, 15), 0)
    if img is not None and img.shape[0] > 0 and img.shape[1] > 0:
        cv2.imshow("Blurred Face", img)
    else:
        print("Error: Processed image is invalid.")

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
