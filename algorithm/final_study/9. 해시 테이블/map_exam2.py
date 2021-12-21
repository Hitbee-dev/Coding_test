def map(dic):
    for i in dic:
        dic[i] = i/100
    return dic

dic = {
    179.5:0,
    162.0:0,
    167.3:0,
    191.2:0,
    183.5:0
}
print(map(dic))