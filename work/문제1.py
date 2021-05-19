import time
print("<<최현우의 숫자 추출 연산>>\n")
num1 = int(input("▣ 네자릿수 정수 => "))
th = int(num1/1000)
hu = int(num1%1000/100)
te = int(num1%1000%100/10)
on = int(num1%1000%100%10)
sum1 = th+hu+te+on
print("\n===== 출력 결과 =====")
print(f"천의 자리: {th}\n백의 자리: {hu}")
print(f"십의 자리: {te}\n일의 자리: {on}")
print(f"{th} + {hu} + {te} + {on} = {sum1}",end="")
time.sleep(10)
