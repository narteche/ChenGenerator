# ChenGenerator
A QBF instance generator written in Python for the so-called Chen Formulas of Type 1 and 2.

## Description

This repository contains Python code for a generator of QBF instances of the two classes of formulas defined by Hubie Chen in his 2016 article _Proof Complexity Modulo de Polynomial Hierarchy_ (available in the `/articles` folder).

## Contents
The content of each folder is:

* `/documentation`: contains a PDF document with the report of the project, descussing the formulas, how they were built and experimental results regarding their performance on available QBF solvers.
* `/articles`: some of the articles used for the documentation of the project. It contains Chen's original paper.
* `/formulas`: Type 1 and Type 2 formulas for sizes between n = 1 and n = 5000 in QCIR and QDIMACS.
* `/generators`: Python scripts for running the generators. Next section explains how to run them.
* `/src`: internal code and tools used for the development of the generators.



## How to run the generators
The generators are two Python scripts: `generate_T1.py` and `generate_T2.py`. There can be found in the ```/generators``` folder.

To run the Type 1 generator, one must run the `generate_T1.py` script. The command is the followiing:

```
python3 generate_T1.py n [filename]
```

The first argument is the value of n. The second argument is the name of a file. If not given, it will print the generated formula on the standard output, though it will not print formulas with more than 100 variables or clauses.

To run the Type 2 generator, one must run the `generate_T2.py` script. The command is one of the following:

```
python3 generate_T2.py n -QCIR [filename]
python3 generate_T2.py n -QDIMACS [filename]
```

The  first  argument  is  the  value  of n. The second  argument  is  either `-QCIR` or `-QDIMACS`, and it specifies the format in which the formula has to be written. The third argument is the name of a file. If not given, it will print the generated formula on the standard output, though it will not print formulaswith more than 100 variables or clauses.

## Available formulas
The repository already contains Type 1 and Type 2 formulas for sizes between n = 1 and n = 5000. These are available in the `/formulas` forlder. Type 1 formulas are available in QDIMACS, while Type 2 formulas are available in QCIR and QDIMACS.
