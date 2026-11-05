import argparse

from dateutil.parser import parse
from dateutil.relativedelta import relativedelta

parser = argparse.ArgumentParser()
parser.add_argument("--name", default="World")
args = parser.parse_args()

diff = relativedelta(parse("15 March 2000"), parse("1 January 2000"))
print(f"Hello, {args.name}! From 1 January to 15 March: {diff.months} months, {diff.days} days")