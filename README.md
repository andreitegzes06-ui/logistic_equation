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

## Extra Visualizations

The project also creates a bifurcation diagram and cobweb diagrams.

The bifurcation diagram shows how the long-term behavior changes when `k` changes.
The cobweb diagrams show how each term is produced from the previous term.

## Presentation Visuals

For LaTeX or Beamer slides, run:

```bash
python presentation_visuals.py
```

New visuals are saved in `presentation_graphs/`.
PNG files are useful for quick viewing, and PDF files are better for LaTeX/Beamer.

## Files

- `main.py`: Python program for calculating and plotting the sequences
- `presentation_visuals.py`: creates high-quality presentation visuals
- `report.md`: short written observations for the assignment
- `latex_figures_snippet.tex`: ready-to-paste LaTeX figure code
- `graphs/`: folder containing the generated PNG graphs
- `presentation_graphs/`: folder containing PNG and PDF presentation visuals
