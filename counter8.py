import RPi.GPIO as GPIO
import time

LED_PINS = [17, 27, 22, 5]

# GPIO 모드를 BCM으로 설정
GPIO.setmode(GPIO.BCM)

# 각 핀을 출력 모드로 설정하고 초기 상태는 LOW(꺼짐)로 지정
for pin in LED_PINS:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)

try:
    while True:
        # 1부터 8까지 순차적으로 표시
        for number in range(1, 9):
            # 각 LED에 대해 number의 이진수에 해당하는 비트 상태로 LED 켜기
            for bit in range(4):  # 비트 0 ~ 3
                if number & (1 << bit):
                    GPIO.output(LED_PINS[bit], GPIO.HIGH)
                else:
                    GPIO.output(LED_PINS[bit], GPIO.LOW)
            time.sleep(1)  # 해당 숫자 상태 1초 유지
        
        # 모든 LED를 꺼준 후 다음 순환
        for pin in LED_PINS:
            GPIO.output(pin, GPIO.LOW)
        time.sleep(1)

except KeyboardInterrupt:
    # Ctrl+C 누를 경우 GPIO 자원 정리
    GPIO.cleanup()