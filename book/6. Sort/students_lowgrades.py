# ������ ���� ������ �л� ����ϱ�

# �Է� ���� | ��� ����
# 2       | �̼��� ȫ�浿
# ȫ�浿 95 |
# �̼��� 77 |

# ��ųʸ��� Ȱ��
N = int(input())
data = {}
for _ in range(N):
    name, score = map(str, input().split())
    data[score] = name
result = sorted(data.items())
for _, name in result:
    print(name, end=" ")