luhn
====

|buildstatus| |coverage|

Generate and verify Luhn check digits

>>> from luhn import *
>>> verify('356938035643809')
True
>>> verify('534618613411236')
False
>>> generate('53461861341123')
4


.. |buildstatus| image:: https://img.shields.io/travis/mmcloughlin/luhn.svg?style=flat-square
   :target: https://travis-ci.org/mmcloughlin/luhn

.. |coverage| image:: https://img.shields.io/coveralls/mmcloughlin/luhn.svg?style=flat-square
   :target: https://coveralls.io/r/mmcloughlin/luhn
