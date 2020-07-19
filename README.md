# Learn_Reel_Ip_Send_Phone
Statik olmayan ıpler İçin anlık çalışçan script ile ip öğrenme

İlk önce https://notify-bot.line.me/en/ adresinden log in olunur.
Profilden My Page alanından Generate Access Token ile Token üretilir.
Oluşturulan bu tokeni kaybetmemek üzere not alınmalıdır.
Daha sonra .py dosyasında token yerine bu üretilen token yazılmalıdır.

Bütün oluşturulan dosyalar Raspberry Pi'nin /home/Desktop/myIpAdress/SendIp dizini altına oluşturulmuştur.

Ip Adresinin değişip değişmediği .sh dosyasında kontrol edilmiştir.

crontab -e ile zamanlayıcı şu şekildedir.
* * * * * cd /home/pi/Desktop/myIpAdress/SendIp && sh ip.sh

satırı eklenerek düzenli olarak kontrol edilmesi sağlanmış olur.
