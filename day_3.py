from collections import Counter


def task1(inp):
    gamma = ''
    epsilon = ''
    for i in range (len(inp[0])):
        common = Counter([x[i] for x in inp])
        if common['0'] > common['1']:
            gamma += '0'
            epsilon += '1'
        else:
            gamma += '1'
            epsilon += '0'
    return int(gamma,2)*int(epsilon,2)


def task2(inp):
    oxygen = inp
    co2 = inp

    for i in range(len(inp[0])):
        common = Counter([x[i] for x in oxygen])
        if common['0'] <= common['1']:
            oxygen = [item for item in oxygen if item[i:].startswith('1')]
        else:
            oxygen = [item for item in oxygen if item[i:].startswith('0')]
        if len(oxygen) == 1:break

    for i in range(len(inp[0])):
        common2 = Counter([x[i] for x in co2])
        if common2['0'] <= common2['1']:
            co2 = [item for item in co2 if item[i:].startswith('0')]
        else:
            co2 = [item for item in co2 if item[i:].startswith('1')]
        if len(co2) ==1: break

    return int(oxygen[0],2)*int(co2[0],2)


if __name__ == '__main__':
    input = []
    with open('input3.txt') as f:
        for line in f:
            input.append(line.strip())
    print(task2(input))