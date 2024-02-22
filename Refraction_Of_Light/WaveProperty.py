from manim import *

class WaveProperty(Scene):
    def construct(self):

        # Adding credit text
        credit_text = Text("Vriha.org", color=GREEN, font_size=20).to_corner(UP + LEFT)
        self.play(Create(credit_text), run_time=0.5)

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
        self.play(Create(sine_wave), run_time=3)

        # Animate the opacity of axes and sine_wave to 0.5
        self.play(
            axes.animate.set_opacity(0.3),
            sine_wave.animate.set_stroke(opacity=0.5),
            run_time=2
        )

        # Add two dotted lines at the crests
        dotted_line_1 = DashedLine(
            start=axes.c2p(np.pi / 2, 0), end=axes.c2p(np.pi / 2, 1), color=RED)
        dotted_line_2 = DashedLine(
            start=axes.c2p(-3*np.pi / 2, 0), end=axes.c2p(-3*np.pi / 2, 1), color=RED)
        self.play(Create(dotted_line_1), Create(dotted_line_2), run_time=1)

        # Add horizontal line between tips of dotted lines
        horizontal_line = DashedLine(dotted_line_1.get_end(), dotted_line_2.get_end(), color=PURPLE)

        self.play(Create(horizontal_line), run_time=2)

         # Shift the line upwards
        self.play(horizontal_line.animate.shift(UP * 1.05), run_time=3)

        # Add text "wavelength" above the line
        wavelength_text = Text("Wavelength", font_size=30).next_to(horizontal_line, UP)
        self.play(Create(wavelength_text), run_time=1)

        self.wait(1)