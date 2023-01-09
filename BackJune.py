# 입출력과 사칙연산
# 2557 HELLO WORLD
# import sys
# print("Hello World!")


# 1000 A + B
# input_data = input().split(' ')
# A = int(input_data[0])
# B = int(input_data[1])
# print(A / B)


# 10171 고양이
# print("\\    /\\")
# print(" )  ( \')")
# print("(  /  )")
# print(" \\(__)|")


# 10172 개
# print("|\\_/|")
# print("|q p|   /}")
# print("( 0 )\"\"\"\\")
# print("|\"^\"`    |")
# print("||_/=\\\\__|")


# 10869 사칙연산
# input_data = input().split(' ')
# A = int(input_data[0])
# B = int(input_data[1])
# print(A + B)
# print(A - B)
# print(A * B)
# print(A // B)
# print(A % B)


# 10430 나머지
# input_data = input().split(' ')
# A = int(input_data[0])
# B = int(input_data[1])
# C = int(input_data[2])
# print((A+B) % C)
# print(((A % C) + (B % C)) % C)
# print((A*B) % C)
# print(((A % C) * (B % C)) % C)


# 2588 곱셈
# input_data = input().split(' ')
# A = int(input_data[0])
# B = input_data[1]
# print(A*int(B[2]))
# print(A*int(B[1]))
# print(A*int(B[0]))
# print(A*int(B))


# 10926 ??!
# id = input()
# print(id + "??!")


#  조건문
# 1330 두 수 비교하기
# input_data = input().split(' ') #a와b가 공백한칸으로 구분
# a = int(input_data[0])
# b = int(input_data[1])
# if a > b:
#     print(">")
# elif a < b:
#     print("<")
# else:
#     print("==")

# a = int(input()) #a와 b를 나눠서 입력
# b = int(input())
# if a > b:
#     print(">")
# elif a < b:
#     print("<")
# else:
#     print("==")


# 9498 시험성적
# score = int(input())
# if score >= 90:
#     print("A")
# elif score >= 80:
#     print("B")
# elif score >= 70:
#     print("C")
# elif score >= 60:
#     print("D")
# else:
#     print("F")


# 2753 윤년
# year = int(input())
# if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
#     print("1")
# else:
#     print("0")


# 2884 알람시계
# time = input().split(' ')
# H = int(time[0])
# M = int(time[1])
# M -= 45
# if M < 0:
#     M += 60
#     H -= 1
#     if H < 0:
#         H = 23
# print(str(H) + " " + str(M))


# 사분면 고르기
# x = int(input())
# y = int(input())
# if x > 0 and y > 0:
#     print(1)
# elif x < 0 and y > 0:
#     print(2)
# elif x < 0 and y < 0:
#     print(3)
# else:
#     print(4)


# 10817 세수
# input_data = list(map(int, input().split(' ')))
# input_data.sort()
# print(input_data[1])


# 2525 오븐시계
# hour, minute = map(int, input().split(' '))
# cook = int(input())

# hour += cook//60
# minute += cook % 60

# if minute >= 60:
#     hour += 1
#     minute -= 60
# if hour >= 24:
#     hour -= 24

# print(str(hour) + " " + str(minute))


# 2480 주사위 3개
# a, b, c = sorted(map(int, input().split(' ')))
# if a == b == c:
#     print(10000+a*1000)
# elif a == b or b == c or a == c:
#     print(1000+b*100)
# else:
#     print(c*100)


# 반복문
# 2739 구구단
# n = int(input())
# for i in range(1, 10):
#     print("{0} * {1} = {2}".format(n, i, n*i))


# 10950 A+B-3
# T = int(input())
# for i in range(T):
#     a, b = map(int, input().split())
#     print(a+b)


# 8393 합
# sum = 0
# n = int(input())
# for i in range(1, n+1):
#     sum += i
# print(sum)


# 25304 영수증
# sum = 0
# x = int(input())
# n = int(input())
# for i in range(n):
#     a, b = map(int, input().split())
#     sum += a*b
# if x == sum:
#     print("Yes")
# else:
#     print("No")


