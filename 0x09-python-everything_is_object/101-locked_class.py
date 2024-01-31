#!/usr/bin/python3
"""Defines locked class."""


class LockedClass:
    """locked the user from making new attr
    for ath except 'first_name'."""

    __slots__ = ["first_name"]
