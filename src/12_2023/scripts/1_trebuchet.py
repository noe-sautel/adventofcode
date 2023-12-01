# TODO: Mv to utils
def open_file(file_path):
    try:
        with open(file_path, "r") as file:
            data = file.read()
        return data
        # return data
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return None


def apply_transformation(
    file_path,
):
    trebuchet_data = open_file(file_path)
    trebuchet_list = trebuchet_data.split("\n")
    number_list = []
    for line in trebuchet_list:
        digits_by_line = [int(character) for character in line if character.isdigit()]
        digits_first_last = [digits_by_line[0], digits_by_line[-1]]
        number_by_line = int("".join(map(str, digits_first_last)))
        number_list.append(number_by_line)

    return sum(number_list)


def main(
    file_path,
):
    print(apply_transformation(file_path))


if __name__ == "__main__":
    main(file_path="src/12_2023/data/1_12.txt")
