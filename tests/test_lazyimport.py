"""Tests for lazyimport."""

from lazyimport import lazyimport


def test_basic():
    global_scope = globals()
    assert 'strct' not in global_scope
