import sys
sys.path.append(r"C:\Users\uil\Desktop\Pepper\pynaoqi-python2.7-2.5.5.5-win32-vs2013\pynaoqi-python2.7-2.5.5.5-win32-vs2013\lib")

from naoqi import ALProxy

PEPPER_IP = "192.168.0.131"   # popravi z dejanskim IP
PORT = 9559

# govorjenje
tts = ALProxy("ALTextToSpeech", PEPPER_IP, PORT)
tts.say("Hej Tina, zdaj govorim iz Visual Studio Code!")

#Zeženi server 
#Set-Location 'C:\Users\uil\Desktop\Pepper\Koda' & 'C:\Python27\python.exe' -m SimpleHTTPServer 8000

tablet = ALProxy("ALTabletService", PEPPER_IP, PORT) 
tablet.showWebview("http://192.168.0.102:8000/tablet.html")  # Use your PC's IP and file name

# link browser http://localhost:8000/tablet.html