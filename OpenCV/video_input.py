#Read a    video stream from camera frame by frame
from cv2 import cv2

cap = cv2.VideoCapture(0)
#using harcascade cascade face classifier
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")


while True:
    ret, frame = cap.read() # this fn returns 2 values 1. bool-means wether camera is active or not and second frame of camera
    #for grayscale video
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    if ret ==False:
        continue

    scalingfactor = 1.3
    NoOfNeighbours = 5
    #giving the current frame to  harcasscade model
    faces = face_cascade.detectMultiScale(gray_frame,scaleFactor=1.3, minNeighbors=5)

    '''drawing a rectangle arround the face
    this.deteMultiScale fn returns (x,y,weidth,height) [list of these tuples]. means one tuple for each image.
    so if there are three images it returns smthing like
    [(,2,3,4), (4,5,6,7), (6,5,4,3)]'''
    for (x,y,w,h) in faces:
        cv2.rectangle(frame, pt1=(x,y), pt2=(x+w,y+h), color=(255,0,0),thickness=2)
    
    #using imshow method to show each frame
    cv2.imshow("Video Frame", frame)
    #cv2.imshow("Gray Frame", gray_frame)

    #wait for  user input -q, then u will stop the loop
    key_pressed = cv2.waitKey(1) & 0xFF # bitwise operation converts 32 bit no to a 8 bit number for comaprison
    if key_pressed ==  ord('q'):
        break

#finally release the camera and destroy all windows
cap.release()
cv2.destroyAllWindows()
