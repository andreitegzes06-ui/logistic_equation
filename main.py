from pathlib import Path

import matplotlib.pyplot as plt


def logistic_sequence(k, p0, n):
    """Return the first n terms of p_(n+1) = k * p_n * (1 - p_n)."""
    values = [p0]

    # Each new value is calculated from the previous value.
    for _ in range(n - 1):
        previous = values[-1]
        next_value = k * previous * (1 - previous)
        values.append(next_value)

    return values


def plot_sequence(values, k, p0, filename):
    """Plot a logistic sequence and save it as a PNG file."""
    term_numbers = list(range(len(values)))

    plt.figure(figsize=(8, 5))
    plt.plot(term_numbers, values, marker="o", markersize=3, linewidth=1)
    plt.title(f"Logistic sequence: k = {k}, p0 = {p0}")
    plt.xlabel("n")
    plt.ylabel("p_n")
    plt.grid(True)
    plt.ylim(0, 1)
    plt.tight_layout()
    plt.savefig(filename)
    plt.close()


def plot_comparison(k, p0_a, p0_b, n, filename):
    """Plot two logistic sequences on the same graph."""
    values_a = logistic_sequence(k, p0_a, n)
    values_b = logistic_sequence(k, p0_b, n)
    term_numbers = list(range(n))

    plt.figure(figsize=(8, 5))
    plt.plot(
        term_numbers,
        values_a,
        marker="o",
        markersize=3,
        linewidth=1,
        label=f"p0 = {p0_a:.3f}",
    )
    plt.plot(
        term_numbers,
        values_b,
        marker="s",
        markersize=3,
        linewidth=1,
        label=f"p0 = {p0_b:.3f}",
    )
    plt.title(f"Comparison for k = {k}")
    plt.xlabel("n")
    plt.ylabel("p_n")
    plt.grid(True)
    plt.ylim(0, 1)
    plt.legend()
    plt.tight_layout()
    plt.savefig(filename)
    plt.close()


def print_sequence(title, values):
    """Print the sequence values in a readable format."""
    print(title)
    for n, value in enumerate(values):
        print(f"p_{n} = {value:.6f}")
    print()


def run_experiment(name, k, p0, n, graphs_folder):
    """Calculate, print, and graph one logistic sequence experiment."""
    values = logistic_sequence(k, p0, n)
    print_sequence(f"{name}: k = {k}, p0 = {p0}, n = {n}", values)

    filename = graphs_folder / f"{name}.png"
    plot_sequence(values, k, p0, filename)

    return values


def main():
    # Create the graphs folder automatically if it does not already exist.
    graphs_folder = Path("graphs")
    graphs_folder.mkdir(exist_ok=True)

    # These experiments match the assignment values.
    experiments = [
        ("part1_k2_2_p0_0_5", 2.2, 0.5, 30),
        ("part1_k2_8_p0_0_5", 2.8, 0.5, 30),
        ("part1_repeat_k2_2_p0_0_2", 2.2, 0.2, 30),
        ("part1_repeat_k2_8_p0_0_2", 2.8, 0.2, 30),
        ("part2_k3_2_p0_0_5", 3.2, 0.5, 50),
        ("part3_k3_45_p0_0_5", 3.45, 0.5, 60),
        ("part4_k3_8_p0_0_500", 3.8, 0.500, 100),
        ("part4_k3_8_p0_0_501", 3.8, 0.501, 100),
    ]

    for name, k, p0, n in experiments:
        run_experiment(name, k, p0, n, graphs_folder)

    comparison_file = graphs_folder / "part4_comparison.png"
    plot_comparison(3.8, 0.500, 0.501, 100, comparison_file)
    print("Comparison graph: k = 3.8, p0 = 0.500 and p0 = 0.501")
    print(f"Saved as {comparison_file}")
    print()

    print("All graphs were saved in the graphs folder.")


if __name__ == "__main__":
    main()
