# Raspberry Pi 버튼으로 LED 제어_3

Raspberry Pi에서 버튼을 **한 번 누르면**, 4개의 LED가 **1초 간격으로 순서대로 켜졌다가 꺼지는** 기능

`gpiozero`와 `time.sleep()`을 사용

**유튜브 : https://youtu.be/ppoUVxWQJzo?si=3J-W7pOx-Vqt28ka**

---

## 📌 회로 연결

| 구성 요소 | 연결된 GPIO 핀 |
|-----------|----------------|
| LED 1     | GPIO 20        |
| LED 2     | GPIO 16        |
| LED 3     | GPIO 7         |
| LED 4     | GPIO 8         |
| 버튼      | GPIO 25        |

> ✅ 버튼은 **풀업 방식**(기본 High → GND로 연결 시 Low)으로 연결
---

## 💡 기능

- 버튼을 **한 번 누르면**, LED가 **1초 간격으로 순서대로 켜지고 꺼짐**
- 총 4개의 LED가 4초에 걸쳐 하나씩 동작
- 이후 버튼을 다시 누르면 같은 시퀀스가 반복
