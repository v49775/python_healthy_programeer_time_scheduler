from pygame import mixer
import time
 #Initialzing pyamge mixer

 #Loading Music Fil
# mixer.music.load('song2.mp3') #Loading Music File
# mixer.music.load('song2.mp3') #Loading Music File

# mixer.music.play() #Playing Music with Pygame

while(1):
    print("please drink water 200ml")

    mixer.init()
    mixer.music.load('bc.mp3')
    mixer.music.play()
    water = input("enter drink to stop song : ")
    if(water=="drink"):
        mixer.music.stop()
    time.sleep(10)

    print("please do the eye workout 10 times")

    mixer.init()
    mixer.music.load('eye.mp3')
    mixer.music.play()
    eye = input("enter done to stop song : ")
    if (water == "done"):
        mixer.music.stop()
    break
    time.sleep(10)

    # print("please do the physical workout 5 min")
    #
    # mixer.init()
    # mixer.music.load('eye.mp4')
    # mixer.music.play()
    # eye = input("enter done to stop song : ")
    # if (water == "done"):
    #     mixer.music.stop()
    break


    # print("please do the eye workout")
    # eye = input("press enter to stop song")
    # if (eye == "x"):
    #     mixer.music.play()
    #     mixer.music.stop()



print(time.asctime())
print(time.time())


