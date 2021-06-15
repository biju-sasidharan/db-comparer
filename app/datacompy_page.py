# import datacompy
import streamlit as st

import utils
import datacompy as dcp

import db_config

if db_config.DB_TYPE == 'SQLITE':
    import db_comparer_sqlite as dc
else:
    import db_comparer_postgresql as dc

@st.cache
def load_source_data(source):
    df = dc.get_data(source, utils.SOURCE_CONNECTION_STRING)
    return df

@st.cache
def load_target_data(target):
    df = dc.get_data(target, utils.TARGET_CONNECTION_STRING)
    return df


def show_datacompy():
    st.subheader("DataCompy")

    st.write("""DataComPy library is a package to compare two dataframes and provide 
    a human-readable output describing the differences. Select the source and target 
    tables to compare and the joining columns to proceed.""")

    col1, col2, col3, col4, col5 = st.beta_columns([1,1,1,1,1])
    with col1:
        st.write("Select tables to compare:")

    with col4:
        st.write("Select columns to join:")

    col1, col2, col3, col4, col5 = st.beta_columns([1,1,1,1,1])
    
    with col1:
        
        source_lst = dc.get_tables(utils.SOURCE_CONNECTION_STRING)
        source_lst.insert(0, 'Select')
        select_source = st.selectbox("Source Table", source_lst)

    with col2:
        # st.write("")
        target_lst = dc.get_tables(utils.TARGET_CONNECTION_STRING)
        target_lst.insert(0, 'Select')
        select_target = st.selectbox("Target Table", target_lst)
    
    with col3:
        st.write("""<style>
        .vl {
                border-left: 3px solid green;
                height: 80px;
                position: absolute;
                left: 50%;
                margin-left: -3px;
                top: 0;
            }
        </style>""", unsafe_allow_html=True)

        st.write("<div class='vl'></div>", unsafe_allow_html=True)

    with col4:
        df = dc.get_schema(select_source)
        source_join_lst = df['column_name'].values.tolist()
        select_join_cols = st.multiselect("Joining Columns", source_join_lst)

    st.write("")
    
    if (select_join_cols != []):
        # print("I am in")
        df_source = load_source_data(select_source)
        df_target = load_target_data(select_target)
        # df_source = dc.get_data(select_source)
        # df_target = dc.get_data(select_target)
        compare = dcp.Compare( 
            df_source, 
            df_target, 
            join_columns = select_join_cols,  
            abs_tol = 0, 
            rel_tol = 0,  
            df1_name = 'Source', 
            df2_name = 'Target' 
        ) 
        compare.matches(ignore_extra_columns = False)  

        st.write("### Comparison Result -", unsafe_allow_html=True)
        st.text(compare.report())