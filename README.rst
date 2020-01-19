
QA Testlink
===========

*qatestlink XMLRPC manager for Testlink*



.. image:: https://img.shields.io/github/issues/netzulo/qatestlink.svg
  :alt: Issues on Github
  :target: https://github.com/netzulo/qatestlink/issues

.. image:: https://img.shields.io/github/issues-pr/netzulo/qatestlink.svg
  :alt: Pull Request opened on Github
  :target: https://github.com/netzulo/qatestlink/issues

.. image:: https://img.shields.io/github/release/netzulo/qatestlink.svg
  :alt: Release version on Github
  :target: https://github.com/netzulo/qatestlink/releases/latest

.. image:: https://img.shields.io/github/release-date/netzulo/qatestlink.svg
  :alt: Release date on Github
  :target: https://github.com/netzulo/qatestlink/releases/latest

+------------------------+-------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------+
|  Branch                |  Linux Deploy                                                           |  Windows Deploy                                                                                  |
+========================+=========================================================================+==================================================================================================+
|  master                |  .. image:: https://travis-ci.org/netzulo/qatestlink.svg?branch=master  |  .. image:: https://ci.appveyor.com/api/projects/status/7low4kw7qa6a5vem/branch/master?svg=true  |
+------------------------+-------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------+


Python tested versions
----------------------

+-------------------+-------------------+-------------------+-------------------+-------------------+
|  **3.7**          |  **3.6**          |  **3.5**          |  **3.4**          |  **>=3.3**        |
+===================+===================+===================+===================+===================+
|    *Supported*    |    *Supported*    |    *Supported*    |    *Supported*    |  *Not Supported*  |
+-------------------+-------------------+-------------------+-------------------+-------------------+


How to install ?
----------------

+ Install from PIP : ``pip install qatestlink``

+ Install from setup.py file : ``python setup.py install``


Documentation
-------------

+ How to use library, searching for `Usage Guide`_.


How to exec tests ?
-------------------

+ 1. Install dependencies for tests : ``pip install -r requirements-tests.txt``
+ 2. Tests from setup.py file : ``python setup.py test``

+ 1. Install TOX : ``pip install tox``
+ 2. Tests from tox : ``tox -l && tox -e TOX_ENV_NAME`` ( *see tox.ini file to get environment names* )

+---------------------+--------------------------------+
| TOX Env name        | Env description                |
+=====================+================================+
| py34,py35,py36      | Python supported versions      |
+---------------------+--------------------------------+
| docs                | Generate doc HTML in /docs     |
+---------------------+--------------------------------+
| flake8              | Exec linter in qalab/ tests/   |
+---------------------+--------------------------------+
| coverage            | Generate XML and HTML reports  |
+---------------------+--------------------------------+


Configuration File
~~~~~~~~~~~~~~~~~~

::

      {
          "connection":{
              "is_https": false,
              "host": "ntz-qa.tk",
              "port": 86
          },
          "dev_key": "1bfd2ef4ceda22b482b12f2b25457495",
          "log_level":"INFO"
      }


Tests
-----

*You will need real testlink app running before you can just execute on command line*

``python setup.py test``


Getting Started
~~~~~~~~~~~~~~~

*Just starting example of usage before read* `Usage Guide`_.

+ 1. Create JSON configuration ( runtime or read from file, *read config section* )
+ 2. Instance **testlink_manager** object ``testlink_manager = TLManager(settings=my_json_config)``
+ 3. Use some *method name with prefix* '**api_**'


.. code:: python


    from qatestlink.core.testlink_manager import TLManager
    from qatestlink.core.utils import settings
    
    
    SETTINGS = settings(
        file_path="/home/user/config/dir/",
        file_name="settings.json"
    )
    
    
    try:
        tlm = TLManager(settings=SETTINGS)
        if not tlm.api_login():
            raise Exception("Not logged for TestlinkWebApp")
        # END
        print(tlm.api_tprojects())
        print("Test PASSED!")
    except Exception as err:
        print("ERROR: {}".format(err))
        import pdb; pdb.set_trace() # TODO, remove DEBUG lane
        print("Test FAILED!")


.. _Usage Guide: USAGE.rst
