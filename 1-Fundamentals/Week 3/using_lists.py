#!/usr/bin/env python
import random

states = ["Washington", "Oregon", "California"]

print(states[random.randint(0, 2)])

states[2] = "Arizona"

print(states[2])

print(len(states))

states.append("New York")

print(states)

states.pop(1)

print(states)
