class ControllerBase():

    def __init__(self, app):
        self._model = None
        self._view = None
        self._app = app
