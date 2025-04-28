import unittest
from health_utils import calculate_bmi, calculate_bmr

class TestHealthUtils(unittest.TestCase):
    def test_bmi_normal_case(self):
        # Test with normal values
        self.assertAlmostEqual(calculate_bmi(1.75, 70), 22.86, places=2)
    
    def test_bmi_edge_cases(self):
        # Test with zero values should raise ValueError
        with self.assertRaises(ValueError):
            calculate_bmi(0, 70)
        
        with self.assertRaises(ValueError):
            calculate_bmi(1.75, 0)
        
        # Test with negative values should raise ValueError
        with self.assertRaises(ValueError):
            calculate_bmi(-1.75, 70)
        
        with self.assertRaises(ValueError):
            calculate_bmi(1.75, -70)
    
    def test_bmr_male(self):
        # Test BMR calculation for males
        # For a male with height 175 cm, weight 70 kg, age 30
        expected_bmr = 88.362 + (13.397 * 70) + (4.799 * 175) - (5.677 * 30)
        self.assertAlmostEqual(calculate_bmr(175, 70, 30, 'male'), round(expected_bmr, 2))
    
    def test_bmr_female(self):
        # Test BMR calculation for females
        # For a female with height 165 cm, weight 60 kg, age 25
        expected_bmr = 447.593 + (9.247 * 60) + (3.098 * 165) - (4.330 * 25)
        self.assertAlmostEqual(calculate_bmr(165, 60, 25, 'female'), round(expected_bmr, 2))
    
    def test_bmr_edge_cases(self):
        # Test with invalid gender
        with self.assertRaises(ValueError):
            calculate_bmr(175, 70, 30, 'invalid')
        
        # Test with zero values
        with self.assertRaises(ValueError):
            calculate_bmr(0, 70, 30, 'male')
        
        with self.assertRaises(ValueError):
            calculate_bmr(175, 0, 30, 'male')
        
        with self.assertRaises(ValueError):
            calculate_bmr(175, 70, 0, 'male')

if __name__ == '__main__':
    unittest.main()