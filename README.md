# Catoptric Server

## Description
The project runs a REST Server and receives HTTP requests to perform movements on a mirror. The server is written in Micronaut, and it calls Python and adafruit's motorkit library to control the motor on raspberry pi's in order to move the mirrors. The proejct is directed at an after school activities for middle school, but it can be adapted for other purposes.

The project is consisted of two parts, the Python motor control scripts, and the micronaut server. The Python motor control scripts can be found at the root level of the project. The Micronaut server can be found in the directory  /CaptoptricServer.

## Table of Contents (Optional)

If your README is long, add a table of contents to make it easy for users to find what they need.

- [Installation](#installation)
- [Usage](#usage)
- [Credits](#credits)

## Installation

What are the steps required to install your project? Provide a step-by-step description of how to get the development environment running.
Enable I2C in the interface options on raspberry pi

#INSTALL ADAFRUIT MOTORKIT
sudo pip3 install adafruit-circuitpython-motorkit

## Usage

Provide instructions and examples for use. Include screenshots as needed.

To add a screenshot, create an `assets/images` folder in your repository and upload your screenshot to it. Then, using the relative filepath, add it to your README using the following syntax:

    ```md
    ![alt text](assets/images/screenshot.png)
    ```

## Credits
Mentor: Professor Chamberlain
Collaborator: Samantha Kodali
Referenced Code from: Scott Siri
