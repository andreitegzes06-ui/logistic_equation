# Report: Logistic Population Growth Model

The logistic difference equation is:

```text
p_(n+1) = k * p_n * (1 - p_n)
```

In this project, I used the logistic difference equation as a simple population growth model. The value `p_n` represents the population in generation `n` as a fraction of the maximum population the environment can support. The factor `(1 - p_n)` represents limited resources, competition, and environmental pressure.

For populations that reproduce in generations, such as insects, a discrete model is useful because birth and death can happen in cycles.

## Part 1: Values of k where 1 < k < 3

Values used:

- `k = 2.2`, `p0 = 0.5`, `n = 30`
- `k = 2.8`, `p0 = 0.5`, `n = 30`

Graph files:

- `graphs/part1_k2_2_p0_0_5.png`
- `graphs/part1_k2_8_p0_0_5.png`

Observation:
Both populations approach a stable long-term fraction of the maximum possible population. For `k = 2.2`, the population approaches about `0.545`. For `k = 2.8`, the population approaches about `0.643`.

## Part 2: Changing p0

Values used:

- `k = 2.2`, `p0 = 0.2`, `n = 30`
- `k = 2.8`, `p0 = 0.2`, `n = 30`

Graph files:

- `graphs/part1_repeat_k2_2_p0_0_2.png`
- `graphs/part1_repeat_k2_8_p0_0_2.png`

Observation:
When the starting population `p0` is changed to `0.2`, the populations still approach the same final levels as in Part 1. This suggests that for `1 < k < 3`, the stable long-term population does not depend much on the starting population. However, the final population level does depend on the growth parameter `k`.

## Part 3: Values of k between 3 and 3.4

Values used:

- `k = 3.2`, `p0 = 0.5`, `n = 50`

Graph file:

- `graphs/part2_k3_2_p0_0_5.png`

Observation:
The population does not settle at one level. It alternates between high and low generations, which is period-2 behavior.

## Part 4: Values of k between 3.4 and 3.5

Values used:

- `k = 3.45`, `p0 = 0.5`, `n = 60`

Graph file:

- `graphs/part3_k3_45_p0_0_5.png`

Observation:
The population has a more complex repeating pattern. Instead of alternating between only two generations, it repeats through more population levels. This is related to period doubling.

## Part 5: Values of k between 3.6 and 4

Values used:

- `k = 3.8`, `p0 = 0.500`, `n = 100`
- `k = 3.8`, `p0 = 0.501`, `n = 100`

Graph files:

- `graphs/part4_k3_8_p0_0_500.png`
- `graphs/part4_k3_8_p0_0_501.png`
- `graphs/part4_comparison.png`

Observation:
The population appears chaotic. The starting populations `0.500` and `0.501` differ by only `0.001` of the maximum possible population, but later the population histories become different. This shows sensitivity to initial conditions.

Chaotic does not mean truly random. The long-term population becomes difficult to predict, even though the equation is deterministic and follows a fixed formula.

## Extra Visualizations

Graph files:

- `graphs/bifurcation_diagram.png`
- `graphs/cobweb_k2_8.png`
- `graphs/cobweb_k3_2.png`
- `graphs/cobweb_k3_8.png`

Observation:
The bifurcation diagram gives a global view of how population behavior changes as the growth parameter `k` changes. For smaller `k` values, the population approaches one stable level. As `k` increases, the stable level splits into cycles. For large `k` values, the population can become chaotic.

The cobweb diagrams show the step-by-step movement from the current population `p_n` to the next generation `p_(n+1)`, including the effect of limited resources through the factor `(1 - p_n)`.

## Extra Presentation Visuals

The file `presentation_visuals.py` creates a separate set of slide-ready graphs in `presentation_graphs/`.

- `process_map` explains how current population, resource limitation, and the next generation fit together.
- `bifurcation_diagram_presentation` shows the global transition from stable population growth to chaos.
- `cobweb_grid` compares stable growth, population cycles, period doubling, and chaos.
- `sensitivity_comparison` shows how nearly identical starting populations can later produce different population histories.
