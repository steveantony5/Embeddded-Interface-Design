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

import sqlite3
from sqlite3 import Error
import time

def create_connection(db_file):
    """ create a database connection to the MYSQL database
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
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
        
        c.execute("CREATE TABLE IF NOT EXISTS magicwand(command VARCHAR(20), label VARCHAR(20))")
    except Error as e:
        print(e)
 
 
def insert_data(conn, data):
    """Inserts new record in my sensordata table
    :param conn: Connection object
    :param data: temperature, humidity and timestamp data to be inserted
    """
    sql = """INSERT INTO magicwand(command, label)
            VALUES (?, ?)"""
            
    cur = conn.cursor()
    cur.execute(sql, data)
    
def read_data(conn):
    """ Reads last 10 temperature record from sensordata table
    :param conn: Connection object
    """
    cur = conn.cursor()
    cur.execute("select * from magicwand")
    output = cur.fetchall()
    for row in output:
        print(row)
    
    return output
    
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
