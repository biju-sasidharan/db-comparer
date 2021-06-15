import streamlit as st
import base64

from email.mime.text import MIMEText
import smtplib

import db_config

if db_config.DB_TYPE == 'SQLITE':
    import db_comparer_sqlite as dc
else:
    import db_comparer_postgresql as dc

HOME_IMAGE = '../images/home.jpg'



def show_home():
    st.subheader("Home")

    st.write("""
    ### Data Migration Quality Checks
This proof of concept (POC) is an attempt to automate the basic quality checks that needs to be carried out during any data migration process. When data is moved from one environment to another, integrity is the key concern. 

*Prototype functionality:*
* Reduces the manual effort involved in quality checking during migration.
* Acts as a single interface incorporating functionalities from multiple libraries.


#### App Content
    - Home: App Description and previous execution summary
    - Custom Data Quality Checker (DQC): Custom built methods for analysing Data Quality
    - DataComPy: In-built Python package to compare 2 Dataframes - Similar To SAS’s "PROC COMPARE"
    - About: Tools & Libraries
    """)
       
    st.write("<center><img src='data:image/png;base64,{}' height=350px; width=700px;></center>".format(base64.b64encode(open(HOME_IMAGE, "rb").read()).decode()), unsafe_allow_html=True)
        
    st.write("")
    st.write("")
    st.write("")
    with st.beta_expander("Monitor Previous Results"):
        st.write("Provides summmary of the previous executions of the app. Column value 1 indicates match and 0 indicates unmatch.")
        st.dataframe(dc.get_app_data())
