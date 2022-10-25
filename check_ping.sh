#!/bin/bash
#check2=$(ping -c 1 172.16.101.10)
#check3=$(ping -c 1 172.16.101.11)

#cat /tmp/servers.list | while read output
#do
ping -c4 210.245.51.189 > /dev/null 2>&1
if [ "$?" != 0 ]; then
# echo -e "Subject: Host Warning\nHost $output Down!" | sendmail nghialv@thaison.vn
token="5520385337:AAGc0Xtsw1xYVYZ0rTzpyrDx-AeVXyf6rh4"
chatid="-711836222"
msg=$(echo "CRITICAL: WAN Down!")
curl -X POST "https://api.telegram.org/bot$token/sendMessage" -d chat_id=$chatid -d text="$msg"
#echo -e "PRVC Alert!: WAN --> DOWN"

else
 exit 0;
fi
#done
