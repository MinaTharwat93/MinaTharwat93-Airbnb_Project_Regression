import streamlit as st
import os
import sys

# Set page configuration at the very top
st.set_page_config(page_title="Airbnb Project", page_icon="🏡", layout="wide")

# Add project directory to Python path
project_dir = "/mount/src/minatharwat93-airbnb_project_regression"
if os.path.exists(project_dir) and project_dir not in sys.path:
    sys.path.append(project_dir)

try:
    # Import modules from the specified path
    from app1 import main as app1_main
    from app2 import display_second_page as app2_main
    
    # Sidebar for navigation
    selected_page = st.sidebar.selectbox(
        label="Choose a page",
        options=["first page", "second page"],
        index=0
    )

    # Map page names to functions
    mapper_name_fn = {
        "first page": app1_main,
        "second page": app2_main
    }

    # Execute the selected function
    if selected_page in mapper_name_fn:
        mapper_name_fn[selected_page]()
    else:
        st.error(f"Error: '{selected_page}' page not found.")

except ImportError as e:
    st.error(f"Failed to import modules: {str(e)}")
    st.markdown("""
    **Troubleshooting steps:**
    1. Verify the files exist at:
       - `/mount/src/minatharwat93-airbnb_project_regression/app1.py`
       - `/mount/src/minatharwat93-airbnb_project_regression/app2.py`
    2. Check file permissions
    3. Ensure all required imports are in each file
    """)

except Exception as e:
    st.error(f"An unexpected error occurred: {str(e)}")