import streamlit as st
import os
import dill
import pandas as pd
import streamlit.components.v1 as components
from sklearn.preprocessing import LabelEncoder
import xgboost as xgb
from sklearn.ensemble import VotingRegressor


# Load the model from the .dill file
def load_model():
    """Load the serialized model with Python version compatibility handling"""
    model_path = r'/mount/src/minatharwat93-airbnb_project_regression\voting_pipeline_model_py3.dill'
    
    if not os.path.exists(model_path):
        st.error(f"Model file not found at: {model_path}")
        return None

    try:
        import dill
        import types
        
        # Create a patched version of CodeType for Python version compatibility
        def create_compatible_code(*args):
            # Handle newer Python versions (19 arguments)
            if len(args) == 19:
                return types.CodeType(
                    args[0],   # argcount
                    args[1],   # posonlyargcount
                    args[2],   # kwonlyargcount
                    args[3],   # nlocals
                    args[4],   # stacksize
                    args[5],   # flags
                    args[6],   # code
                    args[7],   # consts
                    args[8],   # names
                    args[9],   # varnames
                    args[10],  # filename
                    args[11],  # name
                    args[12],  # firstlineno
                    args[13],  # lnotab
                    args[16],  # freevars (adjusted position)
                    args[17]   # cellvars (adjusted position)
                )
            # Default case for standard CodeType
            return types.CodeType(*args)
        
        # Apply the patch to dill
        original_loader = dill._dill._create_code
        dill._dill._create_code = create_compatible_code
        
        # Load the model
        with open(model_path, 'rb') as file:
            model = dill.load(file)
            
        # Restore original loader
        dill._dill._create_code = original_loader
        
        return model
        
    except Exception as e:
        st.error(f"Failed to load model: {str(e)}")
        st.error("""
        Troubleshooting steps:
        1. Verify Python version is 3.8-3.10
        2. Check package versions:
           - xgboost==1.6.0
           - dill==0.3.4
           - scikit-learn==1.0.2
        3. Ensure model file isn't corrupted
        """)
        return None


# Function to make predictions
def make_prediction(model, inputs):
    missing_columns = [
        'neighbourhood', 'latitude', 'longitude', 'room_type',
        'last_review', 'calculated_host_listings_count',
        'number_of_reviews_ltm', 'distance_to_city_center', 'location_cluster'
    ]
    
    for col in missing_columns:
        if col not in inputs:
            if col in ['latitude', 'longitude', 'calculated_host_listings_count', 
                       'number_of_reviews_ltm', 'distance_to_city_center', 'location_cluster']:
                inputs[col] = 0
            elif col == 'neighbourhood':
                inputs[col] = 'Unknown'
            elif col == 'room_type':
                inputs[col] = inputs.get('room_type', 'Private room')
            elif col == 'last_review':
                inputs[col] = 2023  # Numeric year to match pipeline expectation
    
    df = pd.DataFrame([inputs])
    prediction = model.predict(df)
    return prediction[0]

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
    """)

# # Function to display the map (via an iframe)
# def display_map():
#     st.title("USA Map Airbnb")
#     html_file_path = os.path.join(os.path.dirname(__file__), 'usa_map.html')

#     if os.path.exists(html_file_path):
#         with open(html_file_path, 'r') as f:
#             html_content = f.read()
#             components.html(html_content, height=500, width=900)
#     else:
#         st.error("HTML file not found! Please make sure the file path is correct.")

# Streamlit UI for input
def user_input():
    availability_365 = st.number_input('Enter availability_365', min_value=1, max_value=365, value=1)
    minimum_nights = st.number_input('Enter minimum_nights', min_value=1, max_value=365, value=1)

    room_type = st.selectbox('Select Room Type', ['Entire home/apt', 'Private room', 'Shared room', 'Hotel room'])
    city = st.selectbox('Select City', [
        'San Francisco', 'Washington D.C.', 'Oakland', 'Jersey City', 'New Orleans',
        'Los Angeles', 'New York City', 'Cambridge', 'Santa Clara County', 'Asheville',
        'Salem', 'Columbus', 'Rhode Island', 'San Diego', 'Nashville', 'Santa Cruz County',
        'Denver', 'Chicago', 'Austin', 'Pacific Grove', 'Portland', 'Seattle', 'Twin Cities MSA',
        'Broward County', 'Clark County', 'Boston', 'San Mateo County'
    ])
    reviews_category = st.selectbox('Select Reviews Category', [
        '51-200 Reviews', 'No Reviews', '1-10 Reviews', '11-50 Reviews', '201+ Reviews'
    ])
    host_listings_category = st.selectbox('Select Host Listings Category', [
        '1', '6-20', '2-5', '21-50', '100+', '51-100'
    ])
    availability_category = st.selectbox('Select Availability Category', [
        '31-180 days', '181-365 days', '1-30 days'
    ])
    distance_category = st.selectbox('Select Distance Category', [
        'Very Close', 'Close', 'Moderate', 'Far', 'Very Far'
    ])
    season = st.selectbox('Select Season', ['Winter', 'Summer', 'Autumn', 'Spring'])

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
    display_introduction()
    st.write("---")
    # display_map()

    model = load_model()
    inputs = user_input()

    if model:
        if st.button('Make Prediction'):
            with st.spinner("Making prediction..."):
                prediction = make_prediction(model, inputs)
                st.success(f"Predicted Price: ${prediction:.2f}")
        else:
            st.info("Click the button to get the prediction")

if __name__ == "__main__":
    main()
