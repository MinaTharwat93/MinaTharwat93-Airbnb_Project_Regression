import streamlit as st
# import os
import pandas as pd
import streamlit.components.v1 as components

# # Load the model from the .dill file
# def load_model():
#     model_path = r'D:\Epsilon Ai\Airbnb-Project\model.dill'  # Full path to the model file
#     if os.path.exists(model_path):
#         with open(model_path, 'rb') as f:
#             model = dill.load(f)
#         return model
#     else:
#         st.error(f"Model file not found at {model_path}. Please check the file path.")
#         return None

# Function to make predictions
def make_prediction(model, inputs):
    # Add missing columns with placeholders or computed values
    missing_columns = [
        'price_per_distance', 'latitude', 'last_review', 'distance_to_city_center', 
        'neighbourhood', 'price_relative_to_room_type', 'calculated_host_listings_count', 
        'longitude', 'price_per_room_type', 'number_of_reviews_ltm'
    ]
    
    # Assuming you don't have data for some columns, we'll add them with placeholder values
    for col in missing_columns:
        if col not in inputs:
            inputs[col] = 0  # Default placeholder value for missing columns
    
    # # Prepare the input data into a DataFrame for prediction
    # df = pd.DataFrame([inputs])
    # prediction = model.predict(df)
    # return prediction[0]

# Function to display the Airbnb introduction
def display_introduction():
    st.title("Airbnb")
    st.write("""
    **Airbnb** is an online platform that connects hosts offering accommodations with travelers seeking unique places to stay.
    It operates in over 27 cities, providing diverse lodging options like apartments, houses, and unique spaces such as treehouses and castles.
    Airbnb promotes cultural exchange, local tourism, and immersive travel experiences while ensuring safety and trust through secure payments and user reviews.
    It has transformed the hospitality industry by blending technology with the sharing economy.
             
    """
    """
  Dataset link:  https://www.kaggle.com/datasets/kritikseth/us-airbnb-open-data?select=AB_US_2023.csv 
    """
    """
Explain my column: 
1.	neighbourhood: The specific area or neighborhood where the property is located.
2.	latitude: The geographic coordinate indicating the north-south position of the property.
3.	longitude: The geographic coordinate indicating the east-west position of the property.
4.	room_type: The type of room available for booking (e.g., Entire home/apt, Private room, Shared room).
5.	price: The nightly rental price for the property.
6.	minimum_nights: The minimum number of nights required to book the property.
7.	last_review: The date when the property was last reviewed by a guest.
8.	calculated_host_listings_count: The number of listings managed by the same host.
9.	availability_365: The number of days the property is available for booking in a year.
10.	number_of_reviews_ltm: The number of reviews received in the last 12 months.
11.	city: The city where the property is located.
12.	distance_to_city_center (extract): The distance of the property from the city center, often in kilometers or miles.
13.	distance_category (extract): A categorized version of distance_to_city_center (e.g., "Close", "Moderate", "Far").
14.	reviews_category (extract): A classification of properties based on the number or quality of reviews (e.g., "Highly reviewed", "Moderately reviewed").
15.	host_listings_category (extract): A categorization based on the number of listings a host manages (e.g., "Single property host", "Multi-property host").
16.	availability_category (extract): A classification of properties based on their availability (e.g., "High availability", "Low availability").
17.	season (extract): The season (e.g., Summer, Winter) during which the data is relevant or the property is analyzed.
18.	price_per_distance (extract): The price normalized by the distance to the city center (price per unit of distance).
19.	price_per_room_type (extract): The average price normalized based on the type of room.
20.	price_relative_to_room_type (extract): The property's price compared to the average price for its room_type.

    """)

# # Function to display the map (via an iframe)
# def display_map():
#     st.title("USA Map Airbnb")
#     # Ensure the html file path is correct (relative path preferred for portability)
#     html_file_path = './usa_map.html'  # Update this path if needed

#     # Check if file exists and display it
#     if os.path.exists(html_file_path):
#         # Use Streamlit's components to embed the HTML
#         with open(html_file_path, 'r') as f:
#             html_content = f.read()
#             components.html(html_content, height=500, width=900)  # You can adjust height as needed
#     else:
#         st.error("HTML file not found! Please make sure the file path is correct.")

# Streamlit UI for input
def user_input():
    # User inputs for continuous variables
    availability_365 = st.number_input('Enter availability_365', min_value=1, max_value=365, value=1)
    minimum_nights = st.number_input('Enter minimum_nights', min_value=1, max_value=365, value=1)

    # User inputs for categorical variables
    room_type = st.selectbox('Select Room Type', ['Entire home/apt', 'Private room', 'Shared room', 'Hotel room'])
    city = st.selectbox('Select City', ['San Francisco', 'Washington D.C.', 'Oakland', 'Jersey City', 'New Orleans',
                                        'Los Angeles', 'New York City', 'Cambridge', 'Santa Clara County', 'Asheville', 
                                        'Salem', 'Columbus', 'Rhode Island', 'San Diego', 'Nashville', 'Santa Cruz County',
                                        'Denver', 'Chicago', 'Austin', 'Pacific Grove', 'Portland', 'Seattle', 'Twin Cities MSA',
                                        'Broward County', 'Clark County', 'Boston', 'San Mateo County'])
    reviews_category = st.selectbox('Select Reviews Category', ['51-200 Reviews', 'No Reviews', '1-10 Reviews', 
                                                               '11-50 Reviews', '201+ Reviews'])
    host_listings_category = st.selectbox('Select Host Listings Category', ['1', '6-20', '2-5', '21-50', '100+', '51-100'])
    availability_category = st.selectbox('Select Availability Category', ['31-180 days', '181-365 days', '1-30 days'])
    distance_category = st.selectbox('Select Distance Category', ['Very Close', 'Close', 'Moderate', 'Far', 'Very Far'])
    season = st.selectbox('Select Season', ['Winter', 'Summer', 'Autumn', 'Spring'])

    # Prepare the input data for prediction
    inputs = {
        'availability_365': availability_365,
        'minimum_nights': minimum_nights,
        'room_type': room_type,
        'city': city,
        'reviews_category': reviews_category,
        'host_listings_category': host_listings_category,
        'availability_category': availability_category,
        'distance_category': distance_category,
        'season': season
    }
    
    return inputs

# Main function for Streamlit app
def main():
    # Display the Airbnb introduction and map
    display_introduction()
    st.write("---")  # Adds a horizontal line for separation
    # display_map()

    # # Load the pre-trained model
    # model = load_model()

    # Get inputs from the user for prediction
    # inputs = user_input()

    # # When button is clicked, make prediction
    # if model:
    #     # Only run prediction when the button is clicked
    #     if st.button('Make Prediction'):
    #         # Disable the input fields when the button is clicked to avoid reactivity
    #         with st.spinner("Making prediction..."):
    #             prediction = make_prediction(model, inputs)  # Make prediction based on inputs
    #             st.write(f"Predicted Price: ${prediction:.2f}")  # Display the prediction result
    #     else:
    #         st.write("Click the button to get the prediction")

if __name__ == "__main__":
    main()
