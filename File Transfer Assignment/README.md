# File Transfer Assignment

A Python and Tkinter coursework application for moving recently modified entries between two selected folders.

## Features

- Choose source and destination folders using file dialogs.
- Compare each source entry's modification time with a cutoff of 24 hours before the transfer starts.
- Move qualifying entries using `shutil.move` and print transfer or skip messages to the terminal.
- Close the application using its Exit button.

## Technologies Used

Python 3, Tkinter, `os`, `shutil` and `datetime`. The application does not import third-party Python packages.

## Installation and Setup

Clone or download the repository. Use Python 3 with Tkinter and a desktop display.

From the repository root:

```sh
cd "File Transfer Assignment"
```

Prepare two separate temporary folders containing disposable sample files. Set their modification times if you want to compare recent and older entries; files obtained through a fresh checkout may have recent modification times.

## How to Run

```sh
python3 file_transfer.py
```

On Windows, use `py file_transfer.py`.

Choose **Select Source**, choose **Select Destination**, then select **Transfer Files**. Check the destination folder and terminal messages to see the result.

**Transfers move entries out of the source folder; they do not create backup copies.** Use sample data for demonstrations.

## What I Learned

- Connecting Tkinter buttons to folder-selection and transfer functions.
- Listing directory entries and reading modification times.
- Comparing timestamps with a calculated cutoff.
- Moving entries between folders with Python's standard library.

## Known Limitations

- There is no filename-extension filter and no database transfer log.
- Only entries directly inside the selected source folder are examined. The code does not distinguish files from directories before passing qualifying entries to `shutil.move`.
- Empty or invalid paths, permission errors and destination-name conflicts are not handled with user-facing error messages.
- Transfers run in the interface event handler and may make the window unresponsive during longer operations.
- No automated tests are included for this project. This documentation review did not execute transfers.

[Source code](file_transfer.py) · [Back to the repository overview](../README.md)
