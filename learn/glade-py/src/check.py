import sys
import subprocess
import json
sys.path.append("../..")

import earley_parser as parser

f = open('../../../antlr4/config.json')
data = json.load(f)
antlr_programs = data['antlr_programs']
f.close()

exec_map = {}

def check(s, p, label=None):
    if s in exec_map: 
        # Input already tested
        return exec_map[s]
    if p in antlr_programs: v =  _check_antlr(s, p)
    else: v =  _check(s, p)
    exec_map[s] = v
    return v

def _check(s, p):
	try:
		parser.check(s, p)
		# Valid input
		return True

	except Exception as e:
		# Invalid input
		return False

def _check_antlr(s, p):
	try:
		file1 = open('input', 'w')
		file1.write(s)
		file1.close()
		result = subprocess.check_output(get_command(p), shell=True, stderr=subprocess.STDOUT, timeout=10)
		output = result.decode('utf-8')
		if output == '': 
			return True
		else:
			return False
	except Exception as e:
		print("Error: "+str(e))
		return False

def get_command(p):
    cmd = 'python3 ../../../antlr4/' + p + '/parse.py input'
    return cmd
