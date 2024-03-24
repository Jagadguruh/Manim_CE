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

        # New dot at origin
        origin_dot = Dot(color=BLUE)
        origin_dot.add_updater(lambda m: m.move_to(axes.c2p(0, np.sin(x_tracker.get_value()))))
        origin_trail = TracedPath(origin_dot.get_center)
        origin_trail.set_color(BLUE)

        # Timer
        time_label = DecimalNumber(0, num_decimal_places=2).add_updater(lambda t: t.set_value(x_tracker.get_value()))
        time_label.scale(2)  # scale the timer
        time = VGroup(Text("Time:"), time_label).arrange(RIGHT).to_corner(UR)  

        # Add the timer to the scene
        self.add(axes, labels, red_dot, trail, origin_dot, origin_trail, time)
        self.play(x_tracker.animate.set_value(4*np.pi), run_time=20, rate_func=linear)
        origin_dot.clear_updaters()
        red_dot.clear_updaters()