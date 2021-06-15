import streamlit as st

import custom_dqc
import datacompy_page as dcm
import about
import home

from utils import  (HTML_SIDEBAR_TEMPLATE,
                    HTML_SIDEBAR_BUTTON_TEMPLATE,
                    HTML_SIDEBAR_DIV_WIDE_TEMPLATE,
                    HTML_SUMMARY_FONT_IMAGE_TEMPLATE,
                    HTML_EXPAND_HEADER_TEMPLATE
                    )


# Setting page title
PAGE_CONFIG = {"page_title":"Data Quality Checker Tool", "page_icon":"':computer:", "layout":"wide"}
st.set_page_config(**PAGE_CONFIG)


# @st.cache
# def load_image(image_file):
#     img = Image.open(image_file)
#     return img


st.write("""<link rel="stylesheet"
          href="https://fonts.googleapis.com/css?family=Tangerine">
          <u><font style="font-family:'Tangerine'; font-size:48px; color:#873e23;">
          <center><b>Data Quality Checker (DQC)</b></center></font></u>""", unsafe_allow_html=True)

st.markdown(HTML_SIDEBAR_TEMPLATE, unsafe_allow_html=True)
st.markdown(HTML_SIDEBAR_BUTTON_TEMPLATE, unsafe_allow_html=True)
st.markdown(HTML_SIDEBAR_DIV_WIDE_TEMPLATE, unsafe_allow_html=True)
st.markdown(HTML_SUMMARY_FONT_IMAGE_TEMPLATE,  unsafe_allow_html=True)
st.markdown(HTML_EXPAND_HEADER_TEMPLATE,  unsafe_allow_html=True)

# Menu
select_menu = st.sidebar.selectbox("Menu", ['Home', 'Custom DQC', 'DataComPy', 'About'])

# Display page based on the menu selected
if __name__ =="__main__":
    if select_menu == 'Home':
        home.show_home()
    elif select_menu == 'About':
        about.show_about()
    elif select_menu == 'DataComPy':
        dcm.show_datacompy()
    else:
        custom_dqc.show_custom_dqc()