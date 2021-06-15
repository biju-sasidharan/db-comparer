import streamlit as st
import base64

ABOUT_IMAGE = '../images/about.jpg'
DATACOMPY_IMAGE = '../images/datacompy.jpg'

def show_about():
    st.subheader("About")
    st.write("Tool is developed using open source libraries.")
    # st.write("")

    st.write("""#### Tools and Libraries:
- Python
- Streamlit
- Postgresql / Sqlite
- DataComPy
    
    """, unsafe_allow_html=True)
    st.write("")

    st.write("#### Flow diagrams -", unsafe_allow_html=True)
    col1, col2, col3 = st.beta_columns([2,.25,2])
    with col1:
        st.write("<center> Custom Data Quality Checker </center>", unsafe_allow_html=True)
        st.write("<center><img src='data:image/png;base64,{}' height=300px; width=550px;><center>".format(base64.b64encode(open(ABOUT_IMAGE, "rb").read()).decode()), unsafe_allow_html=True)


    with col2:
        st.write("""<style>
        .vl {
                border-left: 3px solid green;
                height: 350px;
                position: absolute;
                left: 50%;
                margin-left: -3px;
                top: 0;
            }
        </style>""", unsafe_allow_html=True)

        st.write("<div class='vl'></div>", unsafe_allow_html=True)


    with col3:
        st.write("<center> DataComPy </center>", unsafe_allow_html=True)
        st.write("<center><img src='data:image/png;base64,{}' height=300px; width=550px;><center>".format(base64.b64encode(open(DATACOMPY_IMAGE, "rb").read()).decode()), unsafe_allow_html=True)
