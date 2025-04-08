# LED Domino

4개의 LED가 도미노처럼 순서대로 켜졌다 꺼지는 효과를 구현

- **유튜브:https://youtu.be/L6J4AVwR3FE?si=RFgH2et6i0DdTtqx**

## 하드웨어 요구 사항

- **Raspberry Pi 5**
- **LED 4개**
- **220Ω 저항 4개** (각 LED에 1개씩 사용)
- 브레드보드 및 점퍼 와이어

## 회로 구성 및 핀 맵

![image](https://github.com/user-attachments/assets/482a8f0e-7e8f-45b2-ba1b-fe3c4738c9b1)
![image](https://github.com/user-attachments/assets/5dac8f83-b9c0-4d1b-badf-ab516a2d72cc)


- **핀 맵:**
  - **LED1 :** GPIO 17  
  - **LED2 :** GPIO 27  
  - **LED3 :** GPIO 22  
  - **LED4 :** GPIO 5

**회로 연결 방법:**
1. 각 LED의 **양극**에 220Ω 저항을 연결합니다.
2. 각 저항의 반대쪽을 Raspberry Pi의 해당 GPIO 핀(위의 핀맵 참조)에 연결합니다.
3. 각 LED의 **음극**은 모두 공통으로 Raspberry Pi의 GND에 연결합니다.
