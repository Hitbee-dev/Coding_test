from collections import Counter

datas = [
    "{{2},{2,1},{2,1,3},{2,1,3,4}}",
    "{{1,2,3},{2,1},{1,2,4,3},{2}}",
    "{{20,111},{111}}",
    "{{123}}",
    "{{4,2,3},{3},{2,3,4,1},{2,3}}"
]

for i in datas:
    buf = []
    ans = []
    replc = i.replace("},", "|").replace("{", "").replace("}", "").split("|") # 문자열 자르기
    for idx, j in enumerate(replc): # 콤마 단위로 buf배열에 extend
        buf.extend(j.split(","))
    for k, v in Counter(buf).most_common(): # extend된 배열을 Counter로 갯수를 셈
        ans.append(k)
    ans = list(map(int, ans)) # 문자열 배열을 정수형 배열로 변환
    print(ans)