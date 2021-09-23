#!/usr/bin/env python3
#! @author: @ruhend(Mudigonda Himansh)
#! Assignment 5
#! Network Commands


import subprocess

command = [ "ping -c 5 www.google.com",
            "traceroute www.google.com", 
            "telnet www.www.google.com 443", 
            "ifconfig",
            "netstat", 
            "ifconfig", 
            "dig www.google.com", 
            "nslookup www.google.com",
            "whois www.google.com" ]

# These commands would work only if the binary is available.

for i in command:
    print("**********************")
    print(i)
    process = subprocess.Popen(i.split())
    op, er = process.communicate()
    print("> "+str(er))


#! OUTPUT
# **********************
# ping -c 5 www.google.com
# PING www.google.com (142.250.77.100): 56 data bytes
# 64 bytes from 142.250.77.100: icmp_seq=0 ttl=54 time=38.735 ms
# 64 bytes from 142.250.77.100: icmp_seq=1 ttl=54 time=36.221 ms
# 64 bytes from 142.250.77.100: icmp_seq=2 ttl=54 time=38.962 ms
# 64 bytes from 142.250.77.100: icmp_seq=3 ttl=54 time=37.588 ms
# 64 bytes from 142.250.77.100: icmp_seq=4 ttl=54 time=30.758 ms

