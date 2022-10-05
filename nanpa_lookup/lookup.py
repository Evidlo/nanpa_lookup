#!/usr/bin/env python3

import sqlite3
import re
import os
import sys
import pprint
import argparse
from datetime import datetime, timedelta
import time
import subprocess


def lookup_number(db, number):
    """Look up single number

    Args:
        db (sqlite3.Connection): numbers database
        number (str): number to lookup

    Returns:
        dict: dict w/ fields 'company', 'email', 'npanxxy', 'ocn', 'type'
    """
    regex = "(?:\+1)?([0-9]{3})-?([0-9]{3})-?([0-9])?(?:[0-9]{3})?"
    match = re.search(regex, number)

    if match is None:
        print("Invalid number")
        return
        # sys.exit()

    npa, nxx, dig7 = match.groups()

    c = db.cursor()

    query = "SELECT * FROM numbers WHERE npanxxy={}"
    result = c.execute(query.format(npa + nxx)).fetchone()
    # print(result.fetchone())

    # try searching without dig7
    if result is None and dig7 is not None:
        result = c.execute(query.format(npa + nxx + dig7)).fetchone()

    if result is None:
        print("No matches found")
        return
        # sys.exit()

    return dict(result)

def android_pull(days):
    """Pull call logs from Android and retrieve all numbers from last N days

    Args:
        days (int): get numbers from last N days

    Returns:

    """
    date_millis = time.mktime((datetime.now() - timedelta(days=days)).timetuple()) * 1000
    subprocess.check_output("adb root", shell=True)
    subprocess.check_output(
        "adb pull /data/data/com.android.providers.contacts/databases/calllog.db",
        shell=True
    )
    calllog = sqlite3.connect("calllog.db")
    calllog.row_factory = sqlite3.Row
    numbers = calllog.cursor().execute(
        f"""SELECT normalized_number FROM calls WHERE date >= {date_millis}
        AND matched_number IS NULL"""
    ).fetchall()

    return [n['normalized_number'] for n in numbers]

def main():

    pp = pprint.PrettyPrinter()

    parser = argparse.ArgumentParser(description="Look up number in NANPA database")
    parser.add_argument("-n", type=str, help="number")
    parser.add_argument("-f", type=str, help="file containing list of numbers")
    parser.add_argument("-a", type=int, default=30, help="pull numbers from ADB device")
    parser.add_argument("--field", type=str, help="print out specific field (company, npanxxy, type, ocn, email)")
    parser.add_argument("--query", type=str, help="make arbitrary SQL query")
    parser.add_argument("--database", type=str, default=None, help="numbers database")
    args = parser.parse_args()

    if args.database is None:
        args.database = os.path.join(os.path.dirname(__file__), 'database.sqlite')
    db = sqlite3.connect(args.database)
    db.row_factory = sqlite3.Row
    columns = db.cursor().execute("SELECT * FROM numbers").fetchone().keys()

    if args.n is not None:
        numbers = [args.n]
    elif args.f is not None:
        with open(args.f, 'r') as f:
            numbers = f.readlines()
    elif args.a:
        numbers = android_pull(args.a)

    for n, number in enumerate(numbers):
        result = lookup_number(db, number)

        if result is None:
            continue

        if args.field is not None:
            if args.field in columns:
                print(result[args.field])
            else:
                print(f"No such field {args.field}")
        else:
            pp.pprint(result)

if __name__ == '__main__':
    main()
