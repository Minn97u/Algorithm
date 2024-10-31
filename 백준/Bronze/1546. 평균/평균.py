N = int(input())
score = list(map(int, input().split()))
max_score = int(max(score))

up_score = [(i / max_score) * 100 for i in score]

avg_score = sum(up_score) / len(up_score)

print(f"{avg_score:.2f}")