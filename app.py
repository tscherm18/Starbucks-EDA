
import streamlit as st
import pandas as pd
import plotly.express as px

# Set page title and icon
st.set_page_config(page_title="Starbuck Dataset Exploration", page_icon="☕️")

# Sidebar navigation
page = st.sidebar.selectbox("Select a Page", ["Home", "Data Overview", "Exploratory Data Analysis"])

# Load dataset
df = pd.read_csv('data/cleaned_starbucks.csv')

# Home Page
if page == "Home":
    st.title("📊 Starbucks Mini Project")
    st.subheader("Welcome to the Starbucks dataset overview!")
    st.write("""
        This app provides an interactive platform to explore the Starbucks dataset. 
        You can visualize the distribution of data, explore relationships between features, and even make predictions on new data!
        Use the sidebar to navigate through the sections.
    """)
    st.image('https://www.foodandwine.com/thmb/fUl1ilvd14PXTFsUM0mid4i7RTo=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/Starbucks-Official-Holiday-Menu-FT-BLOG1124-drinks-8dc7a20889a94736ba5a7b83ae6b522c.jpg', caption="Which Drink is Your Favorite?")
    st.write("Use the sidebar to navigate between different sections")


# Data Overview
elif page == "Data Overview":
    st.title("🔢 Data Overview")

    st.subheader("About the Data")
    st.write("""
        This dataset serves as a comprehensive guide to the nutritional content of Starbucks beverages, making it a valuable resource
        for reasearchers, dietitians, and health-conscious consumers. They're three object variables: Bevarage_category, Beverage, and
        Beverage_prep while the rest our numerical variables of various nutritional stats.
    """)
    st.image('https://www.usatoday.com/gcdn/authoring/authoring-images/2023/08/23/USAT/70655313007-starbucks-fall-beverages.png?crop=1275,719,x82,y0', caption="Starbucks Dataset")

    # Dataset Display
    st.subheader("Quick Glance at the Data")
    if st.checkbox("Show DataFrame"):
        st.dataframe(df)
    

    # Shape of Dataset
    if st.checkbox("Show Shape of Data"):
        st.write(f"The dataset contains {df.shape[0]} rows and {df.shape[1]} columns.")


# Exploratory Data Analysis (EDA)
elif page == "Exploratory Data Analysis":
    st.title("📊 Exploratory Data Analysis (EDA)")

    st.subheader("Select the type of visualization you'd like to explore:")
    eda_type = st.multiselect("Visualization Options", ['Histograms', 'Box Plots', 'Scatterplots', 'Count Plots'])

    obj_cols = df.select_dtypes(include='object').columns.tolist()
    num_cols = df.select_dtypes(include='number').columns.tolist()

    if 'Histograms' in eda_type:
        st.subheader("Histograms - Visualizing Numerical Distributions")
        h_selected_col = st.selectbox("Select a numerical column for the histogram:", num_cols)
        if h_selected_col:
            chart_title = f"Distribution of {h_selected_col.title().replace('_', ' ')}"
            st.plotly_chart(px.histogram(df, x=h_selected_col, title=chart_title))

    if 'Box Plots' in eda_type:
        st.subheader("Box Plots - Visualizing Numerical Distributions")
        b_selected_col = st.selectbox("Select a numerical column for the box plot:", num_cols)
        if b_selected_col:
            chart_title = f"Distribution of {b_selected_col.title().replace('_', ' ')}"
            st.plotly_chart(px.box(df, x=b_selected_col, y='Beverage_category', title=chart_title, color='Beverage_category'))

    if 'Scatterplots' in eda_type:
        st.subheader("Scatterplots - Visualizing Relationships")
        selected_col_x = st.selectbox("Select x-axis variable:", num_cols)
        selected_col_y = st.selectbox("Select y-axis variable:", num_cols)
        if selected_col_x and selected_col_y:
            chart_title = f"{selected_col_x.title().replace('_', ' ')} vs. {selected_col_y.title().replace('_', ' ')}"
            st.plotly_chart(px.scatter(df, x=selected_col_x, y=selected_col_y, title=chart_title))

    if 'Count Plots' in eda_type:
        st.subheader("Count Plots - Visualizing Categorical Distributions")
        selected_col = st.selectbox("Select a categorical variable:", obj_cols)
        if selected_col:
            chart_title = f'Distribution of {selected_col.title()}'
            st.plotly_chart(px.histogram(df, y=selected_col, title=chart_title))