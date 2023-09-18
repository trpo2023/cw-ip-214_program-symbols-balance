from modules.balance_checker import BalanceChecker
from modules import argparser
from modules import utils


def main():
    parser = argparser.init_argparser()
    args = parser.parse_args()

    if not utils.is_valid_c_file(args.input_file):
        print("Error: Invalid file extension. Please provide a .c file.")
        return
    try:
        with open(args.input_file, 'r') as file:
            balance_checker = BalanceChecker()
            text = file.read()
            result = balance_checker.check(text)

            if result.error:
                print("Balance Check Result:")
                print(f"Error: {result.error}")
                print(utils.get_line_by_char_index(text, result.bracket_index))
                if result.bracket_index != -1:
                    print(f"Bracket Index: {result.bracket_index}")
            else:
                print("Balance Check Result:")
                print("> All Good! No errors found in the entire file.")

    except FileNotFoundError:
        print(f"Error: File '{args.input_file}' not found.")
    except PermissionError:
        print(f"Error: Permission denied to read file '{args.input_file}'.")
    except IOError as e:
        print(f"Error reading file '{args.input_file}': {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
