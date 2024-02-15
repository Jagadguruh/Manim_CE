from manim import *

class WaveProperty(Scene):
    def construct(self):
        axes = Axes(
            x_range=[-10, 10, 1],
            y_range=[-5, 5, 1],
            x_length=20,
            y_length=10,
            tips=True,
            axis_config={
                "include_ticks": True,
                "include_tip": False,
                "color": WHITE,
                "stroke_width": 2,
            }
        )
        self.play(Create(axes), run_time=3)

        # Create a sine wave
        sine_wave = ParametricFunction(
            lambda t: np.array([t, np.sin(t), 0]),
            t_range=[-10, 10],
            color=YELLOW
        )
        self.play(Create(sine_wave), run_time=4)

        self.wait(1)