# 15552 빠른 A + B
# import sys
# T = int(input())
# for i in range(T):
#     a, b = map(int, sys.stdin.readline().rstrip().split(' '))
#     print(a+b)


# 11021 A + B -7
# T = int(input())
# for i in range(1, T+1):
#     a, b = map(int, input().split(' '))
#     print("Case #{0}: {1}".format(i, a+b))


# 11022 A + B -8
# T = int(input())
# for i in range(1, T+1):
#     a, b = map(int, input().split(' '))
#     print("Case #{0}: {1} + {2} = {3}".format(i, a, b, a+b))


# 2438 별 찍기 - 1
# n = int(input())
# for i in range(1, n+1):
#     print("*"*i)


# 2439 별 찍기 - 2
# n = int(input())
# for i in range(1, n+1):
#     print(str("*"*i).rjust(n))


# 10952 A + B -5
# while True:
#     a, b = map(int, input().split())
#     if a == 0 and b == 0:
#         break
#     print(a+b)


# 10951 A + B -4
# while True:  # 무한 반복인데 끝을 정하는 조건이 따로 없을 때
#     try:
#         a, b = map(int, input().split())
#         print(a+b)
#     except:
#         break


# 1110 더하기 사이클_내 방법  ---> 정답인데 시간초과 뜸ㅠ
# cnt = 0
# input_data = int(input())
# n = str(input_data).zfill(2)
# while True:
#     a = int(n[0])
#     b = int(n[1])
#     new_n = str(a+b).zfill(2)
#     # print(new_n)
#     cnt += 1
#     n = str(b) + str(new_n[1])
#     # print(n)
#     if str(input_data) == n:
#         print(cnt)
#         break


# 1110 더하기 사이클 다른방법
# cnt = 0
# input_data = int(input())
# n = input_data
# while True:
#     a = n//10
#     b = n % 10
#     c = (a + b) % 10
#     n = b*10 + c
#     cnt += 1
#     if input_data == n:
#         print(cnt)
#         break


# 1차원 배열
# 10807 개수 세기
# n = int(input())
# input_data = list(map(int, input().split()))
# v = int(input())
# print(input_data.count(v))


# 10871 x보다 작은 수
# n, x = map(int, input().split())
# input_data = list(map(int, input().split()))

# for i in input_data:
#     if x > i:
#         print(i, end=" ")


# 10818 최소, 최대
# n = int(input())
# input_data = list(map(int, input().split()))
# print(min(input_data), max(input_data))


# 2562 최댓값
# num_list = []
# for i in range(9):
#     num_list.append(int(input()))
# print(max(num_list))
# index = num_list.index(max(num_list))
# print(index+1)


# 5597 과제 안 내신 분..?
# num_list = [i for i in range(1, 31)]
# for i in range(28):
#     num_list.remove(int(input()))
# print(min(num_list))
# print(max(num_list))


# 3052 나머지
# num_list = []
# for i in range(10):
#     i = int(input())
#     num_list.append(i % 42)
# num_list = set(num_list) #set는 중복제거 해주는 역할
# print(len(num_list))


# 1546 평균
# n = int(input())
# score = list(map(int, input().split()))
# max_score = max(score)
# new_score = []
# for i in score:
#     new_score.append(i/max_score*100)  # 새로운 점수 생성
# avg = sum(new_score)/n
# print(avg)


# 8958 OX퀴즈
# n = int(input())
# for i in range(n):
#     ox_list = list(input())
#     score = 0
#     sum_score = 0
#     for ox in ox_list:
#         if ox == "O":
#             score += 1  # O가 연속되면 1씩 커진다
#             sum_score += score
#         else:
#             score = 0  # X가 나오면 점수 리셋
#     print(sum_score)


