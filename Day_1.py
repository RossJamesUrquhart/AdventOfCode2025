
def part_1(input, start):
    # Function is based on checking after a series of safe inputs, how many times the value was 0.
    # This is done by keeping track of the current value and counting how many times it becomes 0 after processing each input.
    count = 0

    for input in data:
        direction = input[0]
        value = int(input[1:])
        if direction == 'L':
            value *= -1

        current = (current + value) % 100

        if current == 0:
            count += 1

    print(f"value was 0 --- {count} times")

    return count

def part_2(input, start):
    # The second part of the problem is to count how many times the value was 0 during the process, not just at the end of each input. 
    # This is done by checking every intermediate value as we process each input and counting how many times it becomes 0.
    current = start
    count = 0
    num_zeroes = 0

    for input in data:
        direction = input[0]
        value = int(input[1:])
        if direction == 'L':
            step = 1
        else:
            step = -1
        value *= step

        num_zeroes += [
            i % 100 for i in range(current, current + value, step)
        ].count(0)

        current = (current + value) % 100

        if current == 0:
            count += 1

    print(f"value was 0 --- {count} times")

    return num_zeroes

if "__main__" == __name__:

    sample = ["L68",
            "L30",
            "R48",
            "L5",
            "R60",
            "L55",
            "L1",
            "L99",
            "R14",
            "L82",
            "R468",
            "L3000"]

    with open("Day_1_input.txt", 'r') as f:
        data = f.readlines()
        print(len(data))

    current = 50

    print(part_2(input, current))