#!/usr/bin/env python3
from glob import glob
import json, os

from rich.console import Console
from rich.table import Table

def process_file(f):
    fname = f[len("learn/results/info_"):-len(".txt")]
    # LTime, Seed Len, Sigma, Checks
    with open(f) as file:
        txt = file.readlines()
        ltime = [t for t in txt if t.startswith('Time taken to learn')][0].split(':')[1].strip()
        stats_ = [t for t in txt if t.startswith('Average length of seeds')][0].split(':')[1].strip().split(' ')
        avg, stddev = float(stats_[0]), float(stats_[2])
        checks = int([t for t in txt if t.startswith('Total number of checks:')][0].split(':')[1].strip())
        c = "{:,d}".format(checks)
    return (fname, "%2.2f" % float(ltime), "%2.2f" % avg, "%2.2f" % stddev, c)
    #return "%s|%2.2f|%2.2f|%2.2f|%s" % (fname, "%2.2f" % float(ltime), "%2.2f" % avg, "%2.2f" % stddev, c)

console = Console()

table  = Table(show_header=True, header_style='bold #2070b2',
          title='[bold]Table [#2070b2]I[/#2070b2]')
for k in ['Grammar', 'LTime(s)', 'Seed Len', 'σ', 'Checks']:
    table.add_column(k)

with open('order.json') as f:
    order = json.load(fp=f)

#table_1_files = [f for f in glob("learn/results/info_*.txt")]
table_1_files = [("learn/results/info_%s.txt") % f for f in order]
for f in table_1_files:
    if not os.path.exists(f): continue
    table.add_row(*process_file(f))

console.print(table)
