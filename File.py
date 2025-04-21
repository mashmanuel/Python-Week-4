def modify_file_content(input_filename, output_filename):
    """
    Reads a file, modifies its content, and writes it to a new file.
    Handles errors for file operations.
    """
    try:
        # Reading the input file
        with open(input_filename, 'r') as infile:
            lines = infile.readlines()

        # Modifying the content
        modified_lines = [line.strip() + " - Modified\n" for line in lines]

        # Writing to the output file
        with open(output_filename, 'w') as outfile:
            outfile.writelines(modified_lines)

        print(f"Content successfully written to '{output_filename}'.")

    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' does not exist.")
    except IOError:
        print(f"Error: Could not read or write to the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def main():
    print("File Read & Write Challenge 🖋️")
    input_filename = input("Enter the name of the file to read from: ")
    output_filename = input("Enter the name of the file to write to: ")

    modify_file_content(input_filename, output_filename)


if __name__ == "__main__":
    main()