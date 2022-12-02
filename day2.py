def part1(filename):
    with open(filename, "r") as f:
        list = 0
        sum = 0
        while list != "":
            list = f.readline().strip()
            ans = list.split(" ")
            try:
                # add my choice
                if ans[1] == "X":
                    sum += 1
                elif ans[1] == "Y":
                    sum += 2
                elif ans[1] == "Z":
                    sum += 3

                # add lose-draw-win
                if ans[0] == "A" and ans[1] == "X":
                    sum += 3
                elif ans[0] == "A" and ans[1] == "Y":
                    sum += 6
                elif ans[0] == "B" and ans[1] == "Y":
                    sum += 3
                elif ans[0] == "B" and ans[1] == "Z":
                    sum += 6
                elif ans[0] == "C" and ans[1] == "Z":
                    sum += 3
                elif ans[0] == "C" and ans[1] == "X":
                    sum += 6

            except:
                next


def part2(filename):
    with open(filename, "r") as f:
        list = 0
        sum = 0
        while list != "":
            list = f.readline().strip()
            ans = list.split(" ")
            try:
                # add contidtion
                if ans[1] == "Y":
                    sum += 3
                    if ans[0] == "A":
                        sum += 1
                    elif ans[0] == "B":
                        sum += 2
                    elif ans[0] == "C":
                        sum += 3
                elif ans[1] == "Z":
                    sum += 6

                # add other thing
                if ans[1] == "X" and ans[0] == "A":
                    sum += 3
                elif ans[1] == "X" and ans[0] == "B":
                    sum += 1
                elif ans[1] == "X" and ans[0] == "C":
                    sum += 2
                elif ans[1] == "Z" and ans[0] == "A":
                    sum += 2
                elif ans[1] == "Z" and ans[0] == "B":
                    sum += 3
                elif ans[1] == "Z" and ans[0] == "C":
                    sum += 1

            except:
                next

    print(sum)


def main():
    filename = "day2.txt"
    part2(filename)


if __name__ == "__main__":
    main()
