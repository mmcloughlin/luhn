luhn
====

|pypi| |buildstatus| |coverage|

Generate and verify Luhn check digits

Install with

..

    pip install luhn

Use ``verify`` to check digit strings

.. code:: python

    >>> from luhn import *
    >>> verify('356938035643809')
    True
    >>> verify('534618613411236')
    False

and use ``generate`` to produce them

.. code:: python

    >>> generate('53461861341123')
    4


.. |pypi| image:: https://img.shields.io/pypi/v/luhn.svg?style=flat-square
   :target: https://pypi.python.org/pypi/luhn

.. |buildstatus| image:: https://img.shields.io/travis/mmcloughlin/luhn.svg?style=flat-square
   :target: https://travis-ci.org/mmcloughlin/luhn

.. |coverage| image:: https://img.shields.io/coveralls/mmcloughlin/luhn.svg?style=flat-square
   :target: https://coveralls.io/r/mmcloughlin/luhn
