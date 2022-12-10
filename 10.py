# Day 10

import re
import time

import numpy as np
import pyglet
from pyglet import shapes

with open('10.input') as f:
    instructions = [re.match('^(\w{4})\s?(\-?\d*)$', r).groups() for r in f.read().split('\n') if r]


class MyWindow(pyglet.window.Window):
    def __init__(self, width=1280, height=320):
        super().__init__(width, height, "ElfPhone 14 Pro")
        self.batch = pyglet.graphics.Batch()
        self.pixels = []
        for y in range(6):
            row = [shapes.BorderedRectangle(x * 32, height - y * 32 - 32, 32, 32, border=5, color=(0, 0, 0),
                                            border_color=(25, 25, 25), batch=self.batch) for x in range(40)]
            self.pixels.append(row)
        self.label_clk = pyglet.text.Label('Clock: 20 Hz', font_name='Consolas', font_size=24, x=10, y=64, batch=self.batch)
        self.label_ip = pyglet.text.Label('IP: ---', font_name='Consolas', font_size=24, x=310, y=64, batch=self.batch)
        self.label_ax = pyglet.text.Label('AX: ------', font_name='Consolas', font_size=24, x=610, y=64, batch=self.batch)
        self.label_p1 = pyglet.text.Label('Part 1: -----', font_name='Consolas', font_size=24, x=810, y=64, batch=self.batch)
        self.ip = -1
        self.clock_speed = 20
        self.cycle = 0
        self.crt_column = 0
        self.crt_row = 0
        self.ax = 1
        self.signal_strengths_at = []
        self.signal_strengths = []
        self.operation_cycle = []
        self.fade = .99

        self.update_clock_speed()
        self.reset_program()

    def update_clock_speed(self):
        self.label_clk.text = f'Clock: {self.clock_speed} Hz'
        pyglet.clock.schedule_interval(self.update, 1 / self.clock_speed)

    def reset_program(self):
        self.ip = -1
        self.cycle = 0
        self.crt_column = 0
        self.crt_row = 0
        self.ax = 1
        self.signal_strengths_at = [20, 60, 100, 140, 180, 220]
        self.signal_strengths = []
        self.operation_cycle = [0, 0]

    def on_draw(self):
        self.clear()
        self.batch.draw()

    def update(self, delta_time):
        for row in self.pixels:
            for col in row:
                r, g, b, a = col.color
                if r + g + b != 0:
                    col.color = (int(r * self.fade), int(g * self.fade), int(b * self.fade), a)

        if self.operation_cycle[0] == 0:
            self.ip += 1
            self.label_ip.text = f'IP: {self.ip}'
            self.label_ax.text = f'AX: {self.ax}'
            if self.ip == len(instructions):
                self.label_p1.text = f'Part 1: {sum(device.signal_strengths)}'
                if self.clock_speed < 1000:
                    self.clock_speed *= 5
                    self.update_clock_speed()
                self.reset_program()
                return
            instruction, parameter = instructions[self.ip]
            if instruction == 'noop':
                self.operation_cycle = [1, 0]
            elif instruction == 'addx':
                self.operation_cycle = [2, int(parameter)]
            else:
                print(f'Unknown instruction {instruction}.')
                exit(1)

        c = (255, 255, 255) if \
            self.ax - 1 == self.crt_column or self.ax == self.crt_column or self.ax + 1 == self.crt_column \
            else (25, 25, 25)
        self.pixels[self.crt_row][self.crt_column].color = c
        self.crt_column += 1

        if self.crt_column == 40:
            self.crt_row += 1
            self.crt_column = 0

        self.cycle += 1

        if self.cycle in self.signal_strengths_at:
            self.signal_strengths.append(self.cycle * self.ax)

        self.operation_cycle[0] -= 1
        if self.operation_cycle[0] == 0:
            self.ax += self.operation_cycle[1]


device = MyWindow()
pyglet.app.run()
