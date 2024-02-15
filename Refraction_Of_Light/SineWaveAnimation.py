import random
from manim import *

class SineWaveAnimation(ThreeDScene):
    def construct(self, num_waves=20):
        # Create the axes with expanded visibility range
        axes = ThreeDAxes(x_range=[-10, 10], y_range=[-10, 10], z_range=[-10, 10])
        
        # Set the camera orientation
        self.set_camera_orientation(phi=75 * DEGREES, theta=45 * DEGREES)
        
        # Define the wave colors and rotation angles
        wave_colors = [PURPLE, DARK_BLUE, BLUE, GREEN, YELLOW, ORANGE, RED]
        
        # Randomly select colors, rotations, and frequencies for the waves
        random.shuffle(wave_colors)
        wave_colors = wave_colors * ((num_waves + len(wave_colors) - 1) // len(wave_colors))
        random.shuffle(wave_colors)
        wave_colors = wave_colors[:num_waves]
        wave_rotations = [random.uniform(0, 360) * DEGREES for _ in range(num_waves)]
        wave_phases = [random.uniform(0, 2 * PI) for _ in range(num_waves)]
        wave_frequencies = [random.uniform(0.5, 2) for _ in range(num_waves)]
        
        # Create the sine waves
        waves = []
        for color, rotation, phase, frequency in zip(wave_colors, wave_rotations, wave_phases, wave_frequencies):
            wave = ParametricFunction(
                lambda t: np.array([np.sin(frequency * t + phase), 0.25 * t, 0]),
                t_range=[-22*PI, 10*PI],
                color=color,
                stroke_width=3,
                fill_opacity=0,
            )
            wave.rotate(rotation, UP)
            waves.append(wave)

        # Animate the creation of the axes
        self.play(Create(axes), run_time=2)

        # Drop down the axes visibility by 50%
        axes.set_opacity(0.5)
        
        # Create an AnimationGroup for all the waves
        wave_animations = AnimationGroup(*[Create(wave) for wave in waves])
        
        # Play the AnimationGroup to animate all waves at once with a delay between each wave
        self.play(wave_animations, run_time=7)

        # Wait for 2 seconds
        self.wait(2)
        