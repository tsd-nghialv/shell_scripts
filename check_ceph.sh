#!/bin/bash
status="HEALTH_OK"
command=$(ceph -s | grep health)
if [[ -z $status  ]]; then
token="5520385337:AAGc0Xtsw1xYVYZ0rTzpyrDx-AeVXyf6rh4"
chatid="-711836222"
msg=$(echo "CEPH WARNING!")
curl -X POST "https://api.telegram.org/bot$token/sendMessage" -d chat_id=$chatid -d text="$msg"
else
	exit 0;
fi
