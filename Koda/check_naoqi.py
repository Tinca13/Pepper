import sys
from naoqi import ALProxy

# --- CONFIGURATION ---
PEPPER_IP = "192.168.0.131"  # Pepper's IP
PC_IP = "192.168.0.102"      # Your PC's IP (must be on the same Wi-Fi)
PORT = 9559

tablet = ALProxy("ALTabletService", PEPPER_IP, PORT)
tablet.enableWifi() # Ensure tablet wifi is on

        # 2. Define the URL 
        # We use port 8000 because that's where we will run our server
url = "http://{}:8000/novtablet.html".format(PC_IP)
        
print("Telling Pepper to open: " + url)
        
        # 3. Show the webview
tablet.showWebview(url)
        
print("Success! Check Pepper's tablet.")