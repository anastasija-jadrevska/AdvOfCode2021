
def task_1(in_list):
    count = 0
    for i in range(0,len(in_list)-1):
        if in_list[i]<in_list[i+1]:
            count = count+1
    return count


def task_2(in_list):
    count = 0
    for i in range (0,len(in_list)-3):
        sum_1 = in_list[i]+in_list[i+1]+in_list[i+2]
        sum_2 = in_list[i+1]+in_list[i+2]+in_list[i+3]
        if sum_1<sum_2:
            count=count+1
    return count


def improved(in_list):
    # booleans are cast to ints when sum'd
    # a+b+c < b+c+d if a<d

    sum_1 = sum(x < y for x, y in zip(in_list, in_list[1:]))
    sum_2 = sum(x < y for x, y in zip(in_list, in_list[3:]))

    # line for both; result = solve(data,diff)
    solve = lambda data, diff: sum(b > a for a, b in zip(data, data[diff:]))



if __name__ == '__main__':
    int_list = []
    with open('input1.txt') as f:
        for line in f:
            int_list.append(int(line))
    # print(task_2(int_list))
    print(list(zip(int_list, int_list[1:])))



