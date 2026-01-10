#!/usr/bin/env python3
import os


def print_virtual_env():
    try:
        env = os.environ['VIRTUAL_ENV']
        print(f"Your current virtual env is {env}")
    except KeyError:
        print("No active virtual environment")


def main():
    print_virtual_env()


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(e)
