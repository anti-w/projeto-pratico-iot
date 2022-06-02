import RPi.GPIO as GPIO
import time

# We will be using the BCM GPIO numbering
GPIO.setmode(GPIO.BCM)

# Select which GPIOs you will use
GPIO_BUZZER = 18
GPIO_TRIGGER = 23
GPIO_ECHO = 22

# Set BUZZER to OUTPUT mode
GPIO.setup(GPIO_BUZZER, GPIO.OUT)
# Set TRIGGER to OUTPUT mode
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
# Set ECHO to INPUT mode
GPIO.setup(GPIO_ECHO, GPIO.IN)

# Measures the distance between a sensor and an obstacle and returns the measured value


def distance():
    # Send 10 microsecond pulse to TRIGGER
    GPIO.output(GPIO_TRIGGER, True)  # set TRIGGER to HIGH
    time.sleep(0.00001)  # wait 10 microseconds
    GPIO.output(GPIO_TRIGGER, False)  # set TRIGGER back to LOW

    # Create variable start and assign it current time
    start = time.time()
    # Create variable stop and assign it current time
    stop = time.time()
    # Refresh start value until the ECHO goes HIGH = until the wave is send
    while GPIO.input(GPIO_ECHO) == 0:
        start = time.time()

    # Assign the actual time to stop variable until the ECHO goes back from HIGH to LOW = the wave came back
    while GPIO.input(GPIO_ECHO) == 1:
        stop = time.time()

    # Calculate the time it took the wave to travel there and back
    measuredTime = stop - start
    # Calculate the travel distance by multiplying the measured time by speed of sound
    distanceBothWays = measuredTime * 33112  # cm/s in 20 degrees Celsius
    # Divide the distance by 2 to get the actual distance from sensor to obstacle
    distance = distanceBothWays / 2

    # Print the distance to see if everything works correctly
    print("Distance : {0:5.1f}cm".format(distance))
    # Return the actual measured distance
    return distance
