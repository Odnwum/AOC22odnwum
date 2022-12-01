def readfile(filename):
    with open(filename, "r") as f:
        list = f.read()
    list = list.split("\n")
    return list  # actually returns array XD


def main():
    filename = "day1.txt"
    array = readfile(filename)
    arrayofsum = [0]
    j = 0
    for i in array:
        if i != "":
            arrayofsum[j] += int(i)
        else:
            arrayofsum.append(0)
            j += 1

    richelf = max(arrayofsum)
    for i in range(len(arrayofsum)):
        if richelf == arrayofsum[i]:
            elfpos = i
            break
    print(f"Elf number {elfpos} has {richelf} calories ")


if __name__ == "__main__":
    main()
