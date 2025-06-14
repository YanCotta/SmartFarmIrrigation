"""
Utility functions for the SmartFarmIrrigation Dashboard
Provides modular functions for model loading, predictions, and explainability
"""

import joblib
import pandas as pd
import streamlit as st


def load_model(path):
    """
    Load a joblib model from the specified path.
    
    Args:
        path (str): File path to the model
        
    Returns:
        model: Loaded model object or None if file not found
    """
    try:
        model = joblib.load(path)
        return model
    except FileNotFoundError:
        return None
    except Exception as e:
        st.error(f"Error loading model: {str(e)}")
        return None


def make_prediction(model, input_data):
    """
    Make a prediction using the loaded model and input data.
    
    Args:
        model: Trained model pipeline
        input_data (pd.DataFrame): Input features for prediction
        
    Returns:
        tuple: (prediction_label, confidence_percentage)
    """
    try:
        # Make prediction
        prediction = model.predict(input_data)[0]
        prediction_proba = model.predict_proba(input_data)[0]
        
        # Get confidence (probability of predicted class)
        confidence = prediction_proba[prediction] * 100
        
        # Convert prediction to readable label
        prediction_label = "IRRIGATE" if prediction == 1 else "DO NOT IRRIGATE"
        confidence_str = f"{confidence:.1f}%"
        
        return prediction_label, confidence_str
        
    except Exception as e:
        st.error(f"Error making prediction: {str(e)}")
        return "ERROR", "0.0%"


def plot_feature_importance(model, feature_names):
    """
    Extract and display feature importances from the model.
    
    Args:
        model: Trained model pipeline
        feature_names (list): List of feature names
    """
    try:
        # Extract feature importances from the classifier step
        classifier = model.named_steps['classifier']
        feature_importances = classifier.feature_importances_
        
        # Create DataFrame for feature importances
        importance_df = pd.DataFrame({
            'Feature': feature_names,
            'Importance': feature_importances
        }).sort_values('Importance', ascending=True)
        
        # Display feature importance chart
        st.bar_chart(importance_df.set_index('Feature')['Importance'])
        
        # Display importance values
        st.markdown("**Feature Importance Values:**")
        for feature, importance in zip(feature_names, feature_importances):
            st.write(f"- **{feature.title()}**: {importance:.3f}")
            
    except Exception as e:
        st.error(f"Error plotting feature importance: {str(e)}")
