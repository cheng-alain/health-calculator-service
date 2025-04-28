def calculate_bmi(height, weight):
    """
    Calculate Body Mass Index (BMI) given height in meters and weight in kilograms.
    
    BMI = weight (kg) / (height (m))^2
    
    Args:
        height (float): Height in meters
        weight (float): Weight in kilograms
        
    Returns:
        float: The calculated BMI
    """
    if height <= 0 or weight <= 0:
        raise ValueError("Height and weight must be positive values")
    
    bmi = weight / (height ** 2)
    return round(bmi, 2)

def calculate_bmr(height, weight, age, gender):
    """
    Calculate Basal Metabolic Rate (BMR) using the Harris-Benedict equation.
    
    For males:
    BMR = 88.362 + (13.397 x weight (kg)) + (4.799 x height (cm)) - (5.677 x age (years))
    
    For females:
    BMR = 447.593 + (9.247 x weight (kg)) + (3.098 x height (cm)) - (4.330 x age (years))
    
    Args:
        height (float): Height in centimeters
        weight (float): Weight in kilograms
        age (int): Age in years
        gender (str): 'male' or 'female'
        
    Returns:
        float: The calculated BMR in calories per day
    """
    if height <= 0 or weight <= 0 or age <= 0:
        raise ValueError("Height, weight, and age must be positive values")
    
    if gender.lower() not in ['male', 'female']:
        raise ValueError("Gender must be 'male' or 'female'")
    
    if gender.lower() == 'male':
        bmr = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
    else:
        bmr = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)
    
    return round(bmr, 2)