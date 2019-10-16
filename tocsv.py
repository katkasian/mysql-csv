import sqlite3
import argparse
import csv

parser = argparse.ArgumentParser(description = "dbname")
parser.add_argument("db", type = str, help = "dbname")
args =  parser.parse_args()

conn = sqlite3.connect(args.db)
c = conn.cursor()
c.execute("SELECT * FROM tweets")
fname = args.db.split(".")[0] + "csv"

with open(fname, w) as out_csv_file:
    csv_out = csv.writer(out_csv_file)
    csv_out.writerow([d[0] for d in c.description])
    for result in c:
        csv_out.writerow(result)
conn.close()
