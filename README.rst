lazyimport
##########
|PyPI-Status| |PyPI-Versions|  |LICENCE|

.. ..  |Build-Status| |Codecov|

``lazyimport`` lets you import python modules lazily.

.. code-block:: python

  from lazyimport import lazyimport
  lazyimport(globals(), """
    from mypackage import submodule
    import another_package
    """
  )

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

The ``lazyimport`` function and 

.. code-block:: python

  from lazyimport import lazyimport
  lazyimport(globals(), """
    from mypackage import submodule
    import another_package
    """
  )


Credits
=======

Written by Paul Ivanov - https://github.com/ivanov - for the nitime library -
https://github.com/nipy/nitime.

Written by John Arbash Meinel, Martin von Gagern, Martin Packman and others
as part of the the GNU Bazaar revision control system.

As such, lazyimport is distributed under the GNU General Public License v3,
like GNU Bazzar itself.

Slightly adapted to package form by Shay Palachy - https://github.com/shaypal5


.. alternative:
.. https://badge.fury.io/py/yellowbrick.svg

.. |PyPI-Status| image:: https://img.shields.io/pypi/v/lazyimport.svg
  :target: https://pypi.org/project/lazyimport

.. |PyPI-Versions| image:: https://img.shields.io/pypi/pyversions/lazyimport.svg
   :target: https://pypi.org/project/lazyimport

.. |Build-Status| image:: https://travis-ci.org/shaypal5/lazyimport.svg?branch=master
  :target: https://travis-ci.org/shaypal5/lazyimport

.. |LICENCE| image:: https://img.shields.io/badge/License-GNU3-yellow.svg
  :target: https://github.com/shaypal5/lazyimport/blob/master/LICENSE
  
.. .. |LICENCE| image:: https://github.com/shaypal5/lazyimport/blob/master/mit_license_badge.svg
  :target: https://pypi.python.org/pypi/lazyimport
  
.. https://img.shields.io/pypi/l/lazyimport.svg

.. |Codecov| image:: https://codecov.io/github/shaypal5/lazyimport/coverage.svg?branch=master
   :target: https://codecov.io/github/shaypal5/lazyimport?branch=master
