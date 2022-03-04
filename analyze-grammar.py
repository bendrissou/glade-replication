"""
This script takes as argument a grammar, and counts the number 
of non-terminals, rules, and terminals.
The goal is to provide information on size and complexity of Glade synthesized grammars.
"""

import json

def count(grammar):
    keys = len(grammar.keys())
    rules = len([r for k in grammar for r in grammar[k]])

    terminals = []
    nonterminals = []
    for k in grammar:
        for r in grammar[k]:
            index = 0
            is_token = True
            for t in r:
                if t and (t[0], t[-1]) == ('<','>'):
                    nonterminals.append(t)
                    is_token = False
                else:
                    terminals.append(t)
                    index += 1
            if is_token and index > 1:
                del terminals[-index:]
                terminals.append(''.join(r))

    return keys, rules, terminals

def main(g):
    with open('learn/handwritten/%s.json' % g) as f:
        data = f.read()
    grammar = json.loads(data)

    keys, rules, terminals = count(grammar)

    output = "\n ++++++++ Stats of the " + str(g) + " handwritten grammar ++++++++ "
    output = output + "\nTotal number of non-terminals: " + str(keys)
    output = output + "\nTotal number of rules: " + str(rules)
    output = output + "\nTotal number of terminals: " + str(len(set(terminals)))

    with open('learn/synthesized/%s.json' % g) as f:
        data = f.read()
    grammar = json.loads(data)

    keys, rules, terminals = count(grammar)

    output = "\n\n ++++++++ Stats of the " + str(g) + " synthesized grammar ++++++++ "
    output = output + "\nTotal number of non-terminals: " + str(keys)
    output = output + "\nTotal number of rules: " + str(rules)
    output = output + "\nTotal number of terminals: " + str(len(set(terminals)))

    print(output)

    file2 = open('learn/results/eval_%s_grammar.txt' % g, 'w')
    file2.write(output)
    file2.close()

if __name__ == '__main__':
    import sys
    main(sys.argv[1])
