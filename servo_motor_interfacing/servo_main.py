from periphery import PWM
import time

# Open PWM chip 3, channel 0
pwm3 = PWM(2, 0)

# Set frequency to 50Hz
pwm3.frequency = 50

# in servo motor,
# 1ms pulse for 0 degree (LEFT)
# 1.5ms pulse for 90 degree (MIDDLE)
# 2ms pulse for 180 degree (RIGHT)

# so for 50hz, one frequency is 20ms
# duty cycle for 0 degree = (1/20)*100 = 5%
# duty cycle for 90 degree = (1.5/20)*100 = 7.5%
# duty cycle for 180 degree = (2/20)*100 = 10%

pwm3.enable()


try:
    while True:

        # Change duty cycle to .5ms
	pwm3.duty_cycle_ns = 0.5*1000000
	time.sleep(1.5)

	# Change duty cycle to 1.5ms
	pwm3.duty_cycle_ns = 1.5*1000000
		time.sleep(1.5)

	# Change duty cycle to 2.5ms
	pwm3.duty_cycle_ns = 2.5*1000000
	time.sleep(1.5)
		

except KeyboardInterrupt:

    pwm.close()