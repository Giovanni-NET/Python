import math
import os
import time
from turtle import *

def hearta(k):
    return 15 * math.sin(k) ** 3

def heartb(k):
    return 12 * math.cos(k) - 5 * math.cos(2 * k) - 2 * math.cos(3 * k) - math.cos(4 * k)

# تشغيل الأغنية
try:
    os.startfile("lahbaly.mp3")  # تأكد إن الأغنية بنفس الاسم وفي نفس الفولدر
except:
    print("⚠️ مش لاقي الأغنية")

speed(0)
bgcolor("black")
color("red")

# رسم القلب بسرعة
for i in range(6000):
    x = hearta(i) * 20
    y = heartb(i) * 20
    goto(x, y)
    for j in range(5):
        color("pink")
        goto(x, y)

# كتابة التاريخ في نص القلب
penup()
goto(0, 0)
color("white")
write(time.strftime("%d/%m/%Y"), align="center", font=("Arial", 24, "bold"))

# يفضل مفتوح دقيقتين
time.sleep(120)

done()
