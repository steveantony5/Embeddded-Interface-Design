#!/usr/bin/python3

import MySQLdb 
import time

def create_connection():
    """ create a database connection to the MYSQL database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = MySQLdb.connect("localhost", "gandhi", "sorabh", "sensordb")
        return conn
    except Error as e:
        print(e)
 
    return conn
 
 
def create_table(conn):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute("DROP TABLE sensordata")
        c.execute("CREATE TABLE IF NOT EXISTS sensordata(temperature float, humidity float, ttime INTEGER)")
    except Error as e:
        print(e)
 
 
def insert_data(conn, data):
    """Create a new project into the projects table
    :param conn:
    :param project:
    :return: project id
    """
    sql = """INSERT INTO sensordata(temperature, humidity, ttime)
            VALUES (%s, %s, %s)"""
            
    cur = conn.cursor()
    cur.execute(sql, data)
    
def read_temperature(conn):
    cur = conn.cursor()
    cur.execute("select temperature,ttime from sensordata")
    output = cur.fetchall()
    
    return output
    
def read_humidity(conn):
    cur = conn.cursor()
    cur.execute("select humidity,ttime from sensordata")
    output = cur.fetchall()
    
    return output

