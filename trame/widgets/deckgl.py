from trame_deckgl.widgets.deckgl import *


def initialize(server):
    from trame_deckgl import module

    server.enable_module(module)
