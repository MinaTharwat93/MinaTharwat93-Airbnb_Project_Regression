import streamlit as st

def main():
    st.title('Pre-Processing & Modeling')

    # Preprocessing Section
    st.subheader('Pre-Processing')

    # a) Detect & Handle Duplicates
    st.write("""
        a) Detect & Handle Duplicates
        First, we detect and handle any duplicates in the dataset to ensure the data is clean and accurate for modeling.
    """)

    # b) Train-Test Split
    st.write("""
        b) Train-Test Split
        The dataset is then split into training and testing sets to ensure proper validation during model training.
    """)

    # c) Detect & Handle NaNs
    st.write("""
        c) Detect & Handle NaNs
        Missing values are handled using techniques like KNN imputation or SimpleImputer to avoid biasing the model.
    """)

    # d) Detect & Handle Outliers
    st.write("""
        d) Detect & Handle Outliers
        Outliers are detected and removed using logarithmic transformations and upper/lower bounds.
    """)

    # e) Encoding
    st.write("""
        e) Encoding
        Categorical variables are encoded. Ordinal variables are handled using OrdinalEncoder or LabelEncoder, while nominal variables are handled based on the number of unique values.
    """)

    # f) Scaling
    st.write("""
        f) Scaling
        Scaling is applied using RobustScaler to standardize the features and reduce the influence of outliers.
    """)

    # Model Section
    st.subheader('Modeling')


    # 1) Simple Model
    st.write("""
        1) Simple Model
        First, a simple baseline model is built and tested to establish a starting point for performance evaluation.
    """)

    # 2) Validation Accuracy
    st.write("""
        2) Validation Accuracy
        The model’s performance is evaluated to determine if it is underfitting or overfitting.
    """)

    # 3) Hyperparameter Tuning (GridSearchCV)
    st.write("""
        3) Hyperparameter Tuning (GridSearchCV)
        We use GridSearchCV to fine-tune the model and find the best hyperparameters.
    """)

    st.image("/mount/src/minatharwat93-airbnb_project_regression/static/images/pipe1.png", caption="pipeline")

    # Models and Grid Search
    st.subheader('Models & Grid Search')

    # Linear Regression
    st.write("""
        • Linear Regression:
        We use Linear Regression and observe its performance before and after hyperparameter tuning. Accuracy was low using polynomial features.
    """)
    st.image("/mount/src/minatharwat93-airbnb_project_regression/static/images/lin1.png", caption="Linear Regression")
    st.image("/mount/src/minatharwat93-airbnb_project_regression/static/images/lin 2.png", caption="Linear Regression_Poly")


    # Lasso
    st.write("""
        • Lasso:
        We apply Lasso Regression and tune it using GridSearchCV.
    """)

    st.image("/mount/src/minatharwat93-airbnb_project_regression/static/images/la1.png", caption="Lasso")
    st.image("/mount/src/minatharwat93-airbnb_project_regression/static/images/la2.png", caption="Lasso with gridsearch")

    # Ridge
    st.write("""
        • Ridge:
        Ridge Regression is tested and tuned using GridSearchCV.
    """)

    st.image("/mount/src/minatharwat93-airbnb_project_regression/static/images/ri1.png", caption="Ridge")
    st.image("/mount/src/minatharwat93-airbnb_project_regression/static/images/ri2.png", caption="Ridge with gridsearch")

    # ElasticNet
    st.write("""
        • ElasticNet:
        ElasticNet is tested and fine-tuned using GridSearchCV.
    """)
    st.image("/mount/src/minatharwat93-airbnb_project_regression/static/images/el1.png", caption="ElasticNet")
    st.image("/mount/src/minatharwat93-airbnb_project_regression/static/images/el2.png", caption="ElasticNet with gridsearch")

    # KNeighborsRegressor
    st.write("""
        • KNeighborsRegressor:
        K-Nearest Neighbors Regression is used and tuned with GridSearchCV.
    """)
    st.image("/mount/src/minatharwat93-airbnb_project_regression/static/images/kn1.png", caption="KNeighborsRegressor")
    st.image("/mount/src/minatharwat93-airbnb_project_regression/static/images/kn2.png", caption="KNeighborsRegressor with gridsearch")

    # DecisionTreeRegressor
    st.write("""
        • DecisionTreeRegressor:
        Decision Tree Regressor is tested and tuned using GridSearchCV.
    """)
    st.image("/mount/src/minatharwat93-airbnb_project_regression/static/images/dt1.png", caption="DecisionTreeRegressor")
    st.image("/mount/src/minatharwat93-airbnb_project_regression/static/images/dt2.png", caption="DecisionTreeRegressor with gridsearch")

    # RandomForestRegressor
    st.write("""
        • RandomForestRegressor:
        Random Forest Regressor is used and fine-tuned using GridSearchCV.
    """)
    st.image("/mount/src/minatharwat93-airbnb_project_regression/static/images/rf1.png", caption="RandomForestRegressor")
    st.image("/mount/src/minatharwat93-airbnb_project_regression/static/images/rf2.png", caption="RandomForestRegressor with gridsearch")

    # XGBRegressor
    st.write("""
        • XGBRegressor:
        XGBoost Regressor is applied and tuned.
    """)
    st.image("/mount/src/minatharwat93-airbnb_project_regression/static/images/xg1.png", caption="XGBRegressor")
    st.image("/mount/src/minatharwat93-airbnb_project_regression/static/images/xg2.png", caption="XGBRegressor with gridsearch")

    # GradientBoostingRegressor
    st.write("""
        • GradientBoostingRegressor:
        Gradient Boosting Regressor is tested and tuned using GridSearchCV with negative mean squared error. The best score will be negative, but the absolute value is considered.
    """)
    st.image("/mount/src/minatharwat93-airbnb_project_regression/static/images/gb1.png", caption="GradientBoostingRegressor")
    st.image("/mount/src/minatharwat93-airbnb_project_regression/static/images/pipe2.png", caption="pipeline with model")
    st.image("/mount/src/minatharwat93-airbnb_project_regression/static/images/gb2.png", caption="GradientBoostingRegressor with gridsearch")

    # Test Score & Confidence Interval
    st.write("""
        4) Test Score & Confidence Interval
        The final model’s performance is evaluated on the test set, and a confidence interval is calculated to assess the stability of the model.
    """)
    st.image("/mount/src/minatharwat93-airbnb_project_regression/static/images/ggb1.png", caption=" train & test GradientBoostingRegressor with gridsearch")
    st.image("/mount/src/minatharwat93-airbnb_project_regression/static/images/ggb2.png", caption="train & test GradientBoostingRegressor")

    # Save Model
    st.write("""
        5) Save Model
        Once the best-performing model is selected, it is saved using `dill` and stored in JSON and PKL formats for future use.
    """)

if __name__ == "__main__":
    main()
