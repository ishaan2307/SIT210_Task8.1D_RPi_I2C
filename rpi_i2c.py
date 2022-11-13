import smbus   #importing libraries for i2c communicaation. 
import time

light_sensor = 0x23          #default address of light sensor..
off = 0x00     #0x00 when the sensor is off 
on = 0x01       #0x01 when the sensor is on. 
RESET = 0x07        #resets the data values. 

operate_mode = 0x20       #defines the mode in which the device will operate. 

bus = smbus.SMBus(1)  # setting up the i2c interface. 

def converttoanalog(data):       #converting the number into deciaml output. 
    return((data[1] + (256* data[0] )) / 1.2)

def detectlight(addr = light_sensor):         #reading the light input and giving values back. 
    data = bus.read_i2c_block_data(addr, operate_mode)
    return converttoanalog(data)

def main():
    
    while True:
        lux = detectlight()  #detect light intensity. 
        print(lux)      #printing the light intensity. 
        
        if (lux >= 1200):
            print("it is too bright")
        elif(lux > 700 and lux < 1200):
            print(" it is bright")
        elif(lux > 300 and lux < 700):
            print(" there is medium light")
        elif(lux > 30 and lux < 300):
            print("it is dark")
        elif(lux < 30):
            print("it is too dark")
            
        time.sleep(3)
        
main()
