# Flask API Template

This is a simple Flask API with multiple endpoints for handling both **GET** and **POST** requests.

## How to Run the API

1. Install Flask (if not already installed):
   ```sh
   pip install flask
   ```
2. Save the script as `app.py`.
3. Run the Flask server:
   ```sh
   python app.py
   ```
4. The API will be available at:
   ```
   http://127.0.0.1:5000/
   ```

## API Endpoints

### 1. Root Endpoint `/`
- **Method:** `POST` or `GET`
- **Description:** Responds to a message input.
- **Request (JSON for POST):**
  ```json
  {"msg": "ping"}
  ```
- **Response:**
  - If `msg` is "ping":
    ```json
    {"response": "Pong"}
    ```
  - If no data provided:
    ```json
    {"response": "You forgot to say Hi"}
    ```
  - Otherwise:
    ```json
    {"response": "We not talking"}
    ```

### 2. `/tellme`
- **Method:** `GET`
- **Description:** Returns a static security-related message.
- **Response:**
  ```
  Security is overrated
  ```

### 3. `/submit`
- **Method:** `GET`
- **Description:** Returns a personalized message based on query parameters.
- **Request:**
  ```sh
  curl "http://127.0.0.1:5000/submit?name=Alice"
  ```
- **Response:**
  ```
  Technology sucks - Dr. Alice
  ```
  If no name is provided, it defaults to "Unknown":
  ```
  Technology sucks - Dr. Unknown
  ```

### 4. `/postbody`
- **Method:** `POST`
- **Description:** Accepts a JSON body with a `who` field and returns a personalized message.
- **Request (JSON Body):**
  ```json
  {"who": "Alice"}
  ```
- **Response:**
  ```
  Technology sucks - Dr. Alice
  ```
  If `who` is not provided, it may return an error or unexpected output.

## Testing with `curl`
Here are some example `curl` commands to test the endpoints:

### Test Root Endpoint
```sh
curl -X POST http://127.0.0.1:5000/ -H "Content-Type: application/json" -d '{"msg": "ping"}'
```

### Test `/tellme`
```sh
curl http://127.0.0.1:5000/tellme
```

### Test `/submit`
```sh
curl "http://127.0.0.1:5000/submit?name=Alice"
```

### Test `/postbody`
```sh
curl -X POST http://127.0.0.1:5000/postbody -H "Content-Type: application/json" -d '{"who": "Alice"}'
```

## Conclusion
This API provides simple message interactions with both **GET** and **POST** methods. Feel free to expand on it as needed!

