# จงเขียนคำสั่งเพื่อแสดงต้น christmas โดยใช้คำสั่ง for โปรแกรมสามารถกำหนดความสูงของต้น christmas ได้
for i in range(20):  # loop ถาม
    height = int(input("Enter your height :"))
    for x in range(height, 0, -1):
        print((x * " " + (height - x) * "*") +
              "*" + ((height - x) * "*") + (x * " "))
