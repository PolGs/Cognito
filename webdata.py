import time


while (True):
    #Write data to file in CSV format
    with open ('/var/www/html/data.csv','a') as datafile:
        inputs = input()
        datafile.write(inputs + "\n")    
    time.sleep(1.0)
  
