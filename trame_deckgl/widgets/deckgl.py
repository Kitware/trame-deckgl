import json
from trame_client.widgets.core import AbstractElement
from trame_deckgl import module


class Deck(AbstractElement):
    _next_id = 0
    """
    Create a Deck element
    """

    def __init__(self, deck=None, **kwargs):
        super().__init__("trame-deck", **kwargs)
        if self.server:
            self.server.enable_module(module)

        Deck._next_id += 1
        self._key = f"trame__deckgl_{Deck._next_id}"
        self._deck = deck

        self.server.state[self._key] = None
        self._attributes["jsonInput"] = f':jsonInput="{self._key}"'
        self._attr_names += [
            "mapboxApiKey",
            ("mapbox_api_key", "mapboxApiKey"),
            "tooltip",
            "customLibraries",
        ]
        self.update()

    def update(self, deck=None, **kwargs):
        if deck:
            self._deck = deck

        if self._deck:
            self.server.state[self._key] = self.to_data(self._deck)

    @property
    def key(self):
        return self._key

    @property
    def deck(self):
        return self._deck

    @staticmethod
    def to_data(deck, **kwargs):
        """
        Serialize plotly figure
        """
        return json.loads(deck.to_json())


__all__ = [
    "Deck",
]
