import timeit
import arcade
from constants import *


class FPS:
    def __init__(self):
        # FPS
        self.processing_time = 0
        self.fps = False

        # Time for on_draw
        self.draw_time = 0

        # Variables used to calculate frames per second
        self.frame_count = 0
        self.fps_start_timer = None
        self.fps = None

    def calculate_FPS(self):
        if self.fps:
            fps_calculation_freq = 60
            # Once every 60 frames, calculate our FPS
            if self.frame_count % fps_calculation_freq == 0:
                # Do we have a start time?
                if self.fps_start_timer is not None:
                    # Calculate FPS
                    total_time = timeit.default_timer() - self.fps_start_timer
                    self.fps = fps_calculation_freq / total_time
                # Reset the timer
                self.fps_start_timer = timeit.default_timer()
            # Add one to our frame count
            self.frame_count += 1
        else:
            pass

    def draw_FPS(self):
        if self.fps:
            start_time = timeit.default_timer()

            output = f"Processing time: {self.processing_time:.3f}"
            arcade.draw_text(output, SCREEN_WIDTH - 200, 40, arcade.color.RED, 14)

            output = f"Drawing time: {self.draw_time:.3f}"
            arcade.draw_text(output, SCREEN_WIDTH - 175, 25, arcade.color.RED, 14)

            if self.fps is not None:
                output = f"FPS: {self.fps:.0f}"
                arcade.draw_text(output, SCREEN_WIDTH - 75, 10, arcade.color.RED, 14)

            # Stop the draw timer, and calculate total on_draw time.
            self.draw_time = timeit.default_timer() - start_time
        else:
            pass

    def start_time(self):
        return timeit.default_timer()

    def processing(self, start_time):
        self.processing_time = timeit.default_timer() - start_time

    def turn_on_off(self):
        if self.fps:
            self.fps = False
        else:
            self.fps = True
