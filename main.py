import streamlit as st
from Pages import image_detection


def app():
    st.title('VEHICLE DETECTION')
    menu = ['From Image', 'From Video', 'Real Time']
    sidebar = st.sidebar
    choice = sidebar.selectbox("Menu", menu)
    if choice == 'From Image':
        image_detection.detect_from_image()
    

if __name__ == '__main__':
    app()

