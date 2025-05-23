# Raspberry Pi 버튼으로 LED 제어_2

Raspberry Pi에서 버튼을 **누를 때마다** 4개의 LED 상태를 **반전(Toggle)** 시키는 기능

`gpiozero` 라이브러리를 사용

**유튜브 : https://youtu.be/AFLB0szCg6Y?si=QVU7Ix09lH6dCgoK**

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

- 버튼을 **누를 때마다**, 4개의 LED 상태가 **반전**됨  
  (켜져 있으면 꺼지고, 꺼져 있으면 켜짐)
- LED 4개를 **동시에 토글**
