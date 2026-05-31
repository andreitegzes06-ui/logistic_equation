# Logistic Difference Equation Project

This project studies the logistic difference equation:

```text
p_(n+1) = k * p_n * (1 - p_n)
```

The program calculates sequence values for different choices of `k` and `p0`.
It prints the values in the terminal and saves graphs as PNG files.

## Requirements

- Python 3
- matplotlib

Install matplotlib with:

```bash
pip install matplotlib
```

## How to Run

From this folder, run:

```bash
python main.py
```

The program will:

- create the `graphs` folder if it does not exist
- print all sequence values in the terminal
- save all PNG graphs in the `graphs` folder
- create a comparison graph for `p0 = 0.500` and `p0 = 0.501` when `k = 3.8`

## Files

- `main.py`: Python program for calculating and plotting the sequences
- `report.md`: short written observations for the assignment
- `graphs/`: folder containing the generated PNG graphs
