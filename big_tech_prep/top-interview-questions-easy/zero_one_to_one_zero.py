

def convert_zero_one_to_one_zero(string):
    num_list = [i for i in string]
    if len(num_list) == 2 and num_list[0] == '0' and num_list[1] == '1':
        return '10'

    seconds = 0
    while True:
        changed = False
        p1, p2 = 0, 1
        new_list = num_list[:]
        while p2 < len(new_list):
            if new_list[p1] == '0' and new_list[p2] == '1':
                new_list[p1], new_list[p2] = new_list[p2], new_list[p1]
                changed = True

            p1 += 1
            p2 += 1
        if not changed:
            break
        seconds += 1
        num_list = new_list
    return "".join(num_list), seconds


if __name__ == "__main__":
    string = "0101"
    ans,seconds = convert_zero_one_to_one_zero(string=string)
    print(ans, seconds)
