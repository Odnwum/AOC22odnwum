def part1(filename):
    with open(filename, "r") as f:
        list = f.read()
    list = list.split("\n")
    arrayofsum = [0]
    j = 0
    for i in list:
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
    return arrayofsum


def sort(array):
    if array == []:
        return []
    else:
        pivot = array[0]
        lesser = sort([x for x in array[1:] if x < pivot])
        greater = sort([x for x in array[1:] if x >= pivot])
        return lesser + [pivot] + greater


def part2(array):
    array = sort(array)
    print(array)
    top3elvescalories = array[-1] + array[-2] + array[-3]
    return top3elvescalories


def main():
    filename = "day1.txt"
    arrayofsum = part1(filename)
    top3 = part2(arrayofsum)
    print(top3)


if __name__ == "__main__":
    main()
