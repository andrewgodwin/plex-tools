Plex Tools
==========

Some basic Plex tooling that I wrote to manage my music playlists.

* ``playlist-sorter.py``: Sorts a playlist by artist, then album, then track
  number, then title.


Installation
------------

Just ensure you have the right requirements::

    pip3 install -r requirements.txt


Usage
-----

Write an env file like this with your server base URL and token (you can get
your personal token from the end of any "View XML" link in plex)::

    export PLEXAPI_AUTH_SERVER_BASEURL="http://venusaur.internal.aeracode.org:32400"
    export PLEXAPI_AUTH_SERVER_TOKEN="not-a-real-token"

Then, source it in your shell::

    source venusaur.env

Then, run the command you want::

    ./playlist-sorter.py "2022/10 October"
