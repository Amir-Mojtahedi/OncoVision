# Project Setup Guide

This guide outlines the steps to set up and run the backend server for this project using Anaconda/Miniconda.

## 1. Prerequisites: Install Anaconda or Miniconda

This project uses Conda to manage environments and dependencies, defined in `environment.yml` (for Windows/Linux) and `environment-mac.yml` (for macOS). You need to have either Anaconda or Miniconda installed.

* **Anaconda:** A full distribution including Conda, Python, and many scientific packages.
* **Miniconda:** A minimal installer containing only Conda, Python, and their essential dependencies.

Choose one and download it from the official website:

* **Download Anaconda:** [Anaconda Distribution](https://www.anaconda.com/products/distribution)
* **Download Miniconda:** [Miniconda Installers](https://docs.conda.io/en/latest/miniconda.html)

Follow the installation instructions for your operating system provided on the download pages. After installation, open your terminal (Anaconda Prompt on Windows, or your standard terminal on macOS/Linux) to verify the installation:

```sh
conda --version
```

## 2. Navigate to the Backend Directory
Before running the backend code, ensure that you are inside the `back-end` directory. If you are not, navigate to it using the terminal or command prompt:

```sh
cd back-end
```

## 3. Create the Conda Environment

Use the appropriate `.yml` file to create the Conda environment. This command will create an environment called `OncoVision`.

* **On Windows or Linux:**

    ```bash
    conda env create -f environment.yml
    ```

* **On macOS:**

    ```bash
    conda env create -f environment-mac.yml
    ```

This process might take a few minutes as Conda resolves and downloads the required packages.

### 4. Activate the Conda Environment

Once the environment is created, you need to activate it.

```bash
conda activate OncoVision
```

## 5. Run the Backend Server
Once all dependencies are installed, start the backend server by running:

```sh
flask run --debug
```

The backend should now be running and ready for use!

## 6. Verify the Setup
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

