# Web Page Generator

A Python and Tkinter coursework application that creates a simple HTML page from a default message or custom text and opens it in a browser.

## Features

- Enter custom text in a desktop interface.
- Choose **Default HTML Page** to generate a page with the built-in message.
- Choose **Submit Custom Text** to generate a page with the entered text as an HTML heading.
- Write `index.html` and open its local file URL in a new browser tab.

## Technologies Used

Python 3, Tkinter, HTML, `os` and `webbrowser`. The application does not import third-party Python packages.

## Installation and Setup

Clone or download the repository. Use Python 3 with Tkinter, a desktop display and a browser available for local HTML files.

From the repository root:

```sh
cd web_Page_Generator
```

## How to Run

```sh
python3 web_page_generator.py
```

On Windows, use `py web_page_generator.py`.

Select **Default HTML Page**, or enter text and select **Submit Custom Text**. The generated page opens in the browser. Each generation overwrites `index.html` in the current working directory, so run from this project folder and keep any HTML you want to preserve elsewhere.

## What I Learned

- Building a Tkinter interface with labels, an entry field and buttons.
- Reading text input and assembling HTML content.
- Writing a file and resolving its local path.
- Opening generated content through Python's browser module.

## Known Limitations

- The output is a single heading inside a basic HTML page; there is no page-layout editor.
- Custom input is inserted directly into the HTML without escaping or validation. Use plain text for the intended heading output.
- The output filename is fixed, and file-write or browser-opening failures are not handled in the interface.
- No automated tests are included for this project. This documentation review did not run the desktop interface.

[Source code](web_page_generator.py) · [Back to the repository overview](../README.md)
