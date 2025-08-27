
nums = []

def ip():
    n = int(input("소수 판별할 숫자 범위의 최소값을 입력해 주세요: "))
    m = int(input("소수 판별할 숫자 범위의 최대값을 입력해 주세요: "))
    if n >= m:
        print('이럼 안되여')
        ip()
    else:
        for i in range(m - n):
            num = i + n
            nums.append(num)
            print(num)
            if n + i == m - 1 :
                print(m)
                nums.append(m)
                print(nums)
                
                break

ip()
