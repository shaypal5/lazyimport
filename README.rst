lazyimport
##########


``lazyimport`` lets you import python modules lazily.

.. code-block:: python

  from lazyimport import lazyimport
  lazyimport(globals(), """
    from mypackage import submodule
    import another_package
    """

.. contents::

.. section-numbering::


Installation
============

.. ``lazyimport`` is tested on Python 2.7, 3.4, 3.5 and 3.6.

Install ``lazyimport`` with:

.. code-block:: bash

  pip install lazyimport


Use
===

Soon.


Credits
=======

..Written by Paul Ivanov - https://github.com/ivanov - for the nitime library -
https://github.com/nipy/nitime.

Written by John Arbash Meinel, Martin von Gagern, Martin Packman and others
as part of the the GNU Bazaar revision control system.

As such, lazyimport is distributed under the GNU General Public License v3,
like GNU Bazzar itself.

Slightly adapted to package form by Shay Palachy - https://github.com/shaypal5.
