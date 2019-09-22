from PyQt5 import QtWidgets, QtGui,QtCore
from mydesign import Ui_Dialog #importing the generated python class from.ui
from PyQt5.QtWidgets import QTableWidgetItem

import pyqtgraph as pg
import numpy as np
import  random
import dbhandler
import sys
import time

import Adafruit_DHT

'''Sensor pins where the temperature sensor is connected'''
sensor = 22
pin = 22

def get_sensor_data():
    '''get_sensor_data : gets the immediate reading from sensor'''
    
    try:
        h_data, t_data = Adafruit_DHT.read_retry(sensor, pin,retries = 3, delay_seconds=.1)
        print(h_data)
        print(t_data)
        t_data = t_data * 9/5.0 + 32
        current_time = int(time.time())
        data = [t_data, h_data, current_time]
        return data
    
    except:
        print("Error on sensor")
        return [-1000, -1000, 0]

def sensor_periodic():
    '''sensor_periodic : the 15 sec periodic task which reads sensor data'''
    # create a database connection
    db_dump = dbhandler.create_connection()

    # Create table
    dbhandler.create_table(db_dump)

    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin,retries = 3, delay_seconds=.1)
    
    if humidity is not None and temperature is not None:
        print('Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(temperature, humidity))
            
        temperature = temperature * 9/5.0 + 32
        my_time = int(time.time())
        data = (temperature, humidity, my_time)
        dbhandler.insert_data(db_dump, data)
        db_dump.commit()
    else:
        print('Failed to get reading. Try again!')
            
    
            
    db_dump.close()


#inheriting mywindow class from the class QDialog
class mywindow(QtWidgets.QDialog):
    def __init__(self):
        '''Constructor for the class'''
        super(mywindow, self).__init__() #initiating the parent class
        self.ui = Ui_Dialog()
        self.ui.setupUi(self) #calling the function generated in the .ui

        self._update_timer = QtCore.QTimer()
        self._update_timer.timeout.connect(self.periodic_task)
        self._update_timer.start(15000) # milliseconds

        self.ui.lineedit_maxtemp.setText("30");
        self.ui.lineedit_maxhum.setText("18");



        self.ui.pushButton_refresh.clicked.connect(self.refresh)

        self.ui.pushButton_tempgraph.clicked.connect(self.show_temp_graph)

        self.ui.pushButton_humgraph.clicked.connect(self.show_hum_graph)
        
        db_dump = dbhandler.create_connection()
        c = db_dump.cursor()
        c.execute("DROP TABLE IF EXISTS sensordb.sensordata")
        db_dump.close()






    def refresh(self):
        '''refresh : function which updates the status line with immediate reading when refresh button is pressed'''
        print("Display update")
        read_data_list = get_sensor_data()
        print(read_data_list)

        temp = read_data_list[0]
        humidity = read_data_list[1]
        timestamp = read_data_list[2]

        if timestamp!=0:
            if self.ui.checkBox_temp.isChecked():
                print("Celcius display")
                temp = (temp -  32) * 5/9

            self.ui.lineEdit_ts.setText(str(timestamp))
            self.ui.lcd_temp.display(temp)
            self.ui.lcd_temp.repaint()
            self.ui.lcd_humidity.display(humidity)
            self.ui.lcd_humidity.repaint()
            
        else:
            temp = "ERROR"
            humidity = "ERROR"
            self.ui.lineEdit_ts.setText(str(timestamp))
            self.ui.lcd_temp.display(temp)
            self.ui.lcd_temp.repaint()
            self.ui.lcd_humidity.display(humidity)
            self.ui.lcd_humidity.repaint()

    def show_temp_graph(self):
        '''show_temp_graph : function to display graph of last 10 temperature reading'''
        db = dbhandler.create_connection()
        print("Display graph for temperature")
        database_temp = dbhandler.read_temperature(db)
        
        db.close()
        print(database_temp)

        if database_temp!=():
            database_temp = [list(row) for row in database_temp]
            print(database_temp)
            temp, time = map(list, zip(*database_temp))
            if self.ui.checkBox_temp.isChecked():
                print("Celcius display")
                new_temp = [((t -  32) * 5/9) for t in temp]
                temp = new_temp.copy()
                print(temp)


            plotWidget = pg.plot(title="Temperature history")
            plotWidget.plot(time, temp)


    def show_hum_graph(self):
        '''show_hum_graph : function to display graph of last 10 humidity reading'''
        db = dbhandler.create_connection()
        print("Display graph for humidity")
        database_humidity = dbhandler.read_humidity(db)
        
        
        db.close()
        print(database_humidity)

        if database_humidity!=():
            
            database_humidity = [list(row) for row in database_humidity]
            print(database_humidity)
            hum, time = map(list, zip(*database_humidity))
            plotWidget = pg.plot(title="Humidity history")
            plotWidget.plot(time, hum)


    def periodic_task(self):
        '''periodic_task : function which checks if the values have exceeded the limits every 15 secs'''
        sensor_periodic()

        read_data_list = get_sensor_data()
        temp = read_data_list[0]
        humidity = read_data_list[1]
        timestamp = read_data_list[2]

        if timestamp!=0:
            if self.ui.checkBox_temp.isChecked():
                print("Celcius display")
                temp = (temp -  32) * 5/9

            self.ui.lineEdit_ts.setText(str(timestamp))
            self.ui.lcd_temp.display(temp)
            self.ui.lcd_temp.repaint()
            self.ui.lcd_humidity.display(humidity)
            self.ui.lcd_humidity.repaint()
            
            print("Limit check")
            try:
                    temp_limit = float(self.ui.lineedit_maxtemp.text())
                    print(temp_limit)

            except:
                    print("temp limit not specified")
                    temp_limit = 100000

            try:
                    hum_limit = float(self.ui.lineedit_maxhum.text())
                    print(hum_limit)

            except:
                    print("humidity limit not specified")
                    hum_limit = 100000




            if temp>temp_limit and humidity > hum_limit:
                    print("temp and humidity over limit")
                    self.ui.alarm.setText("Temp and humidity exceeded limit")
            elif temp > temp_limit:
                    print("temp over limit")
                    self.ui.alarm.setText("Temp exceeded limit")
            elif humidity > hum_limit:
                    print("humidity over limit")
                    self.ui.alarm.setText("humidity exceeded limit")
            else:
                    self.ui.alarm.setText(" ")
                
        else:
            temp = "ERROR"
            humidity = "ERROR"
            self.ui.lineEdit_ts.setText(str(timestamp))
            self.ui.lcd_temp.display(temp)
            self.ui.lcd_temp.repaint()
            self.ui.lcd_humidity.display(humidity)
            self.ui.lcd_humidity.repaint()
            self.ui.alarm.setText("Check if the sensor is properly connected")


        


def main():


    app = QtWidgets.QApplication([])
    application = mywindow()
    application.show()
    app.exec() # to execute the application


if __name__ == '__main__':
    main()

