Installation
------------
Currently clone or download from `GitHub <https://github.com/Open-ET/flux-data-qaqc/edit/master/README.md>`_.  

.. code-block:: bash

    $ git clone https://github.com/Open-ET/flux-data-qaqc.git

Optionally, as opposed to using PIP, you may install dependencies with the provided Conda virtual environment. This is useful to avoid changing your local Python environment. Note, ``flux-data-qaqc`` has been tested for Python 3.7+, although it may work with versions greater than or equal to 3.4.

First make sure you have the ``fluxdataqaqc`` environment file, you can download it `here <https://raw.githubusercontent.com/Open-ET/flux-data-qaqc/master/environment.yml?token=AB3BJKUKL2ELEM7WPLYLXFC45WQOG>`_. Next to install run,

.. code-block:: bash

    $ conda env create -f environment.yml

To activate the environment before using the ``flux-data-qaqc`` package run,

.. code-block:: bash

    $ conda activate fluxdataqaqc

Run the following to install ``flux-data-qaqc`` in developer mode, soon the package will be uploaded and available on `PYPI <https://pypi.org>`_,

.. code-block:: bash

    $ cd flux-data-qaqc
    $ pip install -e .

Now all package modules and tools should be available in your Python environment PATH and able to be imported. Note if you did not install the Conda virtual environment above, PIP should install dependencies automatically but be sure to be using a version of Python above or equal to 3.4. To test that everything has installed correctly by opening a Python interpretor or IDE and run the following:

.. code-block:: python

    import fluxdataqaqc

and 

.. code-block:: python

    from fluxdataqaqc import Data, QaQc, Plot

If everything has been installed correctly you should get no errors. 
