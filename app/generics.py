import streamlit as st

def show_basic_summary(source_row_count, target_row_count, source_column_count, target_column_count, 
source_diff_len, target_diff_len, df_source, df_target, select_source, select_target):
    if source_row_count != target_row_count:
        st.write("1. #### <b style='color: red;'>There are row count differences between {} and {}.</b>".format(select_source, select_target), unsafe_allow_html=True)
    else:
        st.write("1. #### <b style='color: green;'>Row count of {} and {} matches.</b>".format(select_source, select_target), unsafe_allow_html=True)

    if source_column_count != target_column_count:
        st.write("2. #### <b style='color: red;'>There are difference in column count between {} and {}.</b>".format(select_source, select_target), unsafe_allow_html=True)
    else:
        st.write("2. #### <b style='color: green;'>Number of columns in {} and {} matches.</b>".format(select_source, select_target), unsafe_allow_html=True)

    if (source_diff_len > 0) | (target_diff_len >  0):
        source_to_target_diff = df_source.columns.difference(df_target.columns).tolist()
        target_to_source_diff = df_target.columns.difference(df_source.columns).tolist()

        st.write("3. #### <b style='color: red;'>Discrepancy found in column names -</b>", unsafe_allow_html=True)
        if source_diff_len > 0:
            st.write("  - ##### <b>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{} columns differs in {} table.</b>".format(source_to_target_diff, select_source), unsafe_allow_html=True)

        if target_diff_len > 0:
            st.write("  - ##### <b>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{} columns differs in {} table.</b>".format(target_to_source_diff, select_target), unsafe_allow_html=True)
    else:
        st.write("3. #### <b style='color: green;'>Both the tables have identical/zero column names.</b>", unsafe_allow_html=True)

