# LED Binary Counter8

Raspberry Pi의 GPIO 핀을 사용하여 4개의 LED로 1부터 8까지의 숫자를 이진수 형태로 표시
- **유튜브 :https://youtu.be/026rg5-pR_U?si=MwPw7eyBq3tuOEe3**

## 프로젝트 개요

- **목적:**  
  4개의 LED를 사용해 1부터 8까지의 숫자를 이진수 형태로 순차적으로 표현  
- **구현 방식:**  
  Python 및 RPi.GPIO 라이브러리를 사용하여 LED를 제어

## 하드웨어 요구 사항

- Raspberry Pi 5
- LED 4개
- 220Ω 저항 4개 (LED 보호용)
- 브레드보드 및 점퍼 와이어

## 회로 구성 및 핀 맵

![image](https://github.com/user-attachments/assets/482a8f0e-7e8f-45b2-ba1b-fe3c4738c9b1)
![image](https://github.com/user-attachments/assets/5dac8f83-b9c0-4d1b-badf-ab516a2d72cc)


**핀 맵:**  
- LED1 (비트 0, 2^0): GPIO 17  
- LED2 (비트 1, 2^1): GPIO 27  
- LED3 (비트 2, 2^2): GPIO 22  
- LED4 (비트 3, 2^3): GPIO 5

**연결 방법:**
1. 각 LED의 **양극**에는 220Ω 저항을 연결합니다.
2. 각 저항의 다른 쪽 끝은 Raspberry Pi의 해당 GPIO 핀에 연결합니다.
3. LED의 **음극**은 모두 공통 GND에 연결합니다.
