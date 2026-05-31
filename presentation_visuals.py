from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


OUTPUT_FOLDER = Path("presentation_graphs")
FRAME_FOLDER = OUTPUT_FOLDER / "animation_frames"

BACKGROUND = "#07111f"
PANEL = "#0b1628"
TEXT = "#f2f5f7"
MUTED = "#9fb3c8"
GRID = "#ffffff"
BLUE = "#4cc9f0"
PINK = "#f72585"
YELLOW = "#ffd166"
GREEN = "#80ed99"
ORANGE = "#ff9f1c"


def logistic_next(k, p):
    """Return the next logistic map value."""
    return k * p * (1 - p)


def logistic_sequence(k, p0, n):
    """Return the first n values of the logistic sequence."""
    values = [p0]
    for _ in range(n - 1):
        values.append(logistic_next(k, values[-1]))
    return np.array(values)


def save_figure(fig, filename_base):
    """Save one figure as both PNG and PDF for presentation use."""
    OUTPUT_FOLDER.mkdir(exist_ok=True)
    png_path = OUTPUT_FOLDER / f"{filename_base}.png"
    pdf_path = OUTPUT_FOLDER / f"{filename_base}.pdf"
    fig.savefig(png_path, dpi=300, bbox_inches="tight", facecolor=BACKGROUND)
    fig.savefig(pdf_path, bbox_inches="tight", facecolor=BACKGROUND)
    plt.close(fig)


def style_axis(ax):
    """Apply the same clean dark style to an axis."""
    ax.set_facecolor(PANEL)
    ax.tick_params(colors=MUTED)
    ax.xaxis.label.set_color(TEXT)
    ax.yaxis.label.set_color(TEXT)
    ax.title.set_color(TEXT)
    ax.grid(True, color=GRID, alpha=0.12, linewidth=0.8)
    for spine in ax.spines.values():
        spine.set_color("#30445f")


def plot_curve_and_diagonal(ax, k):
    """Plot y = kx(1 - x) and y = x."""
    x = np.linspace(0, 1, 500)
    y = logistic_next(k, x)
    ax.plot(x, y, color=BLUE, linewidth=2.4, label="next population = kp(1 - p)")
    ax.plot(x, x, color=PINK, linewidth=1.8, linestyle="--", label="same population level")
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)


def draw_cobweb(ax, k, p0, steps, color=TEXT, linewidth=1.1):
    """Draw vertical and horizontal cobweb steps."""
    p = p0
    points = [(p, p)]
    for _ in range(steps):
        next_p = logistic_next(k, p)
        ax.plot([p, p], [p, next_p], color=color, linewidth=linewidth, alpha=0.9)
        ax.plot([p, next_p], [next_p, next_p], color=color, linewidth=linewidth, alpha=0.9)
        points.append((p, next_p))
        points.append((next_p, next_p))
        p = next_p
    return points


def process_map_visual():
    """Create a three-panel explanation of how iteration works."""
    k = 3.2
    p0 = 0.5
    values = logistic_sequence(k, p0, 18)

    fig, axes = plt.subplots(1, 3, figsize=(16, 9), facecolor=BACKGROUND)
    fig.suptitle("Population Growth with Limited Resources", color=TEXT, fontsize=22, y=0.94)

    ax = axes[0]
    style_axis(ax)
    plot_curve_and_diagonal(ax, k)
    ax.scatter([p0], [p0], color=YELLOW, s=70, zorder=5)
    ax.annotate(
        "current population p_n",
        xy=(p0, p0),
        xytext=(0.12, 0.82),
        color=TEXT,
        arrowprops={"arrowstyle": "->", "color": YELLOW},
    )
    ax.annotate(
        "limited resources: 1 - p_n",
        xy=(p0, logistic_next(k, p0)),
        xytext=(0.06, 0.62),
        color=TEXT,
        arrowprops={"arrowstyle": "->", "color": BLUE},
    )
    ax.annotate(
        "next generation p_(n+1)",
        xy=(p0, logistic_next(k, p0)),
        xytext=(0.54, 0.96),
        color=TEXT,
        arrowprops={"arrowstyle": "->", "color": GREEN},
    )
    ax.set_title("A. Growth Rule")
    ax.set_xlabel("current population fraction p_n")
    ax.set_ylabel("next generation p_(n+1)")
    ax.legend(facecolor=PANEL, edgecolor="#30445f", labelcolor=TEXT, loc="lower right")

    ax = axes[1]
    style_axis(ax)
    plot_curve_and_diagonal(ax, k)
    draw_cobweb(ax, k, p0, 12, linewidth=1.2)
    ax.scatter([p0], [logistic_next(k, p0)], color=YELLOW, s=60, zorder=5)
    ax.annotate(
        "next generation p_(n+1)",
        xy=(p0, logistic_next(k, p0)),
        xytext=(0.13, 0.92),
        color=TEXT,
        arrowprops={"arrowstyle": "->", "color": YELLOW},
    )
    ax.annotate(
        "repeat for each generation",
        xy=(0.8, 0.8),
        xytext=(0.58, 0.28),
        color=TEXT,
        arrowprops={"arrowstyle": "->", "color": GREEN},
    )
    ax.annotate(
        "high growth can overshoot\navailable resources",
        xy=(0.82, logistic_next(k, 0.82)),
        xytext=(0.38, 0.08),
        color=TEXT,
        arrowprops={"arrowstyle": "->", "color": ORANGE},
    )
    ax.set_title("B. Generation-to-Generation Steps")
    ax.set_xlabel("current population fraction p_n")
    ax.set_ylabel("next generation p_(n+1)")

    ax = axes[2]
    style_axis(ax)
    ax.plot(range(len(values)), values, color=GREEN, marker="o", markersize=5, linewidth=2)
    ax.set_ylim(0, 1)
    ax.set_title("C. Population History")
    ax.set_xlabel("generation n")
    ax.set_ylabel("population fraction p_n")
    ax.annotate(
        "population alternates\nbetween high and low",
        xy=(12, values[12]),
        xytext=(4.5, 0.35),
        color=TEXT,
        arrowprops={"arrowstyle": "->", "color": GREEN},
    )

    fig.tight_layout(rect=(0, 0, 1, 0.9))
    save_figure(fig, "process_map")


