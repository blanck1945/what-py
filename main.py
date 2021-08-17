from flask import Flask, request
import pywhatkit as kt
from flask_cors import CORS
import os
app = Flask(__name__)
CORS(app)

os.environ['DISPLAY'] = ':0.0'


#send instantly

# def sendwhatmsg_instantly(phone_no: str, message: str, wait_time: int = 20,
#                           tab_close: bool = False, close_time: int = 3) -> None:
#     """Send WhatsApp Message Instantly"""

#     if "+" not in phone_no:
#         raise CountryCodeException("Country code missing from phone_no")

#     parsed_message = quote(message)
#     web.open('https://web.whatsapp.com/send?phone=' +
#              phone_no + '&text=' + parsed_message)
#     time.sleep(2)
#     width, height = pg.size()
#     pg.click(width / 2, height / 2)
#     time.sleep(wait_time - 2)
#     pg.press('enter')
#     if tab_close:
#         close_tab(wait_time=close_time)

@app.route("/")
def index():
    return '<h2>Index Page</h2>'

@app.route('/<name>')
def print_name(name):
    return 'Hi, {}'.format(name)

def addToMinutes(minute):
    return int(minute) + 2

@app.route('/get-message', methods=["POST"])
def getMessages():
    return ""

@app.route("/send-user-message", methods=['POST'])    
def sendUserMsg():
    print("Msg send")
    return "user-send-msg"

@app.route('/send-message', methods=["POST"])
def sendMsg():
    request_data = request.get_json()
    cel = request_data['cel']
    user = request_data['user']
    comercio = request_data['comercio']
    now = request_data['now']

    hora = now.split(':')[0]
    min = addToMinutes(now.split(':')[1])
    kt.sendwhatmsg('+5411' + str(cel), str(user) + ' gracias por comprar en ' + str(comercio) , int(hora),int(min))
    return '<h2>Mensaje enviado con exito</h2>'



if __name__ == '__main__':
    app.run(debug=True)