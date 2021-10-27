#!/usr/bin/env python
# -*- coding: utf-8 -*-
#! @author : @ruhend (Mudigonda Himansh)


def intro():
    size_of_network = 3
    network = [[0 for i in range(size_of_network)]
               for i in range(size_of_network)]
    for i in range(size_of_network):
        for j in range(size_of_network):
            print("Enter the distance between Node ",
                  i + 1,
                  "Node ",
                  j + 1,
                  ": ",
                  end='')
            network[i][j] = int(input())

    return (network)


def dvr(network):
    for i in range(network):
        for j in range(network[0]):
            print(netowrk[i][j])
    print(network[0][2])


def main():
    network = intro()
    dvr(network)


main()
