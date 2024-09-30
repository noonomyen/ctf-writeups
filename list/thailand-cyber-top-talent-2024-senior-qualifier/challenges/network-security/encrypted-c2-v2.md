# Encrypted C2 v2

![1.png](../../images/network-security/encrypted-c2-v2/1.png)

[open_netsec3.pcapng](../../files/open_netsec3.pcapng)

## Solving

![2.png](../../images/network-security/encrypted-c2-v2/2.png)

export ไว้รอเลย

![3.png](../../images/network-security/encrypted-c2-v2/3.png)

จากที่ดูคือเราต้องเอา maps ไปใช้ในการถอดรหัส จะได้จาก handshake และ ข้อความจะเกิดขึ้นตอน callback

![4.png](../../images/network-security/encrypted-c2-v2/4.png)

เราเลยเขียน code loop ถอดมันทุกแบบไปเลย

## Result

![5.png](../../images/network-security/encrypted-c2-v2/5.png)

it work
