
def task1(inp):
    h=d=0
    for i in inp:
        di,val = i.split()
        val = int(val)
        if di == "forward":
            h+=val;
        elif di == "up":
            d-=val;
        else: d+=val;
    return h*d


def task2(inp):
    h=d=a=0
    for i in inp:
        di,val = i.split()
        val = int(val)
        if di == "forward":
            h+=val;d+=a*val
        elif di == "up":
            a-=val
        else: a+=val
    return h*d

# as an improvement - could do in one class and use aim instead of depth in example one,
# as it results in the same values


if __name__ == '__main__':
    list = []
    with open('input2.txt') as f:
        for line in f:
            list.append(line.strip())
    print(task2(list))