# Payload Generator

This Python application is designed to generate payloads for various lambda application. It provides an interactive console-based interface for selecting applications, environments, and samples, and then generates and displays the payload based on the selected configurations.

## Setup Instructions

### Prerequisites

- Python 3.8 or higher installed on your system.
- `pip` package manager installed.

### Setting Up the Virtual Environment

1. Navigate to the project directory:

   ```bash
   cd payload-generator
   ```

2. Create a virtual environment:

   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:

   - On Windows:

     ```bash
     venv\Scripts\activate
     ```

   - On macOS/Linux:

     ```bash
     source venv/bin/activate
     ```

4. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

### Running the Application

1. Ensure the virtual environment is activated.
2. Run the main script:

   ```bash
   python main.py
   ```

## Configuration

The application relies on the following configuration files:

- `config.py`: Contains application and environment choices, as well as paths and other settings.
- `APPLICATION_CONFIG`: Defines application-specific configurations such as queue names and topics.
- `PATHS_CONFIG`: Maps applications to their respective sample file paths.

## Usage

1. Follow the interactive prompts to select the application, environment, and sample.
2. The generated payload will be displayed and copied to the clipboard.
3. Optionally, reuse the payload for additional operations.

## Notes

- Ensure that the `config.py` file is properly set up with valid application and environment configurations before running the application.
- The application clears the console after each payload generation for a clean user experience.
