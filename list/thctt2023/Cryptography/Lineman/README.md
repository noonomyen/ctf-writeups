# Lineman

```
.
└── Lineman.png
```

เราได้รูปๆหนึ่งมา ไม่รู้ว่ามันคืออะไร แต่รู้สึกคุ้นๆ เหมือนเคยเห็นที่ไหนมาก่อน

![1.png](./images/1.png)

อย่างแรกที่จะทำคือ strings เช็คดูว่า มีอะไรซ่อนไว้หรือเปล่า
```
strings Lineman.png
```
![2.png](./images/2.png)

ยังไม่เจออะไรที่ดูแปลกๆ งั้นลอง exiftool
```
exiftool Lineman.png
```
![3.png](./images/3.png)

ก็ยังไม่เจอ งั้นลอง xxd
```
xxd Lineman.png
```
![4.png](./images/4.png)

ก็ยังไม่เจอ งั้นลอง binwalk
```
binwalk Lineman.png
```
![5.png](./images/5.png)

ก็ดูปกติหนิ  จาร้องแล้วนะ  😭😭😭😭 งั้นลอง `Google len` เผื่อจะได้ข้อมูลอะไรเพิ่มเติม

![6.png](./images/6.png)

![7.png](./images/7.png)

เลื่อนๆ ไป เหมือนจะเจอรูปที่คล้ายๆ กัน

![8.png](./images/8.png)

ลองกด `Search image with Google`

![9.png](./images/9.png)

พอเลื่อนๆ ไป เราก็จะเจอคำประมาณ `pigpen`, `Pigpen Cipher`

![12.png](./images/12.png)

Hm มันคืออะไร! พอเราลองไป Search ดู

![10.png](./images/10.png)

เหมือนจะมาถูกทาง งั้นลอง Search `pigpen cipher online decoder` เราก็จะเจอเว็บ สำหรับ decode แล้วเราลอง กดตามภาพที่ได้

![11.png](./images/11.png)

นี้มันใช่ ใช่แน่ๆ แต่ Flags จะอยู่ในรูป `CTT23{}` เพราะงั้น Flags ก็จะเป็น `CTT23{ILOVENCSA}` ง่ายใช่ไหมละ 😏😏😏