# --- www.google.com ping statistics ---
# 5 packets transmitted, 5 packets received, 0.0% packet loss
# round-trip min/avg/max/stddev = 30.758/36.453/38.962/3.009 ms
# > None
# **********************
# traceroute www.google.com
# traceroute to www.google.com (142.250.77.100), 64 hops max, 52 byte packets
#  1  192.168.245.35 (192.168.245.35)  2.478 ms  2.046 ms  1.957 ms
#  2  192.168.0.1 (192.168.0.1)  5.785 ms  5.339 ms  5.780 ms
#  3  10.210.0.1 (10.210.0.1)  15.711 ms  33.363 ms  30.219 ms
#  4  202.88.174.153 (202.88.174.153)  18.892 ms  19.278 ms  20.490 ms
#  5  202.88.174.66 (202.88.174.66)  20.446 ms  24.005 ms  20.509 ms
#  6  202.88.190.45 (202.88.190.45)  20.472 ms  17.917 ms  16.021 ms
#  7  10.241.1.6 (10.241.1.6)  19.072 ms  20.082 ms  22.452 ms
#  8  10.240.254.100 (10.240.254.100)  19.325 ms  25.724 ms  26.737 ms
#  9  10.240.254.1 (10.240.254.1)  31.239 ms  24.672 ms  22.923 ms
# 10  10.241.1.1 (10.241.1.1)  20.272 ms  40.104 ms  28.003 ms
# 11  136.232.28.173.static.jio.com (136.232.28.173)  44.805 ms  28.655 ms  23.416 ms
# 12  * * *
# 13  * * *
# 14  209.85.175.48 (209.85.175.48)  68.625 ms  35.987 ms
#     72.14.217.252 (72.14.217.252)  39.474 ms
# 15  74.125.242.129 (74.125.242.129)  43.252 ms * *
# 16  209.85.248.180 (209.85.248.180)  35.864 ms
#     142.251.55.226 (142.251.55.226)  30.421 ms
#     108.170.253.97 (108.170.253.97)  32.849 ms
# 17  142.251.55.231 (142.251.55.231)  28.856 ms
#     maa05s15-in-f4.1e100.net (142.250.77.100)  35.301 ms  40.754 ms
# > None
# **********************
# telnet www.www.google.com 443
# www.www.google.com: nodename nor servname provided, or not known
# > None
# **********************
# ifconfig
# lo0: flags=8049<UP,LOOPBACK,RUNNING,MULTICAST> mtu 16384
#         options=1203<RXCSUM,TXCSUM,TXSTATUS,SW_TIMESTAMP>
#         inet 127.0.0.1 netmask 0xff000000 
#         inet6 ::1 prefixlen 128 
#         inet6 fe80::1%lo0 prefixlen 64 scopeid 0x1 
#         nd6 options=201<PERFORMNUD,DAD>
# gif0: flags=8010<POINTOPOINT,MULTICAST> mtu 1280
# stf0: flags=0<> mtu 1280
# XHC20: flags=0<> mtu 0
# utun0: flags=8051<UP,POINTOPOINT,RUNNING,MULTICAST> mtu 1380
#         inet6 fe80::5252:dbe:6a2f:3513%utun0 prefixlen 64 scopeid 0x5 
#         nd6 options=201<PERFORMNUD,DAD>
# utun1: flags=8051<UP,POINTOPOINT,RUNNING,MULTICAST> mtu 2000
#         inet6 fe80::6377:ae36:1ccb:2c7d%utun1 prefixlen 64 scopeid 0x6 
#         nd6 options=201<PERFORMNUD,DAD>
# en2: flags=8863<UP,BROADCAST,SMART,RUNNING,SIMPLEX,MULTICAST> mtu 1500
#         options=400<CHANNEL_IO>
#         ether 2e:08:64:f1:52:bf 
#         inet6 fe80::8c8:de31:3987:fc73%en2 prefixlen 64 secured scopeid 0x8 
#         inet 192.168.245.156 netmask 0xffffff00 broadcast 192.168.245.255
#         nd6 options=201<PERFORMNUD,DAD>
#         media: autoselect
#         status: active
# > None
# **********************
# netstat
# Active Internet connections
# Proto Recv-Q Send-Q  Local Address          Foreign Address        (state)    
# tcp4       0      0  192.168.245.156.55554  whatsapp-cdn-shv.https ESTABLISHED
# tcp4       0      0  192.168.245.156.55393  ec2-52-5-133-92..https ESTABLISHED
# tcp4       0      0  192.168.245.156.55277  ec2-44-227-165-1.https ESTABLISHED
# tcp4       0      0  192.168.245.156.54721  server-13-35-238.https ESTABLISHED
# tcp4       0      0  192.168.245.156.54316  20.195.65.205.https    ESTABLISHED
# tcp4       0      0  192.168.245.156.54123  sa-in-f108.1e100.imaps ESTABLISHED
# tcp4       0      0  192.168.245.156.54116  sa-in-f108.1e100.imaps ESTABLISHED
# tcp4       0      0  192.168.245.156.54115  sa-in-f108.1e100.imaps ESTABLISHED
# tcp4       0      0  192.168.245.156.54114  145.33.211.130.b.https ESTABLISHED
# tcp4       0      0  192.168.245.156.53202  13.67.9.5.https        ESTABLISHED
# tcp4       0      0  192.168.245.156.52838  199.36.158.100.https   ESTABLISHED
# tcp4       0      0  192.168.245.156.50577  156.247.107.34.b.https ESTABLISHED
# tcp4       0      0  192.168.245.156.50335  sd-in-f188.1e100.https ESTABLISHED
# tcp4       0      0  192.168.245.156.50334  ec2-18-205-93-20.https ESTABLISHED
# tcp4       0      0  192.168.245.156.50331  maa05s12-in-f14..http  ESTABLISHED
# tcp4       0      0  192.168.245.156.50172  ec2-52-202-62-22.https ESTABLISHED
# tcp4       0      0  192.168.245.156.50163  173.231.94.31.https    ESTABLISHED
# tcp4       0      0  192.168.245.156.49925  17.57.145.116.5223     ESTABLISHED
# tcp4       0      0  localhost.46624        localhost.55525        TIME_WAIT  
# tcp4       0      0  localhost.46624        localhost.55526        TIME_WAIT  
# tcp4       0      0  localhost.55030        localhost.46624        TIME_WAIT  
# tcp4       0      0  192.168.245.156.54138  145.33.211.130.b.https TIME_WAIT  
# tcp4       0      0  localhost.46624        localhost.55548        TIME_WAIT  
# tcp4       0      0  localhost.46624        localhost.55549        TIME_WAIT  
# tcp4       0      0  localhost.46624        localhost.55572        TIME_WAIT  
# tcp4       0      0  localhost.46624        localhost.55573        TIME_WAIT  
# tcp4       0      0  localhost.46624        localhost.55590        TIME_WAIT  
# tcp4       0      0  localhost.46624        localhost.55591        TIME_WAIT  
# tcp4       0      0  localhost.46624        localhost.55612        TIME_WAIT  
# tcp4       0      0  localhost.46624        localhost.55613        TIME_WAIT  
# tcp4       0      0  localhost.46624        localhost.55634        TIME_WAIT  
# tcp4       0      0  localhost.46624        localhost.55635        TIME_WAIT  
# tcp4       0      0  localhost.46624        localhost.55657        TIME_WAIT  
# tcp4       0      0  localhost.46624        localhost.55658        TIME_WAIT  
# tcp4       0      0  localhost.46624        localhost.55663        TIME_WAIT  
# udp4       0      0  192.168.245.156.53051  *.*                               
# udp4       0      0  192.168.245.156.57620  maa03s40-in-f10..https            
# udp4       0      0  *.*                    *.*                               
# udp46      0      0  *.*                    *.*                               
# udp4       0      0  *.*                    *.*                               
# udp6       0      0  *.mdns                 *.*                               
# udp4       0      0  *.mdns                 *.*                               
# udp4       0      0  *.netbios-dgm          *.*                               
# udp4       0      0  *.netbios-ns           *.*                               
# Active Multipath Internet connections
# Proto/ID  Flags      Local Address          Foreign Address        (state)    
# icm6       0      0  *.*                    *.*                               
# Active LOCAL (UNIX) domain sockets
# Address          Type   Recv-Q Send-Q            Inode             Conn             Refs          Nextref Addr
# 5264b0a3969d9ded stream      0      0                0 5264b0a3969d9d25                0                0 /var/run/mDNSResponder
# 5264b0a3969d9d25 stream      0      0                0 5264b0a3969d9ded                0                0
# 5264b0a3969d803d stream      0      0                0 5264b0a3969d7f75                0                0 /var/run/mDNSResponder
# 5264b0a3969d7f75 stream      0      0                0 5264b0a3969d803d                0                0
# 5264b0a3938a093d stream      0      0 5264b0a397538315                0                0                0 /var/folders/5p/2y6w9nfd4w3fl0vp97b1w_cc0000gn/T/.WhatsApp.cZpxak/SS
# 5264b0a3938a0c5d stream      0      0                0 5264b0a3938a0b95                0                0
# 5264b0a3938a0b95 stream      0      0                0 5264b0a3938a0c5d                0                0
# 5264b0a3938a02fd stream      0      0                0 5264b0a39389e7a5                0                0
# 5264b0a39389e7a5 stream      0      0                0 5264b0a3938a02fd                0                0
# 5264b0a3969d79fd stream      0      0                0 5264b0a3969d7935                0                0 /var/run/mDNSResponder
# 5264b0a3969d7935 stream      0      0                0 5264b0a3969d79fd                0                0
# 5264b0a3969da4f5 stream      0      0                0 5264b0a3969da42d                0                0
# 5264b0a3969da42d stream      0      0                0 5264b0a3969da4f5                0                0
# 5264b0a3969da365 stream      0      0                0 5264b0a3969da29d                0                0
# 5264b0a3969da29d stream      0      0                0 5264b0a3969da365                0                0
# 5264b0a3969da045 stream      0      0                0 5264b0a3969d9f7d                0                0
# 5264b0a3969d9f7d stream      0      0                0 5264b0a3969da045                0                0
# 5264b0a3969d9eb5 stream      0      0                0 5264b0a3938a0ded                0                0
# 5264b0a3938a0ded stream      0      0                0 5264b0a3969d9eb5                0                0
# 5264b0a3969d7b8d stream      0      0                0 5264b0a3969d7ac5                0                0 /var/folders/5p/2y6w9nfd4w3fl0vp97b1w_cc0000gn/T/CoreFxPipe_vscode.a01785ad790b74fd8ca4bcbca323cd37
# 5264b0a3969d7ac5 stream      0      0                0 5264b0a3969d7b8d                0                0
# 5264b0a39389e86d stream      0      0 5264b0a393a1e915                0                0                0 /var/folders/5p/2y6w9nfd4w3fl0vp97b1w_cc0000gn/T/CoreFxPipe_vscode.a01785ad790b74fd8ca4bcbca323cd37
# 5264b0a39389fcbd stream      0      0 5264b0a3973b1315                0                0                0 /var/folders/5p/2y6w9nfd4w3fl0vp97b1w_cc0000gn/T/dotnet-diagnostic-3990-1631870240-socket
# 5264b0a3938a0235 stream      0      0                0 5264b0a3938a0acd                0                0
# 5264b0a3938a0acd stream      0      0                0 5264b0a3938a0235                0                0
# 5264b0a3969d948d stream      0      0                0 5264b0a3969d9235                0                0
# 5264b0a3969d9235 stream      0      0                0 5264b0a3969d948d                0                0
# 5264b0a3969d90a5 stream      0      0                0 5264b0a3969d8fdd                0                0
# 5264b0a3969d8fdd stream      0      0                0 5264b0a3969d90a5                0                0
# 5264b0a39389fd85 stream      0      0 5264b0a3973b1415                0                0                0 /var/folders/5p/2y6w9nfd4w3fl0vp97b1w_cc0000gn/T/CoreFxPipe_f3e70055d3c346c989cd650448fde7d2
# 5264b0a3969d7d1d stream      0      0                0 5264b0a3969d7c55                0                0 /var/folders/5p/2y6w9nfd4w3fl0vp97b1w_cc0000gn/T/vscode-efbd5f63fa08af9a19f9c24f817de1d97dd704e1.sock
# 5264b0a3969d7c55 stream      0      0                0 5264b0a3969d7d1d                0                0
# 5264b0a3969da1d5 stream      0      0                0 5264b0a3969da10d                0                0
# 5264b0a3969da10d stream      0      0                0 5264b0a3969da1d5                0                0
# 5264b0a3938a0a05 stream      0      0                0 5264b0a3938a06e5                0                0 /var/folders/5p/2y6w9nfd4w3fl0vp97b1w_cc0000gn/T/vscode-5de46037824cb4b3aeff4ae54c5cc54c1556632e.sock
# 5264b0a3938a06e5 stream      0      0                0 5264b0a3938a0a05                0                0
# 5264b0a3938a14f5 stream      0      0                0 5264b0a3938a142d                0                0
# 5264b0a3938a142d stream      0      0                0 5264b0a3938a14f5                0                0
# 5264b0a3938a11d5 stream      0      0                0 5264b0a3938a110d                0                0
# 5264b0a3938a110d stream      0      0                0 5264b0a3938a11d5                0                0
# 5264b0a3938a1045 stream      0      0                0 5264b0a3938a048d                0                0
# 5264b0a3938a048d stream      0      0                0 5264b0a3938a1045                0                0
# 5264b0a39389fa65 stream      0      0                0 5264b0a39389e935                0                0
# 5264b0a39389e935 stream      0      0                0 5264b0a39389fa65                0                0
# 5264b0a39389e615 stream      0      0 5264b0a397384915                0                0                0 /var/folders/5p/2y6w9nfd4w3fl0vp97b1w_cc0000gn/T/vscode-5de46037824cb4b3aeff4ae54c5cc54c1556632e.sock
# 5264b0a3938a0d25 stream      0      0 5264b0a3969e3a15                0                0                0 /var/folders/5p/2y6w9nfd4w3fl0vp97b1w_cc0000gn/T/vscode-git-0dd8e09022.sock
# 5264b0a3938a1365 stream      0      0                0 5264b0a3938a129d                0                0 /var/run/mDNSResponder
# 5264b0a3938a129d stream      0      0                0 5264b0a3938a1365                0                0
# 5264b0a39389f99d stream      0      0                0 5264b0a39389f8d5                0                0
# 5264b0a39389f8d5 stream      0      0                0 5264b0a39389f99d                0                0
# 5264b0a3938a0875 stream      0      0                0 5264b0a3938a07ad                0                0
# 5264b0a3938a07ad stream      0      0                0 5264b0a3938a0875                0                0
# 5264b0a3938a016d stream      0      0                0 5264b0a3938a00a5                0                0 /var/run/mDNSResponder
# 5264b0a3938a00a5 stream      0      0                0 5264b0a3938a016d                0                0
# 5264b0a39389f67d stream      0      0                0 5264b0a39389f5b5                0                0
# 5264b0a39389f5b5 stream      0      0                0 5264b0a39389f67d                0                0
# 5264b0a39389f425 stream      0      0                0 5264b0a39389f295                0                0 /var/folders/5p/2y6w9nfd4w3fl0vp97b1w_cc0000gn/T/vscode-ipc-563afa84-ef7c-45dd-bd14-65fb71fae75a.sock
# 5264b0a39389f295 stream      0      0                0 5264b0a39389f425                0                0
# 5264b0a39389f1cd stream      0      0                0 5264b0a39389f105                0                0
# 5264b0a39389f105 stream      0      0                0 5264b0a39389f1cd                0                0
# 5264b0a39389f03d stream      0      0                0 5264b0a39389ef75                0                0
# 5264b0a39389ef75 stream      0      0                0 5264b0a39389f03d                0                0
# 5264b0a39389eead stream      0      0                0 5264b0a39389ede5                0                0
# 5264b0a39389ede5 stream      0      0                0 5264b0a39389eead                0                0
# 5264b0a39389ed1d stream      0      0                0 5264b0a39389ec55                0                0
# 5264b0a39389ec55 stream      0      0                0 5264b0a39389ed1d                0                0
# 5264b0a39389eb8d stream      0      0                0 5264b0a39389eac5                0                0
# 5264b0a39389eac5 stream      0      0                0 5264b0a39389eb8d                0                0
# 5264b0a39389fbf5 stream      0      0                0 5264b0a39389fb2d                0                0 /var/run/mDNSResponder
# 5264b0a39389fb2d stream      0      0                0 5264b0a39389fbf5                0                0
# 5264b0a39389f4ed stream      0      0                0 5264b0a39389f35d                0                0
# 5264b0a39389f35d stream      0      0                0 5264b0a39389f4ed                0                0
# 5264b0a3938a061d stream      0      0                0 5264b0a3938a0555                0                0 /var/run/mDNSResponder
# 5264b0a3938a0555 stream      0      0                0 5264b0a3938a061d                0                0
# 5264b0a3938a0eb5 stream      0      0 5264b0a396668b15                0                0                0 /Users/ruhend/Library/Application Support/Code/1.60.1-main.sock
# 5264b0a39389f745 stream      0      0 5264b0a394d3c815                0                0                0 /Users/ruhend/Library/Group Containers/BJ4HAAB9B3.ZoomClient3rd/s.zzhost
# 5264b0a39389ffdd stream      0      0                0 5264b0a38fc73f15                0                0 /var/run/mDNSResponder
# 5264b0a38fc73f15 stream      0      0                0 5264b0a39389ffdd                0                0
# 5264b0a38fc73425 stream      0      0 5264b0a394a61c15                0                0                0 /Users/ruhend/Library/Group Containers/BJ4HAAB9B3.ZoomClient3rd/s.zoomclient
# 5264b0a38fc73bf5 stream      0      0                0 5264b0a38fc73a65                0                0
# 5264b0a38fc73a65 stream      8      0                0 5264b0a38fc73bf5                0                0
# 5264b0a38fc735b5 stream      0      0                0 5264b0a38fc734ed                0                0 /var/run/mDNSResponder
# 5264b0a38fc734ed stream      0      0                0 5264b0a38fc735b5                0                0
# 5264b0a38fc754f5 stream      0      0                0 5264b0a38fc75045                0                0 /var/run/mDNSResponder
# 5264b0a38fc75045 stream      0      0                0 5264b0a38fc754f5                0                0
# 5264b0a387c25ded stream      0      0 5264b0a393889715                0                0                0 /var/folders/5p/2y6w9nfd4w3fl0vp97b1w_cc0000gn/T/.com.google.Chrome.dev.dKZCQZ/SingletonSocket
# 5264b0a38fc7367d stream      0      0                0 5264b0a38fc7335d                0                0 /var/run/mDNSResponder
# 5264b0a38fc7335d stream      0      0                0 5264b0a38fc7367d                0                0
# 5264b0a38fc7542d stream      0      0                0 5264b0a38fc75365                0                0 /tmp/com.adobe.AdobeIPCBroker.ctrl-ruhend
# 5264b0a38fc75365 stream      0      0                0 5264b0a38fc7542d                0                0
# 5264b0a38fc7529d stream      0      0                0 5264b0a38fc751d5                0                0 /tmp/com.adobe.AdobeIPCBroker.ctrl-ruhend
# 5264b0a38fc751d5 stream      0      0                0 5264b0a38fc7529d                0                0
# 5264b0a38fc74f7d stream      0      0                0 5264b0a38fc74d25                0                0 /tmp/com.adobe.AdobeIPCBroker.ctrl-ruhend
# 5264b0a38fc74d25 stream      0      0                0 5264b0a38fc74f7d                0                0
# 5264b0a38fc74c5d stream      0      0                0 5264b0a38fc74875                0                0 /tmp/com.adobe.AdobeIPCBroker.ctrl-ruhend
# 5264b0a38fc74875 stream      0      0                0 5264b0a38fc74c5d                0                0
# 5264b0a38fc74555 stream      0      0                0 5264b0a38fc742fd                0                0 /tmp/com.adobe.AdobeIPCBroker.ctrl-ruhend
# 5264b0a38fc742fd stream      0      0                0 5264b0a38fc74555                0                0
# 5264b0a38fc74235 stream      0      0                0 5264b0a38fc73fdd                0                0 /tmp/com.adobe.AdobeIPCBroker.ctrl-ruhend
# 5264b0a38fc73fdd stream      0      0                0 5264b0a38fc74235                0                0
# 5264b0a38fc7448d stream      0      0                0 5264b0a38fc743c5                0                0 /tmp/com.adobe.AdobeIPCBroker.ctrl-ruhend
# 5264b0a38fc743c5 stream      0      0                0 5264b0a38fc7448d                0                0
# 5264b0a38fc73d85 stream      0      0                0 5264b0a38fc73cbd                0                0 /tmp/com.adobe.AdobeIPCBroker.ctrl-ruhend
# 5264b0a38fc73cbd stream      0      0                0 5264b0a38fc73d85                0                0
# 5264b0a38fc74eb5 stream      0      0                0 5264b0a38fc74ded                0                0 /var/run/mDNSResponder
# 5264b0a38fc74ded stream      0      0                0 5264b0a38fc74eb5                0                0
# 5264b0a38fc72f75 stream      0      0                0 5264b0a38fc72ead                0                0 /var/run/mDNSResponder
# 5264b0a38fc72ead stream      0      0                0 5264b0a38fc72f75                0                0
# 5264b0a38fc726dd stream      0      0                0 5264b0a38fc72615                0                0 /tmp/com.adobe.AdobeIPCBroker.ctrl-ruhend
# 5264b0a38fc72615 stream      0      0                0 5264b0a38fc726dd                0                0
# 5264b0a38fc72de5 stream      0      0                0 5264b0a38fc72d1d                0                0 /tmp/com.adobe.AdobeIPCBroker.ctrl-ruhend
# 5264b0a38fc72d1d stream      0      0                0 5264b0a38fc72de5                0                0
# 5264b0a38fc72c55 stream      0      0 5264b0a39010c215                0                0                0 /tmp/com.adobe.AdobeIPCBroker.ctrl-ruhend
# 5264b0a38fc74b95 stream      0      0                0 5264b0a38fc74a05                0                0 /var/run/mDNSResponder
# 5264b0a38fc74acd stream      0      0                0 5264b0a38fc7493d                0                0 /var/run/mDNSResponder
# 5264b0a38fc747ad stream      0      0                0 5264b0a38fc7461d                0                0 /var/run/mDNSResponder
# 5264b0a38fc74a05 stream      0      0                0 5264b0a38fc74b95                0                0
# 5264b0a38fc7493d stream      0      0                0 5264b0a38fc74acd                0                0
# 5264b0a38fc746e5 stream      0      0                0 5264b0a387c2561d                0                0 /var/run/mDNSResponder
# 5264b0a38fc7461d stream      0      0                0 5264b0a38fc747ad                0                0
# 5264b0a38fc740a5 stream      0      0                0 5264b0a387c25555                0                0 /var/run/mDNSResponder
# 5264b0a387c2593d stream      0      0                0 5264b0a387c25235                0                0 /var/run/mDNSResponder
# 5264b0a387c25875 stream      0      0                0 5264b0a387c2516d                0                0 /var/run/mDNSResponder
# 5264b0a387c257ad stream      0      0                0 5264b0a387c252fd                0                0 /var/run/mDNSResponder
# 5264b0a387c256e5 stream      0      0                0 5264b0a387c250a5                0                0 /var/run/mDNSResponder
# 5264b0a387c2561d stream      0      0                0 5264b0a38fc746e5                0                0
# 5264b0a387c25235 stream      0      0                0 5264b0a387c2593d                0                0
# 5264b0a387c25555 stream      0      0                0 5264b0a38fc740a5                0                0
# 5264b0a387c252fd stream      0      0                0 5264b0a387c257ad                0                0
# 5264b0a387c2516d stream      0      0                0 5264b0a387c25875                0                0
# 5264b0a387c250a5 stream      0      0                0 5264b0a387c256e5                0                0
# 5264b0a387c2548d stream      0      0                0 5264b0a387c253c5                0                0 /var/run/mDNSResponder
# 5264b0a387c253c5 stream      0      0                0 5264b0a387c2548d                0                0
# 5264b0a387c24d85 stream      0      0                0 5264b0a387c24bf5                0                0 /var/run/mDNSResponder
# 5264b0a387c24bf5 stream      0      0                0 5264b0a387c24d85                0                0
# 5264b0a387c24a65 stream      0      0                0 5264b0a387c2499d                0                0 /var/run/mDNSResponder
# 5264b0a387c2499d stream      0      0                0 5264b0a387c24a65                0                0
# 5264b0a387c248d5 stream      0      0                0 5264b0a387c2480d                0                0 /var/run/mDNSResponder
# 5264b0a387c2480d stream      0      0                0 5264b0a387c248d5                0                0
# 5264b0a387c24745 stream      0      0                0 5264b0a387c2467d                0                0 /var/run/usbmuxd
# 5264b0a387c2467d stream      0      0                0 5264b0a387c24745                0                0
# 5264b0a387c245b5 stream      0      0                0 5264b0a387c244ed                0                0 /var/run/mDNSResponder
# 5264b0a387c244ed stream      0      0                0 5264b0a387c245b5                0                0
# 5264b0a387c24425 stream      0      0                0 5264b0a387c2435d                0                0 /var/run/mDNSResponder
# 5264b0a387c2435d stream      0      0                0 5264b0a387c24425                0                0
# 5264b0a387c24295 stream      0      0                0 5264b0a387c241cd                0                0 /var/run/mDNSResponder
# 5264b0a387c241cd stream      0      0                0 5264b0a387c24295                0                0
# 5264b0a387c23f75 stream      0      0                0 5264b0a387c23ead                0                0 /var/run/usbmuxd
# 5264b0a387c23ead stream      0      0                0 5264b0a387c23f75                0                0
# 5264b0a387c2642d stream      0      0                0 5264b0a387c26365                0                0
# 5264b0a387c26365 stream      0      0                0 5264b0a387c2642d                0                0
# 5264b0a387c2629d stream      0      0                0 5264b0a387c261d5                0                0
# 5264b0a387c261d5 stream      0      0                0 5264b0a387c2629d                0                0
# 5264b0a387c2610d stream      0      0                0 5264b0a387c26045                0                0
# 5264b0a387c26045 stream      0      0                0 5264b0a387c2610d                0                0
# 5264b0a387c25f7d stream      0      0                0 5264b0a387c25eb5                0                0
# 5264b0a387c25eb5 stream      0      0                0 5264b0a387c25f7d                0                0
# 5264b0a387c237a5 stream      0      0                0 5264b0a387c236dd                0                0 /var/run/mDNSResponder
# 5264b0a387c236dd stream      0      0                0 5264b0a387c237a5                0                0
# 5264b0a38257a93d stream      0      0                0 5264b0a38257999d                0                0 /var/run/mDNSResponder
# 5264b0a38257999d stream      0      0                0 5264b0a38257a93d                0                0
# 5264b0a382579425 stream      0      0 5264b0a38144f415                0                0                0 /var/tmp/filesystemui.socket
# 5264b0a38257b4f5 stream      0      0 5264b0a38144f315                0                0                0 /private/tmp/com.apple.launchd.rYrS1KqhsO/Listeners
# 5264b0a38257a555 stream      0      0                0 5264b0a38257a3c5                0                0
# 5264b0a38257a3c5 stream      0      0                0 5264b0a38257a555                0                0
# 5264b0a382579a65 stream      0      0 5264b0a383939215                0                0                0 /var/run/pppconfd
# 5264b0a382579745 stream      0      0 5264b0a383063e15                0                0                0 /var/run/displaypolicyd/state
# 5264b0a38257935d stream      0      0 5264b0a3827ab115                0                0                0 /var/run/usbmuxd
# 5264b0a382579295 stream      0      0 5264b0a3827aa615                0                0                0 /var/rpc/ncalrpc/srvsvc
# 5264b0a3825791cd stream      0      0 5264b0a3827ab515                0                0                0 /var/rpc/ncacn_np/srvsvc
# 5264b0a382579105 stream      0      0 5264b0a3827a6215                0                0                0 /var/rpc/ncalrpc/wkssvc
# 5264b0a38257903d stream      0      0 5264b0a3827a6115                0                0                0 /var/rpc/ncacn_np/wkssvc
# 5264b0a382578f75 stream      0      0 5264b0a3827a6015                0                0                0 /var/rpc/ncacn_np/mdssvc
# 5264b0a382578ead stream      0      0 5264b0a3827a5f15                0                0                0 /var/rpc/ncalrpc/lsarpc
# 5264b0a382578de5 stream      0      0 5264b0a3827a5e15                0                0                0 /var/rpc/ncacn_np/lsarpc
# 5264b0a382578d1d stream      0      0 5264b0a3827a5c15                0                0                0 /var/run/mDNSResponder
# 5264b0a382578c55 stream      0      0 5264b0a3827a5b15                0                0                0 /var/run/systemkeychaincheck.socket
# 5264b0a382578b8d stream      0      0 5264b0a3827a5a15                0                0                0 /private/var/run/.sim_diagnosticd_socket
# 5264b0a382578ac5 stream      0      0 5264b0a3827a5915                0                0                0 /var/run/portmap.socket
# 5264b0a3825789fd stream      0      0 5264b0a3827a5815                0                0                0 /var/run/vpncontrol.sock
# 5264b0a382578935 stream      0      0 5264b0a3827a5715                0                0                0 /var/rpc/ncalrpc/NETLOGON
# 5264b0a38257886d stream      0      0 5264b0a3827a6415                0                0                0 /private/var/run/cupsd
# 5264b0a3969d8105 dgram       0      0                0 5264b0a3825786dd                0 5264b0a3969d9c5d
# 5264b0a3969d9c5d dgram       0      0                0 5264b0a3825786dd                0 5264b0a3969d916d
# 5264b0a39389f80d dgram       0      0                0 5264b0a39389e9fd 5264b0a39389e9fd                0
# 5264b0a39389e9fd dgram       0      0                0 5264b0a39389f80d 5264b0a39389f80d                0
# 5264b0a3969d916d dgram       0      0                0 5264b0a3825786dd                0 5264b0a3938a0f7d
# 5264b0a3969d93c5 dgram       0      0                0 5264b0a3969d92fd 5264b0a3969d92fd                0
# 5264b0a3969d92fd dgram       0      0                0 5264b0a3969d93c5 5264b0a3969d93c5                0
# 5264b0a3938a0f7d dgram       0      0                0 5264b0a3825786dd                0 5264b0a39389e6dd
# 5264b0a39389e6dd dgram       0      0                0 5264b0a3825786dd                0 5264b0a38fc73745
# 5264b0a39389ff15 dgram       0      0                0 5264b0a39389fe4d 5264b0a39389fe4d                0
# 5264b0a39389fe4d dgram       0      0                0 5264b0a39389ff15 5264b0a39389ff15                0
# 5264b0a38fc73745 dgram       0      0                0 5264b0a3825786dd                0 5264b0a3938a03c5
# 5264b0a3938a03c5 dgram       0      0                0 5264b0a3825786dd                0 5264b0a38fc73b2d
# 5264b0a38fc73b2d dgram       0      0                0 5264b0a3825786dd                0 5264b0a38fc7416d
# 5264b0a38fc7416d dgram       0      0                0 5264b0a3825786dd                0 5264b0a38fc73295
# 5264b0a38fc73295 dgram       0      0                0 5264b0a3825786dd                0 5264b0a38fc72b8d
# 5264b0a38fc72b8d dgram       0      0                0 5264b0a3825786dd                0 5264b0a38fc72ac5
# 5264b0a38fc72ac5 dgram       0      0                0 5264b0a3825786dd                0 5264b0a38fc729fd
# 5264b0a38fc729fd dgram       0      0                0 5264b0a3825786dd                0 5264b0a38fc731cd
# 5264b0a38fc72935 dgram       0      0                0 5264b0a38fc727a5 5264b0a38fc727a5                0
# 5264b0a38fc727a5 dgram       0      0                0 5264b0a38fc72935 5264b0a38fc72935                0
# 5264b0a38fc731cd dgram       0      0                0 5264b0a3825786dd                0 5264b0a38fc7380d
# 5264b0a38fc7380d dgram       0      0                0 5264b0a3825786dd                0 5264b0a38fc738d5
# 5264b0a38fc738d5 dgram       0      0                0 5264b0a3825786dd                0 5264b0a387c24fdd
# 5264b0a387c24fdd dgram       0      0                0 5264b0a3825786dd                0 5264b0a38fc7286d
# 5264b0a38fc7286d dgram       0      0                0 5264b0a3825786dd                0 5264b0a38fc7510d
# 5264b0a38fc7510d dgram       0      0                0 5264b0a3825786dd                0 5264b0a38fc73e4d
# 5264b0a38fc73e4d dgram       0      0                0 5264b0a3825786dd                0 5264b0a38fc7399d
# 5264b0a38fc7399d dgram       0      0                0 5264b0a3825786dd                0 5264b0a38fc73105
# 5264b0a38fc73105 dgram       0      0                0 5264b0a3825786dd                0 5264b0a38fc7303d
# 5264b0a38fc7303d dgram       0      0                0 5264b0a3825786dd                0 5264b0a387c24f15
# 5264b0a387c24f15 dgram       0      0                0 5264b0a3825786dd                0 5264b0a387c24e4d
# 5264b0a387c24e4d dgram       0      0                0 5264b0a3825786dd                0 5264b0a387c24cbd
# 5264b0a387c24cbd dgram       0      0                0 5264b0a3825786dd                0 5264b0a387c24b2d
# 5264b0a387c24b2d dgram       0      0                0 5264b0a3825786dd                0 5264b0a387c23de5
# 5264b0a387c24105 dgram       0      0                0 5264b0a387c2403d 5264b0a387c2403d                0
# 5264b0a387c2403d dgram       0      0                0 5264b0a387c24105 5264b0a387c24105                0
# 5264b0a387c23de5 dgram       0      0                0 5264b0a3825786dd                0 5264b0a387c23d1d
# 5264b0a387c23d1d dgram       0      0                0 5264b0a3825786dd                0 5264b0a387c23c55
# 5264b0a387c23c55 dgram       0      0                0 5264b0a3825786dd                0 5264b0a38257b045
# 5264b0a38257b045 dgram       0      0                0 5264b0a3825786dd                0 5264b0a387c23b8d
# 5264b0a387c23b8d dgram       0      0                0 5264b0a3825786dd                0 5264b0a387c23ac5
# 5264b0a387c23ac5 dgram       0      0                0 5264b0a3825786dd                0 5264b0a387c239fd
# 5264b0a387c239fd dgram       0      0                0 5264b0a3825786dd                0 5264b0a387c23935
# 5264b0a387c23935 dgram       0      0                0 5264b0a3825786dd                0 5264b0a387c264f5
# 5264b0a387c264f5 dgram       0      0                0 5264b0a3825786dd                0 5264b0a387c2386d
# 5264b0a387c2386d dgram       0      0                0 5264b0a3825786dd                0 5264b0a387c25d25
# 5264b0a387c25d25 dgram       0      0                0 5264b0a3825786dd                0 5264b0a387c25c5d
# 5264b0a387c25c5d dgram       0      0                0 5264b0a3825786dd                0 5264b0a387c25b95
# 5264b0a387c25b95 dgram       0      0                0 5264b0a3825786dd                0 5264b0a387c25acd
# 5264b0a387c25acd dgram       0      0                0 5264b0a3825786dd                0 5264b0a387c25a05
# 5264b0a387c25a05 dgram       0      0                0 5264b0a3825786dd                0 5264b0a38257aa05
# 5264b0a38257aa05 dgram       0      0                0 5264b0a3825786dd                0 5264b0a387c23615
# 5264b0a387c23615 dgram       0      0                0 5264b0a3825786dd                0 5264b0a382578615
# 5264b0a382578615 dgram       0      0                0 5264b0a3825786dd                0 5264b0a38257b42d
# 5264b0a38257b42d dgram       0      0                0 5264b0a3825786dd                0 5264b0a38257b365
# 5264b0a38257b365 dgram       0      0                0 5264b0a3825786dd                0 5264b0a38257b29d
# 5264b0a38257b29d dgram       0      0                0 5264b0a3825786dd                0 5264b0a38257af7d
# 5264b0a38257b1d5 dgram       0      0                0 5264b0a38257b10d 5264b0a38257b10d                0
# 5264b0a38257b10d dgram       0      0                0 5264b0a38257b1d5 5264b0a38257b1d5                0
# 5264b0a38257af7d dgram       0      0                0 5264b0a3825786dd                0 5264b0a38257aeb5
# 5264b0a38257aeb5 dgram       0      0                0 5264b0a3825786dd                0 5264b0a38257aded
# 5264b0a38257aded dgram       0      0                0 5264b0a3825786dd                0 5264b0a38257ad25
# 5264b0a38257ad25 dgram       0      0                0 5264b0a3825786dd                0 5264b0a38257ac5d
# 5264b0a38257ac5d dgram       0      0                0 5264b0a3825786dd                0 5264b0a38257a875
# 5264b0a38257ab95 dgram       0      0                0 5264b0a38257aacd 5264b0a38257aacd                0
# 5264b0a38257aacd dgram       0      0                0 5264b0a38257ab95 5264b0a38257ab95                0
# 5264b0a38257a875 dgram       0      0                0 5264b0a3825786dd                0 5264b0a38257a7ad
# 5264b0a38257a7ad dgram       0      0                0 5264b0a3825786dd                0 5264b0a38257a6e5
# 5264b0a38257a6e5 dgram       0      0                0 5264b0a3825786dd                0 5264b0a38257a61d
# 5264b0a38257a61d dgram       0      0                0 5264b0a3825786dd                0 5264b0a38257a2fd
# 5264b0a38257a2fd dgram       0      0                0 5264b0a3825786dd                0 5264b0a38257a48d
# 5264b0a38257a48d dgram       0      0                0 5264b0a3825786dd                0 5264b0a38257a235
# 5264b0a38257a235 dgram       0      0                0 5264b0a3825786dd                0 5264b0a38257a16d
# 5264b0a38257a16d dgram       0      0                0 5264b0a3825786dd                0 5264b0a38257a0a5
# 5264b0a38257a0a5 dgram       0      0                0 5264b0a3825786dd                0 5264b0a382579cbd
# 5264b0a382579fdd dgram       0      0                0 5264b0a382579f15 5264b0a382579f15                0
# 5264b0a382579f15 dgram       0      0                0 5264b0a382579fdd 5264b0a382579fdd                0
# 5264b0a382579e4d dgram       0      0                0 5264b0a382579d85 5264b0a382579d85                0
# 5264b0a382579d85 dgram       0      0                0 5264b0a382579e4d 5264b0a382579e4d                0
# 5264b0a382579cbd dgram       0      0                0 5264b0a3825786dd                0 5264b0a3825798d5
# 5264b0a382579bf5 dgram       0      0                0 5264b0a382579b2d 5264b0a382579b2d                0
# 5264b0a382579b2d dgram       0      0                0 5264b0a382579bf5 5264b0a382579bf5                0
# 5264b0a3825798d5 dgram       0      0                0 5264b0a3825786dd                0 5264b0a38257980d
# 5264b0a38257980d dgram       0      0                0 5264b0a3825786dd                0 5264b0a38257967d
# 5264b0a38257967d dgram       0      0                0 5264b0a3825786dd                0 5264b0a3825787a5
# 5264b0a3825795b5 dgram       0      0                0 5264b0a3825794ed 5264b0a3825794ed                0
# 5264b0a3825794ed dgram       0      0                0 5264b0a3825795b5 5264b0a3825795b5                0
# 5264b0a3825787a5 dgram       0      0                0 5264b0a3825786dd                0                0
# 5264b0a3825786dd dgram       0      0 5264b0a382572e15                0 5264b0a3969d8105                0 /private//var/run/syslog
# Registered kernel control modules
# id       flags    pcbcount rcvbuf   sndbuf   name 
#        1        9        0   131072   131072 com.apple.flow-divert 
#        2        1       12    65536    65536 com.apple.net.netagent 
#        3        9        0   524288   524288 com.apple.content-filter 
#        4       29        2   524288   524288 com.apple.net.utun_control 
#        5       21        0    65536    65536 com.apple.net.ipsec_control 
#        6        0       21     8192     2048 com.apple.netsrc 
#        7       18        3     8192     2048 com.apple.network.statistics 
#        8        5        0     8192    32768 com.apple.network.tcp_ccdebug 
#        9        1        0     8192     2048 com.apple.network.advisory 
#        a        1        1    16384     2048 com.apple.nke.sockwall 
#        b        0        0     8192     8192 com.apple.fileutil.kext.stateful.ctl 
#        c        0        0     8192     2048 com.apple.fileutil.kext.stateless.ctl 
# > None
# **********************
# ifconfig
# lo0: flags=8049<UP,LOOPBACK,RUNNING,MULTICAST> mtu 16384
#         options=1203<RXCSUM,TXCSUM,TXSTATUS,SW_TIMESTAMP>
#         inet 127.0.0.1 netmask 0xff000000 
#         inet6 ::1 prefixlen 128 
#         inet6 fe80::1%lo0 prefixlen 64 scopeid 0x1 
#         nd6 options=201<PERFORMNUD,DAD>
# gif0: flags=8010<POINTOPOINT,MULTICAST> mtu 1280
# stf0: flags=0<> mtu 1280
# XHC20: flags=0<> mtu 0
# utun0: flags=8051<UP,POINTOPOINT,RUNNING,MULTICAST> mtu 1380
#         inet6 fe80::5252:dbe:6a2f:3513%utun0 prefixlen 64 scopeid 0x5 
#         nd6 options=201<PERFORMNUD,DAD>
# utun1: flags=8051<UP,POINTOPOINT,RUNNING,MULTICAST> mtu 2000
#         inet6 fe80::6377:ae36:1ccb:2c7d%utun1 prefixlen 64 scopeid 0x6 
#         nd6 options=201<PERFORMNUD,DAD>
# en2: flags=8863<UP,BROADCAST,SMART,RUNNING,SIMPLEX,MULTICAST> mtu 1500
#         options=400<CHANNEL_IO>
#         ether 2e:08:64:f1:52:bf 
#         inet6 fe80::8c8:de31:3987:fc73%en2 prefixlen 64 secured scopeid 0x8 
#         inet 192.168.245.156 netmask 0xffffff00 broadcast 192.168.245.255
#         nd6 options=201<PERFORMNUD,DAD>
#         media: autoselect
#         status: active
# > None
# **********************
# dig www.google.com

