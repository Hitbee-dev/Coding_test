# 2) n부터 m까지의 합

# Original Code
def sum_n_to_m(n, m):
    ret_val = 0 # return할 변수
    for i in range(n, m+1): # m도 포함해서 더 해야하기 때문에 m+1
        ret_val += i # n부터 m+1까지 더하기
    return ret_val # 출력

# Revursive Code
def sum_n_to_m_rec(n, m):
    if n == m:
        return n
    else:
        return sum_n_to_m_rec(n, m-1)+m

# Test Code
def compare(func1, func2, n, m):
    ret1 = func1(n, m)
    ret2 = func2(n, m)

    print(f"{func1.__name__}=>{ret1}")
    print(f"{func2.__name__}=>{ret2}")
    print(f"equal?={ret1 == ret2}")
    print()
compare(sum_n_to_m, sum_n_to_m_rec, 3, 120)