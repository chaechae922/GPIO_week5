import RPi.GPIO as GPIO
import time

# 사용할 LED가 연결된 GPIO 핀 번호
LED_PINS = [17, 27, 22, 5]

# GPIO 초기화: BCM 모드로 설정
GPIO.setmode(GPIO.BCM)

# 각 핀을 출력 모드로 설정하고 초기값 LOW로 설정
for pin in LED_PINS:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)

try:
    while True:
        # 각 LED를 순서대로 켜고 잠시 대기한 후 꺼짐
        for pin in LED_PINS:
            GPIO.output(pin, GPIO.HIGH)
            time.sleep(1)  # 0.1초간 LED ON
            GPIO.output(pin, GPIO.LOW)
except KeyboardInterrupt:
    # Ctrl+C 입력 시 안전하게 GPIO 해제
    GPIO.cleanup()