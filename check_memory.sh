#!/bin/bash
mem=$(free -h | grep "Mem" |awk '{print ($3/$2)*100}')
#host=$(hostname -s)
if [[ ${mem//\.*} -ge 80 ]]; then
	echo -e "Subject: Memory Warning!\nMemory Used $mem"%"" | sendmail nghialv@thaison.vn
fi
