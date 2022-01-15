while 1:
    abc = 0

    coin = int(input("금액을 넣어주세요: "))
    print("1. 사과주스 : 500원")
    print("2. 오렌지 주스 : 700원")
    print("3. 포도 주스 : 1200원")
    ans = int(input("음료를 선택해주세요: "))
    if ans == 1:
        if coin == 500:
            print("사과주스가 나왔습니다. 안녕히 가세요")
            continue
        elif coin > 500:
            print("사과주스가 나왔습니다.")
            abc = coin - 500
            print("거스름돈은 %d원 입니다." % abc)
            continue
        else:
            print("잔액이 부족합니다.")
            continue
    elif ans == 2:
        if coin == 700:
            print("오렌지 주스가 나왔습니다. 안녕히 가세요")
            continue
        elif coin > 700:
            print("오렌지 주스가 나왔습니다.")
            abc = coin - 700
            print("거스름돈은 %d원 입니다." % abc)
            continue
        else:
            print("잔액이 부족합니다.")
            continue
    elif ans == 3:
        if coin == 1200:
            print("포도주스가 나왔습니다. 안녕히 가세요")
            continue
        elif coin > 1200:
            print("포도주스가 나왔습니다.")
            abc = coin - 1200
            print("거스름돈은 %d원 입니다." % abc)
            continue
        else:
            print("잔액이 부족합니다.")
            continue
    else:
        print("잘못된 값입니다.")
        continue