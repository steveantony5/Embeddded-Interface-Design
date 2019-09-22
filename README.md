# EID Project 1

### Introduction
This is the first project in Embedded Interface design course offered at CU Boulder. The project includes a temperature polling, storing the data in MySQL database and displaying the temperature and humidity data in PyQT GUI.

### Project Developers
  - Sorabh Gandhi
  - Steve Antony Xavier Kenndy

### Project Work
Steve Antony Xavier Kenndy - QT Design and PyQT graph
Sorabh Gandhi - Temperature polling, My SQL Database

### Installation
Install all the dependencies to run this project. Follow the installation instructions given below,

```sh
$ sudo apt-get install update
$ sudo apt-get install upgrade
$ sudo apt-get install python3-pip
$ sudo apt-get install qt5-default pyqt5-dev pyqt5-dev-tools
$ sudo apt install mariadb-server
$ sudo apt-get install python-mysqldb
$ cd Adafruit_Python_DHT/
$ sudo python3 setup.py install
$ sudo pip3 install pyqtgraph
```

After installing the Adafruit temperature sensor library, create a username, password and 
database in mardia DB by follwing the below steps,
```sh
$ sudo mysql_secure_installation
```
For secure installation, type 'Y' to all the prompts.
```sh
$ sudo mysql -u root -p
>> CREATE DATABASE sensordb;
>> CREATE USER 'gandhi'@'localhost' IDENTIFIED BY 'sorabh';
>> GRANT ALL PRIVILEGES ON sensordb.* TO 'gandhi'@'localhost';
>> FLUSH PRIVILEGES;
```

#### Note
1.) To plot graph, we have used PyQT graph with the approval of the instructor
2.) We have also completed the extra credit part in the PyQT GUI.


