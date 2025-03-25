# bookbot

BookBot is my first [Boot.dev](https://www.boot.dev) project!

Book Bot is a Python project designed to analyze the contents of a book and generate a statistical report. It counts the number of words and characters in the book and provides insights into the frequency of each character.

## Features
- Count total words in a book.
- Count and sort character frequencies (case insensitive).
- Generate a detailed statistical report of the book.

## Example Output
```
--- Begin report of books/frankenstein.txt ---
77986 words found in the document

The 'e' character was found 46043 times
The 't' character was found 30365 times
The 'a' character was found 26743 times
...
The 'z' character was found 243 times
--- End report ---
```

## Requirements
- Python 3.8+
- Basic knowledge of Python, Git, and a CLI (Command Line Interface).

## Setup Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/gabrielms-castro/bookbot.git
   cd bookbot
   ```

2. Add your book `.txt` file to the `books/` directory.

3. Run the program:
   ```bash
   python main.py
   ```

## File Structure
```
bookbot/
├── books/                # Directory for book files
│   └── frankenstein.txt  # Example book file
├── bookbot.py            # Main program file
├── README.md             # Project documentation
```

## How It Works
1. Reads the content of a specified text file (book).
2. Counts the number of words using `split()`.
3. Counts the frequency of each character (a-z) in the book.
4. Generates a formatted report showing total words and sorted character frequencies.
