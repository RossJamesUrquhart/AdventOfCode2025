def part_1(input):
    # This is a brute force method that checks every number in the range, but it works and is fast enough for the input size
    # The first part only checks for numbers that are made up of 2 repeats, so we can check if the first half of the number 
    # is the same as the second half, and if the length of the number is even (since it has to be made up of 2 repeats)
    total_inv = 0
    for invalid_range in input:
        start_range = invalid_range.split("-")[0]
        end_range = invalid_range.split("-")[1]
        for num in range(int(start_range), int(end_range) + 1):
            num_str = str(num)
            half = len(num_str) // 2
            if (num_str[:half] == num_str[-half:]) and (len(num_str) % 2 == 0):

                print(f"invalid number: {num}")
                total_inv += int(num)
    return total_inv

def part_2(input):
    total_inv = 0
    for invalid_range in input:
        start_range = invalid_range.split("-")[0]
        end_range = invalid_range.split("-")[1]
        for num in range(int(start_range), int(end_range) + 1):
            num_str = str(num)
            # Check if the number is a repeated pattern by checking if it exists in its 
            # own double (excluding the first and last character)
            # this method doesn't care how many times it's repeated - the first only 
            # wanted to check for 2 repeats, but the second part wants to check for any 
            # number of repeats, so this method works for both
            if num_str in (num_str + num_str)[1:-1]:
                print(f"invalid number: {num}")
                total_inv += int(num)
            
    return total_inv

if "__main__" == __name__:
    with open("Day_2_input.txt", 'r') as f:
        data = f.read().split(",")
        print(data)

    #sample_input = ["11-22", "95-115", "998-1012", "1188511880-1188511890", "222220-222224", "1698522-1698528", "446443-446449", "38593856-38593862", "565653-565659", "824824821-824824827", "2121212118-2121212124"]

    print(part_2(data))