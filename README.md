# BookBot

BookBot is a simple Python program that analyzes the contents of a .txt book file and prints useful statistics such as word count, character count, and frequency of each letter.

## Features

* Counts the total number of words in a book

* Counts the frequency of each character (case-insensitive)

* Outputs results in a neatly formatted report

## Installation

1.Clone the repository:

```git clone https://github.com/borasaygac/bookbot.git```

```cd bookbot```

2. (Optional) Create and activate a virtual environment:

```python3 -m venv venv```

```source venv/bin/activate```

3. Run the script:

```python main.py <path-to-txt-file>```

* Example Output

--- Begin report of books/frankenstein.txt ---

13461 words found in the document

The 'e' character was found 2345 times

The 't' character was found 1937 times

...

--- End report ---

### Customization

You can analyze any .txt file by passing its path as an argument to main.py.

#### License

This project is licensed under the MIT License - see the LICENSE file for details.

#### Author

Created by borasaygac as part of learning Python fundamentals at [Boot.dev](https://www.boot.dev).
