T = int(input())
grades = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']

def check_degree(T):
    for case in range(1,T+1):
        N,K = map(int,input().split())
        total_list = []

        for stu in range(N):
            a,b,c = map(int,input().split())
            total = (a * 0.35) + (b * 0.45) + (c*0.2)
            total_list.append(total)

        k_score = total_list[K-1]

        total_list.sort(reverse=True)

        div = N // 10

        final_k_score = total_list.index(k_score) // div

        print('#{} {}'.format(case, grades[final_k_score]))
        
check_degree(T)