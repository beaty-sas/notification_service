import pkg_resources

UNKNOWN = 'unknown'

try:
    __version__ = pkg_resources.get_distribution('notification_service').version

except pkg_resources.DistributionNotFound:
    __version__ = UNKNOWN