def show_schema_summary(source_datatype_diff_len, target_datatype_diff_len,
source_null_diff_len, target_null_diff_len,  source_pk_diff_len, target_pk_diff_len,
source_fk_diff_len, target_fk_diff_len, source_idx_diff_len, target_idx_diff_len,
source_trigger_diff_len, target_trigger_diff_len, source_views_diff_len, target_views_diff_len,
select_source, select_target, source_datatype_diff, target_datatype_diff, 
source_null_diff, target_null_diff, source_pk_diff, target_pk_diff, 
source_fk_diff, target_fk_diff, source_idx_diff, target_idx_diff, 
source_trigger_diff, target_trigger_diff, source_views_diff, target_views_diff
):
    if (source_datatype_diff_len > 0) | (target_datatype_diff_len >  0):
        st.write("1. #### <b style='color: red;'>Discrepancy found in data types -</b>", unsafe_allow_html=True)
        if source_datatype_diff_len > 0:
            st.write("  - ##### <b>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{} data type(s) differs in {} table.</b>".format(source_datatype_diff, select_source), unsafe_allow_html=True)
            
        if target_datatype_diff_len > 0:
            st.write("  - ##### <b>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{} data type(s) differs in {} table.</b>".format(target_datatype_diff, select_target), unsafe_allow_html=True)
    else:
        st.write("1. #### <b style='color: green;'>Both the tables have identical/zero data types.</b>", unsafe_allow_html=True)


    # Null
    if (source_null_diff_len > 0) | (target_null_diff_len >  0):
        st.write("2. #### <b style='color: red;'>Discrepancy found in null types -</b>", unsafe_allow_html=True)
        if source_null_diff_len > 0:
            st.write("  - ##### <b>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{} null type differs in {} table.</b>".format(source_null_diff, select_source), unsafe_allow_html=True)
            
        if target_null_diff_len > 0:
            st.write("  - ##### <b>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{} null type differs in {} table.</b>".format(target_null_diff, select_target), unsafe_allow_html=True)
    else:
        st.write("2. #### <b style='color: green;'>Both the tables have identical/zero null types.</b>", unsafe_allow_html=True)


    # Primary key
    if (source_pk_diff_len > 0) | (target_pk_diff_len >  0):
        st.write("3. #### <b style='color: red;'>Discrepancy found in primary keys -</b>", unsafe_allow_html=True)
        if source_pk_diff_len > 0:
            st.write("  - ##### <b>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{} primary keys differs in {} table.</b>".format(source_pk_diff, select_source), unsafe_allow_html=True)
            
        if target_pk_diff_len > 0:
            st.write("  - ##### <b>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{} primary keys differs in {} table.</b>".format(target_pk_diff, select_target), unsafe_allow_html=True)
    else:
        st.write("3. #### <b style='color: green;'>Both the tables have identical/zero primary keys.</b>", unsafe_allow_html=True)

    # Foreign key
    if (source_fk_diff_len > 0) | (target_fk_diff_len >  0):
        st.write("4. #### <b style='color: red;'>Discrepancy found in foreign keys -</b>", unsafe_allow_html=True)
        if source_fk_diff_len > 0:
            st.write("  - ##### <b>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{} foreign keys differs in {} table.</b>".format(source_fk_diff, select_source), unsafe_allow_html=True)
            
        if target_fk_diff_len > 0:
            st.write("  - ##### <b>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{} foreign keys differs in {} table.</b>".format(target_fk_diff, select_target), unsafe_allow_html=True)
    else:
        st.write("4. #### <b style='color: green;'>Both the tables have identical/zero foreign keys.</b>", unsafe_allow_html=True)


    # Index key
    if (source_idx_diff_len > 0) | (target_idx_diff_len >  0):
        st.write("5. #### <b style='color: red;'>Discrepancy found in index keys -</b>", unsafe_allow_html=True)
        if source_idx_diff_len > 0:
            st.write("  - ##### <b>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{} index keys differs in {} table.</b>".format(source_idx_diff, select_source), unsafe_allow_html=True)
            
        if target_idx_diff_len > 0:
            st.write("  - ##### <b>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{} index keys differs in {} table.</b>".format(target_idx_diff, select_target), unsafe_allow_html=True)
    else:
        st.write("5. #### <b style='color: green;'>Both the tables have identical/zero index keys.</b>", unsafe_allow_html=True)

    # Triggers
    if (source_trigger_diff_len > 0) | (target_trigger_diff_len >  0):
        st.write("6. #### <b style='color: red;'>Discrepancy found in trigger -</b>", unsafe_allow_html=True)
        if source_trigger_diff_len > 0:
            st.write("  - ##### <b>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{} triggers differs in {} table.</b>".format(source_trigger_diff, select_source), unsafe_allow_html=True)
            
        if target_trigger_diff_len > 0:
            st.write("  - ##### <b>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{} triggers differs in {} table.</b>".format(target_trigger_diff, select_target), unsafe_allow_html=True)
    else:
        st.write("6. #### <b style='color: green;'>Both the tables have identical/zero triggers.</b>", unsafe_allow_html=True)


    # Views
    if (source_views_diff_len > 0) | (target_views_diff_len >  0):
        st.write("7. #### <b style='color: red;'>Discrepance found in views referenced -</b>", unsafe_allow_html=True)
        if source_views_diff_len > 0:
            st.write("  - ##### <b>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{} views referenced in {} table.</b>".format(source_views_diff, select_source), unsafe_allow_html=True)
            
        if target_views_diff_len > 0:
            st.write("  - ##### <b>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{} views referenced in {} table.</b>".format(target_views_diff, select_target), unsafe_allow_html=True)
    else:
        st.write("7. #### <b style='color: green;'>Both the tables have identical/zero views referenced.</b>", unsafe_allow_html=True)



