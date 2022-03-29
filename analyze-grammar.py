"""
This script takes as argument a grammar, and counts the number 
of non-terminals, rules, and terminals.
The goal is to provide information on size and complexity of Glade synthesized grammars.
"""

import json

f = open('antlr4/config.json')
data = json.load(f)
antlr_programs = data['antlr_programs']
f.close()

def is_nonterminal(t):
    if len(t) < 2: return False
    return (t[0], t[-1]) == ('<', '>')

def count(grammar):
    non_terminals = len([k for k in grammar])
    rules = len([r for k in grammar for r in grammar[k]])
    all_terminals = {t for k in grammar for r in grammar[k] for t in r if not is_nonterminal(t)}
    terminals = len(all_terminals)
    return non_terminals, rules, terminals

def main(g):
    with open('learn/handwritten/%s.json' % g) as f:
        data = f.read()
    if g in antlr_programs: grammar = json.loads(data)['[grammar]']
    else: grammar = json.loads(data)

    keys, rules, terminals = count(grammar)

    output = "\n ++++++++ Stats of the " + str(g) + " handwritten grammar ++++++++ "
    output = output + "\nTotal number of non-terminals: " + str(keys)
    output = output + "\nTotal number of rules: " + str(rules)
    output = output + "\nTotal number of terminals: " + str(terminals)

    with open('learn/synthesized/%s.json' % g) as f:
        data = f.read()
    grammar = json.loads(data)

    keys, rules, terminals = count(grammar)

    output = output + "\n\n ++++++++ Stats of the " + str(g) + " synthesized grammar ++++++++ "
    output = output + "\nTotal number of non-terminals: " + str(keys)
    output = output + "\nTotal number of rules: " + str(rules)
    output = output + "\nTotal number of terminals: " + str(terminals)

    print(output)

    file2 = open('learn/results/eval_%s_grammar.txt' % g, 'w')
    file2.write(output)
    file2.close()

if __name__ == '__main__':
    import sys
    main(sys.argv[1])
