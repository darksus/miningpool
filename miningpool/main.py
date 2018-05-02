#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
miningpool main
"""

import sys

from .stratum import socket_transport
from .stratum.services import ServiceEventHandler
from .stratum import settings as settings

import mining
from .mining.interfaces import Interfaces
from .mining.interfaces import WorkerManagerInterface, TimestamperInterface, \
                            ShareManagerInterface, ShareLimiterInterface

from .mining.interfaces import ShareLimiterInterface

Interfaces.set_share_limiter(ShareLimiterInterface())
Interfaces.set_share_manager(ShareManagerInterface())
Interfaces.set_worker_manager(WorkerManagerInterface())
Interfaces.set_timestamper(TimestamperInterface())

from twisted.internet import defer
on_startup = defer.Deferred()

mining.setup(on_startup)

def main():
    from twisted.internet import reactor
    signing_key = None
    factory = socket_transport.SocketTransportFactory(debug=settings.DEBUG,
        signing_key=signing_key,
        signing_id=settings.SIGNING_ID,
        event_handler=ServiceEventHandler,
        tcp_proxy_protocol_enable=settings.TCP_PROXY_PROTOCOL)

    reactor.listenTCP(3333, factory)
    reactor.run()


if __name__ == "__main__":
    main()