# ; <<>> DiG 9.10.6 <<>> www.google.com
# ;; global options: +cmd
# ;; Got answer:
# ;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 6867
# ;; flags: qr rd ra ad; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 0

# ;; QUESTION SECTION:
# ;www.google.com.                        IN      A

# ;; ANSWER SECTION:
# www.google.com.         153     IN      A       142.250.77.100

# ;; Query time: 3 msec
# ;; SERVER: 192.168.245.35#53(192.168.245.35)
# ;; WHEN: Fri Sep 17 14:51:46 IST 2021
# ;; MSG SIZE  rcvd: 48

# > None
# **********************
# nslookup www.google.com
# Server:         192.168.245.35
# Address:        192.168.245.35#53

# Non-authoritative answer:
# Name:   www.google.com
# Address: 142.250.77.100

# > None
# **********************
# whois www.google.com
# % IANA WHOIS server
# % for more information on IANA, visit http://www.iana.org
# % This query returned 1 object

# refer:        whois.verisign-grs.com

# domain:       COM

# organisation: VeriSign Global Registry Services
# address:      12061 Bluemont Way
# address:      Reston Virginia 20190
# address:      United States

# contact:      administrative
# name:         Registry Customer Service
# organisation: VeriSign Global Registry Services
# address:      12061 Bluemont Way
# address:      Reston Virginia 20190
# address:      United States
# phone:        +1 703 925-6999
# fax-no:       +1 703 948 3978
# e-mail:       info@verisign-grs.com

