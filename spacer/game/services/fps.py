import timeit
import arcade
from constants import *


class FPS:
    """FPS Counter

    The FPS class is a frames per second counter displayed for the user

    Attributes:
        processing_time(int) = Keeps track of how long information is processed
        fps_on(bool) = Whether the counter is on or off
        draw_time = Keeps track of how long it takes program to draw objects
        frame_count(int) = needed to calculated fps
        fps_start_timer(int) = timer to calculate fps
        fps(int) = Frames Per Second
    """

    def __init__(self):
        self.processing_time = 0
        self.fps_on = False
        self.draw_time = 0
        self.frame_count = 0
        self.fps_start_timer = None
        self.fps = None

    def calculate_FPS(self):
        """If on this will calculate the FPS when called"""
        if self.fps_on:
            fps_calculation_freq = 60
            if self.frame_count % fps_calculation_freq == 0:
                if self.fps_start_timer is not None:
                    total_time = timeit.default_timer() - self.fps_start_timer
                    self.fps = fps_calculation_freq / total_time
                self.fps_start_timer = timeit.default_timer()
            self.frame_count += 1
        else:
            pass

    def draw_FPS(self):
        """Draws the results of the calculations and reset the timer."""
        if self.fps_on:
            start_time = timeit.default_timer()

            output = f"Processing time: {self.processing_time:.3f}"
            arcade.draw_text(output, SCREEN_WIDTH - 200, 40, arcade.color.RED, 14)

            output = f"Drawing time: {self.draw_time:.3f}"
            arcade.draw_text(output, SCREEN_WIDTH - 175, 25, arcade.color.RED, 14)

            if self.fps is not None:
                output = f"FPS: {self.fps:.0f}"
                arcade.draw_text(output, SCREEN_WIDTH - 75, 10, arcade.color.RED, 14)

            self.draw_time = timeit.default_timer() - start_time
        else:
            pass

    def start_time(self):
        """Starts a timer

        Returns:
            function: Returns a timer from timeit
        """
        return timeit.default_timer()

    def processing(self, start_time):
        """Calculates processing time

        Args:
            start_time (int): This is the elapsed time
        """
        self.processing_time = timeit.default_timer() - start_time

    def turn_on_off(self):
        """Turns FPS on and off for user"""
        if self.fps_on:
            self.fps_on = False
        else:
            self.fps_on = True