def bifurcation_diagram_presentation():
    """Create a high-quality bifurcation diagram."""
    k_values = np.linspace(2.5, 4.0, 2500)
    all_k = []
    all_p = []

    for k in k_values:
        p = 0.5
        for step in range(1000):
            p = logistic_next(k, p)
            if step >= 700:
                all_k.append(k)
                all_p.append(p)

    fig, ax = plt.subplots(figsize=(16, 9), facecolor=BACKGROUND)
    style_axis(ax)
    ax.scatter(all_k, all_p, s=0.05, color=TEXT, alpha=0.55, rasterized=True)
    ax.axvspan(2.5, 3.0, color=GREEN, alpha=0.08)
    ax.axvspan(3.0, 3.57, color=YELLOW, alpha=0.08)
    ax.axvspan(3.57, 4.0, color=PINK, alpha=0.08)
    ax.text(2.62, 0.12, "stable population", color=GREEN, fontsize=13)
    ax.text(3.12, 0.12, "population cycles", color=YELLOW, fontsize=13)
    ax.text(3.68, 0.12, "chaotic population", color=PINK, fontsize=13)
    ax.set_title("From Stable Population to Chaos", fontsize=22)
    ax.set_xlabel("growth parameter k", fontsize=13)
    ax.set_ylabel("long-term population fraction p_n", fontsize=13)
    ax.set_xlim(2.5, 4.0)
    ax.set_ylim(0, 1)
    fig.tight_layout()
    save_figure(fig, "bifurcation_diagram_presentation")


def cobweb_subplot(ax, k, p0, steps, title):
    """Draw one cobweb subplot."""
    style_axis(ax)
    plot_curve_and_diagonal(ax, k)
    draw_cobweb(ax, k, p0, steps, linewidth=0.75)
    ax.set_title(title)
    ax.set_xlabel("current population fraction p_n")
    ax.set_ylabel("next generation p_(n+1)")
    ax.text(0.04, 0.92, f"k = {k}", transform=ax.transAxes, color=YELLOW, fontsize=11)


def cobweb_grid():
    """Create a 2x2 grid of cobweb diagrams."""
    examples = [
        (2.8, 0.5, 30, "Stable Population Growth, k = 2.8"),
        (3.2, 0.5, 30, "Population Oscillation, k = 3.2"),
        (3.45, 0.5, 35, "Period Doubling in Population Growth\nk = 3.45"),
        (3.8, 0.5, 50, "Chaotic Population Dynamics, k = 3.8"),
    ]

    fig, axes = plt.subplots(2, 2, figsize=(16, 9), facecolor=BACKGROUND)
    fig.suptitle("Cobweb Views of Population Growth Regimes", color=TEXT, fontsize=22, y=0.96)
    for ax, (k, p0, steps, title) in zip(axes.flat, examples):
        cobweb_subplot(ax, k, p0, steps, title)

    fig.tight_layout(rect=(0, 0, 1, 0.93))
    save_figure(fig, "cobweb_grid")


