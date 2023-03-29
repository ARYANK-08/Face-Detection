import cv2 
import imutils
from imutils.video import VideoStream
import mediapipe as mp 
import time 
import psycopg2

# Load Face Detection 
face_detection = mp.solutions.face_detection.FaceDetection()

# Take Video From Webcam
cap = VideoStream(src=0).start()

# Track Attention Spanq
starting_time = time.time()
last_elapsed_time = 0
alert_time=10
flag = True
while True:
    
    
    # Read Frame from video webcam
    frame = cap.read()
    height, width, channels = frame.shape
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Draw a Rectangle
    cv2.rectangle(frame, (0, 0), (width, 70), (128,128,128), -1)

    # Face Detection
    results = face_detection.process(rgb_frame)

    # Is the face Detected?
    if results.detections:
        elapsed_time = int(time.time() - starting_time)
        
        if elapsed_time > alert_time:
            cv2.rectangle(frame ,(0,0),(width,height), (0,0,0),20)
            cv2.putText(frame,"Look At the Customer!" ,(20,200),cv2.FONT_HERSHEY_PLAIN,3,(0,20,215),4)
            cv2.setWindowProperty("Frame",cv2.WND_PROP_TOPMOST,1 )

        last_elapsed_time = elapsed_time
        print("Elapsed: {}".format(elapsed_time))
        print("Face is looking at the billboard")
        flag = True 
    else:
        starting_time=time.time()
        elapsed_time = 0
        if flag==True :
            #Reset the counter 
            starting_time=time.time()
            elapsed_time = 0
            print(last_elapsed_time)
            print("No faces")
            
            #Comment out database part if you dont want db
            conn = psycopg2.connect(
                host="localhost",
                user="postgres",
                password="yourpassword",
                database="postgres"
            )
            if last_elapsed_time !=0:
                cur = conn.cursor()
                cur.execute("INSERT INTO time (AttentionSpan) VALUES (%s)", (last_elapsed_time,)) 
                conn.commit()
                cur.close()
                conn.close()
            flag = False

            
            # Display Frame 
        print(last_elapsed_time)

    cv2.putText(frame, "{} seconds".format(elapsed_time), (10, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 255, 255), 4)
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()





