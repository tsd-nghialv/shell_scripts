#!/bin/bash
status="HEALTH_OK"
command=$(ceph -s | grep health)
if [[ -z $status  ]]; then
token="5542561908:AAGGlo2WYnvC_9ONjprPUponitwSEd1pvck"
chatid="-711836222"
msg=$(echo "CEPH WARNING! $command")
curl -X POST "https://api.telegram.org/bot$token/sendMessage" -d chat_id=$chatid -d text="$msg"
else
	exit 0;
fi
