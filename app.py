from flask import Flask, request, jsonify, send_from_directory
from health_utils import calculate_bmi, calculate_bmr
import logging

# Configuration du logging
logging.basicConfig(
    filename='health_app.log',
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

app = Flask(__name__)

@app.route('/')
def home():
    return send_from_directory('static', 'index.html')

@app.route('/bmi', methods=['POST'])
def bmi():
    data = request.get_json()
    
    try:
        if not data:
            raise ValueError("No input data provided")
        
        if 'height' not in data or 'weight' not in data:
            raise ValueError("Missing required parameters: 'height' (in meters) and 'weight' (in kg)")
        
        height = float(data['height'])
        weight = float(data['weight'])
        
        bmi_value = calculate_bmi(height, weight)
        
        # Determine BMI category
        category = ""
        if bmi_value < 18.5:
            category = "Underweight"
        elif 18.5 <= bmi_value < 25:
            category = "Normal weight"
        elif 25 <= bmi_value < 30:
            category = "Overweight"
        else:
            category = "Obese"
        
        result = {
            "bmi": bmi_value,
            "category": category
        }
        
        logging.info(f"BMI calculation successful: {result}")
        return jsonify(result)
    
    except ValueError as e:
        error_msg = str(e)
        logging.error(f"BMI calculation error: {error_msg}")
        return jsonify({"error": error_msg}), 400
    
    except Exception as e:
        error_msg = f"Unexpected error: {str(e)}"
        logging.error(error_msg)
        return jsonify({"error": error_msg}), 500

@app.route('/bmr', methods=['POST'])
def bmr():
    data = request.get_json()
    
    try:
        if not data:
            raise ValueError("No input data provided")
        
        required_params = ['height', 'weight', 'age', 'gender']
        for param in required_params:
            if param not in data:
                raise ValueError(f"Missing required parameter: '{param}'")
        
        height = float(data['height'])  # in cm
        weight = float(data['weight'])  # in kg
        age = int(data['age'])
        gender = data['gender']
        
        bmr_value = calculate_bmr(height, weight, age, gender)
        
        result = {
            "bmr": bmr_value,
            "unit": "calories/day"
        }
        
        logging.info(f"BMR calculation successful: {result}")
        return jsonify(result)
    
    except ValueError as e:
        error_msg = str(e)
        logging.error(f"BMR calculation error: {error_msg}")
        return jsonify({"error": error_msg}), 400
    
    except Exception as e:
        error_msg = f"Unexpected error: {str(e)}"
        logging.error(error_msg)
        return jsonify({"error": error_msg}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