def download_summary(source_row_count, target_row_count, source_column_count, target_column_count, 
    source_diff_len, target_diff_len, df_source, df_target, df_log, select_source, select_target,
    source_datatype_diff_len, target_datatype_diff_len, source_null_diff_len, target_null_diff_len,  
    source_pk_diff_len, target_pk_diff_len, source_fk_diff_len, target_fk_diff_len, source_idx_diff_len, 
    target_idx_diff_len, source_trigger_diff_len, target_trigger_diff_len, source_views_diff_len, 
    target_views_diff_len, source_datatype_diff, target_datatype_diff, 
    source_null_diff, target_null_diff, source_pk_diff, target_pk_diff, 
    source_fk_diff, target_fk_diff, source_idx_diff, target_idx_diff, 
    source_trigger_diff, target_trigger_diff, source_views_diff, target_views_diff):

    df_log = df_log.append({'summary': 'Basic checks'}, ignore_index=True)

    if source_row_count != target_row_count:
        df_log = df_log.append({'summary': 'There are row count differences between {} and {}'.format(select_source, select_target)}, ignore_index=True)
    else:
        df_log = df_log.append({'summary': 'Row count of {} and {} matches.'.format(select_source, select_target)}, ignore_index=True)

    if source_column_count != target_column_count:
        df_log = df_log.append({'summary': 'There are difference in column count between {} and {}'.format(select_source, select_target)}, ignore_index=True)
    else:
        df_log = df_log.append({'summary': 'Number of columns in {} and {} matches.'.format(select_source, select_target)}, ignore_index=True)

    if (source_diff_len > 0) | (target_diff_len >  0):
        source_to_target_diff = df_source.columns.difference(df_target.columns).tolist()
        target_to_source_diff = df_target.columns.difference(df_source.columns).tolist()
        df_log = df_log.append({'summary': 'Discrepancy found in column names -'}, ignore_index=True)
        if source_diff_len > 0:
            df_log = df_log.append({'summary': '{} columns differs in {} table.'.format(source_to_target_diff, select_source)}, ignore_index=True)

        if target_diff_len > 0:
            df_log = df_log.append({'summary': '{} columns differs in {} table.'.format(target_to_source_diff, select_target)}, ignore_index=True)
    else:
        df_log = df_log.append({'summary': 'Both the tables have identical/zero column names.'}, ignore_index=True)


    if (source_datatype_diff_len > 0) | (target_datatype_diff_len >  0):
        df_log = df_log.append({'summary': 'Discrepancy found in data types -'}, ignore_index=True)
        if source_datatype_diff_len > 0:
            df_log = df_log.append({'summary': '{} data type(s) differs in {} table.'.format(source_datatype_diff, select_source)}, ignore_index=True)

        if target_datatype_diff_len > 0:
            df_log = df_log.append({'summary': '{} data type(s) differs in {} table.'.format(target_datatype_diff, select_target)}, ignore_index=True)
    else:
         df_log = df_log.append({'summary': 'Both the tables have identical/zero data types.'}, ignore_index=True)


    df_log = df_log.append({'summary': ''}, ignore_index=True)

    df_log = df_log.append({'summary': 'Schema checks'}, ignore_index=True)
    # Null
    if (source_null_diff_len > 0) | (target_null_diff_len >  0):
        df_log = df_log.append({'summary': 'Discrepancy found in null types -'}, ignore_index=True)
        if source_null_diff_len > 0:
            df_log = df_log.append({'summary': '{} null type differs in {} table.'.format(source_null_diff, select_source)}, ignore_index=True)

        if target_null_diff_len > 0:
            df_log = df_log.append({'summary': '{} null type differs in {} table.'.format(target_null_diff, select_target)}, ignore_index=True)
    else:
        df_log = df_log.append({'summary': 'Both the tables have identical/zero null types.'}, ignore_index=True)


    # Primary key
    if (source_pk_diff_len > 0) | (target_pk_diff_len >  0):
        df_log = df_log.append({'summary': 'Discrepancy found in primary keys -'}, ignore_index=True)

        if source_pk_diff_len > 0:
            df_log = df_log.append({'summary': '{} primary keys differs in {} table.'.format(source_pk_diff, select_source)}, ignore_index=True)

        if target_pk_diff_len > 0:
            df_log = df_log.append({'summary': '{} primary keys differs in {} table.'.format(target_pk_diff, select_target)}, ignore_index=True)
    
    else:
        df_log = df_log.append({'summary': 'Both the tables have identical/zero primary keys.'}, ignore_index=True)

    # Foreign key
    if (source_fk_diff_len > 0) | (target_fk_diff_len >  0):
        df_log = df_log.append({'summary': 'Discrepancy found in foreign keys -'}, ignore_index=True)

        if source_fk_diff_len > 0:
            df_log = df_log.append({'summary': '{} foreign keys differs in {} table.'.format(source_fk_diff, select_source)}, ignore_index=True)

        if target_fk_diff_len > 0:
            df_log = df_log.append({'summary': '{} foreign keys differs in {} table.'.format(target_fk_diff, select_target)}, ignore_index=True)

    else:
        df_log = df_log.append({'summary': 'Both the tables have identical/zero foreign keys.'}, ignore_index=True)

    # Index key
    if (source_idx_diff_len > 0) | (target_idx_diff_len >  0):
        df_log = df_log.append({'summary': 'Discrepancy found in index keys -'}, ignore_index=True)
        if source_idx_diff_len > 0:
            df_log = df_log.append({'summary': '{} index keys differs in {} table.'.format(source_idx_diff, select_source)}, ignore_index=True)

        if target_idx_diff_len > 0:
            df_log = df_log.append({'summary': '{} index keys differs in {} table.'.format(target_idx_diff, select_target)}, ignore_index=True)

    else:
        df_log = df_log.append({'summary': 'Both the tables have identical/zero index keys.'}, ignore_index=True)

    # Triggers
    if (source_trigger_diff_len > 0) | (target_trigger_diff_len >  0):
        df_log = df_log.append({'summary': 'Discrepancy found in trigger keys -'}, ignore_index=True)
        if source_trigger_diff_len > 0:
            df_log = df_log.append({'summary': '{} triggers differs in {} table.'.format(source_trigger_diff, select_source)}, ignore_index=True)

        if target_trigger_diff_len > 0:
            df_log = df_log.append({'summary': '{} triggers differs in {} table.'.format(target_trigger_diff, select_target)}, ignore_index=True)

    else:
        df_log = df_log.append({'summary': 'Both the tables have identical/zero triggers.'}, ignore_index=True)

    # Views
    if (source_views_diff_len > 0) | (target_views_diff_len >  0):
        df_log = df_log.append({'summary': 'Discrepancy found in views referenced -'}, ignore_index=True)
        if source_views_diff_len > 0:
            df_log = df_log.append({'summary': '{} views referenced in {} table.'.format(source_views_diff, select_source)}, ignore_index=True)

        if target_views_diff_len > 0:
            df_log = df_log.append({'summary': '{} views referenced in {} table.'.format(target_views_diff, select_target)}, ignore_index=True)

    else:
        df_log = df_log.append({'summary': 'Both the tables have identical/zero views referenced.'}, ignore_index=True)

    return df_log

