def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5,67, 32)")


def get_user_input():
    lists = []
    nums = input()
    lists = nums.split(",")
    for i in lists:
        lists.append(float(i))
    return lists


def calc_average(lists):
    total = 0
    for i in lists:
        total += i

    return float(total / len(lists))


def calc_min_max_temp(lists):
    return [int(min(lists)), int(max(lists))]


def calc_median_temp(lists):
    lists.sort()
    if len(lists) % 2 == 0:
        return (lists[int(len(lists) / 2)] + lists[int(len(lists) / 2) - 1]) / 2
    else:
        return lists[int(len(lists) / 2)]


def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    lists = [5, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    print(calc_average(lists))
    print(calc_median_temp(lists))
    print(calc_min_max_temp(lists))


if __name__ == "__main__":
    main()
