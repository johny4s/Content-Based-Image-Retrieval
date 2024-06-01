Demo:
![Screenshot (216)](https://github.com/johny4s/Content-Based-Image-Retrieval/assets/102698461/129d3c7b-f8e6-4869-abdd-0545a2e8e51d)

Workflow:
![image](https://github.com/johny4s/Content-Based-Image-Retrieval/assets/102698461/359928ee-0d6c-4dc3-9817-ebc325c7c91d)

Project Description:
The above coding is all only the software part.I've built a Real time image Search Engine Which takes Real time images as a query through Raspberrypi.
When image is captured by UsbCam,The Raspberrypi directly Sends and saves the image in it's Operating System Folder wirelessly.This Folder is shared with Windows Operating System's Folder Using Samba Folder Share.Windows OS is faster to run than the Raspberrypi OS.When Server is Running,if we Select that newly Captured Image from shared Folder as a query,we will get the resultant Similar Images.

Running:
Step-1: Run the offline.py file to get feature Database from image database.
step-2:Run the server.py file
Step-3:Capture image using pushbutton on usbcam
Step-4:Browse the newly captured image from the shared folder in the Server Website from step-2
Step-5:Click On Submit.


