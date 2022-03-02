
This is the replication package for "“Synthesizing Input Grammars”: A Critical Evaluation". 
PyGlade is a Python implementation of the _Glade_ blackbox grammar synthesis algorithm described by
Bastani et al. in [Synthesizing Program Input
Grammars](https://arxiv.org/pdf/1608.01723.pdf).

The main source file where _Glade_ algorithm is implemented is [glade.py](https://github.com/anonymous-pldi-2022/anonymous-pldi-2022/blob/main/learn/glade-py/src/glade.py).
You can reproduce the experiments by running our [virtual machine](https://figshare.com/s/136eea0d984136abc300).

In this experiment, we learn 25 target languages. Target languages are modeled by source grammars. Most grammars are in [fuzzingbook format](https://www.fuzzingbook.org/html/Grammars.html). The rest are in ANTLR format.

## Requirements:
* CPU of 8 cores minimum.
* python3
* pip3
* maven
* openjdk-11-jdk
* antlr4-python3-runtime version 4.9.2, can be installed by `pip3 install antlr4-python3-runtime==4.9.2`

Alternatively, you can just simply use our virtual machine, which has all the above requirements.

## Running all experiments

### Learning
To run all learning tasks, run command:

    $ make -B learn

This will learn all the 24 grammars.

### Evaluation
Before running the evaluation, we compile the EarleyJava project:

    $ make earleyjava

To collect grammar statistics for all subjects, run:

    $ make analyze

To run the evaluation for all subjects, execute command:

    $ make eval

## Learning a specific grammar
You can also learn one specific grammar e.g. ints. The grammar must be in fuzzingbook format and must be located in `learn/handwritten`

To learn the `ints` grammar, execute:

    $ cd learn/glade-py/src && python3 glade.py ints

## Learning a new grammar
To test a new grammar `mygrammar`, first place your grammar file in `learn/handwritten`. The grammar must be stored in fuzzingbook format.

Next, generate seed inputs by running the following command:

    $ cd learn/glade-py/src && python3 fuzz.py mygrammar

This will generate 50 random seed inputs and save them in the text file `learn/seeds/mygrammar_inputs.txt`. Redundant seed inputs are automatically removed.

Then execute the learning algorithm:

    $ cd learn/glade-py/src && python3 glade.py mygrammar


## Evaluating a specific grammar
After learning a given grammar, you can run the evaluation to obtain the precision and recall scores. For example, to evaluate `xml` learned grammar, we run:

    $ cd learn/results && make eval SUBJECT=xml

You can substitute `xml` with the name of the grammar you want to evaluate.

To collect statistics of the learned grammar, i.e., number of non-terminals, rules, and terminals, run:

    $ python3 analyze-grammar.py xml

## Evaluation results
Source grammars can be found in `learn/handwritten`

ANTLR source grammars can be found in `antlr4/*/` where * can be relpaced by the target language name.

Synthesized grammars can be found under `learn/synthesized`.

The files containing precision scores are: `learn/results/eval_*_precision.txt`.

The files containing recall scores are: `learn/results/eval_*_recall.txt`. Please note that the total recall score for a given subject can be obtained by summing up the 10 subscores in the file.

The files containing execution statistics are: `learn/results/info_*.txt`.

Statistics on the synthesized grammars are stored in `learn/results/eval_*_grammar.txt`.
