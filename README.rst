=====================
gpstk-examples-python
=====================

Examples of using `GPSTk <https://github.com/SGL-UT/GPSTk>`_ from Python, since the examples included by GPSTk are somewhat broken for Python.
Some `examples <http://www.gpstk.org/pythondoc/examples.html>`_ were originally written for GPSTk 2.2, but I fixed them to work with GPSTk 2.10.

.. contents::

.. image:: example5.png
    :alt: example 5

Examples
========

1
-
current time in several formats::

    ./example1.py
     
2
-
basic RINEX read/write/query::

    ./example2.py

3
-
is PRN in view?::      

    ./example3.py data/rinex3obs_data.txt
    
4
-
advanced RINEX processing::

    ./example4.py data/rinex3obs_data.txt data/rinex3nav_data.txt
    
5
-
plot elevation for the day::

    ./example5.py
    
6
-
numerous time format conversions::

    ./example6.py -h


Install
=======

GPStk 2.10 requires Python 2.7. You can use Anaconda to switch to Python 2.7 by::

    conda create -n py27 python=2.7
    . activate py27
 

1. Download gpstk source::

    git clone https://github.com/SGL-UT/GPSTk
    cd GPSTk
2. prereqs::

    apt install g++ make cmake swig doxygen sphinx-common
3. Build & install. This take several minutes, and emits a very large number of C++11 deprecation warnings::

    ./build.sh -ue
    

Notes
=====
If you get an error like

    CMake Error at swig/PythonSetup.cmake:45 (string): string sub-command REGEX, mode MATCH needs at least 5 arguments total to command.

Create a file GPSTk/swig/CustomPythonSetup.cmake with contents (assuming python in ~/anaconda2)

.. code:: cmake

    set( PYTHONLIBS_FOUND "TRUE" )
    set( PYTHON_LIBRARIES
        "$ENV{HOME}/anaconda2/lib/libpython2.7.so"
        CACHE FILEPATH "File Path to system python shared object library" )
    set( PYTHON_INCLUDE_DIRS
        "$ENV{HOME}/anaconda2/include/python2.7"
         CACHE PATH "Directory Path to system python includes" ) 


`Reference Install Procedure -- just points back here <https://www.scivision.co/installing-gpstk-in-anaconda-python/>`_

`Example Reference from GPSTk 2.2 <http://www.gpstk.org/pythondoc/examples.html>`_


