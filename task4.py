import json

INPUT_FILE = "input_1.csv"


def csv_to_list_dict(
        filename: str,
        delimiter: str = ",", new_line: str = "\n"
) -> list[dict]:
    with open(filename, encoding="utf-8") as f:
        file_data = f.read()
        headers_list = file_data.split(new_line)[0].split(delimiter)
        list_dict = []
        for i in range(1, len(file_data.split(new_line))-1):
            list_dict.append(dict(zip(headers_list, file_data.split(new_line)[i].split(delimiter))))
        return list_dict


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))

with open("output_file.json", "x", encoding="utf-8") as f:
    f.write(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
