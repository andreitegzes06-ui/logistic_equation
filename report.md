# Report: Logistic Difference Equation

The logistic difference equation is:

```text
p_(n+1) = k * p_n * (1 - p_n)
```

In this project, I calculated and plotted several sequences for different values of `k` and `p0`.

## Part 1: Values of k where 1 < k < 3

Values used:

- `k = 2.2`, `p0 = 0.5`, `n = 30`
- `k = 2.8`, `p0 = 0.5`, `n = 30`

Graph files:

- `graphs/part1_k2_2_p0_0_5.png`
- `graphs/part1_k2_8_p0_0_5.png`

Observation:
Both sequences converge to a stable value. For `k = 2.2`, the sequence approaches about `0.545`. For `k = 2.8`, the sequence approaches about `0.643`.

## Part 2: Changing p0

Values used:

- `k = 2.2`, `p0 = 0.2`, `n = 30`
- `k = 2.8`, `p0 = 0.2`, `n = 30`

Graph files:

- `graphs/part1_repeat_k2_2_p0_0_2.png`
- `graphs/part1_repeat_k2_8_p0_0_2.png`

Observation:
When `p0` is changed to `0.2`, the sequences still approach the same final values as in Part 1. This suggests that for `1 < k < 3`, the limit does not depend much on `p0`. However, the limit does depend on `k`.

## Part 3: Values of k between 3 and 3.4

Values used:

- `k = 3.2`, `p0 = 0.5`, `n = 50`

Graph file:

- `graphs/part2_k3_2_p0_0_5.png`

Observation:
The sequence does not converge to one value. It oscillates between two values, which is period-2 behavior.

## Part 4: Values of k between 3.4 and 3.5

Values used:

- `k = 3.45`, `p0 = 0.5`, `n = 60`

Graph file:

- `graphs/part3_k3_45_p0_0_5.png`

Observation:
The sequence has a more complex oscillation. This is related to period doubling.

## Part 5: Values of k between 3.6 and 4

Values used:

- `k = 3.8`, `p0 = 0.500`, `n = 100`
- `k = 3.8`, `p0 = 0.501`, `n = 100`

Graph files:

- `graphs/part4_k3_8_p0_0_500.png`
- `graphs/part4_k3_8_p0_0_501.png`
- `graphs/part4_comparison.png`

Observation:
The sequence appears chaotic. The starting values `0.500` and `0.501` are almost the same, but later the graphs become different. This shows sensitivity to initial conditions.

Chaotic does not mean truly random. The sequence is deterministic because it follows a fixed formula, but small changes in `p0` can produce very different long-term behavior.

## Extra Visualizations

Graph files:

- `graphs/bifurcation_diagram.png`
- `graphs/cobweb_k2_8.png`
- `graphs/cobweb_k3_2.png`
- `graphs/cobweb_k3_8.png`

Observation:
The bifurcation diagram gives a global view of the logistic sequence. For smaller `k` values, the sequence approaches one value. As `k` increases, the stable value splits into cycles. For large `k` values, the behavior becomes chaotic.

The cobweb diagrams show the step-by-step movement from `p_n` to `p_(n+1)`.

## Extra Presentation Visuals

The file `presentation_visuals.py` creates a separate set of slide-ready graphs in `presentation_graphs/`.

- `process_map` explains how iteration works.
- `bifurcation_diagram_presentation` shows the global transition from stability to chaos.
- `cobweb_grid` compares convergence, cycles, and chaos.
- `sensitivity_comparison` shows sensitive dependence on initial conditions.
