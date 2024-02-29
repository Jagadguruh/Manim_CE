from manim import *
import numpy as np

class SinewaveTracer(Scene):
    def construct(self):
        axes = Axes(
            x_range=[0, 4*np.pi, 1], 
            y_range=[-2, 2, 1], 
            x_length=10,
            y_length=4,
            x_axis_config={"include_numbers": True},
            y_axis_config={"include_numbers": True},
        )
        
        labels = axes.get_axis_labels(x_label="t", y_label="y")
        x_tracker = ValueTracker(0)

        red_dot = Dot(color=RED)
        red_dot.add_updater(lambda m: m.move_to(axes.c2p(x_tracker.get_value(), np.sin(x_tracker.get_value()))))
        trail = TracedPath(red_dot.get_center)
        trail.set_color(RED)

        self.add(axes, labels, red_dot, trail)
        self.play(x_tracker.animate.set_value(4*np.pi), run_time=20, rate_func=linear)
        red_dot.clear_updaters()