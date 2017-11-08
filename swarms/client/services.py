from . import Client, Auth, Campaigns, Jobs, Tasks


def get(config):
    cli = Client(
        config.base_url,
        config.username,
        config.password,
    )

    auth = Auth(cli)
    auth.authenticate()

    return Campaigns(cli), Jobs(cli), Tasks(cli)
