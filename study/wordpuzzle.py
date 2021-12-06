# 알고리즘 문제 : 알파벳 낱말 퀴즈 배치하기

# 7x7 의 판이 존재한다.
# N개의 단어가 주어지며, 각 단어의 길이는 1~N 사이로 주어진다.
# 각 단어들은 알파벳 소문자로만 이루어져 있다.

# 단어들은 7x7판에 모두 채워질 수 있는 개수로 주어지며, N개의 단어를 7x7 판에 다음과 같은 조건으로 배치한다.
# 1. 단어는 한 행 또는 한 열에서만 배치될 수 있다.
# 2. 두 개의 단어가 서로 일치하는 알파벳이 없는 경우 서로 독립 관계이다.
# 3. 두 개의 단어가 일치하는 알파벳이 존재하는 경우 일치하는 알파벳을 기준으로 직교할 수 있다.
# 4. 직교하지 않는 모든 단어는 단어와 단어 사이에 한칸 이상의 거리가 존재해야 한다.
# 5. 직교가 가능한 알파벳이 존재하면, 직교를 우선하여 배치한다.
# 6. 단어가 배치되지 않은 공간은 '*' 로 표시한다.

# 출력은 여러 종류로 나올 수 있으며 

# [ 입력 예시 ]
# 3
# grape
# banana
# apple

# [ 출력 예시 ]
# **b****
# **a*a**
# **n*p**
# **a*p**
# **n*l**
# grape**
# *******