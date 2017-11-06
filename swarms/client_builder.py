from client import Client, auth
import config


def build():
    cli = Client(
        config.base_url,
        config.username,
        config.password,
    )

    auth.authenticate(cli)

    return cli
