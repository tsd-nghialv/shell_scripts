#!/bin/bash
dock=`docker ps | awk '{if ($7!="Up" && $7!="Exited") print $NF}'`
if [[ -z $dock ]]; then
        exit 0;
else
#url="https://api.telegram.org/bot"
token="5520385337:AAGc0Xtsw1xYVYZ0rTzpyrDx-AeVXyf6rh4"
chatid="-711836222"
msg=$(echo -e "CRITICAL: `hostname -s` - Service Down!!\n$dock")

curl -X POST "https://api.telegram.org/bot$token/sendMessage" -d chat_id=$chatid -d text="$msg"
fi
