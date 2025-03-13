# balance : 통장에 들어있는 기본금액을 담는 변수
# 1.입금, 2.출금, 3.영수증 보기, 4.종료
balance = 3000

while True:
    num = input("원하는 기능을 입력해주세요.(1.입금, 2.출금, 3.영수증 보기, 4.종료")

    if num == "1":
        deposit_amount = input("입금할 금액을 입력해주세요. : ")
        if deposit_amount.isdigit() and int(deposit_amount) > 0 :
            balance += int(deposit_amount)
            print(f'{deposit_amount}원 입금되었습니다. 총 금액은{balance}원 입니다.')
        
        else:
            print("정신차리고, 제대로 숫자로 입금액을 눌러!!")
    if num == "2":
        withdraw_amount = input("출금할 금액을 입력해주세요. : ")
        if withdraw_amount.isdigit() and int(deposit_amount) > 0 :
            withdraw_amount = min(balance, int(withdraw_amount))
            balance -= withdraw_amount
            print(f'고객님이 출금한 금액은{withdraw_amount}원 이고, 현재잔액은 {balance}원 입니다.')
        else:
            print("정신차리고, 제대로 숫자로 입금액을 눌러!!")
    if num == "3":
        print("영수증 보기 입니다.")
    if num == "4":
        print("종료 합니다.")

        break
