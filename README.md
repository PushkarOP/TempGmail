# Gmail Temporary Email

This Python script creates a temporary email address using your Gmail account and checks for incoming emails to that address. It uses the Gmail API to read emails and extract their content.

## Features

- Generates a temporary email address using your Gmail account.
- Checks for incoming emails to the temporary email address.
- Extracts and prints the content of the received email.

## Prerequisites

- Python 3.6 or higher
- Google API Client Library for Python
- Gmail API enabled on your Google account

## Setup

1. **Clone the repository:**

    ```sh
    git clone https://github.com/PushkarOP/TempGmail.git
    cd TempGmail
    ```

2. **Install dependencies:**

    ```sh
    pip install -r requirements.txt
    ```

3. **Enable the Gmail API:**

    - Go to the [Google Cloud Console](https://console.cloud.google.com/).
    - Create a new project or select an existing project.
    - Enable the Gmail API for your project.
    - Create OAuth 2.0 credentials and download the `credentials.json` file.
    - Place the `credentials.json` file in the root directory of the project.

4. **Update the base email:**

    - Open the `main.py` file.
    - Replace `change_here@gmail.com` with your actual Gmail address in the `BASE_EMAIL` variable.

## Usage

1. **Run the script:**

    ```sh
    python main.py
    ```

2. **Follow the on-screen instructions to authenticate with your Google account.**

3. **The script will generate a temporary email address and start checking for incoming emails.**

## Notes

- The script checks for new emails every 10 seconds.
- The temporary email address is generated by appending random characters to your base email address.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## Acknowledgements

- [Google API Client Library for Python](https://github.com/googleapis/google-api-python-client)
- [Gmail API](https://developers.google.com/gmail/api)

