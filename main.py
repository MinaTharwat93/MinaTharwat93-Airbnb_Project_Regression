import streamlit as st

# Set page configuration at the very top
st.set_page_config(page_title="Airbnb Project", page_icon="🏡", layout="wide")

# Sidebar for navigation
selected_page = st.sidebar.selectbox(
    label="Choose a page",
    options=["first page", "second page", "third page"]
)

# Map page names to script files
mapper_name_fn = {
    "first page": '/mount/src/minatharwat93-airbnb_project_regression/app1.py',
    "second page": '/mount/src/minatharwat93-airbnb_project_regression/app2.py',
    "third page": '/mount/src/minatharwat93-airbnb_project_regression/app3.py'
}

# Execute the selected script
if selected_page in mapper_name_fn:
    exec(open(mapper_name_fn[selected_page]).read())
else:
    st.error(f"Error: '{selected_page}' script not found.")
