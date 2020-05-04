#!/usr/bin/env python3

import click
import logic


@click.command()
def cli():
    """Parse CLI input."""
    logic.example()
