#!/bin/bash
disk=$(df -h / | egrep -v "Size|Used" | sed -e 's/G//g' | awk '{print $2-$3}')
#echo $disk

if [ $disk -le 40 ]; then
 echo -e "Subject: Disk Warning!\nDisk Low is $disk"G"" | sendmail nghialv@thaison.vn
else
 exit 0;
fi
