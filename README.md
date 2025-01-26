# Translator App

This is a simple GUI-based Translator application built using Python and the `tkinter` library. It allows users to input text, specify a target language, and translate the text into the desired language using the `googletrans` library.

## Features

- **User-friendly Interface**: A clean and responsive design built with `tkinter` and `ttk` widgets.
- **Text Translation**: Translate text from one language to another by specifying the target language code.
- **Real-time Results**: The translated text is displayed instantly after clicking the "Translate" button.
- **Customizable Design**: The app uses a styled theme for better visual appeal.

## Requirements

To run this project, you need to have the following installed on your machine:

- Python 3.x
- `tkinter` (pre-installed with Python)
- `googletrans` library

You can install `googletrans` by running:
```bash
pip install googletrans==4.0.0-rc1


## How to Run

    Clone this repository or copy the project files to your local machine.
    Ensure all dependencies are installed (see the Requirements section above).
    Open a terminal or command prompt and navigate to the project directory.
    Run the following command: python AI_translate.py
    The Translator application will open in a new window.


## How to Use

    Enter the text you want to translate in the "Text to translate" field.
    Enter the target language code (e.g., en for English, fr for French) in the "Target language" field.
    Click the "Translate" button.
    The translated text will appear below in blue.


## Examples of Language Codes

Here are a few examples of target language codes you can use:

    English: en
    French: fr
    Spanish: es
    German: de
    Chinese: zh-cn
    Arabic: ar

For a complete list of supported language codes, refer to the Google Translate API documentation.


## Future Improvements

    Add support for multiple source languages detection.
    Enhance the UI with additional customization options.
    Provide a dropdown menu for selecting the target language instead of manual input.

## License

This project is open-source and available under the MIT License. Feel free to modify and distribute it as you wish.
