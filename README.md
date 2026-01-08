# FastApi Tutorial

## Installation
Use command: `pip install "fastapi[standard]"` to install the full standard version of fastapi and uvicorn server and others

> Note: make sure you have python and pip are installed, pip is added to path. After installation of fastapi make sure to restart the terminal, otherwise uvicorn not found error will pop

Command to start the server:
`uvicorn [module_name]:[variable_name] --reload`
- [`module_name`]: This is the Python file (without the `.py`). If your file is `server.py`, you use `server`.
- [`variable_name`]: This is the name of the variable where you created the FastAPI instance inside that file (usually `app = FastAPI()`).
- `--reload`: This is a flag that tells Uvicorn to "watch" your files. Every time you hit **Ctrl+S** (save), the server restarts itself so you can see your changes instantly.

