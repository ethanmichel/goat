from flask import Flask, request, Response
from flask_ngrok import run_with_ngrok
import cv2
import numpy as np
import jsonpickle
from imgprocessing import *


# init Flask app
app = Flask(__name__)
run_with_ngrok(app)

# process picture & return T/F as to whether person should be rammed
@app.route('/img', methods=["POST"])
def processimg():
    r = request
    # convert string of image data to uint8
    nparr = np.fromstring(r.data, np.uint8)
    # decode image
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    cv2.imwrite("currentframe.jpg", img)
    # detect ppl in image
    dp_points = see_people("currentframe.jpg")
    print(f"DP POINTS: {dp_points}")
    # check if they fit the qualities to be rammable & return
    ram_status = are_they_rammable(dp_points, "newframe.jpg")
    print(f"RAM STATUS: {ram_status}")
    ram_response = {
        'should_ram': str(ram_status)
    }
    dill = jsonpickle.encode(ram_response)
    return str(ram_status)


# run app
if __name__ == '__main__':
    app.run()
