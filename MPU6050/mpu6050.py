import time

from periphery import I2C


# Open i2c-0 controller    
i2c = I2C("/dev/i2c-1")


# Read byte at address 0x100 of EEPROM at 0x50
#msgs = [I2C.Message([0x01, 0x00]), I2C.Message([0x00], read=True)]
#i2c.transfer(0x50, msgs)
#print("0x100: 0x{:02x}".format(msgs[1].data[0]))

#i2c.close()

PWR_M = 0x6B
DIV = 0x19
CONFIG  = 0x1A
GYRO_CONFIG = 0x1B
ACC_CONFIG = 0x1C

INT_EN  = 0x38

ACCEL_X = 0x3B
ACCEL_Y = 0x3D
ACCEL_Z = 0x3F

GYRO_X  = 0x43
GYRO_Y  = 0x45
GYRO_Z  = 0x47

TEMP = 0x41

Device_Address = 0x68   # device address

AxCal=0
AyCal=0
AzCal=0

GxCal=0
GyCal=0
GzCal=0

# write_byte_data ( address , offset , data )

#i2c.transfer( address , msg )

# i2c.Message( data[] , read = True/False , flags=0)


def InitMPU():

    #bus.write_byte_data(Device_Address, DIV, 7)
    msgs = [I2C.Message([DIV]), I2C.Message([0x07])]
    i2c.transfer(Device_Address, msgs)

    #bus.write_byte_data(Device_Address, PWR_M, 1)
    msgs = [I2C.Message([PWR_M]), I2C.Message([0x01])]
    i2c.transfer(Device_Address, msgs)

    #bus.write_byte_data(Device_Address, CONFIG, 0)
    msgs = [I2C.Message([CONFIG]), I2C.Message([0x00])]
    i2c.transfer(Device_Address, msgs)

    #bus.write_byte_data(Device_Address, GYRO_CONFIG, 24)
    msgs = [I2C.Message([GYRO_CONFIG]), I2C.Message([0x18])]           # +-2000 deg/s
    i2c.transfer(Device_Address, msgs)

    #bus.write_byte_data(Device_Address, ACC_CONFIG, 24)                # +- 16g
    msgs = [I2C.Message([ACC_CONFIG]), I2C.Message([0x18])]
    i2c.transfer(Device_Address, msgs)

    #bus.write_byte_data(Device_Address, INT_EN, 1)
    msgs = [I2C.Message([INT_EN]), I2C.Message([0x01])]
    i2c.transfer(Device_Address, msgs)

    time.sleep(1)



def readMPU(addr):
    
    # high = bus.read_byte_data(Device_Address, addr)
    msgs = [I2C.Message([addr]), I2C.Message([0x00], read=True)]
    i2c.transfer(Device_Address, msgs)
    high = msgs[1].data[0]

    # low = bus.read_byte_data(Device_Address, addr+1)
    msgs = [I2C.Message([addr+1]), I2C.Message([0x00], read=True)]
    i2c.transfer(Device_Address, msgs)
    low = msgs[1].data[0]

    value = ((high << 8) | low)
    
    if(value > 32768):
        value = value - 65536
    
    return value



def accel():
    
    x = readMPU(ACCEL_X)
    y = readMPU(ACCEL_Y)
    z = readMPU(ACCEL_Z)

    Ax = (x/16384.0-AxCal) 
    Ay = (y/16384.0-AyCal) 
    Az = (z/16384.0-AzCal)

    #print "X="+str(Ax)

    print(" Ax = %f , Ay = %f , Az = %f "%(Ax,Ay,Az))

    time.sleep(.01)

def gyro():
    global GxCal
    global GyCal
    global GzCal

    x = readMPU(GYRO_X)
    y = readMPU(GYRO_Y)
    z = readMPU(GYRO_Z)

    Gx = x/131.0 - GxCal
    Gy = y/131.0 - GyCal
    Gz = z/131.0 - GzCal
    
    print(" Gx = %f , Gy = %f , Gz = %f "%(Gx,Gy,Gz))
    time.sleep(.01)

 
def temp():
    tempRow=readMPU(TEMP)
    tempC=(tempRow / 340.0) + 36.53

    tempC="%.2f" %tempC

    print("tempC : ",tempC) 
    time.sleep(.2)


def calibrate():
    
    print("Calibrate....")
   
    global AxCal
    global AyCal
    global AzCal

    x=0
    y=0
    z=0

    for i in range(50):
        x = x + readMPU(ACCEL_X)
        y = y + readMPU(ACCEL_Y)
        z = z + readMPU(ACCEL_Z)

    x= x/50
    y= y/50
    z= z/50

    AxCal = x/16384.0
    AyCal = y/16384.0 
    AzCal = z/16384.0

    print("AxCal : ",AxCal) 
    print("AyCal : ",AyCal) 
    print("AzCal : ",AzCal) 

    global GxCal
    global GyCal
    global GzCal

    x=0
    y=0
    z=0

    for i in range(50):
        x = x + readMPU(GYRO_X)
        y = y + readMPU(GYRO_Y)
        z = z + readMPU(GYRO_Z)

    x= x/50
    y= y/50
    z= z/50

    GxCal = x/131.0
    GyCal = y/131.0
    GzCal = z/131.0

    print("GxCal : ",GxCal) 
    print("GyCal : ",GyCal) 
    print("GzCal : ",GzCal) 


print("MPU6050 Interface")
InitMPU()
calibrate()


while 1:
    InitMPU()
    temp()
    time.sleep(1)  
    accel()
    time.sleep(1)
    gyro()