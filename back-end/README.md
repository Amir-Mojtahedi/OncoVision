# Project Setup Guide

## 1. Navigate to the Backend Directory
Before running the backend code, ensure that you are inside the `back-end` directory. If you are not, navigate to it using the terminal or command prompt:

```sh
cd back-end
```

## 2. Install Python
Make sure you have Python installed on your system. It is recommended to install the **Long-Term Support (LTS) version** from the official Python website:

[Download Python](https://www.python.org/downloads/)

To verify that Python is installed, run:

```sh
python --version
```

or

```sh
python3 --version
```

## 3. Create a Virtual Environment
It is best practice to use a virtual environment to manage dependencies. To create a virtual environment named `.venv`, run the following command:

```sh
python -m venv .venv
```

## 4. Activate the Virtual Environment
Once the virtual environment is created, you need to activate it:

- **On Windows (Command Prompt):**
  ```sh
  .venv\Scripts\activate
  ```
- **On Windows (PowerShell):**
  ```sh
  .venv\Scripts\Activate.ps1
  ```
- **On macOS/Linux:**
  ```sh
  source .venv/bin/activate
  ```

After activation, your terminal prompt should change to indicate that the virtual environment is active.

## 5. Ensure `pip` is Installed
Check if `pip` (Python’s package manager) is installed and up to date:

```sh
python -m ensurepip --default-pip
python -m pip install --upgrade pip
```

## 6. Install Required Dependencies
The backend dependencies are listed in `requirements.txt`. Install them by running:

```sh
pip install -r requirements.txt
```

## 7. Run the Backend Server
Once all dependencies are installed, start the backend server by running:

```sh
flask run --debug
```

The backend should now be running and ready for use!

## 8. Verify the Setup
To confirm that the backend is running correctly, make a `GET` request to `http://127.0.0.1:5000/api/status` using Postman or `curl`.

- **Using Postman:** Send a `GET` request to `http://127.0.0.1:5000/api/status`.
- **Using `curl`:** Run the following command in your terminal:
  
  ```sh
  curl -X GET http://127.0.0.1:5000/api/status
  ```

You should receive a JSON response:

```json
{
    "status": "ok",
    "statusCode": 200
}
```

