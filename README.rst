High-scale spatial rendering for trame
===========================================================================

trame-deckgl extend trame **widgets** with components that can interface with PyDeck while being powered by Deck.gl.
Deck integration in trame allow you to create rich visualization by leveraging `PyDeck <https://pydeck.gl/index.html>`_ (`Apache License <https://github.com/visgl/deck.gl/blob/master/bindings/pydeck/LICENSE.txt>`_).


Installing
-----------------------------------------------------------

trame-deckgl can be installed with `pip <https://pypi.org/project/trame-deckgl/>`_:

.. code-block:: bash

    pip install --upgrade trame-deckgl


Usage
-----------------------------------------------------------

The `Trame Tutorial <https://kitware.github.io/trame/docs/tutorial.html>`_ is the place to go to learn how to use the library and start building your own application.

The `API Reference <https://trame.readthedocs.io/en/latest/index.html>`_ documentation provides API-level documentation.


License
-----------------------------------------------------------

trame-deckgl is made available under the MIT License. For more details, see `LICENSE <https://github.com/Kitware/trame-deckgl/blob/master/LICENSE>`_
This license has been chosen to match the one use by `Deck.gl <https://github.com/visgl/deck.gl/blob/master/LICENSE>`_ which is use within trame-deckgl.


Community
-----------------------------------------------------------

`Trame <https://kitware.github.io/trame/>`_ | `Discussions <https://github.com/Kitware/trame/discussions>`_ | `Issues <https://github.com/Kitware/trame/issues>`_ | `RoadMap <https://github.com/Kitware/trame/projects/1>`_ | `Contact Us <https://www.kitware.com/contact-us/>`_

.. image:: https://zenodo.org/badge/410108340.svg
    :target: https://zenodo.org/badge/latestdoi/410108340


Enjoying trame?
-----------------------------------------------------------

Share your experience `with a testimonial <https://github.com/Kitware/trame/issues/18>`_ or `with a brand approval <https://github.com/Kitware/trame/issues/19>`_.


Example: PyDeck
-----------------------------------------------------------

The Deck component relies on the server for generating the map definition.

.. code-block:: python

    import pydeck as pdk
    from trame.widgets import deckgl

    deck = pdk.Deck(
      map_provider="mapbox",
      map_style="mapbox://styles/mapbox/light-v9",
      initial_view_state={
          "latitude": 37.76,
          "longitude": -122.4,
          "zoom": 11,
          "pitch": 50,
      },
      layers=selected_layers,
    )

    widget = deckgl.Deck(mapboxApiKey=..., deck=deck)
    widget.update(deck2)
