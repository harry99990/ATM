# balance : 통장에 들어있는 기본금액을 담는 변수
# 1.입금, 2.출금, 3.영수증 보기, 4.종료
balance = 3000

while True:
    num = input("원하는 기능을 입력해주세요.(1.입금, 2.출금, 3.영수증 보기, 4.종료")

    if num == "1":
        print("입금 기능입니다.")
    if num == "2":
        print("출금 기능입니다.")
    if num == "3":
        print("영수증 보기 입니다.")
    if num == "4":
        print("종료 합니다.")

        break