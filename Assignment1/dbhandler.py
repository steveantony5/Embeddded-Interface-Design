#!/usr/bin/python3

'''**
 * @\file	dbhandler.py
 * @\author	Sorabh Gandhi
 * @\brief	This file contains the API to perform operations in MYSQL DB 
 * @\date	09/20/2019
 *
 * @\Reference: https://pimylifeup.com/raspberry-pi-mysql/
 *
 *'''

import MySQLdb 
import time

def create_connection():
    """ create a database connection to the MYSQL database
    """
    conn = None
    try:
        conn = MySQLdb.connect("localhost", "gandhi", "sorabh", "sensordb")
        return conn
    except Error as e:
        print(e)
 
    return conn
 
 
def create_table(conn):
    """ create a table in the MYSQL database
    :param conn: Connection object
    """
    try:
        c = conn.cursor()
        
        c.execute("CREATE TABLE IF NOT EXISTS sensordata(id int NOT NULL AUTO_INCREMENT, temperature float, humidity float, ttime INTEGER, PRIMARY KEY (id))")
    except Error as e:
        print(e)
 
 
def insert_data(conn, data):
    """Inserts new record in my sensordata table
    :param conn: Connection object
    :param data: temperature, humidity and timestamp data to be inserted
    """
    sql = """INSERT INTO sensordata(temperature, humidity, ttime)
            VALUES (%s, %s, %s)"""
            
    cur = conn.cursor()
    cur.execute(sql, data)
    
def read_temperature(conn):
    """ Reads last 10 temperature record from sensordata table
    :param conn: Connection object
    """
    cur = conn.cursor()
    stmt = "SHOW TABLES LIKE 'sensordata'"
    cur.execute(stmt)
    result = cur.fetchone()
    if result:
        cur.execute("select temperature,ttime from sensordata order by id desc limit 10")
        output = cur.fetchall()
    
        return output
    else:
        return ()
    
def read_humidity(conn):
    """ Reads last 10 humidity record from sensordata table
    :param conn: Connection object
    """
    cur = conn.cursor()
    stmt = "SHOW TABLES LIKE 'sensordata'"
    cur.execute(stmt)
    result = cur.fetchone()
    if result:
        cur.execute("select humidity,ttime from sensordata order by id desc limit 10")
        output = cur.fetchall()
    
        return output
    else:
        return ()

