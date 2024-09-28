# Medium

[Mobile2.zip](../../files/Mobile2.zip)

## Solving

![1.png](../../images/mobile-security/medium/1.png)

สำหรับข้อนี้จะพบ flag ได้ที่ assets ของ apk

เอาไปแปลงใน Cyber Chef ด้วย `From Hex`

## Result

![2.png](../../images/mobile-security/medium/2.png)

### Cheat

```sh
binwalk -e Mobile2.apk && cat $(find . -name flag.txt) | xxd -r -p
```
