import streamlit as st
import pandas as pd

# Define the function
def fert_recommend(crop_name, N, P, K):
    title = " Fertilizer Suggestion "

    # Load the data
    df = pd.read_csv("fertilizer.csv")

    # Retrieve the recommended N, P, K values for the selected crop
    nr = df[df["Crop"] == crop_name]["N"].iloc[0]
    pr = df[df["Crop"] == crop_name]["P"].iloc[0]
    kr = df[df["Crop"] == crop_name]["K"].iloc[0]

    # Calculate the difference in nutrient levels
    n = nr - N
    p = pr - P
    k = kr - K
    temp = {abs(n): "N", abs(p): "P", abs(k): "K"}
    max_value = temp[max(temp.keys())]

    # Determine the key based on the differences
    if max_value == "N":
        key = "NHigh" if n < 0 else "Nlow"
    elif max_value == "P":
        key = "PHigh" if p < 0 else "Plow"
    else:
        key = "KHigh" if k < 0 else "Klow"

    return fertilizer_dic[key]

# Streamlit app
st.title("Fertilizer Suggestion")

# User inputs
crop_name = st.text_input("Enter crop name")
N = st.number_input("Enter Nitrogen value", min_value=0, step=1)
P = st.number_input("Enter Phosphorous value", min_value=0, step=1)
K = st.number_input("Enter Potassium value", min_value=0, step=1)

if st.button("Submit"):
    # Example fertilizer dictionary (update this with your actual values)
    fertilizer_dic = {
        "NHigh": "You should reduce nitrogen levels.",
        "Nlow": "You should increase nitrogen levels.",
        "PHigh": "You should reduce phosphorus levels.",
        "Plow": "You should increase phosphorus levels.",
        "KHigh": "You should reduce potassium levels.",
        "Klow": "You should increase potassium levels."
    }

    try:
        # Get the recommendation
        recommendation = fert_recommend(crop_name, N, P, K)

        # Display the recommendation
        st.success(f"Recommendation: {recommendation}")

    except Exception as e:
        st.error(f"Error: {str(e)}")





