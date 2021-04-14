#!/bin/bash
# Used to launch the py4web server with sane configuration (probably should be dockerized later)
py4web run -H 127.0.0.1 -P 8000 -d full apps
