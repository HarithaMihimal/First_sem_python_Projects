a = int(input(""))

if a <= 30:
    print(2.5 * a + 30)
elif 30 < a <= 60:
    print(2.5 * 30 + 4.85 * (a - 30) + 60)
elif 60 < a <= 90:
    print(7.85 * 60 + 10.00 * (a - 60) + 90)
elif 90 < a <= 120:
    print(7.85 * 60 + 10.00 * 30 + 27.75 * (a - 90) + 480)
elif 120 < a <= 180:
    print(7.85 * 60 + 10.00 * 30 + 27.75 * 30 + 32.00 * (a - 120) + 480)
elif a > 180:
    print(7.85 * 60 + 10.00 * 30 + 27.75 * 30 + 32.00 * 60 + 45.00 * (a - 180) + 540)
