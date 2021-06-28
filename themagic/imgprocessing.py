# imports
from imageai.Detection import ObjectDetection
import PIL
from PIL import Image
import json
import cv2


# parse config
with open('config.json') as f:
    CONFIG = json.load(f)

# initialize obj. detection model
detector = ObjectDetection()
detector.setModelTypeAsTinyYOLOv3()
detector.setModelPath('yolo-tiny.h5')
detector.loadModel(detection_speed="fastest")

# get current frame & detect people
def see_people(currentframe):
    detections = detector.detectObjectsFromImage(input_image=currentframe, output_image_path="newframe.jpg")
    # sort detected objects into "persons", with probability assigned in config.json
    detected_people = []
    for eachObject in detections:
        if eachObject["name"] == "person" and eachObject["percentage_probability"] >= CONFIG["confidence"]:
            detected_people.append(eachObject)
    return detected_people

# check if the person is in the middle of the screen
def are_they_rammable(detected_people, newframe):
    if detected_people == None:
        return False
    else:
        # get size/resolution cutoffs
        img = PIL.Image.open(newframe)
        width, height = img.size
        left_width = width / CONFIG["left_divisor"]
        right_width = width / CONFIG["right_divisor"]
        #
        # write lines to img
        data = cv2.imread('newframe.jpg')
        height, width = data.shape[0], data.shape[1]
        cv2.line(data, tuple([int(width / 5), 0]), tuple([int(width / 5), height]), (252,3,3), 5)
        cv2.line(data, tuple([int(width / 1.25), 0]), tuple([int(width / 1.25), height]), (252,3,3), 5)
        cv2.imwrite('newframelined.jpg', data)
        #
        index = 1
        for dp in detected_people:
            print(f"Reviewing DP #{index} of {len(detected_people)}...")
            index+=1
            RAMPOINTS=0
            points = dp["box_points"]
            # check X coord 1
            if points[0] >= left_width:
                RAMPOINTS+=1
                print("+1 on left")
            else:
                pass
            # check X coord 2
            if points[2] <= right_width:
                print("+1 on right")
                RAMPOINTS+=1
            else:
                pass
            print(f"RAM POINTS TOTAL = {RAMPOINTS}")
            if RAMPOINTS == 2:
                return True
            # if the code has reached this point, then a person should be between accepted ranges
        return False
    return False
