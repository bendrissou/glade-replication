# Replication for "Synthesizing Input Grammars: A Replication Study"

##  Overview

This is the virtual machine replication package for
 "Synthesizing Input Grammars: A Replication Study"
 which was submitted as paper-id `453`.

The Replication package is provided as Zenodo DOI is

```
https://doi.org/10.5281/zenodo.6326396
```

The corresponding GitHub repository for replication is:

```
https://github.com/bendrissou/glade-replication
```

### Time for Evaluation

The learning time for all grammars is 4 days (Table 1). With evaluation of
results, the complete run can take more than one week.

Our submission contains 5 tables. These are:

1. Glade II execution
2. Glade II scores
3. Source Grammars
4. Synthesized GLADE-II grammars
5. Glade Learning Accuracy

We show how to replicate all tables 1, 2, 3, and 4.

Table 5 contains a subset of Table 2 results and Arvada results that we quote
from that paper. Hence, we do not replicate it.

The complete source code of our implementation of
GLADE is provided at

```
 https://github.com/bendrissou/PyGlade
```

## Prerequisites

### RAM
All experiments were done with 10GB of RAM.

##  Getting started

Install the following software:

* Vagrant [Version 2.2.9](https://releases.hashicorp.com/vagrant/2.2.9/vagrant_2.2.9_x86_64.deb) 
* Virtualbox [Version 6.1.10](https://download.virtualbox.org/virtualbox/6.1.10/virtualbox-6.1_6.1.10-138449~Ubuntu~xenial_amd64.deb) 

Next, download the following files from the Zenodo DOI
to the directory `replication-453`

* pyglade.box

**Check:** change to `replication-453`, and ensure that the following files are
present:

```
$ cd replication-453
$ ls
pyglade.box

$ du -ksh pyglade.box
1.6G    pyglade.box

$ md5sum pyglade.box
9d2f6d486a762a18845899eb2f99ceac *pyglade.box
```

### Importing the box

Execute the following command to launch the virtual machine:

```
$ vagrant box add pyglade ./pyglade.box
==> box: Box file was not detected as metadata. Adding it directly...
==> box: Adding box 'pyglade' (v0) for provider:
    box: Unpacking necessary files from: file:///path/to/pyglade/pyglade.box
==> box: Successfully added box 'pyglade' (v0) for 'virtualbox'!
```

### Bring up the virtual machine

The following command will bring up the virtual machine.

```
$ vagrant init pyglade
$ vagrant up
Bringing machine 'default' up with 'virtualbox' provider...
==> default: Importing base box 'pyglade'...
==> default: Matching MAC address for NAT networking...
==> default: Setting the name of the VM: replication_default_1646422743780_54483
==> default: Clearing any previously set network interfaces...
==> default: Preparing network interfaces based on configuration...
    default: Adapter 1: nat
==> default: Forwarding ports...
    default: 22 (guest) => 2222 (host) (adapter 1)
==> default: Booting VM...
==> default: Waiting for machine to boot. This may take a few minutes...
    default: SSH address: 127.0.0.1:2222
    default: SSH username: vagrant
    default: SSH auth method: private key
    default: Warning: Connection reset. Retrying...
    default: Warning: Remote connection disconnect. Retrying...
==> default: Machine booted and ready!
==> default: Checking for guest additions in VM...
    default: Guest Additions Version: 5.2.42
    default: VirtualBox Version: 6.1
==> default: Mounting shared folders...
    default: /vagrant => /path/to/pyglade
```

### Verify the box import.

The commands inside the guest system are indicated by a `vm$ ` prefix.
Anytime `vm$ ` is used, it means to either ssh into the vagrant box as
below, or if you are already in the VM, use the shell inside VM.

```
$ vagrant ssh

vm$ free -g
              total        used        free      shared  buff/cache   available
Mem:              9           0           9           0           0           9
Swap:             0           0           0
```

### Procedure

You will find the code repository "glade-replication" in the home directory of the virtual machine, enter directory:

```
vm$ pwd
/home/vagrant
vm$ cd glade-replication
vm$ ls
Makefile  README.md  analyze-grammar.py  antlr4  learn
```

#### Experiments

These are the provided experiments:

1. URL
2. Lisp
3. XML
4. Grep
5. Ints
6. Decimals
7. Floats
8. JSON
9. Palindrome
10. Paren
11. BoolAdd
12. TwoParenD
13. TwoAnyParenD
14. BinParen
15. BinAnyParen
16. Tiny
17. Lua
18. Pascal
19. MySQL
20. XPath
21. C
22. TinyC
23. Basic

##### Learning the `ints` grammar

To show how we can run one experiment at a time, we use the `ints` as an example.
To learn the `ints` grammar, execute:

```
vm$ (cd learn/glade-py/src; python3 glade.py ints)
```

After the command is executed, you should find the inferred grammar `ints.json` in the folder `learn/synthesized`

```
vm$ ls learn/synthesized/
ints.json
```

You can inspect the grammar as follows:
```
cat learn/synthesized/ints.json | jq .
```

##### Reproducing ALL experiments

##### Table 1

To run all learning tasks, run command:

```
vm$ make -B learn
```

This will learn all of the 24 grammars.

The files containing execution statistics (Table 1) are placed in:
`learn/results/info_XXX.txt`. For example, results of learning ints is

```
vm$ cat learn/results/info_ints.txt 

 ++++++++ Execution stats for ints ++++++++ 
Time taken to learn ints is: 0.4360830783843994
Average length of seeds: 2.0833333333333335 ± 1.1873172373979173
Total number of checks: 3216
```

You can inspect the whole table by using

```
vm$ ./show_table_1.py
                          Table I                          
┏━━━━━━━━━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━┓
┃ Grammar         ┃ LTime(s) ┃ Seed Len ┃ σ     ┃ Checks  ┃
┡━━━━━━━━━━━━━━━━━╇━━━━━━━━━━╇━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━┩
└─────────────────┴──────────┴──────────┴───────┴─────────┘
```

#### Evaluation

```
vm$ make earleyjava
```

##### Table 2

To run the evaluation for all subjects (Table 2), execute command:

```
vm$ make eval
```

The files containing precision scores (Table 2) are placed at:

`learn/results/eval_XXX_precision.txt`

The files containing recall scores (Table 2) are placed at:

`learn/results/eval_XXX_recall.txt`

Please note that the total recall score for a given subject can be obtained by summing up the 10 subscores in the file.

As before, the table can be inspected by:

```
vm$ ./show_table_2.py 
                     Table II                     
┏━━━━━━━━━┳━━━━━━━━━━━┳━━━━━━━━┳━━━━━━┳━━━━━━━━━━┓
┃ Grammar ┃ Precision ┃ Recall ┃ F1   ┃ Size(KB) ┃
┡━━━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━╇━━━━━━╇━━━━━━━━━━┩
└─────────┴───────────┴────────┴──────┴──────────┘
```

##### Table 3

The Table 3 provides a summary of source grammars.

```
vm$ python3 ./analyze-grammar.py xml

 ++++++++ Stats of the xml handwritten grammar ++++++++ 
Total number of non-terminals: 12
Total number of rules: 140
Total number of terminals: 65

 ++++++++ Stats of the xml synthesized grammar ++++++++ 
Total number of non-terminals: 692
Total number of rules: 16518
Total number of terminals: 65
```

As before, the table can be inspected by:

```
vm$ ./show_table_3.py 
                       Table III                       
┏━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━┓
┃ Grammar         ┃ Non-terminals ┃ Rules ┃ Terminals ┃
┡━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━┩
└─────────────────┴───────────────┴───────┴───────────┘
```

##### Table 4

To collect grammar statistics for all subjects (Table 4), run:

```
vm$ make analyze
```

Statistics on the synthesized grammars (Table 4) are stored in:

`learn/results/eval_XXX_grammar.txt`

As before, the table can be inspected by:

```
vm$ ./show_table_4.py 
                       Table IV                       
┏━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━┓
┃ Grammar         ┃ Non-terminals ┃ Rules ┃ Terminals ┃
┡━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━┩
└─────────────────┴───────────────┴───────┴───────────┘
```

##### Learning a new grammar

To test a new grammar mygrammar, first place your grammar file in `learn/handwritten`. The grammar must be stored in fuzzingbook format.

Next, generate seed inputs by running the following command:

```
vm$ (cd learn/glade-py/src; python3 fuzz.py mygrammar)
```

This will generate 50 random seed inputs and save them in the text file
`learn/seeds/mygrammar_inputs.txt`. Redundant seed inputs are automatically removed.

Then execute the learning algorithm:

```
vm$ (cd learn/glade-py/src; python3 glade.py mygrammar)
```

##### Evaluating a specific grammar

After learning a given grammar, you can run the evaluation to obtain the precision and recall scores. For example, to evaluate xml learned grammar, we run:

```
vm$ (cd learn/results; make eval SUBJECT=xml)
```

You can substitute xml with the name of the grammar you want to evaluate.

To collect statistics of the learned grammar, i.e., number of non-terminals, rules, and terminals, run:

```
vm$ python3 analyze-grammar.py xml
```

##### Summary of Evaluation results

Source grammars can be found in `learn/handwritten`

ANTLR source grammars can be found in antlr4/XXX/ where XXX can be relpaced by the target language name.

Synthesized grammars can be found under `learn/synthesized`

##### Table 1 results

```
vm$ ./show_table_1.py
                          Table I                          
┏━━━━━━━━━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━┓
┃ Grammar         ┃ LTime(s) ┃ Seed Len ┃ σ     ┃ Checks  ┃
┡━━━━━━━━━━━━━━━━━╇━━━━━━━━━━╇━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━┩
└─────────────────┴──────────┴──────────┴───────┴─────────┘
```

##### Table 2 results

```
vm$ ./show_table_2.py 
                     Table II                     
┏━━━━━━━━━┳━━━━━━━━━━━┳━━━━━━━━┳━━━━━━┳━━━━━━━━━━┓
┃ Grammar ┃ Precision ┃ Recall ┃ F1   ┃ Size(KB) ┃
┡━━━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━╇━━━━━━╇━━━━━━━━━━┩
└─────────┴───────────┴────────┴──────┴──────────┘
```

##### Table 3 results

```
vm$ ./show_table_3.py 
                       Table III                       
┏━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━┓
┃ Grammar         ┃ Non-terminals ┃ Rules ┃ Terminals ┃
┡━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━┩
└─────────────────┴───────────────┴───────┴───────────┘
```

##### Table 4 results

```
vm$ ./show_table_4.py 
                       Table IV                       
┏━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━┓
┃ Grammar         ┃ Non-terminals ┃ Rules ┃ Terminals ┃
┡━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━┩
└─────────────────┴───────────────┴───────┴───────────┘
```


Note: The EXACT numbers reported in the paper may not be always reproducible, e.g. number of checks, size of grammar. This is because during some executions, some checks may exceed the timeout specified and return False, resulting in slightly different grammars.