# 4344 평균은 넘겠지
# c = int(input())
# for i in range(c):
#     cnt = 0
#     nums = list(map(int, input().split()))
#     n = nums[0]
#     sum_score = sum(nums[1:])
#     avg = sum_score/n
#     for score in nums[1:]:
#         if score > avg:
#             cnt += 1
#     rate = cnt/n * 100
#     print(f'{rate:.3f}%')


# 함수
# 15596 정수N개의 합
# def solve(a):
#     ans = 0
#     for i in range(0, len(a)):
#         ans += a[i]
#     return ans


# # 4673 셀프 넘버
# def d(n):  # 생성자 n을 통해 d(n)을 만들어주는 수식
#     n = n + sum(map(int, str(n)))
#     return n
# # 셀프 넘버가 아닌 수들(생성자가 있는 수들)이 들어갈 집합
# no_selfnum = set()
# for i in range(1, 10001):
#     no_selfnum.add(d(i))  # 집합에 넣어줌
# # 셀프넘버 출력하기
# for j in range(1, 10001):
#     if j not in no_selfnum:
#         print(j)


# 1065 한수
# 함수 사용 안함
# n = int(input())
# hansu = 0
# for i in range(1, n+1):
#     if i < 100:
#         hansu += 1
#     else:
#         n = list(map(int, str(i)))
#         if n[0] - n[1] == n[1] - n[2]:
#             hansu += 1
# print(hansu)

# 함수 사용함
# def hansu(n):
#     hansu_cnt = 0
#     for i in range(1, n+1):
#         if i < 100:
#             hansu_cnt += 1
#         else:
#             n = list(map(int, str(i)))
#             if n[0]-n[1] == n[1]-n[2]:
#                 hansu_cnt += 1
#     return hansu_cnt
# n = int(input()) #함수는 입력을 return 후에
# print(hansu(n)) #함수를 출력


# 문자열
# 11654 아스키 코드
# a = input()
# print(ord(a))
# ord(): 문자의 아스키 코드값을 리턴하는 함수
# chr(): 아스키 코드값을 입력받아 그 코드에 해당하는 문자를 출력해주는 함수


# 11720 숫자의 합
# n = int(input())
# num = list(map(int, input()))
# sum = 0
# for i in num:
#     sum += i
# print(sum)

# 11720 다른 방법
# n = input()
# print(sum(map(int, input())))


# 10809 알파벳 찾기
# s = input()
# alphabet = [i for i in range(97, 123)]  # 아스키 코드 범위
# for i in alphabet:
#     print(s.find(chr(i)))  # 아스키코드(숫자)를  원래 문자로


# # 2675 문자열 반복
# t = int(input())
# for i in range(t):
#     test_case = input().split()
#     r = int(test_case[0])
#     s = str(test_case[1])
#     for i in s:
#         print(i*r, end="") #줄넘어가지 않고 바로 옆에 출력되도록
#     print() # 줄넘김


# 1157 단어공부 // 어려웠음 다시 풀어보기ㅜ
# word = input().upper()
# u_word = list(set(word))
# cnt_list = []
# for i in u_word:
#     cnt = word.count(i)
#     cnt_list.append(cnt)
# if cnt_list.count(max(cnt_list)) > 1:
#     print("?")
# else:
#     max_index = cnt_list.index(max(cnt_list))
#     print(u_word[max_index])


# 1152 단어의 개수
# word = input().split()
# print(len(word))


# 2908 상수
# a, b = list(input().split())
# a = a[::-1]  # [::-1] 역순
# b = b[::-1]
# if a > b:
#     print(a)
# else:
#     print(b)


# 5622 다이얼 // 계속 틀림..
# num = ["ABC", "DEF", "GHI", "JKL", "MN0", "PQRS", "TUV", "WXYZ"]
# n = input()
# time = 0
# for i in num:
#     for j in i:
#         for x in n:
#             if j == x:
#                 time += num.index(i) + 3
# print(time)


# 2941 크로아티아 알파벳
# croatia = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
# word = input()

# for i in croatia:
#     word = word.replace(i, "*")
#     print(word)
# print(len(word))


