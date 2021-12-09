


if __name__ == '__main__':
    input = []
    
    with open('input3.txt') as f:
        for line in f:
            input.append(line.strip())
    print(task2(input))