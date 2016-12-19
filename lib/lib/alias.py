#!/usr/bin/python
# -*- coding: utf-8 -*-

# pylint's name standards are insane
# pylint: disable=invalid-name

"""
[lib/lib/alias.py]

Defines the "alias" command.
"""

verbs = {}

def alias(env, args, kwargs):
    """CMD1 CMD2@Return the user."""
    env.verbs[args[0]] = env.verbs[args[1]]

verbs["alias"] = alias