# 1316 그룹 단어 체커
# n = int(input())
# group_word = 0
# for i in range(n):
#     word = list(input())
#     error = 0
#     for j in range(len(word)-1):
#         if word[j] != word[j+1]:
#             new_word = word[j+1:]
#             if word[j] in new_word:
#                 error += 1
#     if error == 0:
#         group_word += 1
# print(group_word)


# 기본 수학1
# 1712 손익분기점
# a, b, c = map(int, input().split())
# if c <= b:
#     print(-1)
# else:
#     print(int(a/(c-b)+1))


# 2292 벌집
# n = int(input())
# sum = 1
# cnt = 0
# index = 0
# while True:
#     sum += 6*index
#     if n > sum:
#         cnt += 1
#         index += 1
#     else:
#         break
# print(cnt+1)


# 1193 분수찾기


# 2869 달팽이는 올라가고 싶다
# a, b, v = map(int, input().split())
# n = (v-b)/(a-b)
# if n == int(n):
#     print(int(n))
# else:
#     print(int(n)+1)

# **while을 사용한 풀이 --> 작동은 되는데 시간초과로 뜸, 부등호 때문
# a, b, v = map(int, input().split())
# height = 0
# n = 0
# while True:
#     height += a
#     n += 1
#     if height < v:
#         height -= b
#     else:
#         break
# print(n)


# # 10250 ACM
# t = int(input())
# for i in range(t):
#     h, w, n = map(int, input().split())
#     f=0
#     ho=0
#     if n%h == 0:
#         f = h*100
#         ho = n//h
#     else:
#         f = (n%h)*100
#         ho = (n//h)+1
#     print(f+ho)


# 2775 부녀회장이 될테야
# t = int(input())
# for _ in range(t):
#     f = int(input())
#     ho = int(input())
#     f0 = [x for x in range(1, ho+1)]
#     for j in range(f):
#         for i in range(1, ho):
#             f0[i] += f0[i-1]
#     print(f0[-1])


# 2839 설탕 배달
# n = int(input())
# cnt = 0
# while n >= 0:
#     if n % 5 == 0:
#         cnt += (n//5)
#         print(cnt)
#         break
#     n -= 3
#     cnt += 1
# else:
#     print(-1)


# 기본 수학 2
# 1978 소수찾기
# n = int(input())
# num = map(int, input().split())
# sosu = 0
# for i in num:
#     error = 0
#     if i > 1:
#         for j in range(2, i):
#             if i % j == 0:
#                 error += 1
#         if error == 0:
#             sosu += 1
# print(sosu)


# 2581 소수
# a = int(input())
# b = int(input())
# sosu_sum = 0
# sosu = []
# for i in range(a, b+1):
#     error = 0
#     if i > 1:
#         for j in range(2, i):
#             if i % j == 0:
#                 error += 1
#         if error == 0:
#             sosu.append(i)
#             sosu_sum += i
# if not sosu: --> 리스트가 비어있으면, 아무것도 없으면
#     print(-1)
# else:
#     print(sosu_sum)
#     print(min(sosu))


# 11653 소인수분해
# n = int(input())
# if n == 1:
#     print("")
# for i in range(2, n+1):
#     if n % i == 0:
#         while n % i == 0:
#             print(i)
#             n = n/i


# 1929 소수 구하기
# a, b = map(int, input().split())
# for i in range(a, b+1):
#     if i == 1:
#         continue
#     for j in range(2, int(i**0.5)+1):  --> i의 제곱근을 구해 그 제곱근 까지의 약수를 구함
#         if i % j == 0:
#             break
#     else:
#         print(i)


# 베르트랑 공준
from math import sqrt

while True:
    n = int(input())
    if n == 0:
        break
    sosu = 0
    for i in range(n+1, 2*n+1):
        if i == 1:
            continue
        for j in range(2, int(sqrt(i)+1)):
            if i % j == 0:
                break
        if error == 0:
            sosu += 1
print(sosu)
