#!/usr/bin/env python3
from glob import glob
import json, os, os.path

from rich.console import Console
from rich.table import Table

def process_file(fname):
    # learn/results/eval_XXX_precision.txt
    # learn/results/eval_XXX_recall.txt
    project = fname[len("learn/results/eval_"):-len("_precision.txt")]
    if not os.path.exists("learn/results/eval_%s_recall.txt" % project): return None
    with open("learn/results/eval_%s_precision.txt" % project) as pf:
        pval_1, pval_2 = pf.read().strip().split(':')[1].strip().split('/')
        pval = (int(pval_1)*1.0/int(pval_2))
        pval_s = "%2.2f" % (pval)

    rval_1, rval_2 = 0, 0
    with open("learn/results/eval_%s_recall.txt" % project) as rf:
        for line in rf.readlines():
            r_1, r_2 = line.strip().split(':')[1].strip().split('/')
            rval_1 += int(r_1)
            rval_2 += int(r_2)

    rval = (rval_1*1.0/rval_2)
    rval_s = "%2.2f" % rval
    f1 = "%2.2f" % (2*pval*rval/(pval+rval))

    if not os.path.exists('learn/synthesized/%s.json' % project):
        size = '_'
    else:
        size = "%2.2f" % (os.path.getsize('learn/synthesized/%s.json' % project)/1024.0)

    return (project, pval_s, rval_s, f1, size)

console = Console()

table  = Table(show_header=True, header_style='bold #2070b2',
          title='[bold]Table [#2070b2]II[/#2070b2]')
for k in ['Grammar', 'Precision', 'Recall', 'F1', 'Size(KB)']:
    table.add_column(k)

with open('order.json') as f:
    order = json.load(fp=f)

#table_2_files = [f for f in glob("learn/results/eval_*_precision.txt")]
table_2_files = ["learn/results/eval_%s_precision.txt" % f for f in order]
for f in table_2_files:
    if not os.path.exists(f): continue
    v = process_file(f)
    if v is None: continue
    table.add_row(*v)

console.print(table)
