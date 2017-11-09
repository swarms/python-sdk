Swarms API Python SDK
=====================

This repo contains a Python software development kit to interface with the
Swarms' API, as well as examples of use.

Get started
-----------

This has been tested with Python 2.7 and Python 3.5 (should work with other 3.x
versions too). Install the package from PyPI with `pip install swarms_sdk` or include
`swarms_sdk` in your `requirements.txt` file.

To get your credentials, you currently need to shoot us an email: `info@swarms.tech`

Simplest sample usage:

    from swarms.sdk import services

    config = lambda: None
    config.base_url = 'https://api.swarms.tech/'
    config.username = 'email@example.com'
    config.password = 'password'

    campaigns, jobs, tasks, results = services.get(config)

    print(campaigns.get_all())

For more usage samples, please look at the examples in `swarms/create.py`
(creates campaigns/jobs/tasks), `swarms/retrieve.py`, and `swarms/delete.py`.
