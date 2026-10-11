from main import Song, Thumbnail, Album

ARTISTS: dict[str, str] = {
        "ARTIST": "Cool ass artist"
}

def get_songs() -> list[Song]:
    return [
        Song("YOUTUBE_MUSIC_URL", "SONG_NAME", "SONG_ARTIST", "THUMBNAIL_NAME"),
    ]

def get_thumbnails() -> list[Thumbnail]:
    return [
        Thumbnail("YOUTUBE_MUSIC_URL", "THUMBNAIL_NAME")
    ]

def get_config() -> dict[str, bool | int | float | str]:
    return {
        "embed-lrc": False,
    }
