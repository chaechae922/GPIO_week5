# Raspberry Pi 버튼으로 LED 제어_1

Raspberry Pi에서 버튼을 눌렀을 때 4개의 LED를 **켜고**, 버튼에서 손을 떼면 **끄는** 기능

`gpiozero` 라이브러리를 사용하여 작성

**유튜브 : https://youtu.be/vZTQ9si_d5U?si=wV0QKB2ghcMDlWxJ**

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

- 버튼을 누르면 모든 LED가 **켜짐**
- 버튼에서 손을 떼면 모든 LED가 **꺼짐**
- 총 4개의 LED를 동시에 제어
