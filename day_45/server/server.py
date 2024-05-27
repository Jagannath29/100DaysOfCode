from flask import Flask, request, jsonify
import util


app = Flask(__name__)


@app.route('/get_location_and_society')
def get_location_and_society():
    response = jsonify({
        'locations': util.get_location_and_society(),
        'society': util.get_location_and_society()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/predict_home_price', methods = ['POST', 'GET'])
def predict_home_price():
    sqft = float(request.form['total_sqft'])
    location = request.form['location']
    bed = int(request.form['bed'])
    bath = int(request.form['bath'])
    area_type = int(request.form['area_type'])
    society = request.form['society']

    response = jsonify({
        'estimated_price': util.get_price(location, sqft, area_type, bed, bath, society)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


if __name__ == '__main__':
    print('Starting Flask server...')
    util.load_saved_artifacts()
    app.run()