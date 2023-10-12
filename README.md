
## Text File Combiner

This simple python script consolidates the content of all `.txt` files within a specified directory into a single `.txt` file. It's particularly useful for aggregating text data without manual copy-pasting, providing a streamlined way to compile textual information from multiple files into one.


### Usage

* **Without Arguments:**
  When run without any arguments, the script will combine all `.txt` files in its current directory and output the combined content into a file named `output.txt`.
  ```python
  python run.py
  ```
* **With a Specific Directory:**
  You can specify the directory of the `.txt` files as a argument. The output will be saved as `output.txt` in the script's directory.
  ```python
  python run.py {path}
  ```
* **With a Specific Directory and Output File:**
  To specify both the directory of the `.txt` files and the output file, use two arguments.
  ```python
  python run.py {path} {file_name}
  ```

#### Parameters

* `directory` (optional): The path to the directory containing `.txt` files to combine. Defaults to the current directory (`.\`).
* `output` (optional): The name of the output file where the combined content will be written. Defaults to `output.txt`.

#### Example

```python
python run.py .\directory\ combined_output.txt
```

This will combine all `.txt` files in `.\directory` and write the combined content to `combined_output.txt`.

### Notes

* Ensure that the script has the necessary read/write permissions for the specified directories and files.
* The script appends a newline character between the content of different files to ensure separation in the combined output.
* Ensure that the file paths and names do not contain invalid characters.

### Requirements

* Python 3.x
