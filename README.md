# Resume_ATS_using_google_gemini_pro_vision

## Install Requirements

1. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

## Add Your API Key

2. Create a `.env` file and store the Google Gemini API key:
    ```sh
    echo GOOGLE_API_KEY="your_api_key" > .env
    ```

## Create a Virtual Environment

3. Create a virtual environment:
    ```sh
    conda create -p venv python==3.10
    ```

4. Start the virtual environment:
    ```sh
    conda activate venv/
    ```

## Install Poppler

5. Download and install Poppler for Windows:
    - Go to the [Poppler for Windows GitHub releases page](https://github.com/oschwartz10612/poppler-windows/releases).
    - Download the latest release (e.g., `Release-XX.XX.XX.zip`).
    - Extract the downloaded zip file.
    - Move the extracted folder to a convenient location (e.g., `C:\poppler`).

6. Add Poppler to the PATH:
    - Open the Start Menu and search for "Environment Variables".
    - Select "Edit the system environment variables".
    - In the System Properties window, click the "Environment Variables" button.
    - In the Environment Variables window, find the `Path` variable in the "System variables" section and select it. Click "Edit".
    - In the Edit Environment Variable window, click "New" and add the path to the Poppler `bin` directory (e.g., `C:\poppler\bin`).
    - Click "OK" to close all the windows.

7. Verify the Poppler installation:
    ```sh
    pdfinfo -v
    ```

    If Poppler is correctly installed, you should see version information printed out.

## Run App Using Streamlit

8. Run the app:
    ```sh
    streamlit run app.py
    ```