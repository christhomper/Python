# Nerves of Steel 1.0 by Chris Thompson
import time
import random
print('Welcome to the Nerves of Steel')
print()
print('Everyone stand up')
print('Stay standing as long as you dare')
print('Sit down just before you think the time will end.')
print('Anyone still standing when the time ends loses')
print('The last person to sit down before the time ended will win.')

stand_time = random.randint(5, 20)

print ('Stays standing for', stand_time, 'seconds.')

time.sleep(stand_time)

print('****TIME UP****')

