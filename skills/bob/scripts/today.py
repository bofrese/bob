#!/usr/bin/env python3
"""Print today's date as YYYY-MM-DD. Usage: today.py [--selftest]"""
import re
import sys
from datetime import date


def today():
    return date.today().isoformat()


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        assert re.fullmatch(r"\d{4}-\d{2}-\d{2}", today())
        print("ok")
    else:
        print(today())
