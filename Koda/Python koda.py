# zagon serverja, vtipkaj v terminal: python -m SimpleHTTPServer 8000
# -*- coding: utf-8 -*-
import sys
import time
from naoqi import ALProxy

# --- KONFIGURACIJA ---
PEPPER_IP = "192.168.0.131"  # IP od tvojega Pepperja
PC_IP = "192.168.0.102"      # IP tvojega računalnika (mora biti na istem Wi-Fi)
PORT = 9559

def main():
    try:
        print("Povezujem se z ALTabletService na {}...".format(PEPPER_IP))
        tablet = ALProxy("ALTabletService", PEPPER_IP, PORT)
        
        # 1. Omogočimo Wi-Fi na tablici (za vsak slučaj)
        tablet.enableWifi()

        # 2. Skrijemo trenutni pogled, da "prebudimo" servis
        print("Resetiram pogled na tablici...")
        tablet.hideWebview()
        time.sleep(1)

        # 3. URL s časovnim žigom (?v=...)
        # To prisili tablico, da ignorira predpomnilnik (cache) in naloži stran s PC-ja
        timestamp = int(time.time())
        url = "http://{}:8000/tablet.html?v={}".format(PC_IP, timestamp)
        
        print("Naročam Pepperju, naj odpre: " + url)
        
        # 4. Prikažemo stran
        tablet.showWebview(url)
        print("Uspeh! Poglej na tablico.")
        print("Če še vedno ne vidiš ničesar, preveri, če tvoj terminal s strežnikom beleži 'GET' zahtevo.")

    except Exception as e:
        print("Napaka pri povezavi ali izvajanju: ")
        print(e)

if __name__ == "__main__":
    main()
	