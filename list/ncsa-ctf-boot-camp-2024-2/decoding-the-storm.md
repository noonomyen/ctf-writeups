# Decoding the Storm

Tag: `web` `obfuscate`

เราได้ไฟล์ html โดยเราต้องหา flag ในเว็บนี้

[web1_ctf.zip](./files/web1_ctf.zip)

## Screen

![2-1-1.png](./images/2-1-1.png)

## Solving

![2-1-2.png](./images/2-1-2.png)

เมื่อเราได้เปิดดู html แล้วพบว่ามีจุดหนึ่งใน code พร้อมกับ hit ที่บอกว่าข้อมูลอยู่ในรูปอะไร ซึ่งถ้ามองด้วยตาปล่าวจะรู้ว่ามันคือ code ที่ถูก obfuscate

![2-1-3.png](./images/2-1-3.png)

เราจึงได้แยก javascript ดังกล่าวออกมา

![2-1-4.png](./images/2-1-4.png)

ทำการ deobfuscate

## Result

![2-1-5.png](./images/2-1-5.png)
