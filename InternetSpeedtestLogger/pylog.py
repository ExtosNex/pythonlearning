import datetime
import subprocess
import os

#could use this module but am too lazy
#import speedtest

gettime = str(datetime.datetime.now()) 
file = open(os.getcwd() + "/log.txt", "a")

#Runs  `speedtest` and write it to a string
speedvalue = subprocess.run(["speedtest", "--simple"], stdout=subprocess.PIPE).stdout.decode("utf-8")


#speedvalue = str(os.system("speedtest"))

def speedtest():
    #st = speedtest.Speedtest()
    #file.write(st.download)
    #os.system("speedtest >> log.txt")
    file.write(speedvalue)

def space():
    file.write("\n" + "==============================" + "\n")

def writetime():
    file.write("\n" + gettime + "\n\n")


space()
writetime()
speedtest()
space()