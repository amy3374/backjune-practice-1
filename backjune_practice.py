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
