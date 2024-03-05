from flask import Flask, request

app = Flask(__name__)

# Declare the global variable for storing the IP address
ip = '0'

@app.route('/get_ip', methods=['GET'])
def get_ip():
    return ip, 200

@app.route('/update_ip', methods=['POST'])
def update_ip():
    global ip
    if request.data:
        print("Received payload data:", request.data)
        ip = request.data.decode("utf-8")  # Convert bytes to string
        return "Payload data received successfully"
    else:
        return "No payload data received"

if __name__ == '__main__':
    app.run(debug=False,host='0.0.0.0',port=20000)

