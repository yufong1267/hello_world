#!/usr/bin/env python
# coding: utf-8

# In[13]:


import RPi.GPIO as GPIO


# In[14]:


import time


# In[15]:


GPIO.setmode(GPIO.BOARD)


# In[17]:


GPIO_TRIGGER = 19
GPIO_ECHO = 21
#led_pin = 23


# In[18]:


# Set TRIGGER to OUTPUT mode
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
#GPIO.setup(led_pin, GPIO.OUT)
# Set ECHO to INPUT mode
GPIO.setup(GPIO_ECHO, GPIO.IN)


# In[19]:


def distance():
  # Send 10 microsecond pulse to TRIGGER
  GPIO.output(GPIO_TRIGGER, True) # set TRIGGER to HIGH
  time.sleep(0.00001) # wait 10 microseconds
  GPIO.output(GPIO_TRIGGER, False) # set TRIGGER back to LOW
 
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
  distanceBothWays = measuredTime * 33112 # cm/s in 20 degrees Celsius
  # Divide the distance by 2 to get the actual distance from sensor to obstacle
  distance = distanceBothWays / 2

  # Print the distance to see if everything works correctly
  print("Distance : {0:5.1f}cm".format(distance))
  # Return the actual measured distance
  return distance


# In[20]:


def beep_freq():
  # Measure the distance
  dist = distance()
  # If the distance is bigger than 50cm, we will not beep at all
  if dist > 50:
    return -1
  # If the distance is between 50 and 30 cm, we will beep once a second
  elif dist <= 50 and dist >=10:
    return 1
  # If the distance is between 30 and 20 cm, we will beep every twice a second
  elif dist < 30 and dist >= 20:
    return 0.5
  # If the distance is between 20 and 10 cm, we will beep four times a second
  elif dist < 20 and dist >= 10:
    return 0.25
  # If the distance is smaller than 10 cm, we will beep constantly
  else:
    return 0


# In[21]:


def main():
    try:
    # Repeat till the program is ended by the user
        while True: 
            led_pin = 12
          # Get the beeping frequency
            freq = beep_freq()
            # No beeping
            if freq == -1:
                #print(12123123)
                time.sleep(0.5)
                print("distance > 50")
                GPIO.output(led_pin, GPIO.HIGH)
                GPIO.output(gpio_buzzer, GPIO.HIGH)
                
                time.sleep(0.5)
                GPIO.output(led_pin, GPIO.LOW)
                GPIO.output(gpio_buzzer, GPIO.LOW)
            # Constant beeping
            elif freq == 1:
                time.sleep(0.25)
                print("10 <= distance < 50")
                GPIO.output(led_pin, GPIO.HIGH)
                GPIO.output(gpio_buzzer, GPIO.HIGH)
                time.sleep(0.25)
                GPIO.output(led_pin, GPIO.LOW)
                GPIO.output(gpio_buzzer, GPIO.LOW)
            elif freq == 0:
                time.sleep(0.1)
                print("distance < 10")
                GPIO.output(led_pin, GPIO.HIGH)
                GPIO.output(gpio_buzzer, GPIO.HIGH)
                time.sleep(0.1)
                GPIO.output(led_pin, GPIO.LOW)
                GPIO.output(gpio_buzzer, GPIO.LOW)
            # Beeping on certain frequency
            else:
                time.sleep(0.2) # Beep is 0.2 seconds long
                time.sleep(freq) # Pause between beeps = beeping frequency
  # If the program is ended, stop beeping and cleanup GPIOs
    except KeyboardInterrupt:
        GPIO.cleanup()


# In[22]:


if __name__ == "__main__":
    main()


# In[16]:


GPIO.setup(12, GPIO.OUT)

gpio_buzzer = 33

GPIO.setup(gpio_buzzer, GPIO.OUT)


# In[14]:


get_ipython().system('pinout')


# In[ ]:




