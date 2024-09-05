# How to Redirect Standard Input and Output to a File in Python

This code demonstrates a small calculator that shows how to use standard input and output while maintaining clean code in Python.

To read from and write to files, we need to use import sys.

The following part of the code:
```python
fout = open("input.txt", 'rt')  
sys.stdin = fout  
```
reads input from a file in the folder and fills the variable numbers with the values obtained from `input("~>").strip().split(" ").`

The next part of the code:
```python
fout = open("output.txt", 'wt')  
sys.stdout = fout  
```
redirects the output, writing the results of the calculations to a text file