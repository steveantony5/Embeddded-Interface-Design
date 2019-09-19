from PyQt5 import QtWidgets, QtGui,QtCore
from mydesign import Ui_Dialog #importing the generated python class from.ui
from PyQt5.QtWidgets import QTableWidgetItem

import pyqtgraph as pg
import numpy as np
import  random
import dbhandler
import sensorpoll


#inheriting mywindow class from the class QDialog
class mywindow(QtWidgets.QDialog):
    def __init__(self):
        super(mywindow, self).__init__() #initiating the parent class
        self.ui = Ui_Dialog() 
        self.ui.setupUi(self) #calling the function generated in the .ui

        self._update_timer = QtCore.QTimer()
        self._update_timer.timeout.connect(self.check_limit)
        self._update_timer.start(15000) # milliseconds
        
        self.ui.lineedit_maxtemp.setText("30");
        self.ui.lineedit_maxhum.setText("18");
        
        

        self.ui.pushButton_refresh.clicked.connect(self.refresh) 

        self.ui.pushButton_tempgraph.clicked.connect(self.show_temp_graph) 

        self.ui.pushButton_humgraph.clicked.connect(self.show_hum_graph) 
        
        




    def refresh(self):
        print("Display update")
        read_data_list = sensorpoll.get_sensor_data()
        
        temp = read_data_list[0]
        humidity = read_data_list[1]
        timestamp = read_data_list[2]

        if self.ui.checkBox_temp.isChecked():
            print("Celcius display")
            temp = (temp -  32) * 5/9

        self.ui.lineEdit_ts.setText(str(timestamp))
        self.ui.lcd_temp.display(temp)
        self.ui.lcd_temp.repaint()
        self.ui.lcd_humidity.display(humidity)
        self.ui.lcd_humidity.repaint()

    def show_temp_graph(self):
        db = dbhandler.create_connection()
        print("Display graph for temperature")
        database_temp = dbhandler.read_temperature(db)
        database_temp = [list(row) for row in database_temp]
        print(database_temp)
        db.close()
        
        temp, time = map(list, zip(*database_temp))
        if self.ui.checkBox_temp.isChecked():
            print("Celcius display")
            new_temp = [((t -  32) * 5/9) for t in temp]
            temp = new_temp.copy()
            print(temp)
            
            
        plotWidget = pg.plot(title="Temperature history")
        plotWidget.plot(time, temp)
        
    def show_hum_graph(self):
        db = dbhandler.create_connection()
        print("Display graph for temperature")
        database_humidity = dbhandler.read_humidity(db)
        database_humidity = [list(row) for row in database_humidity]
        print(database_humidity)
        db.close()
        
        hum, time = map(list, zip(*database_humidity))
        plotWidget = pg.plot(title="Humidity history")
        plotWidget.plot(time, hum)
        

    def check_limit(self):
            
        read_data_list = sensorpoll.get_sensor_data()
        temp = read_data_list[0]
        humidity = read_data_list[1]
        timestamp = read_data_list[2]

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

        
        
                




   

  
def main():
    

    app = QtWidgets.QApplication([])
    application = mywindow()
    application.show()
    app.exec() # to execute the application

    
if __name__ == '__main__':
    main()

