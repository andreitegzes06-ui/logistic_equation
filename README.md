# Logistic Difference Equation Project

This project studies the logistic difference equation:

```text
p_(n+1) = k * p_n * (1 - p_n)
```

The program calculates sequence values for different choices of `k` and `p0`, prints the values in the terminal, and saves plots as PNG files in the `graphs` folder.

## Requirements

- Python 3
- matplotlib

Install matplotlib if needed:

```bash
python -m pip install matplotlib
```

## How to Run

From this folder, run:

```bash
python main.py
```

The program will:

- create the `graphs` folder if it does not exist
- print all sequence values in the terminal
- save all plots as PNG files in `graphs`

## Files

- `main.py`: Python program for calculating and plotting the sequences
- `report.md`: short written observations for the assignment
- `graphs/`: folder containing the generated PNG graphs
