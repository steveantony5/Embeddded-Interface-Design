#!/usr/bin/python
# Copyright (c) 2014 Adafruit Industries
# Author: Tony DiCola

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import sys
import time

import Adafruit_DHT
import dbhandler


sensor = 22
pin = 22

def get_sensor_data():
    h_data, t_data = Adafruit_DHT.read_retry(sensor, pin)
    t_data = t_data * 9/5.0 + 32
    current_time = int(time.time())
    data = [t_data, h_data, current_time]
    return data

def main():
    # create a database connection
    db = dbhandler.create_connection()

    #project_table = CREATE TABLE IF NOT EXISTS sensordata(temperature float, humidity float, ttime TIME)

    # Create table
    dbhandler.create_table(db)

    i = 0
    while i < 30:
    # Try to grab a sensor reading.  Use the read_retry method which will retry up
    # to 15 times to get a sensor reading (waiting 2 seconds between each retry).
        humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
        
        temperature = temperature * 9/5.0 + 32
        my_time = int(time.time())
        data = (temperature, humidity, my_time)
        dbhandler.insert_data(db, data)
        db.commit()

    # Note that sometimes you won't get a reading and
    # the results will be null (because Linux can't
    # guarantee the timing of calls to read the sensor).
    # If this happens try again!
        if humidity is not None and temperature is not None:
            print('Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(temperature, humidity))
        else:
            print('Failed to get reading. Try again!')
            sys.exit(1)

        i = i + 1
        time.sleep(15)
        

    db.close()

if __name__ == '__main__':
    main()

