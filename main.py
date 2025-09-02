from time_series_visualizer import draw_line_plot, draw_bar_plot, draw_box_plot

if __name__ == "__main__":
    # Line plot
    fig1 = draw_line_plot()
    fig1.savefig("line_plot.png")
    print("Line plot saved as line_plot.png")

    # Bar plot
    fig2 = draw_bar_plot()
    fig2.savefig("bar_plot.png")
    print("Bar plot saved as bar_plot.png")

    # Box plots
    fig3 = draw_box_plot()
    fig3.savefig("box_plot.png")
    print("Box plots saved as box_plot.png")
