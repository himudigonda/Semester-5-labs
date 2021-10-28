#!/usr/bin/env python3
#! @author: @ruhend(Mudigonda Himansh)
#! Assignment 6
#! Address Block
""" [Question]
1.  Address -> given
    a. What class is it
    b. create n subnets, each with m number of hosts => how many hosts are available still?
    c. create +o subnets, each with m numver of hosts => how many hosts are available now?
        IP Address Class	Default Subnet Mask
        Class A	            255.0.0.0
        Class B	            255.255.0.0
        Class C	            255.255.255.0

        0-127   -> a
        128-... -> b
"""


def _input():
    # n is ipaddress[-1]
    ipaddress = [190, 100, 0, 0]  # 198.169.x.x
    no_of_hosts = 256
    no_of_subnets = 64
    return ipaddress, no_of_hosts, no_of_subnets


def _calc_class_type(ipaddress):
    class_selector = ipaddress[0]
    class_type = ''
    if class_selector in range(0, 127):
        class_type = 'A'
    elif class_selector in range(128, 191):
        class_type = 'B'
    elif class_selector in range(192, 223):
        class_type = 'C'
    elif class_selector in range(224, 239):
        class_type = 'D'
    elif class_selector in range(240, 255):
        class_type = 'E'
    return class_type


def _calc_no_addresses(ipaddress):
    n = ipaddress[-1]
    no_of_address = 2**(32 - n)
    return no_of_address


def Class_Type():
    ipaddress, no_of_hosts, no_of_subnets = _input()
    no_of_address = _calc_no_addresses(ipaddress)
    class_type = _calc_class_type(ipaddress)
    print(class_type)


def Divide_Subnets_Hosts():
    ipaddress, no_of_hosts, no_of_subnets = _input()
    reserved_subnet_addresses = ipaddress[2]
    reserved_host_addresses = ipaddress[3]
    for i in range(reserved_subnet_addresses,
                   reserved_subnet_addresses + no_of_subnets):
        print(ipaddress)
        for j in range(reserved_host_addresses,
                       reserved_host_addresses + no_of_hosts):
            print(
                str(1) + " Customer: " + str(ipaddress[0]) + "." +
                str(ipaddress[1]) + "." + str(i) + "." + str(j))
            #+ "/" + str(ipaddress[-1]))
    ipaddress[2], ipaddress[3] = i, j
    print(ipaddress)


def main():
    Class_Type()
    Divide_Subnets_Hosts()


main()
