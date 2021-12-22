import RPi.GPIO as GPIO

in1 = 16
in2 = 26
in3 = 20
in4 = 21
en_r = 13
en_l = 12

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
pins = [in1, in2, in3, in4, en_r, en_l]
GPIO.setup(pins, GPIO.OUT)

pwm_r = GPIO.PWM(en_r, 50)
pwm_r.start(0)
pwm_l = GPIO.PWM(en_l, 50)
pwm_l.start(0)


def drive(speed_r, speed_l):
    if speed_r > 0:
        GPIO.output(in1, GPIO.HIGH)
        GPIO.output(in2, GPIO.LOW)
    else:
        GPIO.output(in1, GPIO.LOW)
        GPIO.output(in2, GPIO.HIGH)
    if speed_l > 0:
        GPIO.output(in3, GPIO.HIGH)
        GPIO.output(in4, GPIO.LOW)
    else:
        GPIO.output(in3, GPIO.LOW)
        GPIO.output(in4, GPIO.HIGH)
    pwm_r.ChangeDutyCycle(abs(speed_r))
    pwm_l.ChangeDutyCycle(abs(speed_l))


if __name__ == '__main__':
    while True:
        try:
            r = int(input('r: '))
            l = int(input('l: '))
            drive(r, l)
        except KeyboardInterrupt:
            pwm_r.stop()
            pwm_l.stop()
            GPIO.cleanup()
            break
