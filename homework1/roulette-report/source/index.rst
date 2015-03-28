.. Roulette documentation master file, created by
   sphinx-quickstart on Thu Mar 26 14:05:53 2015.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Roulette's documentation!
====================================

Classes and methods
===================

.. py:class:: Player(playername, money_set)

A player can play at the roulette table and win or lose money

    .. py:method:: bet(mainoption,option,money)

    .. py:method:: getbetoptions()

    .. py:method:: getbettedmoney(mainoption,option)

    .. py:method:: bet(mainoption,option,money)

    .. py:method:: wins(money)

    .. py:method:: loses(money)

    .. py:method:: getmoneystatus()

    .. py:method:: cleanupbets():


.. py:class::  RouletteTable()

    .. py:method:: starting_playing()

    .. py:method:: betting_phase()

    .. py:method:: rotate_roulette()

    .. py:method:: getcolor()

    .. py:method:: checkeven()

    .. py:method:: addmoney2table(money)

    .. py:method:: takemoneyfromtable(money)

    .. py:method:: winning_quote(option)::

    .. py:method:: payout_phase::

    .. py:method:: nextround()::

    .. py:method:: stop_playing()::


Sphinx info (remove later)
==========================

.. note::

   Achtung: reStructuredText ist *fast* wie markdown, aber es 
   gibt dann und wann kleine Unterschiede (zb bei Tabellen), dafür kann es
   aber auch mehr. Github interpretiert das geschriebene als markdown,
   dadurch sieht der text hier etwas anders aus als in dem fertigen report
   (z.b. diese "note" box hier)

Install guide für sphinx:

.. code-block:: bash

    pip install sphinx
    pip install rst2pdf

Dokumentation Builden (liunx):

Sind die oberen beiden Pakete installiert, kann man die dokumentation
in verschiedene Formate builden. Ich hab jetzt nur erfahrungen unter linux,
sollte unter windows aber sehr ähnlich gehen (make.bat verwenden)

.. code-block:: bash

    cd roulette-report/

    make pdf 
    make html 
    make epub
    ...
   

**reStructuredText Primer**
http://sphinx-doc.org/rest.html

**Documenting python in Sphinx** 
http://sphinx-doc.org/domains.html#domains

Header level 2
--------------

header level 3
^^^^^^^^^^^^^^
