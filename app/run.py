# run.py
import uvicorn
from app import main

if __name__ == "__main__":
    try:
        uvicorn.run(main.app, host="0.0.0.0", port=8000, log_level="info", reload=True)
    except KeyboardInterrupt:
        print("Shutting down gracefully...")
    except Exception as e:
        print(f"Unexpected error: {e}")
    finally:
        print("Server stopped.")
