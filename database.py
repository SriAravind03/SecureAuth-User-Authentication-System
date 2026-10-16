import sqlite3

DATABASE = "users.db"

def get_db_connection():
    """Establishes a database connection with a timeout of 5 seconds."""
    conn = sqlite3.connect(DATABASE, timeout=5)
    conn.row_factory = sqlite3.Row  # Enables dictionary-like row access
    return conn

def init_db():
    """Creates the 'users' table if it does not exist."""
    with get_db_connection() as conn:
        c = conn.cursor()
        c.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                email TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL
            )
        """)
        conn.commit()
    print("✅ Database initialized successfully.")

# Run this function only when this file is executed directly
if __name__ == "__main__":
    init_db()

