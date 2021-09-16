#!/usr/bin/env python3
#! @author: @ruhend(Mudigonda Himansh)
#! Assignment 6
#! Network Commands


import subprocess

command = ["ping -c 5 ruhend.github.io", 
"traceroute ruhend.github.io", "telnet www.ruhend.github.io 443", "ifconfig",
           "netstat", "ifconfig", "dig ruhend.github.io", "nslookup ruhend.github.io","whois ruhend.github.io"]

for i in command:
    print("**********************")
    print(i)
    process = subprocess.Popen(i.split())
    op, er = process.communicate()
    print("> "+str(er))
