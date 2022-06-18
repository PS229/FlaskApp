from flask import Flask, jsonify, request

app = Flask(__name__)
contacts = [
    {
        "id":1, 
        "name":u"Raj",
        "contact":u"9753845475",
        "done":False
    },
    {
        "id":2, 
        "name":u"Ram",
        "contact":u"9213988235",
        "done":False
    }
]
@app.route("/")
def helloworld():
    return "Hello World"
@app.route("/add-contact", methods = ["POST"])
def addtask():
    if not request.json:
        return jsonify({
            "status": "error",
            "message": "Please provide the data"
        },400)
    contact = {
        "id":contacts[-1]["id"]+1, 
        "name":request.json["name"],
        "contact":request.json.get("contact", ""),
        "done":False
    }
    contacts.append(contact)
    return jsonify ({
        "status":"Success",
        "message":"Task added succesfully"
    })

@app.route("/get-contact")
def gettask():
    return jsonify({
        "data":contacts
    })

if __name__ == "__main__":
    app.run()
