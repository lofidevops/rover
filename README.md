# Rover

Just another Mars rover CLI.

## Installation

1. Install Python 3.x and pipenv. (See
   <https://docs.pipenv.org/install/> for a tutorial.)

2. Get source:

        git clone https://github.com/david-libremone/rover.git

3. Install with pipenv:

        cd rover
        pipenv install --dev -e .

## Usage

```
pipenv run rover input.txt output.txt
```

This will parse `input.txt` and write the final rover positions to `output.txt`.

```
pipenv run rover input.txt -
```

Write to STDOUT rather than a file.

```
pipenv run rover input.txt - --verbose
```

Performs the same simulation, but prints the rover state at each step along the way.

A sample input file is included with the source, it should work as follows:

```
$ pipenv run rover sample.txt - --verbose
-: 1 2 N
L: 1 2 W
M: 0 2 W
L: 0 2 S
M: 0 1 S
L: 0 1 E
M: 1 1 E
L: 1 1 N
M: 1 2 N
M: 1 3 N
-: 3 3 E
M: 4 3 E
M: 5 3 E
R: 5 3 S
M: 5 2 S
M: 5 1 S
R: 5 1 W
M: 4 1 W
R: 4 1 N
R: 4 1 E
M: 5 1 E
1 3 N
5 1 E
```

### Input format

```
GX GY
RX RY RO
IIIIIIIIIII
RX RY RO
IIIIIIII...
```

* GX, GY: upper-right limit of the quadrant
* RX, RY, RO: rover initialisation: starting position and orientation
* IIII...: instructions for rover
* Every rover requires an initialisation line, then an instruction line

### Instructions

* L: turn left
* R: turn right
* M: move forward in current orientation

### Skipped instructions

A rover will skip instructions that put it in an invalid position:

* Move beyond a limit
* Move onto another rover
* Start on top of another rover (the second rover will be skipped entirely)

### Output format

```
RX RY RO
RX RY RO
```

* RX, RY, RO: The final position of each rover

If a rover attempts to start on top of another rover, its final position will
be `-1 -1 O`

## Testing

```
pipenv run pytest
```

## Sharing and contributions

Rover  
<https://github.com/david-libremone/rover>  
Copyright 2020 David Seaward  
SPDX-License-Identifier: GPL-3.0-or-later  

Shared under GPL-3.0-or-later. We adhere to the Contributor Covenant
2.0 without modification, and certify origin per DCO 1.1 with a
signed-off-by line. Contributions under the same terms are welcome.

For details see:

* [COPYING.GPL.md], full license text
* [CODE_OF_CONDUCT.md], full conduct text
* [CONTRIBUTING.DCO.md], full origin text (`git -s`)

<!-- Links -->

[COPYING.GPL.md]: COPYING.GPL.md
[CODE_OF_CONDUCT.md]: CODE_OF_CONDUCT.md
[CONTRIBUTING.DCO.md]: CONTRIBUTING.DCO.md