def email_summary(source_row_count, target_row_count, source_column_count, target_column_count, 
    source_diff_len, target_diff_len, df_source, df_target, df_log, select_source, select_target,
    source_datatype_diff_len, target_datatype_diff_len, source_null_diff_len, target_null_diff_len,  
    source_pk_diff_len, target_pk_diff_len, source_fk_diff_len, target_fk_diff_len, source_idx_diff_len, 
    target_idx_diff_len, source_trigger_diff_len, target_trigger_diff_len, source_views_diff_len, 
    target_views_diff_len, source_datatype_diff, target_datatype_diff, 
    source_null_diff, target_null_diff, source_pk_diff, target_pk_diff, 
    source_fk_diff, target_fk_diff, source_idx_diff, target_idx_diff, 
    source_trigger_diff, target_trigger_diff, source_views_diff, target_views_diff):

    # df_log = df_log.append({'summary': 'Basic checks'}, ignore_index=True)
    str_email = 'Basic checks:' + '\n'
    if source_row_count != target_row_count:
        str_email = str_email + 'There are row count differences between {} and {}'.format(select_source, select_target) + '\n'
    else:
        str_email = str_email + 'Row count of {} and {} matches.'.format(select_source, select_target) + '\n'

    if source_column_count != target_column_count:
        str_email = str_email + 'There are difference in column count between {} and {}'.format(select_source, select_target) + '\n'
    else:
        str_email = str_email + 'Number of columns in {} and {} matches.'.format(select_source, select_target) + '\n'

    if (source_diff_len > 0) | (target_diff_len >  0):
        source_to_target_diff = df_source.columns.difference(df_target.columns).tolist()
        target_to_source_diff = df_target.columns.difference(df_source.columns).tolist()
        str_email = str_email + 'Discrepancy found in column names -' + '\n'
        if source_diff_len > 0:
            str_email = str_email + '{} columns differs in {} table.'.format(source_to_target_diff, select_source) + '\n'

        if target_diff_len > 0:
            str_email = str_email + '{} columns differs in {} table.'.format(target_to_source_diff, select_target) + '\n'
    else:
        str_email = str_email + 'Both the tables have identical/zero column names.' + '\n'


    if (source_datatype_diff_len > 0) | (target_datatype_diff_len >  0):
        str_email = str_email + 'Discrepancy found in data types -' + '\n'
        if source_datatype_diff_len > 0:
            str_email = str_email + '{} data type(s) differs in {} table.'.format(source_datatype_diff, select_source) + '\n'

        if target_datatype_diff_len > 0:
            str_email = str_email + '{} data type(s) differs in {} table.'.format(target_datatype_diff, select_target) + '\n'
    else:
         str_email = str_email + 'Both the tables have identical/zero data types.' + '\n'


    # df_log = df_log.append({'summary': ''}, ignore_index=True)
    str_email = str_email + '\n'

    str_email = str_email + 'Schema checks:' + '\n'
    # Null
    if (source_null_diff_len > 0) | (target_null_diff_len >  0):
        str_email = str_email + 'Discrepancy found in null types -' + '\n'
        if source_null_diff_len > 0:
            str_email = str_email + '{} null type differs in {} table.'.format(source_null_diff, select_source) + '\n'

        if target_null_diff_len > 0:
            str_email = str_email + '{} null type differs in {} table.'.format(target_null_diff, select_target) + '\n'
    else:
        str_email = str_email + 'Both the tables have identical/zero null types.' + '\n'


    # Primary key
    if (source_pk_diff_len > 0) | (target_pk_diff_len >  0):
        str_email = str_email + 'Discrepancy found in primary keys -' + '\n'

        if source_pk_diff_len > 0:
            str_email = str_email + '{} primary keys differs in {} table.'.format(source_pk_diff, select_source) + '\n'

        if target_pk_diff_len > 0:
           str_email = str_email + '{} primary keys differs in {} table.'.format(target_pk_diff, select_target) + '\n'
    
    else:
        str_email = str_email + 'Both the tables have identical/zero primary keys.' + '\n'

    # Foreign key
    if (source_fk_diff_len > 0) | (target_fk_diff_len >  0):
        str_email = str_email + 'Discrepancy found in foreign keys -' + '\n'

        if source_fk_diff_len > 0:
            str_email = str_email + '{} foreign keys differs in {} table.'.format(source_fk_diff, select_source) + '\n'

        if target_fk_diff_len > 0:
            str_email = str_email + '{} foreign keys differs in {} table.'.format(target_fk_diff, select_target) + '\n'

    else:
        str_email = str_email + 'Both the tables have identical/zero foreign keys.' + '\n'

    # Index key
    if (source_idx_diff_len > 0) | (target_idx_diff_len >  0):
        str_email = str_email + 'Discrepancy found in index keys -' + '\n'
        if source_idx_diff_len > 0:
            str_email = str_email + '{} index keys differs in {} table.'.format(source_idx_diff, select_source) + '\n'

        if target_idx_diff_len > 0:
            str_email = str_email + '{} index keys differs in {} table.'.format(target_idx_diff, select_target) + '\n'

    else:
        str_email = str_email + 'Both the tables have identical/zero index keys.' + '\n'

    # Triggers
    if (source_trigger_diff_len > 0) | (target_trigger_diff_len >  0):
        str_email = str_email + 'Discrepancy found in trigger keys -' + '\n'
        if source_trigger_diff_len > 0:
            str_email = str_email + '{} triggers differs in {} table.'.format(source_trigger_diff, select_source) + '\n'

        if target_trigger_diff_len > 0:
            str_email = str_email + '{} triggers differs in {} table.'.format(target_trigger_diff, select_target) + '\n'

    else:
        str_email = str_email + 'Both the tables have identical/zero triggers.' + '\n'

    # Views
    if (source_views_diff_len > 0) | (target_views_diff_len >  0):
        str_email = str_email + 'Discrepancy found in views referenced -' + '\n'
        if source_views_diff_len > 0:
            str_email = str_email + '{} views referenced in {} table.'.format(source_views_diff, select_source) + '\n'

        if target_views_diff_len > 0:
            str_email = str_email + '{} views referenced in {} table.'.format(target_views_diff, select_target) + '\n'

    else:
        str_email = str_email + 'Both the tables have identical/zero views referenced.' + '\n'

    return str_email


