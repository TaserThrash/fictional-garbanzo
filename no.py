import os
import cv2


path = "Images"

images = []


for file in os.listdir(path):
    name, ext = os.path.splitext(file)

    if ext in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:
        file_name = path + "/" + file

        print(file_name)
               
        images.append(file_name)
        
print(len(images))
count = len(images)

frame = cv2.imread(images[0])
height, width, channel = frame.shape
size = (width, height)

output = cv2.VideoWriter("POSSIBLY.mp4", cv2.VideoWriter_fourcc(*"DIVX"), 1, size)

for i in range(len(images) - 1):
    frame = cv2.imread(images[i])
    output.write(frame)

output.release()
