from pathlib import Path

# Compute local path to serve
serve_path = str(Path(__file__).with_name("serve").resolve())

# Serve directory for JS/CSS files
serve = {"__trame_deckgl": serve_path}

# List of JS files to load (usually from the serve path above)
scripts = [
    "__trame_deckgl/trame-deckgl.umd.min.js",
]

# List of Vue plugins to install/load
vue_use = ["TrameDeckGL"]
