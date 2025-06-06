import yaml


_config = None


def get_config():
    global _config
    if _config is None:
        with open('settings.yaml', 'r') as file:
            _config = yaml.safe_load(file)
    return _config

def write_config():
    '''
    NOTE enable config change via Telegram
    this funtion is planned for later, allowing
    the write config changes to the file for
    persistent changes via the telegram bot
    interface.
    '''
    with open('config.yaml', 'w') as file:
        yaml.safe_dump(_config, file, sort_keys=False)
    return