try:
    age = int(input("나이를 입력"))

except:
    print("입력이 정확하지 않습니다")
    while True:
        try:
            age = int(input("나이를 입력"))
        except:
            print("입력이 정확하지 않습니다")
        
    
        else:
            break
        #     # if age <= 18:
        #     #     print("미성년자는 출입금지 입니다.")
        #     #     break
        #     # else:
        #     #     print("환영합니다.")
        #     #     break

else:
    if age <= 18:
        print("미성년자는 출입금지 입니다. ")
    else:
        print("환영합니다.")


# try:
#     a = [1,2]
#     print(a[3])
#     3 / 0
# except ZeroDivisionError as e:
#     print("Infinite")

# except IndexError:
#     print("인덱스 할 수 없음")


