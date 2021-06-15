import streamlit as st
import base64
import time

import pandas as pd

import generics as gn

import utils
from utils import  (
    HTML_RANDOM_TEMPLATE, 
    HTML_HEADER_TEMPLATE,
    HTML_SIDEBAR_TEMPLATE,
    HTML_SIDEBAR_BUTTON_TEMPLATE,
    HTML_SIDEBAR_DIV_WIDE_TEMPLATE,
    HTML_ROWCOUNT_TICK_IMAGE_TEMPLATE,
    HTML_COLCOUNT_TICK_IMAGE_TEMPLATE,
    HTML_COLNAME_TICK_IMAGE_TEMPLATE,
    HTML_DATATYPE_TICK_IMAGE_TEMPLATE,
    HTML_NULL_TICK_IMAGE_TEMPLATE,
    HTML_PK_TICK_IMAGE_TEMPLATE,
    HTML_FK_TICK_IMAGE_TEMPLATE,
    HTML_IDX_TICK_IMAGE_TEMPLATE,
    HTML_VIEWS_TICK_IMAGE_TEMPLATE,
    HTML_SUMMARY_FONT_IMAGE_TEMPLATE,
    HTML_EXPAND_HEADER_TEMPLATE,
    HTML_TRIGGER_TICK_IMAGE_TEMPLATE
)

import db_config

if db_config.DB_TYPE == 'SQLITE':
    import db_comparer_sqlite as dc
else:
    import db_comparer_postgresql as dc

import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


RIGHT_TICK_IMAGE = "../images/right.jpg"
WRONG_TICK_IMAGE = "../images/wrong.jpg"
SOURCE_COLOR = '../images/source_color.jpg'
TARGET_COLOR = '../images/target_color.jpg'

@st.cache
def load_source_data(source):
    df = dc.get_data(source, utils.SOURCE_CONNECTION_STRING)
    return df

@st.cache
def load_target_data(target):
    df = dc.get_data(target, utils.TARGET_CONNECTION_STRING)
    return df

def send_email(email_text, recipient_email):
    
    if st.button("Send Email"):

        port = 465  # For SSL
        smtp_server = "smtp.gmail.com"
        sender_email = "custom.dqc@gmail.com"  
        receiver_email = recipient_email
        password = 'Test@123'

        message = MIMEMultipart("alternative")
        message["Subject"] = "Data Quality Check"
        message["From"] = sender_email
        message["To"] = receiver_email

        text = """{}""".format(email_text)
        part1 = MIMEText(text, "plain")

        message.attach(part1)

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message.as_string())
            
        st.success("Email send successfully to {}".format(recipient_email)) 

def truncate(string, width):
    if len(string) > width:
        string = string[:width-3] + '...'
    return string

def make_downloadable(data):
    timestr = time.strftime("%Y%m%d-%H%M%S")
    csvfile = data.to_csv(index=False)
    b64 = base64.b64encode(csvfile.encode()).decode()  # B64 encoding
    st.markdown("### ** Download CSV File ** ")
    new_filename = "dqc_summary_{}.csv".format(timestr)
    href = f'<a href="data:file/csv;base64,{b64}" download="{new_filename}">Click Here!</a>'
    st.markdown(href, unsafe_allow_html=True)


