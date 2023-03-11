import cv2
import face_recognition


img=cv2.imread('Messi1.jpg')
resize=cv2.resize(img,(400,400))
rgb_img=cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_encoding=face_recognition.face_encodings(rgb_img)[0]

img1=cv2.imread('messi-hair.jpg')
resize1=cv2.resize(img1, (400,400))
rgb_img1=cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
img_encoding2=face_recognition.face_encodings(rgb_img1)[0]

result=face_recognition.compare_faces([img_encoding],img_encoding2)
print("result:",result)

cv2.imshow("image",resize)
cv2.imshow("elon",resize1)
cv2.waitKey(0)
cv2.destroyAllWindows()