#!/bin/bash
cpu=$(cat /proc/loadavg | awk '{print $1}')
host=$(hostname -s)
token="1242479340:AAGczsaOjF4I8qYaun2R2rQmwjt0gEdboSw"
chatid="-414590858"
msg_hig=$(echo -e "Warning -> CPU High\nCurrent CPU is $cpu% on $host")
msg_ok=$(echo -e "OK -> CPU Good\nCurrent CPU is $cpu% on $host")

if [[ ${cpu//\.*} -ge 80 ]]; then

curl -X POST "https://api.telegram.org/bot$token/sendMessage" -d chat_id=$chatid -d text="$msg_hig"

# echo -e "Subject: Warning -> CPU High\nCurrent CPU is $cpu% on $host"| sendmail nghialv@thaison.vn

else

curl -X POST "https://api.telegram.org/bot$token/sendMessage" -d chat_id=$chatid -d text="$msg_ok"

# echo -e "Subject: OK -> CPU Good\nCurrent CPU is $cpu% on $host" | sendmail nghialv@thaison.vn

fi
