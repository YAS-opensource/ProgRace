import os

from src import app

if __name__ == "__main__":
    # Use port 3000 if no PORT variable found in environment
    PORT = int(os.environ.get("PORT", 3000))
    app.run(host="0.0.0.0", port=PORT)
