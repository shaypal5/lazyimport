"""Tests for lazyimport."""

import pytest

from lazyimport import lazyimport
from lazyimport.errors import (
    InvalidImportLine,
)


def test_basic():
    assert 'strct' not in globals()
    lazyimport(globals(), """import strct""")
    assert 'strct' in globals()
    listi = [8, 2, 5]
    res = strct.lists.all_but(listi, 1)  # noqa: F821
    assert res == [8, 5]
    globals().pop('strct')


def test_name_collision():
    with pytest.raises(InvalidImportLine):
        lazyimport(globals(), """foo()""")


def test_multi_import():
    for name in ['strct', 'comath']:
        assert name not in globals()
    lazyimport(
        globals(),
        """
        import strct
        import comath"""
    )
    for name in ['strct', 'comath']:
        assert name in globals()
    listi = [8, 2, 5]
    res = strct.lists.all_but(listi, 1)  # noqa: F821
    assert res == [8, 5]
    res = comath.array.percentile([4, 6, 8, 9, 11], 0.4)  # noqa: F821
    assert res == 7.0
