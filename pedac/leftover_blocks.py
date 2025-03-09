'''
Leftover Blocks

Write a program that, given the number of available blocks, calculates the 
number of blocks left over after building the tallest possible valid structure.

[P]
Input: Integer representing the number of available blocks
Output: Integer representing the number of blocks left over
Rules:
  Explicit:
    - The building blocks are cubes
    - The structure is built in layers
    - The top layer is a single block
    - A block in an upper layer must be supported by four blocks in a lower
      layer
    - A block in a lower layer can support more than one block in an upper layer
    - You cannot leave gaps between blocks
  Implicit:
    - Number of blocks
      layer 1: 1
      layer 2: 4
      layer 3: 9
      ...
      layer n: n^2

[D]
Input: Integer
Output: Integer

[A]
- Initialize `layer` to 0
- Initialize `blocks_needed` to 0

- Iterate from layer 0,
  - Calculate the total number of blocks needed to build the next layer
  - If the total blocks needed exceed the number of block available,
    - Break the iteration
  - Increment `layer` by 1
  - Increment `blocks_needed` by `layer` * `layer`

- Calcuate the number of block available minus the total blocks needed to build
  up to the current layer
- Return the above number

'''

def calculate_leftover_blocks(n_blocks):
    layer = 0
    blocks_needed = 0

    while True:
        next_layer = layer + 1
        blocks_needed_next_layer = blocks_needed + next_layer**2

        if blocks_needed_next_layer > n_blocks:
            break
        
        layer += 1
        blocks_needed += layer**2
        
    return n_blocks - blocks_needed

print(calculate_leftover_blocks(0) == 0)  # True
print(calculate_leftover_blocks(1) == 0)  # True
print(calculate_leftover_blocks(2) == 1)  # True
print(calculate_leftover_blocks(4) == 3)  # True
print(calculate_leftover_blocks(5) == 0)  # True
print(calculate_leftover_blocks(6) == 1)  # True
print(calculate_leftover_blocks(14) == 0) # True
