import os
import subprocess
import sys


def ensure_correct_env(expected_name: str) -> None:
    venv_path = os.environ.get("VIRTUAL_ENV")
    if not venv_path:
        raise RuntimeError("VIRTUAL_ENV is not set. Activate the required virtual environment.")

    if os.path.basename(venv_path) != expected_name:
        raise RuntimeError(f"Wrong virtual env: {venv_path}. Expected: {expected_name}")


def write_requirements_install_file(filename: str) -> None:
    content = "beautifulsoup4\npytest\n"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)


def pip_install_requirements(req_file: str) -> None:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", req_file])


def print_installed_packages() -> None:
    subprocess.check_call([sys.executable, "-m", "pip", "freeze"])


def freeze_to_requirements(filename: str) -> None:
    with open(filename, "w", encoding="utf-8") as f:
        subprocess.check_call([sys.executable, "-m", "pip", "freeze"], stdout=f)


def main() -> None:
    ensure_correct_env("denishac")

    temp_req = "requirements_install.txt"
    final_req = "requirements.txt"

    write_requirements_install_file(temp_req)
    pip_install_requirements(temp_req)

    print_installed_packages()
    freeze_to_requirements(final_req)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
        raise
