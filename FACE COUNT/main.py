import cv2


# Load the cascades
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#initialize face count to 0 
total_face_count = 0
#generate id
#count id 


# Open the webcam
video_capture = cv2.VideoCapture(0)

while True:
    # Read a frame from the webcam
    _, frame = video_capture.read()

    # Convert the frame to grayscale
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the frame
    faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5)

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
    
    # Show the frame and the number of faces detected
    font = cv2.FONT_HERSHEY_SIMPLEX
    text = f'{len(faces)} faces detected'
    cv2.putText(frame, text, (10, 50), font, 1, (255, 255, 255), 2, cv2.LINE_AA)
    

#counting    
    num_faces = len(faces)
    total_face_count += num_faces
 
    
    print(len(faces))
    cv2.imshow('PEOPLE COUNTING', frame)
    # Check if the user pressed the 'q' key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam
video_capture.release()
cv2.destroyAllWindows()

