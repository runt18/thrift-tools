import os

_resources_dir = os.path.join(
    os.path.realpath(os.path.dirname(__file__)),
    'resources'
)


def get_pcap_path(capture_file):
    return os.path.join(_resources_dir, '{0!s}.pcap'.format((capture_file)))


def get_log_path(log_file):
    return os.path.join(_resources_dir, '{0!s}.logfile'.format((log_file)))
