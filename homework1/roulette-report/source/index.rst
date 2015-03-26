.. Roulette documentation master file, created by
   sphinx-quickstart on Thu Mar 26 14:05:53 2015.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Roulette's documentation!
====================================

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

Header level 2
--------------

header level 3
^^^^^^^^^^^^^^



