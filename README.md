# FastApi Tutorial

## Installation
Use command: `pip install "fastapi[standard]"` to install the full standard version of fastapi and uvicorn server and others

> Note: make sure you have python and pip already installed, pip is added to path. After installation of fastapi make sure to restart the terminal, otherwise uvicorn not found error will pop

### troubleshooting installation
Error: `'pip' is not recognized as an internal or external command, operable program or batch file.`

Fix:
- Option 1: The Quick Bypass
  - `python -m pip install "fastapi[standard]"`
- Option 2: The Permanent Fix (Adding to Path)
  - Find your Python Scripts folder: It is usually located at: `C:\Users\YourUsername\AppData\Local\Programs\Python\Python312\Scripts` (Look for the folder that contains pip.exe).
  - Open Environment Variables:
    - Press the Windows Key and type "Env".
    - Select "Edit the system environment variables".
    - Click Environment Variables at the bottom right.
  - Edit the Path:
    - Under "System variables", find Path and click Edit.
    - Click New and paste the path to your Scripts folder.
  - Restart your Terminal: Close Command Prompt/VS Code and reopen it for the changes to take effect.


Error: `uvicorn : The term 'uvicorn' is not recognized as the name of a cmdlet, function, script file, or operable program. Check the spelling of the name, or if a path was included, verify that the path is correct and try again.`

Fix: This error is the "cousin" of the pip error
- Same steps as `pip`
- If same steps already completed (during pip fix): its probably you need to restart your terminal

## Starting the server
Command to start the server:
`uvicorn [module_name]:[variable_name] --reload`
- [`module_name`]: This is the Python file (without the `.py`). If your file is `server.py`, you use `server`.
- [`variable_name`]: This is the name of the variable where you created the FastAPI instance inside that file (usually `app = FastAPI()`).
- `--reload`: This is a flag that tells Uvicorn to "watch" your files. Every time you hit **Ctrl+S** (save), the server restarts itself so you can see your changes instantly.

> if the module is inside another subfolder: use `.` to show the path, example: 
if project structure : `api/main.py`
command to run: `uvicorn api.main:app --reload` 


> Misconception: People think `--reload` should be used in production. False. It’s heavy on resources and only for development. In production, you'd use a stable process manager.

## FastApi Docs
A POST request is the standard way to create or send data to a server.

For code: `@app.post("/create")`
When you type `http://127.0.0.1:8000/create` directly into your browser's address bar and hit Enter, the browser always sends a GET request. FastAPI sees the browser asking for a **"GET"** and says: **"I have a route for /create, but not for GET. Method Not Allowed."**

### Fix:
- Use the Built-in Documentation
  - Go to `http://127.0.0.1:8000/docs`. (whatever server address)
  - Click on the **POST** button for `/create`.
  - Click **"Try it out"**.
  - Edit the JSON body (put in a name and price).
  - Click **Execute**.
- Use tools like **Postman or Hoppscotch**