import cv2
import dropbox

def take_snapshot():
    videoCaptureObject = cv2.VideoCapture(0)
    ret,frame =videoCaptureObject.read()
    print(ret)
    cv2.imwrite("newimage.jpg",frame)
    videoCaptureObject.release()

# name = input("Enter image name")  
take_snapshot()

accesstoken = "INSERT ACCESS TOKEN"

dbx = dropbox.Dropbox(accesstoken)

path = "newimage.jpg"

fileContent = open(path, "rb").read()

# dbx.files_upload(FILECONTENT, DESTINATION PATH, mode=dropbox.files.WriteMode.overwrite)

dbx.files_upload(fileContent, "/modulecopy.py", mode=dropbox.files.WriteMode.overwrite)


