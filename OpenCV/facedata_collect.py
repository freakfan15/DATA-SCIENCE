import cv2
import numpy as np

#Init camera
cap = cv2.VideoCapture(0)
#Face detect
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")

skip = 0
face_data = []
dataset_path = "./data/"
#face_section=[]

file_name = input("Enter the name of person: ")
while True:
    ret, frame = cap.read() # this fn returns 2 values 1. bool-means wether camera is active or not and second frame of camera

    if ret ==False:
        continue
    
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #giving the current frame to  harcasscade model
    faces = face_cascade.detectMultiScale(gray_frame,scaleFactor=1.3, minNeighbors=5)
    faces = sorted(faces, key=lambda f:f[2]*f[3])

    
    #iterating from largest to smallest face according to area(f[2]*f[3])
    for face in faces[-1:]:
        x,y,w,h = face
        cv2.rectangle(frame, pt1=(x,y), pt2=(x+w,y+h), color=(255,0,0),thickness=2)

        #extract(crop out the required face) :region of interest
        offset=10
        face_section  = frame[y-offset:y+h+offset,x-offset:x+w+offset]
        face_section = cv2.resize(face_section, (100,100))

        skip+=1
        if(skip%10 ==0):
            face_data.append(face_section)
            print(len(face_data))
        

    #using imshow method to show each frame
    cv2.imshow("Video Frame", frame)
    #cv2.imshow("Face Section", face_section)    

    #wait for  user input -q, then u will stop the loop
    key_pressed = cv2.waitKey(1) & 0xFF # bitwise operation converts 32 bit no to a 8 bit number for comaprison
    if key_pressed ==  ord('q'):
        break

#convert our face into a numpy array
face_data = np.asarray(face_data)
face_data = face_data.reshape((face_data.shape[0], -1))
print(face_data.shape)

#save this file into file system
np.save(dataset_path+file_name+'.npy', face_data)
print("Data successfully saved at"+ dataset_path+file_name+'.npy')

#finally release the camera and destroy all windows
cap.release()
cv2.destroyAllWindows()