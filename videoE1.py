import cv2
import os

def video(path, out):


    pre_imgs = os.listdir(path)
    img = []
    for i in pre_imgs:
        i = path + i
        img.append(i)

    cv2_fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    frame = cv2.imread(img[0])
    size = list(frame.shape)
    del size[2]
    size.reverse()
    video = cv2.VideoWriter(out, cv2_fourcc, 6, size)

    for i in range(len(img)):
        video.write(cv2.imread(img[i]))

    video.release()


path = 'images/'
out = 'videoForMin.mp4'
video(path, out)

#path = 'incidentesImages/'
#out = 'videoForMinIncidentes.mp4'
#video(path, out)