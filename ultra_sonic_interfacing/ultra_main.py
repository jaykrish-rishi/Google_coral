from periphery import GPIO
import time

trig = GPIO("/dev/gpiochip2", 13, "out")  # pin 37 trig
echo = GPIO("/dev/gpiochip4", 13, "in")  # pin 36 echo

trig.write(False)
print("Calibrating...")
time.sleep(2)

print ("place the object")


try :
    while True :
        trig.write(True)
        time.sleep(0.00001)
        trig.write(False)
        
        while echo.read() == False :
            print("in 0 read")

        while echo.read() == True :
            pluse_start = time.time()
            print("in 1 read")
        pluse_end = time.time()

        pluse_duration = pluse_end - pluse_start

        distance = pluse_duration * 17150

        distance = round(distance+1.15 , 2)

        if distance<=20 and distance >=5:
            print("distance : %f cm"%(distance))
            i=1

        if distance >20 and i==1 :
            print (" place the object ")
            i=0

        time.sleep(2)

except KeyboardInterrupt :
    trig.write(False)
    trig.close()
    echo.close()