def sensitivity_comparison():
    """Compare two nearby initial values in the chaotic range."""
    k = 3.8
    n = 100
    values_a = logistic_sequence(k, 0.500, n)
    values_b = logistic_sequence(k, 0.501, n)
    difference = np.abs(values_a - values_b)
    first_large_difference = int(np.argmax(difference > 0.1))
    if difference[first_large_difference] <= 0.1:
        first_large_difference = 25

    fig, axes = plt.subplots(
        2,
        1,
        figsize=(16, 9),
        facecolor=BACKGROUND,
        gridspec_kw={"height_ratios": [2, 1]},
        sharex=True,
    )
    fig.suptitle(
        "Sensitive Dependence in Chaotic Population Growth",
        color=TEXT,
        fontsize=22,
        y=0.97,
    )
    fig.text(
        0.5,
        0.925,
        "Two almost identical starting populations can later produce different population histories.",
        color=MUTED,
        fontsize=14,
        ha="center",
    )

    ax = axes[0]
    style_axis(ax)
    ax.plot(values_a, color=BLUE, linewidth=2, label="p0 = 0.500")
    ax.plot(values_b, color=PINK, linewidth=2, label="p0 = 0.501")
    ax.axvline(first_large_difference, color=YELLOW, linestyle="--", linewidth=1.5)
    ax.annotate(
        "starting populations differ by 0.001\nof maximum possible population",
        xy=(first_large_difference, values_a[first_large_difference]),
        xytext=(first_large_difference + 8, 0.82),
        color=TEXT,
        arrowprops={"arrowstyle": "->", "color": YELLOW},
    )
    ax.set_ylabel("population fraction p_n")
    ax.set_ylim(0, 1)
    ax.legend(facecolor=PANEL, edgecolor="#30445f", labelcolor=TEXT)

    ax = axes[1]
    style_axis(ax)
    ax.plot(difference + 1e-8, color=YELLOW, linewidth=2)
    ax.axvline(first_large_difference, color=YELLOW, linestyle="--", linewidth=1.5)
    ax.set_yscale("log")
    ax.set_xlabel("generation n")
    ax.set_ylabel("population difference")

    fig.tight_layout(rect=(0, 0, 1, 0.9))
    save_figure(fig, "sensitivity_comparison")


def regime_summary():
    """Create a simple four-column visual summary."""
    examples = [
        (
            "1 < k < 3",
            "Stable population",
            "The population approaches\na steady level.",
            2.8,
            0.5,
            30,
            GREEN,
        ),
        (
            "3 < k < 3.4",
            "Two-generation cycle",
            "The population alternates\nbetween high and low generations.",
            3.2,
            0.5,
            50,
            YELLOW,
        ),
        (
            "3.4 < k < 3.5",
            "More complex cycles",
            "The population repeats\nthrough more values.",
            3.45,
            0.5,
            60,
            ORANGE,
        ),
        (
            "3.6 < k < 4",
            "Chaotic population",
            "Small starting changes can lead\nto different long-term behavior.",
            3.8,
            0.5,
            100,
            PINK,
        ),
    ]

    fig, axes = plt.subplots(1, 4, figsize=(16, 9), facecolor=BACKGROUND)
    fig.suptitle("Population Growth Regimes", color=TEXT, fontsize=22, y=0.92)

    for ax, (interval, phrase, description, k, p0, n, color) in zip(axes, examples):
        values = logistic_sequence(k, p0, n)
        style_axis(ax)
        ax.plot(values, color=color, marker="o", markersize=3, linewidth=1.5)
        ax.set_title(interval)
        ax.set_xlabel("generation n")
        ax.set_ylim(0, 1)
        ax.text(0.07, 0.88, phrase, transform=ax.transAxes, color=TEXT, fontsize=14, weight="bold")
        ax.text(0.07, 0.78, description, transform=ax.transAxes, color=MUTED, fontsize=9.5)
        ax.text(0.07, 0.68, f"k = {k}", transform=ax.transAxes, color=MUTED, fontsize=12)
        if ax is axes[0]:
            ax.set_ylabel("population fraction p_n")
        else:
            ax.set_yticklabels([])

    fig.tight_layout(rect=(0, 0, 1, 0.88))
    save_figure(fig, "regime_summary")


def animation_frames():
    """Create PNG frames for a simple cobweb animation."""
    FRAME_FOLDER.mkdir(parents=True, exist_ok=True)
    k = 3.2
    p0 = 0.5

    for frame in range(40):
        fig, ax = plt.subplots(figsize=(16, 9), facecolor=BACKGROUND)
        style_axis(ax)
        plot_curve_and_diagonal(ax, k)
        draw_cobweb(ax, k, p0, frame + 1, linewidth=1.2)
        ax.set_title(f"Population Cobweb Iteration Frame {frame:03d}")
        ax.set_xlabel("current population fraction p_n")
        ax.set_ylabel("next generation p_(n+1)")
        fig.tight_layout()
        fig.savefig(
            FRAME_FOLDER / f"frame_{frame:03d}.png",
            dpi=160,
            bbox_inches="tight",
            facecolor=BACKGROUND,
        )
        plt.close(fig)


def main():
    OUTPUT_FOLDER.mkdir(exist_ok=True)
    process_map_visual()
    bifurcation_diagram_presentation()
    cobweb_grid()
    sensitivity_comparison()
    regime_summary()
    animation_frames()
    print("Presentation visuals saved in presentation_graphs/")


if __name__ == "__main__":
    main()
