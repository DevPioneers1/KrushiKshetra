import streamlit as st
import numpy as np
import pickle

# Mock function for weather_fetch (replace it with your implementation)
def weather_fetch(city):
    # Example: Return temperature and humidity as mock data
    if city:
        return 30, 70  # Mock temperature and humidity
    else:
        return None

# Mock crop recommendation model (replace with your actual model)
class MockModel:
    def predict(self, data):
        return ["Wheat"]  # Mock prediction, replace with actual model prediction
crop_recommendation_model = MockModel()

# Streamlit App
def main():
    st.title('Crop Recommendation')

    st.subheader('Enter the following details:')
    N = st.number_input("Nitrogen content (N)", min_value=0, value=0, step=1)
    P = st.number_input("Phosphorous content (P)", min_value=0, value=0, step=1)
    K = st.number_input("Potassium content (K)", min_value=0, value=0, step=1)
    ph = st.number_input("pH value", value=7.0, step=0.1)
    rainfall = st.number_input("Rainfall (mm)", value=100.0, step=0.1)
    city = st.text_input("City Name")

    if st.button("Predict"):
        if weather_fetch(city) is not None:
            temperature, humidity = weather_fetch(city)
            data = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
            my_prediction = crop_recommendation_model.predict(data)
            final_prediction = my_prediction[0]

            st.success(f"Recommended Crop: {final_prediction}")
        else:
            st.error("Unable to fetch weather data. Please try again.")

if __name__ == '__main__':
    main()