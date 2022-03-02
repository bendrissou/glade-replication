learn:
	cd learn/glade-py/src && python3 glade.py url
	cd learn/glade-py/src && python3 glade.py lisp
	cd learn/glade-py/src && python3 glade.py xml
	cd learn/glade-py/src && python3 glade.py \grep
	cd learn/glade-py/src && python3 glade.py json
	cd learn/glade-py/src && python3 glade.py ints
	cd learn/glade-py/src && python3 glade.py decimals
	cd learn/glade-py/src && python3 glade.py floats
	cd learn/glade-py/src && python3 glade.py bin_any_paren
	cd learn/glade-py/src && python3 glade.py bin_paren
	cd learn/glade-py/src && python3 glade.py bool_add
	cd learn/glade-py/src && python3 glade.py palindromes
	cd learn/glade-py/src && python3 glade.py paren
	cd learn/glade-py/src && python3 glade.py two_any_paren_d
	cd learn/glade-py/src && python3 glade.py two_paren
	cd learn/glade-py/src && python3 glade.py two_paren_d
	cd learn/glade-py/src && python3 glade.py lua
	cd learn/glade-py/src && python3 glade.py pascal
	cd learn/glade-py/src && python3 glade.py mysql
	cd learn/glade-py/src && python3 glade.py xpath
	cd learn/glade-py/src && python3 glade.py c
	cd learn/glade-py/src && python3 glade.py tinyc
	cd learn/glade-py/src && python3 glade.py tiny
	cd learn/glade-py/src && python3 glade.py basic

earleyjava:
	cd learn/EarleyJava && make compile

analyze:
	python3 analyze-grammar.py url
	python3 analyze-grammar.py lisp
	python3 analyze-grammar.py xml
	python3 analyze-grammar.py \grep
	python3 analyze-grammar.py ints
	python3 analyze-grammar.py decimals
	python3 analyze-grammar.py floats
	python3 analyze-grammar.py bin_any_paren
	python3 analyze-grammar.py bin_paren
	python3 analyze-grammar.py bool_add
	python3 analyze-grammar.py palindromes
	python3 analyze-grammar.py paren
	python3 analyze-grammar.py two_any_paren_d
	python3 analyze-grammar.py two_paren
	python3 analyze-grammar.py two_paren_d
	python3 analyze-grammar.py lua
	python3 analyze-grammar.py pascal
	python3 analyze-grammar.py mysql
	python3 analyze-grammar.py xpath
	python3 analyze-grammar.py c
	python3 analyze-grammar.py tinyc
	python3 analyze-grammar.py tiny
	python3 analyze-grammar.py basic

eval:
	cd learn/results && make eval SUBJECT=url
	cd learn/results && make eval SUBJECT=lisp
	cd learn/results && make eval SUBJECT=xml
	cd learn/results && make eval SUBJECT=\grep
	cd learn/results && make eval SUBJECT=ints
	cd learn/results && make eval SUBJECT=decimals
	cd learn/results && make eval SUBJECT=floats
	cd learn/results && make eval SUBJECT=json
	cd learn/results && make eval SUBJECT=bin_any_paren
	cd learn/results && make eval SUBJECT=bin_paren
	cd learn/results && make eval SUBJECT=bool_add
	cd learn/results && make eval SUBJECT=palindromes
	cd learn/results && make eval SUBJECT=paren
	cd learn/results && make eval SUBJECT=two_any_paren_d
	cd learn/results && make eval SUBJECT=two_paren
	cd learn/results && make eval SUBJECT=two_paren_d
	cd learn/results && make eval-antlr-precision SUBJECT=lua
	cd learn/results && make eval-antlr-precision SUBJECT=pascal
	cd learn/results && make eval-antlr-precision SUBJECT=mysql
	cd learn/results && make eval-antlr-precision SUBJECT=xpath
	cd learn/results && make eval-antlr-precision SUBJECT=c
	cd learn/results && make eval-antlr-precision SUBJECT=tinyc
	cd learn/results && make eval-antlr SUBJECT=tiny
	cd learn/results && make eval-antlr-precision SUBJECT=basic







