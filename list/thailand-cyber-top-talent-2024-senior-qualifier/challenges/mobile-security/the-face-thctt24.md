# The Face THCTT24

คำใบ้คือ ใครหายไป

[Mobile.zip](../../files/Mobile.zip)

## Solving

`com.example.thefacethctt24.MainActivity`

![1.png](../../images/mobile-security/the-face-thctt24/1.png)

เราเริ่มจากจุดที่ใช้ random ค่าเพื่อเลือกรูปไปแสดง แล้วเราพบว่า 32 หายไปจาก array

แล้วรูปที่ 32 อยู่ที่ไหน ?

เพื่อความมักง่ายเราจะใช้ binwalk แล้ว search ชื่อไฟล์

```sh
binwalk -e TheFaceTHCTT24.apk
find . -name "*32*"
```

![2.png](../../images/mobile-security/the-face-thctt24/2.png)

![3.png](../../images/mobile-security/the-face-thctt24/3.png)

โดนเกรียนจริง

## Result

GIMP

![4.png](../../images/mobile-security/the-face-thctt24/4.png)
