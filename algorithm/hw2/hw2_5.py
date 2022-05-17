# 5) Fractal Image

# rectree.py를 참고해서 나만의 프랙탈 이미지를 그려보자.
# - 직접 그려도 좋고, 검색해서 변형해도 좋음
# - 이상한 그림이 나와도, 미완성이어도 점수를 다 줄 예정이니 마음 편하게 놀아볼 것
# - 단, 똑같이 그리지는 말기
# - 예제를 검색해서 수정한 경우 출처를 주석으로 써둘 것
# - turtle 모듈 사용법은 간단하므로 예제를 찾아보기 바람

import turtle as t
import random as r

def fractal_tree(length, angle):
	if(length*0.1 < 1):
		t.color("green")
	else:
		t.color("brown")

	if(length < 10):
		return
	else:
		t.pensize(length * 0.1) # 새로 그려질 때 마다 나무 줄기가 얇아지도록 설정
		t.forward(length) # 정해진 길이만큼 그림

		t.right(angle) # 오른쪽으로 꺾을 각도
		fractal_tree(length * r.uniform(0.6, 0.9), r.randint(10, 40)) # 재귀 호출로 다음 가지 이어서 그리도록(길이, 각도)
		t.left(angle * 2) # 왼쪽으로는 오른쪽각도의 2배만큼 꺾어준다.
		fractal_tree(length * r.uniform(0.8, 0.9), r.randint(10, 40)) # 재귀 호출로 다음 가지 이어서 그리도록(길이, 각도)
		t.right(angle)
		
		t.pensize(length * 0.1)
		t.backward(length)

t.speed(0)
t.penup()
t.setpos(0, -200)
t.pendown()
t.left(90)
fractal_tree(100, r.randint(15, 35))
t.done()