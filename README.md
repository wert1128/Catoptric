# Catoptric Server

## Description
The project runs a REST Server and receives HTTP requests to perform movements on a mirror. The server is written in Micronaut, and it calls Python and adafruit's motorkit library to control the motor on raspberry pi's in order to move the mirrors. The proejct is directed at an after school activities for middle school, but it can be adapted for other purposes.

The project is consisted of two parts, the Python motor control scripts, and the micronaut server. The Python motor control scripts can be found at the root level of the project. The Micronaut server can be found in the directory  /CaptoptricServer.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Credits](#credits)
- [CodeDirectory](#codeDirectory)

## Installation
1. Follow STEP 1 in the following link to enable I2C: 
https://www.raspberrypi-spy.co.uk/2014/11/enabling-the-i2c-interface-on-the-raspberry-pi/
2. Install Adafruit Motorkit on Raspberry Pi
    ```md
    sudo pip3 install adafruit-circuitpython-motorkit
    ```
3. Install Java on Raspberry Pi
    ```md
    sudo apt update
    sudo apt install default-jdk
    ```

## Usage
It should be used with appropriate hardware set up, for detail: see Professor Chamberlain
To Start the server:
    ```md
    cd CatoptricServer
    ./gradlew run
    ```
    
## CodeDirectory
The following files contain the code you should be concerned with:
1. Python Script that control the motor movement: 
    ```md
    CatoptricController.py
    ```
2. Micronaut server controller that handles http request and calls Python script:
    ```md
    /CatoptricServer/src/main/java/codes/recursive/controller/DefaultController.java
    ```
    
## Credits
- Mentor: Professor Chamberlain
- Collaborator: Samantha Kodali
- Referenced Code from: Scott Siri
