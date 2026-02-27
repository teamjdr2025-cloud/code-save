import time

def loading():
    time.sleep(2)
    print('loading')
    time.sleep(1)
    print('.')
    time.sleep(1)
    print('.')
    time.sleep(1)
    print('.')

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
            print(i,'는(은) ',nums[i],'이다')
    loading()
    rechose()

result = ''

def moduler(p,mod):
    r = p % mod
    if r > mod//2:
        r -= mod
    return r

def factorial(f):
    a= 1
    for i in range(f):
        a = a * (i + 1)
    return a

def willsen():
    a = int(input('소수 판별할 값을 입력해 주세요 \n 답:'))
    a_f = factorial(a - 1)
    if moduler(a_f, a) == -1:
        result = '소수'
    else:
        result = '합성수'
    print(a,'는(은)', result, '이다')
    loading()
    rechose()

def chose():
    cho = int(input('[소수 판별 프로그램]소수 판별할 방법을 정해주세요 \n 1 : 윌슨의 정리 \n 2 : 에라토스테네스의 체 \n 답:'))
    if cho == 2:
        print('에라토스테네스의 체 실행')
        ip()
    elif cho == 1:
        print('윌슨의 정리 실행')
        willsen()
    else: 
        print('이럼 안됨')
        chose()

def rechose():
    recho = int(input('소수 판별법을 다시 실행 하시겠습니까? \n 1 : 예 \n 2 : 아니요 \n 답:'))
    if recho == 1:
        chose()
    if recho == 2:
        print('ㅉㅉ')

chose()