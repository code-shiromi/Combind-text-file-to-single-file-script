"""
Python script for combining the content of all .txt files in a directory into a single .txt file.

"""
import os, sys

def combine(directory = '.\\', output = "output.txt"):
    """
    Combine the content of all .txt files in a directory into a single .txt file.

    Parameters:
        directory (str): The source directory containing .txt files.
        output (str): The destination file to write the combined content to.
    """
    try:
        # Get all .txt files in the source directory
        #all_files = os.listdir(directory)
        files = [f for f in os.listdir(directory) if f.endswith('.txt')]
        
        # Open the destination file
        with open(output, 'a', encoding='utf-8') as written:
            # Iterate through each .txt file
            for file in files:
                path = os.path.join(directory, file)
                # Open the source .txt file
                with open(path, 'r', encoding='utf-8') as src_file:
                    # Write the content to the destination file
                    written.write(src_file.read())
                    # Optionally, add a newline character between files
                    written.write('\n')
        print(f"All .txt files in {directory} have been combined into {output}.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    if len(sys.argv) == 3:
        for arg in sys.argv[2:]:
            if arg.endswith('.txt'):
                output = arg
            else:
                output = arg + '.txt'
        print(f"Your path was {sys.argv[1]}, and your output file will be {output}")
        combine(sys.argv[1], output)
    elif len(sys.argv) == 2:
        print(f"Your path was {sys.argv[1]}, and your output file will be output.txt")
        combine(sys.argv[1])
    elif len(sys.argv) == 1:
        print("No path was entered, so the current directory will be used. The output file will be output.txt.")
        combine()
    else:
        sys.exit('Invalid arguments entered.')