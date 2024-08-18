test_cases = int(input().strip())

for _ in range(test_cases):
    input_values = input().split()
    result = 0
    try:
        n1 = input_values[0]
        n2 = input_values[1]
        result = (int(n1) // int(n2))
        print(result)
    except (ZeroDivisionError, ValueError) as e:
        print(f"Error Code: {e}")
