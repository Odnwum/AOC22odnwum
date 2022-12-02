def readfile(filename):
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
    return sum


def main():
    filename = "day2.txt"
    sum = readfile(filename)
    print(sum)


if __name__ == "__main__":
    main()
