#!/usr/bin/env python3

import smtplib
import argparse
import email
import sys
import email.message

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--from-field", type=str, help="From", required=True)
parser.add_argument("-t", "--to-field", type=str, nargs="+", help="To", required=True)
parser.add_argument("-s", "--subject", type=str, help="Subject", required=True)
parser.add_argument("-m", "--message", type=str, help="messages", required=True)
parser.add_argument("-S", "--server", type=str, help="server", required=True)
args = parser.parse_args()

message = email.message.EmailMessage()
message["From"] = args.from_field
message["To"] = args.to_field
message["Subject"] = args.subject
message.set_content(args.message)

try:
    print(message)
    with smtplib.SMTP(args.server) as server:
        server.send_message(message)
    print("Sent!")
except Exception as exc:
    print(f"Exception: {exc!r} {exc!s}")
    sys.exit(1)