# contact:      technical
# name:         Registry Customer Service
# organisation: VeriSign Global Registry Services
# address:      12061 Bluemont Way
# address:      Reston Virginia 20190
# address:      United States
# phone:        +1 703 925-6999
# fax-no:       +1 703 948 3978
# e-mail:       info@verisign-grs.com

# nserver:      A.GTLD-SERVERS.NET 192.5.6.30 2001:503:a83e:0:0:0:2:30
# nserver:      B.GTLD-SERVERS.NET 192.33.14.30 2001:503:231d:0:0:0:2:30
# nserver:      C.GTLD-SERVERS.NET 192.26.92.30 2001:503:83eb:0:0:0:0:30
# nserver:      D.GTLD-SERVERS.NET 192.31.80.30 2001:500:856e:0:0:0:0:30
# nserver:      E.GTLD-SERVERS.NET 192.12.94.30 2001:502:1ca1:0:0:0:0:30
# nserver:      F.GTLD-SERVERS.NET 192.35.51.30 2001:503:d414:0:0:0:0:30
# nserver:      G.GTLD-SERVERS.NET 192.42.93.30 2001:503:eea3:0:0:0:0:30
# nserver:      H.GTLD-SERVERS.NET 192.54.112.30 2001:502:8cc:0:0:0:0:30
# nserver:      I.GTLD-SERVERS.NET 192.43.172.30 2001:503:39c1:0:0:0:0:30
# nserver:      J.GTLD-SERVERS.NET 192.48.79.30 2001:502:7094:0:0:0:0:30
# nserver:      K.GTLD-SERVERS.NET 192.52.178.30 2001:503:d2d:0:0:0:0:30
# nserver:      L.GTLD-SERVERS.NET 192.41.162.30 2001:500:d937:0:0:0:0:30
# nserver:      M.GTLD-SERVERS.NET 192.55.83.30 2001:501:b1f9:0:0:0:0:30
# ds-rdata:     30909 8 2 E2D3C916F6DEEAC73294E8268FB5885044A833FC5459588F4A9184CFC41A5766

# whois:        whois.verisign-grs.com

# status:       ACTIVE
# remarks:      Registration information: http://www.verisigninc.com

# created:      1985-01-01
# changed:      2017-10-05
# source:       IANA

# # whois.verisign-grs.com

# No match for domain "WWW.GOOGLE.COM".
# >>> Last update of whois database: 2021-09-17T09:21:39Z <<<

# > None