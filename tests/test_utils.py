"""
Test suite for the SmartFarmIrrigation utils module
"""

import pytest
import pandas as pd
import numpy as np
from unittest.mock import Mock, patch
import sys
import os

# Add the scripts directory to the path
scripts_path = os.path.join(os.path.dirname(__file__), '..', 'scripts')
sys.path.insert(0, scripts_path)

try:
    from utils import load_model, make_prediction
except ImportError as e:
    pytest.skip(f"Could not import utils module: {e}", allow_module_level=True)


class TestUtilsFunctions:
    """Test class for utility functions"""
    
    def test_load_model_success(self):
        """Test successful model loading"""
        with patch('joblib.load') as mock_load:
            # Setup mock
            mock_model = Mock()
            mock_load.return_value = mock_model
            
            # Test
            result = load_model('test_path.joblib')
            
            # Assert
            assert result == mock_model
            mock_load.assert_called_once_with('test_path.joblib')
    
    def test_load_model_file_not_found(self):
        """Test model loading when file doesn't exist"""
        with patch('joblib.load', side_effect=FileNotFoundError):
            result = load_model('nonexistent_path.joblib')
            assert result is None
    
    def test_make_prediction_success(self):
        """Test successful prediction making"""
        # Create mock model
        mock_model = Mock()
        mock_model.predict.return_value = np.array([1])
        mock_model.predict_proba.return_value = np.array([[0.2, 0.8]])
        
        # Create test input data
        input_data = pd.DataFrame({
            'humidity': [45.0],
            'phosphorus': [1],
            'potassium': [1],
            'ph': [6.5]
        })
        
        # Test
        prediction_label, confidence = make_prediction(mock_model, input_data)
        
        # Assert
        assert prediction_label == "IRRIGATE"
        assert confidence == "80.0%"
        mock_model.predict.assert_called_once()
        mock_model.predict_proba.assert_called_once()
    
    def test_make_prediction_do_not_irrigate(self):
        """Test prediction for do not irrigate case"""
        # Create mock model
        mock_model = Mock()
        mock_model.predict.return_value = np.array([0])
        mock_model.predict_proba.return_value = np.array([[0.9, 0.1]])
        
        # Create test input data
        input_data = pd.DataFrame({
            'humidity': [70.0],
            'phosphorus': [0],
            'potassium': [1],
            'ph': [5.0]
        })
        
        # Test
        prediction_label, confidence = make_prediction(mock_model, input_data)
        
        # Assert
        assert prediction_label == "DO NOT IRRIGATE"
        assert confidence == "90.0%"
    
    @patch('streamlit.error')
    def test_make_prediction_error_handling(self, mock_st_error):
        """Test error handling in make_prediction"""
        # Create mock model that raises an exception
        mock_model = Mock()
        mock_model.predict.side_effect = Exception("Test error")
        
        # Create test input data
        input_data = pd.DataFrame({
            'humidity': [45.0],
            'phosphorus': [1],
            'potassium': [1],
            'ph': [6.5]
        })
        
        # Test
        prediction_label, confidence = make_prediction(mock_model, input_data)
        
        # Assert
        assert prediction_label == "ERROR"
        assert confidence == "0.0%"
        mock_st_error.assert_called_once()


class TestDataValidation:
    """Test class for data validation scenarios"""
    
    def test_input_data_format(self):
        """Test that input data has the correct format"""
        # Create test data
        input_data = pd.DataFrame({
            'humidity': [45.0],
            'phosphorus': [1],
            'potassium': [1],
            'ph': [6.5]
        })
        
        # Validate structure
        assert len(input_data.columns) == 4
        assert 'humidity' in input_data.columns
        assert 'phosphorus' in input_data.columns
        assert 'potassium' in input_data.columns
        assert 'ph' in input_data.columns
        
        # Validate data types
        assert input_data['humidity'].dtype in [np.float64, np.float32]
        assert input_data['phosphorus'].dtype in [np.int64, np.int32]
        assert input_data['potassium'].dtype in [np.int64, np.int32]
        assert input_data['ph'].dtype in [np.float64, np.float32]


if __name__ == "__main__":
    pytest.main([__file__])
