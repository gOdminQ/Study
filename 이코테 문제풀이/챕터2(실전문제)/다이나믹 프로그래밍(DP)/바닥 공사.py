# 내가 작성한 코드

n = int(input())

d = [0] * 1000
d[0] = 1
d[1] = 3

for i in range(2, n):
    d[i] = d[i - 1] + 2 * d[i - 2]

print(d[n - 1] % 796796)



# 답안 예시
# 정수 N을 입력 받기
n = int(input())

# 앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화
d = [0] * 1001

# 다이나믹 프로그래밍(Dynamic Programming) 진행 (보텀업)
d[1] = 1
d[2] = 3
for i in range(3, n + 1):
    d[i] = (d[i - 1] + 2 * d[i - 2]) % 796796

# 계산된 결과 출력
print(d[n])



# 코멘트

d[i] 자체에 796796으로 나눈값을 저장해도 전체 갯수 세는데에 지장없다는 생각을 못했다.
