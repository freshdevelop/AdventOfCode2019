#!/usr/bin/python
input_file = 'input.txt'

def main():
    fp = open(input_file)
    data = [int(i) for i in fp.read().strip()]
    width = 25
    height = 6

    # data = [int(i) for i in '123456789012']
    # width = 3
    # height = 2

    data = [data[layer * (width * height):(layer + 1) * (width * height)] for layer in range(len(data) / (width * height))]
    zeros = [layer.count(0) for layer in data]
    print data[zeros.index(min(zeros))].count(1) * data[zeros.index(min(zeros))].count(2)

    fp.close()

if __name__ == "__main__":
   main()