from grongier.pex._common import _Common

class _OutboundAdapter(_Common):
    """ Responsible for sending the data to the external system."""

    def __init__(self):
        """ The BusinessHost variable provides access to the BusinessOperation associated with the OutboundAdapter."""
        super().__init__()
        self.BusinessHost = None
    
    def OnConnected(self):
        """ The OnConnected() method is called when the component is connected or reconnected after being disconnected.
        Use the OnConnected() method to initialize any structures needed by the component."""
        pass

    def OnInit(self):
        """ The OnInit() method is called when the component is started.
        Use the OnInit() method to initialize any structures needed by the component."""
        pass

    def OnTearDown(self):
        """ Called before the component is terminated. Use it to freee any structures."""
        pass

    def _set_iris_handles(self, handleCurrent, handlePartner):
        """ For internal use only. """
        self.irisHandle = handleCurrent
        self.BusinessHost = handlePartner
        return

    def _dispatch_on_connected(self, hostObject):
        """ For internal use only. """
        self.OnConnected()
        return

    def _dispatch_on_init(self, hostObject):
        """ For internal use only. """
        self.OnInit()
        return

    def _dispatchOnTearDown(self, hostObject):
        """ For internal use only. """
        self.OnTearDown()
        return