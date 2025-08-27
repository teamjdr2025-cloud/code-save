
nums = {}
def ip():
    n = int(input("소수 판별할 숫자 범위의 최소값을 입력해 주세요: "))
    m = int(input("소수 판별할 숫자 범위의 최대값을 입력해 주세요: "))
    if n >= m:
        print('이럼 안되여')
        ip()
    else:
        for i in range(2, m + 1):
            if i < n:
                    continue
            for o in range(2, m + 1):
                if i % o == 0:
                    if i != o:
                        nums[i] = '합성수'
                        break
                    else:
                        continue
                else:
                    nums[i] = '소수'
                    continue
            print(i,'는 ',nums[i],'이다')

ip()
