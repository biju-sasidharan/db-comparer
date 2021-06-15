import pandas as pd
import sqlite3

import db_config as dbc

source_db = dbc.SQLITE_SOURCE_DATABASE
target_db = dbc.SQLITE_TARGET_DATABASE

def source_connection():
    source_conn_string = source_db
    # print(source_conn_string)
    return source_conn_string

def target_connection():
    target_conn_string = target_db

    return target_conn_string

def get_tables(connection_string='SOURCE'):
    if connection_string == 'SOURCE':
        connection_string = source_connection()
    else:
        connection_string = target_connection()

    conn = sqlite3.connect(connection_string)
    sql = "SELECT name as table_name FROM sqlite_master \
        WHERE type = 'table' AND name <> 'app_data' ORDER BY name"
    df = pd.read_sql(sql, conn)
    conn.close()
    return df['table_name'].values.tolist()

def get_data(tablename, connection_string='SOURCE'):
    if connection_string == 'SOURCE':
        connection_string = source_connection()
    else:
        connection_string = target_connection()

    conn = sqlite3.connect(connection_string)
    sql = "SELECT * FROM " + tablename 
    df = pd.read_sql(sql, conn)
    conn.close()
    return df

def get_schema(tablename, connection_string='SOURCE'):
    if connection_string == 'SOURCE':
        connection_string = source_connection()
    else:
        connection_string = target_connection()

    conn = sqlite3.connect(connection_string)
    sql = """SELECT name as column_name, *
        FROM pragma_table_info('""" + tablename + """') """

    df = pd.read_sql(sql, conn)
    df['column_info'] = df['name'] + ': ' + df['type']
    df['column_is_nullable'] = df['name'] + ' - ' + df['notnull'].astype(str)
    conn.close()
    return df

def get_views(tablename, connection_string='SOURCE'):
    if connection_string == 'SOURCE':
        connection_string = source_connection()
    else:
        connection_string = target_connection()

    conn = sqlite3.connect(connection_string)
    sql = "SELECT name AS view_name FROM sqlite_master WHERE type = 'view' AND tbl_name = '" + tablename + "'"

    df = pd.read_sql(sql, conn)
    conn.close()
    return df

def get_primary_keys(tablename, connection_string='SOURCE'):
    if connection_string == 'SOURCE':
        connection_string = source_connection()
    else:
        connection_string = target_connection()

    conn = sqlite3.connect(connection_string)
    sql = "select name AS key_column from pragma_table_info('" + tablename + "') WHERE pk = 1"

    df = pd.read_sql(sql, conn)
    conn.close()
    return df


def get_foreign_keys(tablename, connection_string='SOURCE'):
    if connection_string == 'SOURCE':
        connection_string = source_connection()
    else:
        connection_string = target_connection()

    conn = sqlite3.connect(connection_string)

    sql = "SELECT * FROM pragma_foreign_key_list('" + tablename + "')"

    df = pd.read_sql(sql, conn)
    df['fkey'] = df['from'] + ' -> ' + df['table'] + '.' + df['to']
    conn.close()
    return df


def get_indexes(tablename, connection_string='SOURCE'):
    if connection_string == 'SOURCE':
        connection_string = source_connection()
    else:
        connection_string = target_connection()

    conn = sqlite3.connect(connection_string)

    sql = """SELECT tbl_name AS tablename, name AS indexname
            FROM sqlite_master
            WHERE type='index' AND tbl_name = '""" + tablename + """'
            ORDER BY name
    """
    df = pd.read_sql(sql, conn)
    conn.close()
    return df

def get_triggers(tablename, connection_string='SOURCE'):
    if connection_string == 'SOURCE':
        connection_string = source_connection()
    else:
        connection_string = target_connection()

    conn = sqlite3.connect(connection_string)

    sql = "SELECT name AS trigger_name FROM sqlite_master WHERE type = 'trigger' AND tbl_name = '" + tablename + "'"

    df = pd.read_sql(sql, conn)
    conn.close()
    return df

def get_app_data():
    conn = sqlite3.connect(source_connection())
    print(source_connection())
    sql = """SELECT created_on, source_table, target_table, rows_count, col_count, col_name, data_type, null_check, 
        pk_check, fk_check, idx_check, trigger_check, views_check 
        FROM app_data ORDER BY created_on DESC
    """
    df = pd.read_sql(sql, conn)
    conn.close()
    return df

def insert_app_data(source_table, target_table, rows_count, col_count, col_name, data_type, null_check, 
        pk_check, fk_check, idx_check, trigger_check, views_check):
    conn = sqlite3.connect(source_connection())
    cur = conn.cursor()
    sql = """INSERT INTO app_data(source_table, target_table, rows_count, col_count, col_name, data_type, null_check, pk_check, 
    fk_check, idx_check, trigger_check, views_check) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"""
    # print(sql)
    cur.execute(sql, (source_table, target_table, rows_count, col_count, col_name, data_type, null_check, pk_check, fk_check, idx_check, trigger_check, views_check))
    conn.commit()
    conn.close()