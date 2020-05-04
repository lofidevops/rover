# Rover

Just another Mars rover CLI.

## Installation

1. Install Python 3.x and pipenv. (See
   <https://docs.pipenv.org/install/> for a tutorial.)

2. Get source:

        git clone https://example.com/rover.git

3. Install with pipenv:

        cd rover
        pipenv install --dev -e .

## Usage

```
pipenv run rover input.txt -
```

This will parse `input.txt` and write the results to STDOUT. Replace
`-` with a filename to write to an output file. Run
```pipenv run rover --help``` for additional details.

A sample input file is included with the source.

## Sharing and contributions

Rover  
<https://example.com>  
Copyright 2020 David Seaward  
SPDX-License-Identifier: GPL-3.0-or-later  

Shared under GPL-3.0-or-later. We adhere to the Community Covenant
2.0 without modification, and certify origin per DCO 1.1 with a
signed-off-by line. Contributions under the same terms are welcome.

For details see:

* [COPYING.GPL.md], full license text
* [CODE_OF_CONDUCT.md], full conduct text
* [CONTRIBUTING.DCO.md], full origin text (`git -s`)

<!-- Links -->

[COPYING.GPL.md]: COPYING.AGPL.md
[CODE_OF_CONDUCT.md]: CODE_OF_CONDUCT.md
[CONTRIBUTING.DCO.md]: CONTRIBUTING.DCO.md
