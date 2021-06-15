import pandas as pd
import psycopg2

import db_config as dbc

db_host = dbc.DB_HOST
db_user = dbc.DB_USER
db_password = dbc.DB_PASSWORD
db_port = dbc.DB_PORT
source_db = dbc.DB_SOURCE_DATABASE
target_db = dbc.DB_TARGET_DATABASE

def source_connection():
    source_conn_string = "host="+ db_host +" port="+ db_port +" dbname="+ source_db +" user=" + db_user + " password="+ db_password

    return source_conn_string

def target_connection():
    target_conn_string = "host="+ db_host +" port="+ db_port +" dbname="+ target_db +" user=" + db_user + " password="+ db_password

    return target_conn_string


def get_tables(connection_string='SOURCE'):
    if connection_string == 'SOURCE':
        connection_string = source_connection()
    else:
        connection_string = target_connection()

    conn = psycopg2.connect(connection_string)
    sql = "SELECT table_name FROM INFORMATION_SCHEMA.tables \
        WHERE table_type = 'BASE TABLE' AND table_schema = 'public' \
        AND table_name <> 'app_data' \
        AND table_catalog='"  + source_db + "' ORDER BY table_name"
    df = pd.read_sql(sql, conn)
    conn.close()
    return df['table_name'].values.tolist()

def get_data(tablename, connection_string='SOURCE'):
    if connection_string == 'SOURCE':
        connection_string = source_connection()
    else:
        connection_string = target_connection()

    conn = psycopg2.connect(connection_string)

    sql = "SELECT * FROM " + tablename 
    df = pd.read_sql(sql, conn)
    conn.close()
    return df

def get_schema(tablename, connection_string='SOURCE'):
    if connection_string == 'SOURCE':
        connection_string = source_connection()
    else:
        connection_string = target_connection()

    conn = psycopg2.connect(connection_string)
    sql = """SELECT table_name, column_name, 
        concat(column_name, ': ', data_type, '(', character_maximum_length, numeric_precision, ')') as column_info, 
        concat(column_name, ' - ', is_nullable) as column_is_nullable
        FROM information_schema.columns
        WHERE table_schema='public'
        AND position('_' in table_name) <> 1
        AND table_name = '""" + tablename  + """'
        ORDER BY 1, 2""" 
    # print(sql)
    df = pd.read_sql(sql, conn)
    conn.close()
    return df

def get_views(tablename, connection_string='SOURCE'):
    if connection_string == 'SOURCE':
        connection_string = source_connection()
    else:
        connection_string = target_connection()

    conn = psycopg2.connect(connection_string)
    sql = """select u.view_schema as schema_name,
            u.view_name
        from information_schema.view_table_usage u
        join information_schema.views v 
            on u.view_schema = v.table_schema
            and u.view_name = v.table_name
        where u.table_schema not in ('information_schema', 'pg_catalog')
        and u.table_name = '""" + tablename  + """'
        order by u.view_schema,
         u.view_name""" 
    # print(sql)
    df = pd.read_sql(sql, conn)
    conn.close()
    return df

def get_primary_keys(tablename, connection_string='SOURCE'):
    if connection_string == 'SOURCE':
        connection_string = source_connection()
    else:
        connection_string = target_connection()

    conn = psycopg2.connect(connection_string)
    sql = """select kcu.table_schema,
            kcu.table_name,
            kcu.ordinal_position as position,
            kcu.column_name as key_column
        from information_schema.table_constraints tco
        join information_schema.key_column_usage kcu 
            on kcu.constraint_name = tco.constraint_name
            and kcu.constraint_schema = tco.constraint_schema
            and kcu.constraint_name = tco.constraint_name
        where tco.constraint_type = 'PRIMARY KEY'
        and kcu.table_name = '""" + tablename  + """'
        order by kcu.table_schema,
         kcu.table_name,
         position""" 
    # print(sql)
    df = pd.read_sql(sql, conn)
    conn.close()
    return df


def get_foreign_keys(tablename, connection_string='SOURCE'):
    if connection_string == 'SOURCE':
        connection_string = source_connection()
    else:
        connection_string = target_connection()

    conn = psycopg2.connect(connection_string)
    sql = """SELECT tc.constraint_type,
            concat(kcu.column_name, ' -> ', ccu.table_name, '.', ccu.column_name) as fkey
        FROM 
            information_schema.table_constraints AS tc 
            JOIN information_schema.key_column_usage AS kcu
            ON tc.constraint_name = kcu.constraint_name
            AND tc.table_schema = kcu.table_schema
            JOIN information_schema.constraint_column_usage AS ccu
            ON ccu.constraint_name = tc.constraint_name
            AND ccu.table_schema = tc.table_schema
        WHERE tc.constraint_type = 'FOREIGN KEY'
        and tc.table_name = '""" + tablename  + """'
        """ 
    # print(sql)
    df = pd.read_sql(sql, conn)
    conn.close()
    return df


def get_indexes(tablename, connection_string='SOURCE'):
    if connection_string == 'SOURCE':
        connection_string = source_connection()
    else:
        connection_string = target_connection()

    conn = psycopg2.connect(connection_string)
    sql = """SELECT
            tablename, indexname
        FROM pg_indexes
        WHERE schemaname = 'public'
        and tablename = '""" + tablename  + """'
        ORDER BY indexname
        """ 
    # print(sql)
    df = pd.read_sql(sql, conn)
    conn.close()
    return df

def get_triggers(tablename, connection_string='SOURCE'):
    if connection_string == 'SOURCE':
        connection_string = source_connection()
    else:
        connection_string = target_connection()

    conn = psycopg2.connect(connection_string)
    sql = """SELECT event_object_table, trigger_name
        FROM information_schema.triggers
        WHERE trigger_schema NOT IN ('pg_catalog', 'information_schema')
        and event_object_table = '""" + tablename  + """'
        ORDER BY trigger_name
        """ 
    # print(sql)
    df = pd.read_sql(sql, conn)
    conn.close()
    return df

def get_app_data():
    conn = psycopg2.connect(source_connection())
    sql = """SELECT created_on, source_table, target_table, rows_count, col_count, col_name, data_type, null_check, 
        pk_check, fk_check, idx_check, trigger_check, views_check 
        FROM app_data ORDER BY created_on DESC
    """
    df = pd.read_sql(sql, conn)
    conn.close()
    return df

def insert_app_data(source_table, target_table, rows_count, col_count, col_name, data_type, null_check, 
        pk_check, fk_check, idx_check, trigger_check, views_check):
    conn = psycopg2.connect(source_connection())
    cur = conn.cursor()
    sql = """INSERT INTO app_data(source_table, target_table, rows_count, col_count, col_name, data_type, null_check, pk_check, 
    fk_check, idx_check, trigger_check, views_check) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
    print(sql)
    cur.execute(sql, (source_table, target_table, rows_count, col_count, col_name, data_type, null_check, pk_check, fk_check, idx_check, trigger_check, views_check))
    conn.commit()
    conn.close()