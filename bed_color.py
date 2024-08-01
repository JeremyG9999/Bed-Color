import random
class Bed:
    def __init__(self):
        self.lst = []
        self.amount = int(input("How many total beds are there: "))
    def bed_list(self):
        for _ in range(self.amount):
            color = random.choice(["red", "blue", "green"])
            self.lst.append(color)
        count_red = self.lst.count("red")
        count_green = self.lst.count("green")
        count_blue = self.lst.count("blue")
        print(f"There are {count_red} red beds in the mansion of beds")
        print(f"There are {count_green} green beds in the mansion of beds")
        print(f"There are {count_blue} blue beds in the mansion of beds")
def main():
    run = Bed()
    run.bed_list()
main()