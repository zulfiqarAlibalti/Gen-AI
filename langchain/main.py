import streamlit as st
import langchain_helper

st.title("Tech Startup Name Generator")

# Sidebar to pick a tech area
tech_name = st.sidebar.selectbox("Pick a Tech", ("web3", "AI", "Computer Vision", "Wearable Sensors", "Imaging"))

if tech_name:
    # Call the function from langchain_helper to get the tech startup name and target area
    response = langchain_helper.generate_tech_Startup_name(tech_name)

    # Display the generated tech startup name
    st.header(response['tech_startup_name'])

    # Split and display the target areas
    target_area = response['target_area'].split(",")
    st.write("**Target Area**")
    for area in target_area:
        st.write("-", area)
