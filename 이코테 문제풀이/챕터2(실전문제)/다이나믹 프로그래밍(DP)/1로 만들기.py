# 내가 작성한 코드

n = int(input())

d = [0] * 30001

def func(x):
    if x == 1:
        return 0
    if d[x] != 0:
        return d[x]
    if x % 5 == 0:
        d[x] = min(func(x // 5), func(x - 1)) + 1
        return d[x]
    if x % 3 == 0:
        d[x] = min(func(x // 3), func(x - 1)) + 1
        return d[x]
    if x % 2 == 0:
        d[x] = min(func(x // 2), func(x - 1)) + 1
        return d[x] 
    else:
        d[x] = func(x - 1) + 1 
        return d[x]
        
print(func(n))  
        

# 답안 예시

# 정수 X를 입력 받기
x = int(input())

# 앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화
d = [0] * 1000001

# 다이나믹 프로그래밍(Dynamic Programming) 진행(보텀업)
for i in range(2, x + 1):
    # 현재의 수에서 1을 빼는 경우
    d[i] = d[i - 1] + 1
    # 현재의 수가 2로 나누어 떨어지는 경우
    if i % 2 == 0:
        d[i] = min(d[i], d[i // 2] + 1)
    # 현재의 수가 3으로 나누어 떨어지는 경우
    if i % 3 == 0:
        d[i] = min(d[i], d[i // 3] + 1)
    # 현재의 수가 5로 나누어 떨어지는 경우
    if i % 5 == 0:
        d[i] = min(d[i], d[i // 5] + 1)

print(d[x])




# 코멘트
앞으로 가능하면 무조껀 보텀업으로 하자. 훨 간단해 보임.
# 보텀업으로 연습

x = int(input())

d = [0] * 30001

for i in range(2, x + 1):
  d[i] = d[i - 1] + 1  
  if i % 2 == 0:
    d[i] = min(d[i // 2], d[i - 1]) + 1
  if i % 3 == 0:
    d[i] = min(d[i // 3], d[i - 1]) + 1
  if i % 5 == 0:
    d[i] = min(d[i // 5], d[i - 1]) + 1

print(d[x])
# 추가 코멘트
답지 방식 : d[i] = min(d[i], d[i // 2] + 1)
내방식 : d[i] = min(d[i // 2], d[i - 1]) + 1

