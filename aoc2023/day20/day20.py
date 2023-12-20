import sys
from collections import deque
from enum import Enum
from math import lcm


class Signal(Enum):
    LOW = 1,
    HIGH = 2


class FlipFlop:
    def __init__(self, name, destinations):
        self.name = name
        self.destinations = destinations
        self.on = False

    def handle_pulse(self, signal: Signal, parent):
        if signal == Signal.HIGH:
            return tuple([])
        elif signal == Signal.LOW:
            if self.on:
                self.on = False
                return tuple([self.name, Signal.LOW, self.destinations])
            else:
                self.on = True
                return tuple([self.name, Signal.HIGH, self.destinations])

    def to_string(self):
        return f'{self.name} - {str(self.on)} - {",".join(self.destinations)}'


class Conjunction:
    def __init__(self, name, destinations, memory):
        self.name = name
        self.destinations = destinations
        self.memory = memory

    def handle_pulse(self, signal: Signal, parent):
        self.memory[parent] = signal
        if all([s == Signal.HIGH for s in self.memory.values()]):
            return tuple([self.name, Signal.LOW, self.destinations])
        else:
            return tuple([self.name, Signal.HIGH, self.destinations])

    def to_string(self):
        return f'{self.name} - {",".join(self.destinations)} - {self.memory}'


def parse():
    D = open(sys.argv[1]).read().strip().split('\n')
    configuration = []
    for line in D:
        module, destination = line.split(' -> ')
        destination = destination.split(', ')
        configuration.append((module, destination))

    return configuration


def solve_p1():
    configuration = parse()
    broadcaster = []
    modules = []
    for line in configuration:
        name, destinations = line
        if name == 'broadcaster':
            broadcaster = destinations
        elif name.startswith('%'):
            module = FlipFlop(name[1:], destinations)
            modules.append(module)
        elif name.startswith('&'):
            memory = dict([(n[1:], Signal.LOW) for n, dest in configuration if name[1:] in dest])
            module = Conjunction(name[1:], destinations, memory)
            modules.append(module)

    lo, hi = 0, 0
    for i in range(0, 1000):
        q = deque()
        q.append(('', Signal.LOW, broadcaster))
        lo += 1
        while q:
            parent, signal, destinations = q.popleft()

            if signal == Signal.LOW:
                lo += len(destinations)
            elif signal == Signal.HIGH:
                hi += len(destinations)

            for dest in destinations:
                module = next((m for m in modules if m.name == dest), None)
                if module is not None:
                    next_signal = module.handle_pulse(signal, parent)
                    if len(next_signal) > 0:
                        q.append(next_signal)

    print('Part 1:', lo * hi)


def solve_p2():
    configuration = parse()
    broadcaster = []
    modules = []
    for line in configuration:
        name, destinations = line
        if name == 'broadcaster':
            broadcaster = destinations
        elif name.startswith('%'):
            module = FlipFlop(name[1:], destinations)
            modules.append(module)
        elif name.startswith('&'):
            memory = dict([(n[1:], Signal.LOW) for n, dest in configuration if name[1:] in dest])
            module = Conjunction(name[1:], destinations, memory)
            modules.append(module)

    count = 0
    kl, vm, kv, vb = 0, 0, 0, 0
    while any([n == 0 for n in [kl, vm, kv, vb]]):
        count += 1
        q = deque()
        q.append(('', Signal.LOW, broadcaster))
        while q:
            parent, signal, destinations = q.popleft()

            if signal == Signal.HIGH and 'll' in destinations:
                if parent == 'kl' and kl == 0:
                    kl = count
                elif parent == 'vm' and vm == 0:
                    vm = count
                elif parent == 'kv' and kv == 0:
                    kv = count
                elif parent == 'vb' and vb == 0:
                    vb = count

            for dest in destinations:
                module = next((m for m in modules if m.name == dest), None)
                if module is not None:
                    next_signal = module.handle_pulse(signal, parent)
                    if len(next_signal) > 0:
                        q.append(next_signal)

    print('Part 1:', lcm(kl, vm, kv, vb))


solve_p1()
solve_p2()