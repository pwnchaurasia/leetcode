var = ["1??3????7", "1????8???2", "2???3???7"]


# num1???num2
# num1 + num2 ==10 and count of ? in between those numbers is exactly 3 then True
# otherwise False


def check_pairs(s):
    stack = []
    for i in range(len(s)):
        ch = s[i]
        if ch.isdigit():
            if stack:
                prev_digit, prev_idx = stack[-1]
                q_count = s[prev_idx + 1:i].count('?')
                if int(prev_digit) + int(ch) == 10 and q_count == 3:
                    return True
            stack.append((ch, i))
    return False


varss = ["1??3????7", "1????8???2", "2???3???7"]

for var in varss:
    print(check_pairs(var))
