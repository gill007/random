METHODS AND DESIGN APPROACH

A low cost and efficient smart home system is presented in our design. This system has two main modules: the hardware interface module and the software communication module. At the heart of this system is the Arduino UNO  microcontroller which is also capable of functioning as a micro web server and the interface for all the hardware modules. All communication and controls in this system pass through the microcontroller. It  offers switching functionalities to control lighting, fans and other home appliances connected to the relay system. 

SOFTWARE REQUIREMENTS
•	Arduino IDE (version 1.5 or above)
•	Web Browser (Google Chrome/Firefox)


HARDWARE REQUIREMENTS
•	Arduino Uno
•	ESP8266 Module
•	Relay
•	Breadboard
•	Jumper Cables
•	Lights
 
 
 LIMITATIONS

1.	Low memory of arduino and Esp8266 doesnot allow to connect more devices:Due to the low memory of arduino UNO and Esp8266 , they doesn’t allow more devices to connect which is quite a loss for it. 

2.	Sometimes feedback may be delayed : Using Esp8266 with arduino UNO, it may delay the feedback required to run  the project. 


3.	Esp8266 interferes with arduino sketch uploading: The moment a sketch is uploaded in the arduino Esp8366 interferes with it and creates a lot  fuzz and sometimes crashes the program. 

4.	System crashes due to any damage in the interconnection:  If there is any damage due to rupturing of cables or the fibers the entire system gets crashed. This will not be the case of radio signals or the other signals. Here there will be a problem of signal receiving. The wiring of the system results in crash in most of the systems.

5.	Human errors: If the human does not handle the kit safely or if he/she does not use the correct keys to perform the operations, human errors may occur. Human errors also lead to destructions of the machine. Then there will be a huge system crash.

