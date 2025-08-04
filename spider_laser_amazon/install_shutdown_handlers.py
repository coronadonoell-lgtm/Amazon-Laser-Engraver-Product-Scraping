from twisted.internet import reactor


def install_shutdown_handlers(_signal_handler):
    """
    Install shutdown signal handlers on supported Twisted reactors.
    Safely skip if the reactor does not support _handleSignals (e.g., on Windows).

    Note: This accesses a protected Twisted method used by Scrapy itself.
    """
    handle_signals = getattr(reactor, "_handleSignals", None)
    if callable(handle_signals):
        try:
            handle_signals()
        except (AttributeError, NotImplementedError):
            pass
