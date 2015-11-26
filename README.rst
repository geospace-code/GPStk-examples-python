.. image:: https://codeclimate.com/github/scienceopen/gpstk-examples-python/badges/gpa.svg
   :target: https://codeclimate.com/github/scienceopen/gpstk-examples-python
   :alt: Code Climate

=====================
gpstk-examples-python
=====================
Examples of using GPStk 2.5 from Python.

Install of GPStk in Python
==========================

GPStk requires Python 2.7.

1) Download gpstk source::

    git clone https://github.com/SGL-UT/GPSTk
    cd GPSTk

2) Install prereqs::

    sudo apt-get install g++ make cmake swig doxygen libsphinxbase1

3) Assuming you're using Anaconda Python installed to ``~/anaconda``, create a file ``CustomPythonSetup.cmake`` with the content::
    
    set( PYTHONLIBS_FOUND "TRUE" )
    set( PYTHON_LIBRARIES 
     "$ENV{HOME}/anaconda/lib/libpython2.7.so"
     CACHE FILEPATH "File Path to system python shared object library" )  
    set( PYTHON_INCLUDE_DIRS
     "$ENV{HOME}/anaconda/include"
     CACHE PATH "Directory Path to system python includes" )
    


`Reference Install Procedure <https://scivision.co/installing-gpstk-in-anaconda-python/>`_

.. image:: example5.png
    :alt: example 5
