def is_multiple(a, b):
    if a == 0 or b == 0:
        return False
    
    if a % b == 0:
        return True, f"{a} is a multiple of {b}"
    if b % a == 0:
        return True, f"{b} is a multiple of {a}"
    
    return False, "Neither is a multiple of the other"

def main_section_4():
    print(" Section 4: REPL Loop")

    samples = [
        (10, 5),
        (15, 3),
        (7, 2),
        (-1, 0)
    ]

    for num1, num2 in samples:
        if num1 < 0 or num2 < 0:
            print("Negative number detected. Exiting...")
            break

        result, message = is_multiple(num1, num2)
        if result:
            print(f"Checking {num1} and {num2}: YES! {message}")
        else:
            print(f"Checking {num1} and {num2}: NO. {message}")

if __name__ == "__main__":
    main_section_4()
