import pygame
import time
from pygame.locals import *
import sys
from math import *
import os
from os import listdir
from os.path import isfile, join

def main():
    #size = (1024,600)
    size = (1024,768)
    pygame.display.set_mode(size,FULLSCREEN)
    main_surface = pygame.display.get_surface()

    folders = ["webcam", "rain", "strikes"]
    interval = 500.0 / 1000.0

    s = 0
    while True:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()

	loggingDate = time.strftime('%Y-%m-%d %H:%M:%S')
	for folder in folders:
	    files = sorted(listdir(folder))
	    if len(files) < 3:
		slideshowInterval = 2
	    else:
		slideshowInterval = interval
	
	    for name in files:
		file = join(folder, name)
		if not isfile(file):
		    continue

		try:
                    picture = pygame.image.load(file)
                    picture = pygame.transform.scale(picture,size)

                    main_surface.blit(picture, (0, 0))
                    pygame.display.update()

                    time.sleep(slideshowInterval)
		except Exception as e:
            	    print (loggingDate + " Error: ", e)
            	    time.sleep(10)
		    continue
	    time.sleep(1)

if __name__ == "__main__":
    main()
