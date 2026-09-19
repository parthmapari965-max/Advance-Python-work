def count_lines(input_path):
    with open(input_path, "r") as f:
        return sum(1 for _ in f)


def extract_first_lines(input_path, n=2):
    first_lines = []

    with open(input_path, "r") as f:
        for i, line in enumerate(f):
            if i >= n:
                break
            first_lines.append(line)

    return first_lines


def write_lines(output_path, lines):
    with open(output_path, "w") as f:
        f.writelines(lines)


if __name__ == "__main__":
    input_path = "input.txt"
    output_path = "output_first_two_lines.txt"

    total_lines = count_lines(input_path)
    print("Total number of lines:", total_lines)

    first_two = extract_first_lines(input_path, 2)

    print("\nFirst two lines:")
    for line in first_two:
        print(line.rstrip())

    write_lines(output_path, first_two)

    print("\nExtracted lines written to:", output_path)