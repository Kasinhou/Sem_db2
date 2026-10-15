# Pripojenie na Oracle databazu.

import os
from pathlib import Path

import oracledb
from dotenv import load_dotenv

# .env je v o uroven vyssie ako /src
PROJECT_ROOT = Path(__file__).resolve().parent.parent
load_dotenv(PROJECT_ROOT / ".env")

# Vytvori a vrati nove spojenie na Oracle databazu
def get_connection():
    user = os.getenv("ORACLE_USER")
    password = os.getenv("ORACLE_PASSWORD")
    dsn = os.getenv("ORACLE_DSN")

    missing = [name for name, value in (
        ("ORACLE_USER", user),
        ("ORACLE_PASSWORD", password),
        ("ORACLE_DSN", dsn),
    ) if not value]
    if missing:
        raise RuntimeError(
            "Chybaju hodnoty v .env: " + ", ".join(missing)
        )

    return oracledb.connect(user=user, password=password, dsn=dsn)


def test_connection():
    # Skuska pripojenia na db
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT USER, SYSTIMESTAMP FROM DUAL")
            return cur.fetchone()


if __name__ == "__main__":
    try:
        db_user, server_time = test_connection()
        print("Pripojenie OK.")
        print(f"Prihlaseny pouzivatel: {db_user}")
        print(f"Cas servera: {server_time}")
    except Exception as exc:
        print("Pripojenie ZLYHALO:")
        print(f"{type(exc).__name__}: {exc}")
