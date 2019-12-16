#!/usr/bin/python
input_file = 'input.txt'

def main():
    fp = open(input_file)
    data = [int(i) for i in fp.read().strip()]
    width = 25
    height = 6

    # data = [int(i) for i in '0222112222120000']
    # width = 2
    # height = 2

    data = [data[layer * (width * height):(layer + 1) * (width * height)] for layer in range(len(data) / (width * height))]
    pixels = [ str( column[min([column.index(elem) if elem in column else len(column) - 1 for elem in [0, 1]])] ) for column in [[data[layer][index] for layer in range(len(data))] for index in range(len(data[0]))]]
    for _ in [''.join(row) for row in [pixels[layer * width:(layer + 1) * width] for layer in range(len(pixels) / width)]]:
        print _

    fp.close()

if __name__ == "__main__":
   main()

#     ## #   ##### #  # #### 
#      # #   #   # #  # #    
#      #  # #   #  #### ###  
#      #   #   #   #  # #    
#   #  #   #  #    #  # #    
#    ##    #  #### #  # #    