def show_custom_dqc():
    # Header
    st.subheader("Custom Data Quality Checker")
    st.write("""Select source and target tables from the dropdown list to automate the process.""")

    col1, col2, col3, col4 = st.beta_columns([1,1,1,2])
    with col1:
        source_lst = dc.get_tables(utils.SOURCE_CONNECTION_STRING)
        source_lst.insert(0, 'Select')
        select_source = st.selectbox("Source Table", source_lst)
    
    with col2:
        target_lst = dc.get_tables(utils.TARGET_CONNECTION_STRING)
        target_lst.insert(0, 'Select')
        select_target = st.selectbox("Target Table", target_lst)

    if (select_source != 'Select') & (select_target != 'Select'):
        with st.beta_expander("Basic Checks"):
            st.write("This section provides basic quality checks between the source and target tables.")
            col1, col2, col3, col4 = st.beta_columns([2, 2, 1, 1])

            with col1:
                st.write("#### Source")
                df_source = load_source_data(select_source)
                source_row_count = df_source.shape[0]
                source_column_count = df_source.shape[1]
                source_column_names = str(df_source.columns.tolist())

                st.write("* ###### Row count: <b style='color: blue;'>{} rows </b>".format(source_row_count), unsafe_allow_html=True)
                st.write("* ###### Column count: <b style='color: blue;'>{} columns</b>".format(source_column_count), unsafe_allow_html=True)
                st.write("* ###### Column names: <b style='color: blue;'>{}</b>".format(truncate(source_column_names, 50)), unsafe_allow_html=True)

            with col2:
                st.write("#### Target")
                df_target = load_target_data(select_target)
                target_row_count = df_target.shape[0]
                target_column_count = df_target.shape[1]
                target_column_names = str(df_target.columns.tolist())

                st.write("* ###### Row count: <b style='color: blue;'>{} rows</b>".format(target_row_count), unsafe_allow_html=True)
                st.write("* ###### Column count: <b style='color: blue;'>{} columns</b>".format(target_column_count), unsafe_allow_html=True)
                st.write("* ###### Column names: <b style='color: blue;'>{}</b>".format(truncate(target_column_names, 50)), unsafe_allow_html=True)
        
    
            with col3:
                st.write("#### Summary Stats")

                if source_row_count != target_row_count:
                    row_count_tick_image = WRONG_TICK_IMAGE
                else:
                    row_count_tick_image = RIGHT_TICK_IMAGE

                if source_column_count != target_column_count:
                    column_count_tick_image = WRONG_TICK_IMAGE
                else:
                    column_count_tick_image = RIGHT_TICK_IMAGE

                source_diff_len = len(df_source.columns.difference(df_target.columns))
                target_diff_len = len(df_target.columns.difference(df_source.columns))
                
                if (source_diff_len > 0) | (target_diff_len >  0):
                    column_name_tick_image = WRONG_TICK_IMAGE
                else:
                    column_name_tick_image = RIGHT_TICK_IMAGE

                st.markdown(
                    HTML_ROWCOUNT_TICK_IMAGE_TEMPLATE.format(base64.b64encode(open(row_count_tick_image, "rb").read()).decode()),
                    unsafe_allow_html=True
                )

                st.markdown(
                    HTML_COLCOUNT_TICK_IMAGE_TEMPLATE.format(base64.b64encode(open(column_count_tick_image, "rb").read()).decode()),
                    unsafe_allow_html=True
                )
                
                st.markdown(
                    HTML_COLNAME_TICK_IMAGE_TEMPLATE.format(base64.b64encode(open(column_name_tick_image, "rb").read()).decode()),
                    unsafe_allow_html=True
                )

            with col4:
                st.write("")
                st.write("")
                st.write("")
                basic_detailedsummary_buttonclick = st.button('Show Summary Report', 'basic')

        if basic_detailedsummary_buttonclick:
            st.write("")
            st.write("#### Summary Report: ")
            gn.show_basic_summary(source_row_count, target_row_count, 
                source_column_count, target_column_count, source_diff_len, 
                target_diff_len, df_source, df_target, 
                select_source, select_target
            )

        st.write("")

        with st.beta_expander("Schema Checks"):
            st.write("This section provides schema level quality checks between the source and target tables.")
            col1, col2, col3, col4 = st.beta_columns([2, 2, 1, 1])

            with col1:
                st.write("#### Source")
                
                df_source_schema = dc.get_schema(select_source, utils.SOURCE_CONNECTION_STRING)
                source_column_datatypes = str(df_source_schema.column_info.tolist())
                source_column_is_nullable = str(df_source_schema.column_is_nullable.tolist())
                
                df_source_views = dc.get_views(select_source, utils.SOURCE_CONNECTION_STRING)
                source_views = str(df_source_views.view_name.tolist())

                df_source_primary_keys = dc.get_primary_keys(select_source, utils.SOURCE_CONNECTION_STRING)
                source_primary_keys = str(df_source_primary_keys.key_column.tolist())

                df_source_foreign_keys = dc.get_foreign_keys(select_source, utils.SOURCE_CONNECTION_STRING)
                source_foreign_keys = str(df_source_foreign_keys.fkey.tolist())

                df_source_indexes = dc.get_indexes(select_source, utils.SOURCE_CONNECTION_STRING)
                source_indexes = str(df_source_indexes.indexname.tolist())

                df_source_triggers = dc.get_triggers(select_source, utils.SOURCE_CONNECTION_STRING)
                source_triggers = str(df_source_triggers.trigger_name.tolist())

                st.write("* ###### Data types: <b style='color: blue;'>{}</b>".format(truncate(source_column_datatypes, 100)), unsafe_allow_html=True)
                st.write("* ###### Null check: <b style='color: blue;'>{}</b>".format(source_column_is_nullable), unsafe_allow_html=True)
                st.write("* ###### Primary key columns: <b style='color: blue;'>{}</b>".format(truncate(source_primary_keys, 50)), unsafe_allow_html=True)
                st.write("* ###### Foreign keys: <b style='color: blue;'>{}</b>".format(truncate(source_foreign_keys, 50)), unsafe_allow_html=True)
                st.write("* ###### Index check: <b style='color: blue;'>{}</b>".format(truncate(source_indexes, 50)), unsafe_allow_html=True)
                st.write("* ###### Triggers: <b style='color: blue;'>{}</b>".format(truncate(source_triggers, 50)), unsafe_allow_html=True)
                st.write("* ###### Referenced views: <b style='color: blue;'>{}</b>".format(truncate(source_views, 50)), unsafe_allow_html=True)

            with col2:
                st.write("#### Target")
                df_target_schema = dc.get_schema(select_target, utils.TARGET_CONNECTION_STRING)
                target_column_datatypes = str(df_target_schema.column_info.tolist())
                target_column_is_nullable = str(df_target_schema.column_is_nullable.tolist())
    
                df_target_views = dc.get_views(select_target, utils.TARGET_CONNECTION_STRING)
                target_views = str(df_target_views.view_name.tolist())

                df_target_primary_keys = dc.get_primary_keys(select_target, utils.TARGET_CONNECTION_STRING)
                target_primary_keys = str(df_target_primary_keys.key_column.tolist())

                df_target_foreign_keys = dc.get_foreign_keys(select_target, utils.TARGET_CONNECTION_STRING)
                target_foreign_keys = str(df_target_foreign_keys.fkey.tolist())

                df_target_indexes = dc.get_indexes(select_target, utils.TARGET_CONNECTION_STRING)
                target_indexes = str(df_target_indexes.indexname.tolist())

                df_target_triggers = dc.get_triggers(select_target, utils.TARGET_CONNECTION_STRING)
                target_triggers = str(df_target_triggers.trigger_name.tolist())

                st.write("* ###### Data types: <b style='color: blue;'>{}</b>".format(truncate(target_column_datatypes, 100)), unsafe_allow_html=True)
                st.write("* ###### Null check: <b style='color: blue;'>{}</b>".format(target_column_is_nullable), unsafe_allow_html=True)
                st.write("* ###### Primary key columns: <b style='color: blue;'>{}</b>".format(truncate(target_primary_keys, 50)), unsafe_allow_html=True)
                st.write("* ###### Foreign keys: <b style='color: blue;'>{}</b>".format(truncate(target_foreign_keys, 50)), unsafe_allow_html=True)
                st.write("* ###### Index check: <b style='color: blue;'>{}</b>".format(truncate(target_indexes, 50)), unsafe_allow_html=True)
                st.write("* ###### Triggers: <b style='color: blue;'>{}</b>".format(truncate(target_triggers, 50)), unsafe_allow_html=True)
                st.write("* ###### Referenced views: <b style='color: blue;'>{}</b>".format(truncate(target_views, 50)), unsafe_allow_html=True)
            
        
            with col3:
                st.write("#### Summary Stats")

                # Data  Types
                source_datatype_diff = set(df_source_schema.column_info.to_dict().values()).difference(df_target_schema.column_info.to_dict().values())
                target_datatype_diff = set(df_target_schema.column_info.to_dict().values()).difference(df_source_schema.column_info.to_dict().values())
                source_datatype_diff_len = len(source_datatype_diff)
                target_datatype_diff_len = len(target_datatype_diff)
                if (source_datatype_diff_len > 0) | (target_datatype_diff_len >  0):
                    schema_datatype_tick_image = WRONG_TICK_IMAGE
                else:
                    schema_datatype_tick_image = RIGHT_TICK_IMAGE

                # Null Check
                source_null_diff = set(df_source_schema.column_is_nullable.to_dict().values()).difference(df_target_schema.column_is_nullable.to_dict().values())
                target_null_diff = set(df_target_schema.column_is_nullable.to_dict().values()).difference(df_source_schema.column_is_nullable.to_dict().values())
                source_null_diff_len = len(source_null_diff)
                target_null_diff_len = len(target_null_diff)
                if (source_null_diff_len > 0) | (target_datatype_diff_len >  0):
                    schema_nulltype_tick_image = WRONG_TICK_IMAGE
                else:
                    schema_nulltype_tick_image = RIGHT_TICK_IMAGE

                # Primary Key
                source_pk_diff = set(df_source_primary_keys.key_column.to_dict().values()).difference(df_target_primary_keys.key_column.to_dict().values())
                target_pk_diff = set(df_target_primary_keys.key_column.to_dict().values()).difference(df_source_primary_keys.key_column.to_dict().values())
                source_pk_diff_len = len(source_pk_diff)
                target_pk_diff_len = len(target_pk_diff)
                if (source_pk_diff_len > 0) | (target_pk_diff_len >  0):
                    schema_pk_tick_image = WRONG_TICK_IMAGE
                else:
                    schema_pk_tick_image = RIGHT_TICK_IMAGE

                # Foreign Key
                source_fk_diff = set(df_source_foreign_keys.fkey.to_dict().values()).difference(df_target_foreign_keys.fkey.to_dict().values())
                target_fk_diff = set(df_target_foreign_keys.fkey.to_dict().values()).difference(df_source_foreign_keys.fkey.to_dict().values())
                source_fk_diff_len = len(source_fk_diff)
                target_fk_diff_len = len(target_fk_diff)
                if (source_fk_diff_len > 0) | (target_fk_diff_len >  0):
                    schema_fk_tick_image = WRONG_TICK_IMAGE
                else:
                    schema_fk_tick_image = RIGHT_TICK_IMAGE

                # Index
                source_idx_diff = set(df_source_indexes.indexname.to_dict().values()).difference(df_target_indexes.indexname.to_dict().values())
                target_idx_diff = set(df_target_indexes.indexname.to_dict().values()).difference(df_source_indexes.indexname.to_dict().values())
                source_idx_diff_len = len(source_idx_diff)
                target_idx_diff_len = len(target_idx_diff)
                if (source_idx_diff_len > 0) | (target_idx_diff_len >  0):
                    schema_idx_tick_image = WRONG_TICK_IMAGE
                else:
                    schema_idx_tick_image = RIGHT_TICK_IMAGE

                # Trigger
                source_trigger_diff = set(df_source_triggers.trigger_name.to_dict().values()).difference(df_target_triggers.trigger_name.to_dict().values())
                target_trigger_diff = set(df_target_triggers.trigger_name.to_dict().values()).difference(df_source_triggers.trigger_name.to_dict().values())
                source_trigger_diff_len = len(source_trigger_diff)
                target_trigger_diff_len = len(target_trigger_diff)
                if (source_trigger_diff_len > 0) | (target_trigger_diff_len >  0):
                    schema_trigger_tick_image = WRONG_TICK_IMAGE
                else:
                    schema_trigger_tick_image = RIGHT_TICK_IMAGE

                # Views
                source_views_diff = set(df_source_views.view_name.to_dict().values()).difference(df_target_views.view_name.to_dict().values())
                target_views_diff = set(df_target_views.view_name.to_dict().values()).difference(df_source_views.view_name.to_dict().values())
                source_views_diff_len = len(source_views_diff)
                target_views_diff_len = len(target_views_diff)
                if (source_views_diff_len > 0) | (target_views_diff_len >  0):
                    schema_views_tick_image = WRONG_TICK_IMAGE
                else:
                    schema_views_tick_image = RIGHT_TICK_IMAGE

                st.markdown(
                    HTML_DATATYPE_TICK_IMAGE_TEMPLATE.format(base64.b64encode(open(schema_datatype_tick_image, "rb").read()).decode()),
                    unsafe_allow_html=True
                )

                st.markdown(
                    HTML_NULL_TICK_IMAGE_TEMPLATE.format(base64.b64encode(open(schema_nulltype_tick_image, "rb").read()).decode()),
                    unsafe_allow_html=True
                )

                st.markdown(
                    HTML_PK_TICK_IMAGE_TEMPLATE.format(base64.b64encode(open(schema_pk_tick_image, "rb").read()).decode()),
                    unsafe_allow_html=True
                )

                st.markdown(
                    HTML_FK_TICK_IMAGE_TEMPLATE.format(base64.b64encode(open(schema_fk_tick_image, "rb").read()).decode()),
                    unsafe_allow_html=True
                )

                st.markdown(
                    HTML_IDX_TICK_IMAGE_TEMPLATE.format(base64.b64encode(open(schema_idx_tick_image, "rb").read()).decode()),
                    unsafe_allow_html=True
                )

                st.markdown(
                    HTML_TRIGGER_TICK_IMAGE_TEMPLATE.format(base64.b64encode(open(schema_trigger_tick_image, "rb").read()).decode()),
                    unsafe_allow_html=True
                )

                st.markdown(
                    HTML_VIEWS_TICK_IMAGE_TEMPLATE.format(base64.b64encode(open(schema_views_tick_image, "rb").read()).decode()),
                    unsafe_allow_html=True
                )

            with col4:
                st.write("")
                st.write("")
                st.write("")
                st.write("")
                st.write("")
                st.write("")
                schema_detailedsummary_buttonclick = st.button('Show Summary Report', 'schema')

        if schema_detailedsummary_buttonclick:
            st.write("")
            st.write("#### Summary Report: ")

            gn.show_schema_summary(source_datatype_diff_len, target_datatype_diff_len,
                source_null_diff_len, target_null_diff_len,  source_pk_diff_len, target_pk_diff_len,
                source_fk_diff_len, target_fk_diff_len, source_idx_diff_len, target_idx_diff_len,
                source_trigger_diff_len, target_trigger_diff_len, source_views_diff_len, target_views_diff_len,
                select_source, select_target, source_datatype_diff, target_datatype_diff, 
                source_null_diff, target_null_diff, source_pk_diff, target_pk_diff, 
                source_fk_diff, target_fk_diff, source_idx_diff, target_idx_diff, 
                source_trigger_diff, target_trigger_diff, source_views_diff, target_views_diff
                )

        st.write("")
        with st.beta_expander("Data Checks"):
            st.write("This section provides data level checks between the source and target tables.")
            # st.write("")
            st.write("###### <img src='data:image/png;base64,{}' height=10px; width=10px;> - source values that are different from target".format(base64.b64encode(open(SOURCE_COLOR, "rb").read()).decode()), unsafe_allow_html=True)
            st.write("###### <img src='data:image/png;base64,{}' height=10px; width=10px;> - target values that are different from source".format(base64.b64encode(open(TARGET_COLOR, "rb").read()).decode()), unsafe_allow_html=True)

            frames = [
                df_source.merge(df_target, how = 'outer' ,indicator=True).loc[lambda x : x['_merge']=='left_only'],
                df_source.merge(df_target, how = 'outer' ,indicator=True).loc[lambda x : x['_merge']=='right_only']
                ]
            df = pd.concat(frames)

            df.rename(columns={'_merge': 'remarks'}, inplace=True)
            df['remarks'].replace('left_only', 'UNMATCHED DATA IN SOURCE TABLE', inplace=True)
            df['remarks'].replace('right_only', 'UNMATCHED DATA IN TARGET TABLE', inplace=True)
            df['remarks'] = df['remarks'].astype('object')

            st.dataframe(df.style.apply(lambda x: ['background: lightgreen' if x.remarks == 'UNMATCHED DATA IN SOURCE TABLE'
                                else 'background-color: cyan' for i in x], 
                    axis=1))

        # App data insertion
        (rows_count, col_count, col_name, data_type, null_check, pk_check, fk_check, 
        idx_check, trigger_check, views_check) = gn.insert_app_data(source_row_count, target_row_count, 
            source_column_count, target_column_count, source_diff_len, target_diff_len, 
            source_datatype_diff_len, target_datatype_diff_len, source_null_diff_len, target_null_diff_len,  
            source_pk_diff_len, target_pk_diff_len, source_fk_diff_len, target_fk_diff_len, source_idx_diff_len, 
            target_idx_diff_len, source_trigger_diff_len, target_trigger_diff_len, source_views_diff_len, 
            target_views_diff_len)

        dc.insert_app_data(select_source, select_target, rows_count, col_count, col_name, data_type, null_check, pk_check, fk_check, idx_check, trigger_check, views_check)
 
        # Download + Email
        st.write("")
        with st.beta_expander("Download / Email Summary"):
            # Log file DB
            df_log = pd.DataFrame(columns=['summary'])

            col1, col2 = st.beta_columns(2)
            with col1:
                df_log = gn.download_summary(source_row_count, target_row_count, 
                    source_column_count, target_column_count, source_diff_len, 
                    target_diff_len, df_source, df_target, df_log,
                    select_source, select_target,
                    source_datatype_diff_len, target_datatype_diff_len, source_null_diff_len, target_null_diff_len,  
                    source_pk_diff_len, target_pk_diff_len, source_fk_diff_len, target_fk_diff_len, source_idx_diff_len, 
                    target_idx_diff_len, source_trigger_diff_len, target_trigger_diff_len, source_views_diff_len, 
                    target_views_diff_len, source_datatype_diff, target_datatype_diff, 
                    source_null_diff, target_null_diff, source_pk_diff, target_pk_diff, 
                    source_fk_diff, target_fk_diff, source_idx_diff, target_idx_diff, 
                    source_trigger_diff, target_trigger_diff, source_views_diff, target_views_diff
                )
                make_downloadable(df_log)
            with col2:
                st.write("A text email with the summary results will be send from the email id custom.dqc@gmail.com")

                email_summary = gn.email_summary(source_row_count, target_row_count, 
                    source_column_count, target_column_count, source_diff_len, 
                    target_diff_len, df_source, df_target, df_log,
                    select_source, select_target,
                    source_datatype_diff_len, target_datatype_diff_len, source_null_diff_len, target_null_diff_len,  
                    source_pk_diff_len, target_pk_diff_len, source_fk_diff_len, target_fk_diff_len, source_idx_diff_len, 
                    target_idx_diff_len, source_trigger_diff_len, target_trigger_diff_len, source_views_diff_len, 
                    target_views_diff_len, source_datatype_diff, target_datatype_diff, 
                    source_null_diff, target_null_diff, source_pk_diff, target_pk_diff, 
                    source_fk_diff, target_fk_diff, source_idx_diff, target_idx_diff, 
                    source_trigger_diff, target_trigger_diff, source_views_diff, target_views_diff)

                # st.text(email_summary)
                receipient_email = st.text_input('Enter Recipient Email') 
                if receipient_email == "":
                    st.warning("Please enter a vaild recipient email.")
                # else:
                send_email(email_summary, receipient_email)
