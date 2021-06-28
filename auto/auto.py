# imports
from cv2 import *
import requests
import random, time
import json
import gpiozero as gz


# initialize webcam/video-cap 
cam = VideoCapture(0)

def getapiresponse(API_URL, FILENAME):
    # prepare HTTP headers
    content_type = 'image/jpeg'
    headers = {'content-type': content_type}
    # process & encode jpg image
    img = cv2.imread(FILENAME)
    _, img_encoded = cv2.imencode('.jpg', img)
    response = requests.post(API_URL, data=img_encoded.tobytes(), headers=headers)
    return response.text

# use eyes
def eyes():
    ret, img = cam.read()
    imwrite("currentframe.png", img)


# parse config
with open('config.json') as f:
    CONFIG = json.load(f)

# motor/GPIO pins
FRONT_POS = gz.OutputDevice(CONFIG["front_pos"])
FRONT_NEG = gz.OutputDevice(CONFIG["front_neg"])
BACK_POS = gz.OutputDevice(CONFIG["back_pos"])
BACK_NEG = gz.OutputDevice(CONFIG["back_neg"])

# functions

def goforward():
    #BACK_POS.off()
    BACK_NEG.on()

def reversereverse():
    #BACK_NEG.off()
    BACK_POS.on()

def stop():
    BACK_POS.off()
    BACK_NEG.off()

def turnleft():
    #FRONT_POS.off()
    FRONT_NEG.on()

def turnright():
    #FRONT_NEG.off()
    FRONT_POS.on()

def gostraight():
    FRONT_POS.off()
    FRONT_NEG.off()


# MOTOR FUNCTIONS / BEHAVIOR:
def chargeforward():
    print("Starting charge...")
    stop()
    gostraight()
    goforward()
    time.sleep(7)
    stop()
    print("Rammed!")

def idleanimation():
    print("Starting idle animation...")
    direction = random.randint(1,4)
    time_spent_walking = random.randint(1,3)
    stop()
    gostraight()
    if direction == 1:
        print("Going left-backward")
        turnright()
        reversereverse()
        time.sleep(time_spent_walking)
        stop()
        gostraight()
    elif direction == 2:
        print("Going right-backward")
        turnleft()
        reversereverse()
        time.sleep(time_spent_walking)
        stop()
        gostraight()
    elif direction == 3:
        print("Going left")
        #gostraight()
        turnleft()
        goforward()
        time.sleep(time_spent_walking)
        stop()
        gostraight()
    elif direction == 4:
        print("Going right")
        #gostraight()
        turnright()
        goforward()
        time.sleep(time_spent_walking)
        stop()
        gostraight()
    print("Done")

def nostop():
    stop()
    gostraight()
    print("Stopped!")





# get API url
print("Enter API url: ")
API_URL = input()

# infinite loop
while True:
    try:
        eyes()
        print("Taking a pic...")
        shouldgoatramthem = getapiresponse(API_URL, "currentframe.png")
        print(shouldgoatramthem)
        if shouldgoatramthem == "True":
            chargeforward()
        else:
            idleanimation()
        print("Done w/ ramming evaluation.")
        nostop()
        print("Cycle done, resetting.")
    except:
        print("ERROR! Skipping...")
