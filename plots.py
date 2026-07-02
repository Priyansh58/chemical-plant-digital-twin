import matplotlib.pyplot as plt

def create_line_plot(df, x_column, y_column, title, y_label):
    fig, ax = plt.subplots(figsize=(7,3.5))

    ax.plot(
        df[x_column],
        df[y_column],
        marker = "o",
        linewidth = 2,
    )
    ax.set_title(title)
    ax.set_xlabel("Time")
    ax.set_ylabel(y_label)

    ax.grid(True)
    # ax.legend()

    return fig