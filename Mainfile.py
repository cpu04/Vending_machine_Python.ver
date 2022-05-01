def apple(apcoin):
    app = 0
    if apcoin == 500:
        print("사과주스가 나왔습니다. 안녕히 가세요")
    elif apcoin > 500:
        print("사과주스가 나왔습니다.")
        app = apcoin - 500
        print("거스름돈은 %d원 입니다." % app)
    else:
        print("잔액이 부족합니다.")    
def orange(orcoin):
    ora = 0
    if orcoin == 700:
        print("오렌지 주스가 나왔습니다. 안녕히 가세요")
    elif orcoin > 700:
        print("오렌지 주스가 나왔습니다.")
        ora = orcoin - 700
        print("거스름돈은 %d원 입니다." % ora)
    else:
        print("잔액이 부족합니다.")
def grape(grcoin):
    grc = 0
    if grcoin == 1200:
        print("포도주스가 나왔습니다. 안녕히 가세요")
    elif grcoin > 1200:
        print("포도주스가 나왔습니다.")
        grc = grcoin - 1200
        print("거스름돈은 %d원 입니다." % grc)
    else:
        print("잔액이 부족합니다.")


while(1):
    coin = int(input("금액을 넣어주세요: "))
    print("1. 사과주스 : 500원")
    print("2. 오렌지 주스 : 700원")
    print("3. 포도 주스 : 1200원")
    ans = int(input("음료를 선택해주세요: "))
    if ans == 1:
        apple(coin)
    elif ans == 2:
        orange(coin)
    elif ans == 3:
        grape(coin)
    else:
        print("잘못된 값입니다.")   