#!/usr/bin/env python3
from glob import glob
import os.path

from rich.console import Console
from rich.table import Table

import json, os

with open('antlr4/config.json') as fp:
    data = json.load(fp)
    antlr_programs = data['antlr_programs']

def is_nonterminal(t):
    return (t[0], t[-1]) == ('<', '>')

def count(grammar):
    non_terminals = len([k for k in grammar])
    rules = len([r for k in grammar for r in grammar[k]])
    all_terminals = {t for k in grammar for r in grammar[k] for t in r if t and not is_nonterminal(t)}
    terminals = len(all_terminals)
    return non_terminals, rules, terminals

def process_file(fname):
    project = fname[len("learn/handwritten/"):-len(".json")]
    with open('learn/handwritten/%s.json' % project) as f:
        data = f.read()
    if project in antlr_programs: grammar = json.loads(data)['[grammar]']
    else: grammar = json.loads(data)
    nt, rules, terms = count(grammar)

    return (project, str(nt), str(rules), str(terms))

console = Console()

table  = Table(show_header=True, header_style='bold #2070b2',
          title='[bold]Table [#2070b2]III[/#2070b2]')
for k in ['Grammar', 'Non-terminals', 'Rules', 'Terminals']:
    table.add_column(k)

with open('order.json') as f:
    order = json.load(fp=f)

#table_3_files = [f for f in glob("learn/handwritten/*.json")]
table_3_files = ["learn/handwritten/%s.json" % f for f in order]
for f in table_3_files:
    if not os.path.exists(f): continue
    v = process_file(f)
    if v is None: continue
    table.add_row(*v)

console.print(table)
