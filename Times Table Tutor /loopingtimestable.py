import time
count = 1
times_value = 5
while count > 0:
    result = count * times_value 
    print(count,'times', times_value, 'equals',result)
    count = count + 1
    time.sleep(1.5)
    
