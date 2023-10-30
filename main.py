import re
import os

DATA_DIR = "data"

def process_file(file_path: str, regex_pattern: str):
    try:
        with open(file_path, "r") as file:
            file_content = file.read()

            matches = re.findall(regex_pattern, file_content, re.IGNORECASE)
            if matches:
                print(f"---> Matches in {file_path}:")
                for match in matches:
                    print(match, "\n")
            else:
                print(f"No matches found in {file_path}\n")
    except Exception as e:
        print(f"An error occurred while processing {file_path}: {e}\n")

def main():
    """
    Main function that processes all files in the data/ directory.


    Example Regex to find names starting with G and ending with L: \bG[A-Za-z -\',.]*L\b

    Output:
        ---> Matches in data/data_1.txt:
        Gol

        ---> Matches in data/data_2.txt:
        Gabriel
    """

    regex_pattern = input("Enter the regular expression pattern: ")

    for filename in os.listdir("data"):
        if filename.endswith(".txt"):
            file_path = os.path.join(DATA_DIR, filename)
            process_file(file_path, regex_pattern)

if __name__ == "__main__":
    main()
