#!/usr/bin/env python3

import sys

import click
from plexapi.server import PlexServer


@click.command
@click.argument("input_playlists", nargs=-1, required=True)
@click.argument("output_playlist")
def main(input_playlists, output_playlist):
    plex = PlexServer()

    # Read in all items, deduping on the way
    items = {}
    for input_playlist in input_playlists:
        click.echo(f"Reading {input_playlist}...")
        playlist = plex.playlist(input_playlist)
        for item in playlist:
            items[item.key] = item

    click.echo(f"{len(items)} items found from all playlists")

    # Write out the items into a new playlist
    plex.createPlaylist(output_playlist, items=list(items.values()))
    click.echo(f"Created playlist {output_playlist}")


if __name__ == "__main__":
    main()
