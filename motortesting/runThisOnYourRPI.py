from flask import Flask
from flask import *
from flask import request
from flask import Flask
import gpiozero as gz
import json


# parse config
with open('config.json') as f:
    CONFIG = json.load(f)

# motor/GPIO pins
FRONT_POS = gz.OutputDevice(CONFIG["front_pos"])
FRONT_NEG = gz.OutputDevice(CONFIG["front_neg"])
BACK_POS = gz.OutputDevice(CONFIG["back_pos"])
BACK_NEG = gz.OutputDevice(CONFIG["back_neg"])

# init Flask app
app = Flask(__name__)


# front pos. on
@app.route('/fp_on', methods=['GET'])
def fp_on():
    FRONT_POS.on()
    return True
# front pos. off
@app.route('/fp_off', methods=["GET"])
def fp_off():
    FRONT_POS.off()
    return True

# front neg. on
@app.route('/fn_on', methods=['GET'])
def fn_on():
    FRONT_NEG.on()
    return True
# front neg. off
@app.route('/fn_off', methods=["GET"])
def fn_off():
    FRONT_NEG.off()
    return True

# back pos. on
@app.route('/bp_on', methods=['GET'])
def bp_on():
    BACK_POS.on()
    return True
# back pos. off
@app.route('/bp_off', methods=["GET"])
def bp_off():
    BACK_POS.off()
    return True

# back neg. on
@app.route('/bn_on', methods=['GET'])
def bn_on():
    BACK_NEG.on()
    return True
# back neg. off
@app.route('/bn_off', methods=["GET"])
def bn_off():
    BACK_NEG.off()
    return True


# run app
if __name__ == '__main__':
    app.run(port=80)
