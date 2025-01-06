import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Page configuration
# st.set_page_config(page_title="Data Analysis", layout="wide")

# Second page
def display_second_page():
    st.title("EDA - Visualization:")

    # Uni-variate numerical analysis
    st.subheader("Uni-variate Numerical Analysis")
    st.code("""
    num_cols = df.select_dtypes(include='number').columns

    for col in num_cols:
        fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(8,5))
        sns.histplot(df[col], kde=True, ax=axes[0])
        axes[0].set_title(f'{col} - Histogram with KDE')
        sns.boxplot(df[col], ax=axes[1])
        axes[1].set_title(f'{col} - Boxplot')
        plt.tight_layout()
        plt.show()
    """)
    
    # Images related to uni-variate numerical analysis
    for i in range(1, 12):
        img_path = f"/mount/src/minatharwat93-airbnb_project_regression/uni{i}.png"
        st.image(img_path, caption=f"Uni-variate Numerical Image {i}")

    # Uni-variate categorical analysis
    st.subheader("Uni-variate Categorical Analysis")
    st.code("""
    for column in df.select_dtypes(include="O").columns:
        plt.tight_layout()
        
        # Get the top 30 most frequent values
        top_30 = df[column].value_counts().head(30)

        sns.barplot(x=top_30.index, y=top_30.values, palette='viridis')
        if column == 'neighbourhood':
            plt.title(f'Countplot of {column} (Top 30)', fontsize=14)
        else:
            plt.title(f'Countplot of {column}', fontsize=14)
        plt.xlabel(column, fontsize=12)
        plt.ylabel('Count', fontsize=12)
        plt.xticks(rotation=90)
        plt.show()
    """)
    
    # Images related to uni-variate categorical analysis
    for i in range(1, 9):
        img_path = f"/mount/src/minatharwat93-airbnb_project_regression/unic{i}.png"
        st.image(img_path, caption=f"Uni-variate Categorical Image {i}")

    # Average price per room type
    st.subheader("What is the average price per room type?")
    st.code("""
    room_type_avg_price = df.groupby('room_type')['price'].median()
    plt.pie(room_type_avg_price, labels=room_type_avg_price.index, autopct='%1.1f%%', startangle=90)
    plt.title('Average Price per Room Type')
    plt.show()
    """)
    st.image("/mount/src/minatharwat93-airbnb_project_regression/static/images/q1.png", caption="Average Price per Room Type")
    st.image("D:/Epsilon Ai/Airbnb-Project/static/images/qd1.png", caption="Price Distribution")

    # Price variation over time across seasons
    st.subheader("How does the price vary over time across different seasons?")
    st.code("""
    df['last_review'] = pd.to_datetime(df['last_review'])
    df_year = df['last_review'].dt.year
    plt.figure(figsize=(8, 5))
    sns.lineplot(data=df, x=df_year, y='price', hue='season', ci=False)
    plt.title('Price Over Time by Season')
    plt.ylabel('Price')
    plt.xlabel('Year')
    plt.legend(title='Season')
    plt.tight_layout()
    plt.show()
    """)
    st.image("D:/Epsilon Ai/Airbnb-Project/static/images/q2.png", caption="Price Over Time by Season")
    st.image("D:/Epsilon Ai/Airbnb-Project/static/images/qd2.png", caption="Price Variation")

    # Correlation between price and availability
    st.subheader("How does the price of properties correlate with their availability for the year?")
    st.code("""
    sns.boxplot(x='room_type', y='availability_365', data=df)
    plt.title('Availability by Room Type')
    plt.show()
    """)
    st.image("D:/Epsilon Ai/Airbnb-Project/static/images/q3.png", caption="Availability by Room Type")
    st.image("D:/Epsilon Ai/Airbnb-Project/static/images/qd3.png", caption="Price vs Availability")

    # Top 10 neighborhoods with highest listings and room types
    st.subheader("Top 10 Neighborhoods with Highest Listings and Room Types")
    st.code("""
    top_neighbourhoods = df[df['neighbourhood'].isin(df['neighbourhood'].value_counts().head(10).index)]
    plt.figure(figsize=(10,6))
    sns.countplot(data=top_neighbourhoods, y='neighbourhood', hue='room_type', order=df['neighbourhood'].value_counts().head(10).index)
    plt.title('Top 10 Neighbourhoods with Highest Number of Listings')
    plt.xlabel('Number of Listings')
    plt.ylabel('Neighbourhood')
    plt.show()
    """)
    st.image("D:/Epsilon Ai/Airbnb-Project/static/images/q4.png", caption="Top 10 Neighborhoods")
    st.image("D:/Epsilon Ai/Airbnb-Project/static/images/qd4.png", caption="Listings by Room Type")

    # Relationship between minimum nights and room type across seasons
    st.subheader("What is the relationship between minimum nights and room type across different seasons?")
    st.code("""
    sns.barplot(x='room_type', y='minimum_nights', hue='season', data=df, ci=False)
    plt.title('Minimum Nights by Room Type and Season')
    plt.show()
    """)
    st.image("D:/Epsilon Ai/Airbnb-Project/static/images/q5.png", caption="Minimum Nights by Room Type")
    st.image("D:/Epsilon Ai/Airbnb-Project/static/images/qd5.png", caption="Room Type Seasonal Comparison")

    # Distribution of room types across cities
    st.subheader("What is the distribution of room types across cities?")
    st.code("""
    room_type_city = df.groupby('city')['room_type'].value_counts().unstack()
    room_type_city.plot(kind='bar', stacked=True)
    plt.title('Distribution of Room Types Across Cities')
    plt.show()
    """)
    st.image("D:/Epsilon Ai/Airbnb-Project/static/images/q6.png", caption="Room Types Distribution")

    # Price variation over time by room type
    st.subheader("How does the price of accommodations vary over time by room type?")
    st.code("""
    sns.lineplot(data=df, x=df_year, y='price', hue='room_type', ci=False)
    plt.title('Price Over Time by Room Type')
    plt.ylabel('Price')
    plt.xlabel('Year')
    plt.legend(title='Room Type')
    plt.tight_layout()
    plt.show()
    """)
    st.image("D:/Epsilon Ai/Airbnb-Project/static/images/q7.png", caption="Price Variation by Room Type")
    st.image("D:/Epsilon Ai/Airbnb-Project/static/images/qd7.png", caption="Price Trends")

    # Heatmap of correlations
    st.subheader("Correlation Heatmap")
    st.code("""
    plt.figure(figsize=(10,8))
    sns.heatmap(df.select_dtypes(include=['number']).corr(), fmt=".2f", annot=True)
    """)
    st.image("D:/Epsilon Ai/Airbnb-Project/static/images/heatmap.png", caption="Correlation Heatmap")

# Display the page
display_second_page()
