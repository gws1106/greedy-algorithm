#거스름돈 문제
n = 1260                         #거슬러 줘야 할 돈

coin_types = [500, 100, 50, 10]  #거스름돈 단위
cnt = 0                          #동전의 최소 개수

for coin in coin_types:
    
    if n // coin > 0:            #몫 > 0 == 거슬러줄 수 있다
        cnt = cnt + n // coin
        n %= coin                #거스르고 남은 나머지 값을 저장

print(cnt)
        
