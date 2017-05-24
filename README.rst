=====================
gpstk-examples-python
=====================

**Note that all examples are currently (Oct 2016) broken with Python 2.7. There are numerous issues open on the GPSTk repo, but no code changes since May 2016. The issues are with GPSTk!**

Examples of using GPStk from Python.
Since the examples were `originally written for GPSTk 2.2 <http://www.gpstk.org/pythondoc/examples.html>`_, some of the examples don't work anymore.

.. contents::

.. image:: example5.png
    :alt: example 5

Example Description
===================

=========  ===============  ==================================   ================
Example #  works GPSTk 2.9  Description                          Example Commmand
=========  ===============  ==================================   ================
1          True             current time in several formats      ./example1.py
2          True             basic RINEX read/write/query         ./example2.py
3          Partially        is PRN in view?                      ./example3.py data/rinex3obs_data.txt
4          False            advanced RINEX processing            ./example4.py data/rinex3obs_data.txt data/rinex3nav_data.txt
5          True             plot elevation for the day           ./example5.py
6          True             numerous time format conversions     ./example6.py -h
=========  ===============  ==================================   ================

Install of GPStk in Anaconda Python
===================================

GPStk 2.9 requires Python 2.7--here we use Anaconda Python 2.7 installed to ~/anaconda2. 

1. Download gpstk source::

    git clone https://github.com/SGL-UT/GPSTk
    cd GPSTk

2. prereqs::

    sudo apt-get install g++ make cmake swig doxygen sphinx-common

3. ensure that python2.7 opens, not python3 when you type ``python``. If you need, add a line to ``~/.bashrc``::

    conda create -n py27 python=2.7
    source activate py27

4. build & install::

    ./build.sh -ue
    

Note
----
If you get an error like::

    CMake Error at swig/PythonSetup.cmake:45 (string): string sub-command REGEX, mode MATCH needs at least 5 arguments total to command.

Create a file GPSTk/swig/CustomPythonSetup.cmake with contents (assuming python in ~/anaconda2)::

    set( PYTHONLIBS_FOUND "TRUE" )
    set( PYTHON_LIBRARIES
        "$ENV{HOME}/anaconda2/lib/libpython2.7.so"
        CACHE FILEPATH "File Path to system python shared object library" )
    set( PYTHON_INCLUDE_DIRS
        "$ENV{HOME}/anaconda2/include/python2.7"
         CACHE PATH "Directory Path to system python includes" ) 


`Reference Install Procedure -- just points back here <https://scivision.co/installing-gpstk-in-anaconda-python/>`_

`Example Reference from GPSTk 2.2 <http://www.gpstk.org/pythondoc/examples.html>`_


