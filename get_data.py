import time
import os
import sys
import urllib
from math import *
from os import listdir
from os.path import isfile, join

def main():
    webcamUrl="http://77.235.177.234/record/current.jpg"
    rainUrl="http://iras.skywarn.de/radardaten/public/aktuell.png"
    strikesUrl="http://images.blitzortung.org/Images/image_b_de.png"

    folders = ["webcam", "rain", "strikes"]
    maxImages = 30
    interval = 30

    i = 0
    while True:
	print("")
	print("")
	
	currentTime = time.time()
        prefix=str(currentTime)[:10] + "_"
	loggingDate=time.strftime('%Y-%m-%d %H:%M:%S')

        opener = urllib.URLopener()
	try: 	    
	    print (loggingDate + " Download webcam image")
            opener.retrieve(webcamUrl, "webcam/" + prefix + "webcam.jpg")
	except Exception as e:
	    print (loggingDate + " Error: ", e)
            time.sleep(10)

	try:
            if i % 5 == 0: 
	    	print (loggingDate + " Download rain image")
	    	opener.retrieve(rainUrl, "rain/" + prefix + "rain.jpg")
	except Exception as e:
	    print (loggingDate + " Error: ", e)
            time.sleep(10)
            
	try:
	    print (loggingDate + " Download strikes image")
            opener.retrieve(strikesUrl, "strikes/" + prefix + "strikes.jpg")
        except Exception as e:
	    print (loggingDate + " Error: ", e)
            time.sleep(10)
	
	print("")
	print("Cleanup...")
	for folder in folders:
	    print("")
	    i = 0
	    
	    files = sorted(listdir(folder))
            for name in reversed(files):
                file = join(folder, name)
                if not isfile(file):
                    continue

		i += 1
		if i <= maxImages:
		    #print("[" + str(i) + "] Keep " + file)
		    continue
		else: 
		    #print("Remove " + file)
		    os.unlink(file)
		
	i += 1
	time.sleep(interval)

if __name__ == "__main__":
    main()
