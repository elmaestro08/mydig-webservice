import logging

config = {
    'debug': True,
    'server': {
        'host': '127.0.0.1',
        'port': 5000,
    },
    'repo': {
        'local_path': '../../mydig-projects-test',
        'github': {
            'enable_sync': True,
            'remote_url': 'https://github.com/GreatYYX/mydig-project-test.git',
            # generate & deploy ssh key
            # https://help.github.com/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent/
            'ssh_key_file_path': '/Users/yixiang/.ssh/mydig_key'
        }
    },
    'logging': {
        'file_path': 'log.log',
        'format': '%(asctime)s %(levelname)s %(message)s',
        'level': logging.INFO
    },
    'es': {
        # do not add / at the end
        'url': 'http://localhost:9200'
    },
    'users': {
        'admin': '123' # basic YWRtaW46MTIz
    }
}