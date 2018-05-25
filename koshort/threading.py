from threading import Thread


class PropagatingThread(Thread):
    """PropagatingThread is just a fancy wrapper for Thread to manage exceptions.

    Raises:
        self.exception: Exception defined in higher-level.

    Returns:
        self.ret: Thread target object.
    """

    def run(self):
        self.exception = None
        try:
            if hasattr(self, '_Thread__target'):
                # Thread uses name mangling prior to Python 3.
                self.ret = self._Thread__target(*self._Thread__args, **self._Thread__kwargs)
            else:
                self.ret = self._target(*self._args, **self._kwargs)
        except BaseException as e:
            self.exception = e

    def join(self):
        super(PropagatingThread, self).join()
        if self.exception:
            raise self.exception
        return self.ret
