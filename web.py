from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/send-location', methods=['POST'])
def send_location():
    data = request.get_json()
    latitude = data.get('lat')
    longitude = data.get('lon')

    # Here you can send this location to a cybersecurity manager or nearby police station
    print(f"Received Location: Latitude = {latitude}, Longitude = {longitude}")

    # For demonstration purposes, we return a success response
    return jsonify({"status": "success", "message": "Location sent to manager."})

if __name__ == '__main__':
    app.run(debug=True)
