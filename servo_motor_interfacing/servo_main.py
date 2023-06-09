from periphery import PWM
import time

# Open PWM chip 0, channel 0
pwm = PWM(0, 0)

# Set frequency to 50Hzs
pwm.frequency = 50

pwm.duty_cycle = 0.05 # Change duty cycle to .5ms 

# in servo motor,
# 1ms pulse for 0 degree (LEFT)
# 1.5ms pulse for 90 degree (MIDDLE)
# 2ms pulse for 180 degree (RIGHT)

# so for 50hz, one frequency is 20ms
# duty cycle for 0 degree = (1/20)*100 = 5%
# duty cycle for 90 degree = (1.5/20)*100 = 7.5%
# duty cycle for 180 degree = (2/20)*100 = 10%

pwm.enable()


try:
	while True:
		pwm.duty_cycle = 0.05 # Change duty cycle to .5ms 
		time.sleep(1.5)
		pwm.duty_cycle = 0.075 # Change duty cycle to 1.5ms
		time.sleep(1.5)
		pwm.duty_cycle = 0.1 # Change duty cycle to 2.5ms
		time.sleep(1.5)
		print("in while loop")
		time.sleep(2)


except KeyboardInterrupt:
	pwm.close()

finally :
	pwm.close()
