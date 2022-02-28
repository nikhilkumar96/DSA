# Enter your code here. Read input from STDIN. Print output to STDOUT
"""
create ROBOT which takes input the commands and gives final output as the position of grid

e.g. [ west_1, south_2]

"""


class Robo:
    def __init__(self, i=0, j=0):
        self.i = i
        self.j = j

    def reset(self):
        self.i = 0
        self.j = 0

    def north(self, val):
        self.i += val

    def south(self, val):
        self.i -= val

    def east(self, val):
        self.j += val

    def west(self, val):
        self.j -= val

    def print_final(self):
        print(self.i, self.j)


def main():
    instruc = list(input().split(' '))
    robo_obj = Robo()
    for ins in instruc:
        if len(ins.split('_')) == 1:
            robo_obj.reset()
        else:
            robo_obj.__getattribute__(ins.split('_')[0])(int(ins.split('_')[1]))
    robo_obj.print_final()


main()
