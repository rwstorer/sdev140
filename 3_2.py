import random

how_many: str = input('How many numbers')
output_file = open('output.txt','wt')
# convert to int
for i in range(int(how_many)+1):
    rand_num: int = random.randint(1, 500)
    # write the number to a file
    output_file.write(str(rand_num)+"\r\n")
    # print the number to the console
    print(rand_num)