def insert_app_data(source_row_count, target_row_count, source_column_count, target_column_count, 
    source_diff_len, target_diff_len, 
    source_datatype_diff_len, target_datatype_diff_len, source_null_diff_len, target_null_diff_len,  
    source_pk_diff_len, target_pk_diff_len, source_fk_diff_len, target_fk_diff_len, source_idx_diff_len, 
    target_idx_diff_len, source_trigger_diff_len, target_trigger_diff_len, source_views_diff_len, 
    target_views_diff_len):

    if source_row_count != target_row_count:
        rows_count = 0
    else:
        rows_count = 1

    if source_column_count != target_column_count:
        col_count = 0
    else:
        col_count = 1

    if (source_diff_len > 0) | (target_diff_len >  0):
        col_name = 0
    else:
        col_name = 1

    if (source_datatype_diff_len > 0) | (target_datatype_diff_len >  0):
        data_type = 0
    else:
        data_type = 1

    # Null
    if (source_null_diff_len > 0) | (target_null_diff_len >  0):
        null_check = 0
    else:
        null_check = 1

    # Primary key
    if (source_pk_diff_len > 0) | (target_pk_diff_len >  0):
        pk_check = 0
    else:
        pk_check = 1

    # Foreign key
    if (source_fk_diff_len > 0) | (target_fk_diff_len >  0):
        fk_check = 0
    else:
        fk_check = 1

    # Index key
    if (source_idx_diff_len > 0) | (target_idx_diff_len >  0):
        idx_check = 0
    else:
        idx_check = 1

    # Triggers
    if (source_trigger_diff_len > 0) | (target_trigger_diff_len >  0):
        trigger_check = 0
    else:
        trigger_check = 1

    # Views
    if (source_views_diff_len > 0) | (target_views_diff_len >  0):
        views_check = 0
    else:
        views_check = 1

    return rows_count, col_count, col_name, data_type, null_check, pk_check, fk_check, idx_check, trigger_check, views_check