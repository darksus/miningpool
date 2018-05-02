
from miningpool.stratum import socket_transport
from miningpool.stratum.services import ServiceEventHandler
from miningpool.stratum import settings as settings

import miningpool.mining

from miningpool.mining.interfaces import Interfaces
from miningpool.mining.interfaces import WorkerManagerInterface, TimestamperInterface, \
                            ShareManagerInterface, ShareLimiterInterface

from miningpool.mining.interfaces import ShareLimiterInterface

Interfaces.set_share_limiter(ShareLimiterInterface())
Interfaces.set_share_manager(ShareManagerInterface())
Interfaces.set_worker_manager(WorkerManagerInterface())
Interfaces.set_timestamper(TimestamperInterface())

from twisted.internet import defer
on_startup = defer.Deferred()

miningpool.mining.setup(on_startup)

if __name__ == '__main__':
    from twisted.internet import reactor
    signing_key = None
    factory = socket_transport.SocketTransportFactory(debug=settings.DEBUG,
        signing_key=signing_key,
        signing_id=settings.SIGNING_ID,
        event_handler=ServiceEventHandler,
        tcp_proxy_protocol_enable=settings.TCP_PROXY_PROTOCOL)

    reactor.listenTCP(3333, factory)
    reactor.run()
else:
    from twisted.application import service

    application = service.Application("stratum-server")

    signing_key = None
    factory = socket_transport.SocketTransportFactory(debug=settings.DEBUG,
        signing_key=signing_key,
        signing_id=settings.SIGNING_ID,
        event_handler=ServiceEventHandler,
        tcp_proxy_protocol_enable=settings.TCP_PROXY_PROTOCOL)

    socket = internet.TCPServer(3333, factory)
    socket.setServiceParent(application)
