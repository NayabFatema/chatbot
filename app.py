from twilio.rest import Client
from flask import Flask,request

app = Flask(__name__)
client = Client("ACfca1b4e0df93658d951ce0e161d36761", "67ed7e1f3ec382554577afd497a553d4")

@app.route('/' , methods=['GET'])
def func():

    print("Nayab Fatema")
    var = client.messages.create(to = "whatsapp:+917020258862" , from_="whatsapp:+14155238886", body = " hello")

    print(var)

    return "Hello world"

@app.route('/sms',methods=["POST"])
def POSTfunc():
    recieveMsg = request.form.get("Body")
    print(recieveMsg)

    if(recieveMsg=="Hi"):
        print(client.messages.create(to = "whatsapp:'+917020258862" , from_="whatsapp:+1455238886", body = " hello, How are you"))

    return "<Response></Response>"
if __name__ == "__main__":
    app.run(debug=True)

