from flask import *
from flask_ngrok import run_with_ngrok
import requests


# init Flask app
app = Flask(__name__)
run_with_ngrok(app)


# webpage / index
@app.route('/')
def index():
    return render_template('index.html')


# FRONT POS
@app.route('/frontpos_on', methods=["GET"])
def frontpos_on():
    print("Sending API request to RPi: Front Pos. On...")
    requests.get(f"http://{RPI_API}/fp_on")
    return render_template('index.html')
@app.route('/frontpos_off', methods=["GET"])
def frontpos_off():
    print("Sending API request to RPi: Front Pos. Off...")
    requests.get(f"http://{RPI_API}/fp_off")
    return render_template('index.html')

# FRONT NEG
@app.route('/frontneg_on', methods=["GET"])
def frontneg_on():
    print("Sending API request to RPi: Front Neg. On...")
    requests.get(f"http://{RPI_API}/fn_on")
    return render_template('index.html')
@app.route('/frontneg_off', methods=["GET"])
def frontneg_off():
    print("Sending API request to RPi: Front Neg. Off...")
    requests.get(f"http://{RPI_API}/fn_off")
    return render_template('index.html')

# BACK POS
@app.route('/backpos_on', methods=["GET"])
def backpos_on():
    print("Sending API request to RPi: Back Pos. On...")
    requests.get(f"http://{RPI_API}/bp_on")
    return render_template('index.html')
@app.route('/backpos_off', methods=["GET"])
def backpos_off():
    print("Sending API request to RPi: Back Pos. Off...")
    requests.get(f"http://{RPI_API}/bp_off")
    return render_template('index.html')

# BACK NEG
@app.route('/backneg_on', methods=["GET"])
def backneg_on():
    print("Sending API request to RPi: Back Neg. On...")
    requests.get(f"http://{RPI_API}/bn_on")
    return render_template('index.html')
@app.route('/backneg_off', methods=["GET"])
def backneg_off():
    print("Sending API request to RPi: Back Neg. Off...")
    requests.get(f"http://{RPI_API}/bn_off")
    return render_template('index.html')




# run & get RPi API URL/URI
if __name__ == '__main__':
    print("Please enter URL/URI for RPi API:")
    RPI_API = input()
    app.run()
