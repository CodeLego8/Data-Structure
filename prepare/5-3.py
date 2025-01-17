try:
    age = int(input("나이를 입력"))
except:
    print("입력이 정확하지 않습니다")   
else:
    if age <= 18:
        print("미성년자는 출입금지 입니다. ")
    else:
        print("환영합니다.")
