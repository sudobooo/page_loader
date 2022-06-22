"""Page-loader engine"""

from page_loader.download import download


__all__ = ('download',)


class ExpectedException(Exception):
    """Own class for catching and handling exceptions."""

    pass
