# Yeu cau cai dat Module Test-OpenPort
# install-module Test-OpenPort

$test=Test-OpenPort 210.2.120.232 -Port 80,8080,8081,8084,8090,8091,8092 | sort-object Status | Where-Object {($_.Status -match 'False')} | Out-File -FilePath D:\test_connect.txt
$content=get-content -Path D:\test_connect.txt -Raw

#Check file. Neu ko co noi dung trong File -> Ket qua True -> Thoat Shell
if ($content -eq $Null)
{
    exit 0
}

#Gui Alert toi quan tri neu co Port False
else 
{
    #Send-MailMessage -from nghialv@thaison.vn -to nghialv@thaison.vn -Subject "Warning Port!! -> HAPROXY HCM" -Body $content -SmtpServer mail1.thaison.vn -Port 25 -Credential nghialv@thaison.vn
    
    $api = '5542561908:AAGGlo2WYnvC_9ONjprPUponitwSEd1pvck'
    $chatid = '-606599992'
    #$URL = "https://api.telegram.org/bot$api/sendMessage"
    $msg = "Port Warning!! -> HAPROXY HCM $content"
    Invoke-RestMethod -Uri ('https://api.telegram.org/bot{0}/sendMessage?chat_id={1}&text={2}' -f $api, $chatid, $msg)
}