from pathlib import Path
import os
import environ


def get_env_value(env_key: str) -> str:
    env = environ.Env()

    env.read_env(os.path.join(Path(__file__).resolve().parent.parent, '.env'))
    print(env('SECRET_KEY'))
    return env(env_key)
