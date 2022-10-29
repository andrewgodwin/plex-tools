#!/usr/bin/env python3

import sys

import click
from plexapi.server import PlexServer


@click.command
@click.argument("playlist_name")
def main(playlist_name):
    plex = PlexServer()

    playlist = plex.playlist(sys.argv[1])

    click.echo(f"{len(playlist)} items in playlist. Sorting...")

    items = [
        {
            "artist": item.artist(),
            "album": item.album(),
            "item": item,
        }
        for item in playlist
    ]
    items.sort(
        key=lambda entry: (
            entry["artist"].title,
            entry["album"].year or 0,
            entry["album"].title,
            entry["item"].trackNumber or 0,
            entry["item"].title,
        )
    )

    for entry in reversed(items):
        playlist.moveItem(entry["item"], None)


if __name__ == "__main__":
    main()
