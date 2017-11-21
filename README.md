Swarms API Python SDK
=====================

[![Build Status](https://travis-ci.org/swarms/python-sdk.svg?branch=master)](https://travis-ci.org/swarms/python-sdk)

This repo contains a Python software development kit to interface with the
[Swarms' API](https://swarms.docs.apiary.io/), as well as examples of use.

Get started
-----------

This has been tested with Python 2.7 and Python 3.5 (should work with other 3.x
versions too). Install the package from PyPI with `pip install swarms-sdk` or
include `swarms-sdk` in your `requirements.txt` file.

To get your credentials, you currently need to shoot us an email:
`info@swarms.tech`

Examples
--------

Simplest sample usage:

    from swarms.sdk import services

    config = lambda: None
    config.base_url = 'https://api.swarms.tech/'
    config.username = 'email@example.com'
    config.password = 'password'

    campaigns, jobs, tasks, results = services.get(config)

    print(campaigns.get_page())

For more usage examples, please look at how to [create resources][create],
[retrieve resources][retrieve], and [delete everything][delete].

[create]: https://github.com/swarms/python-sdk/blob/master/swarms/create.py
[retrieve]: https://github.com/swarms/python-sdk/blob/master/swarms/retrieve.py
[delete]: https://github.com/swarms/python-sdk/blob/master/swarms/delete.py

Resource upload
---------------

The SDK downloads any referenced resources and uploads them to Swarms' servers.
This is done to prevent breakage when the original resources disappear.

Information about the API
-------------------------

Please see the [API docs](https://swarms.docs.apiary.io/) for general information.
See the [components overview](https://swarms.docs.apiary.io/#reference/components-overview)
to learn what types of components are available in your tasks.

Development
-----------

To release a new version, increase version number in `setup.py`, create package
with `python setup.py sdist` and release the package with `twine upload`.
