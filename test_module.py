def test_draw_line_plot():
    from time_series_visualizer import draw_line_plot
    assert draw_line_plot() is not None

def test_draw_bar_plot():
    from time_series_visualizer import draw_bar_plot
    assert draw_bar_plot() is not None

def test_draw_box_plot():
    from time_series_visualizer import draw_box_plot
    assert draw_box_plot() is not None
