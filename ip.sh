#!/bin/bash

url="http://ipinfo.io/ip"

ip=$(curl -sS $url)

#echo "$ip" > /home/pi/Desktop/myIpAdress/ipReel.txt

file="/home/pi/Desktop/myIpAdress/SendIp/ipReel.txt"

while IFS= read line
do
	if [ $line != $ip ]
	then
	echo "$ip" > /home/pi/Desktop/myIpAdress/SendIp/ipReel.txt
	python3 /home/pi/Desktop/myIpAdress/SendIp/ipAddressSend.py
	fi
done <"$file"

