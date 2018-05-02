''' A simple wrapper for pylibmc. It can be overwritten with simple hashing if necessary '''
import miningpool.lib.settings as settings
import miningpool.lib.logger
log = miningpool.lib.logger.get_logger('Cache')

try:
    import pylibmc

    class Cache():
        def __init__(self):
            # Open a new connection
            self.mc = pylibmc.Client([settings.MEMCACHE_HOST + ":" + str(settings.MEMCACHE_PORT)], binary=True)
            log.info("Caching initialized")

        def set(self, key, value, time=settings.MEMCACHE_TIMEOUT):
            return self.mc.set(settings.MEMCACHE_PREFIX + str(key), value, time)

        def get(self, key):
            return self.mc.get(settings.MEMCACHE_PREFIX + str(key))

        def delete(self, key):
            return self.mc.delete(settings.MEMCACHE_PREFIX + str(key))

        def exists(self, key):
            return str(key) in self.mc.get(settings.MEMCACHE_PREFIX + str(key))

except:

    class Cache():
        def __init__(self):
            self.mc = dict()

        def set(self, key, value, time=0):
            self.mc[key] = value
            return value

        def get(self, key):
            return self.mc.get(key, None)

        def delete(self, key):
            return self.mc.remove(key)

        def exists(self, key):
            return self.mc.has_key(key)

    pass
