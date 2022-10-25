#!/bin/bash
dock=`docker ps |grep nova |awk '{if ($7!="Up" && $7!="Exited") print $NF,$7}'`
if [[ -z $dock ]]; then
	exit 0;
else
echo -e "Subject: Dich vu Nova Not Running\n$dock" | sendmail nghialv@thaison.vn
fi
