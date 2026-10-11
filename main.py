import os
import sys
import math
import subprocess
import re
import yt_dlp
import ffmpeg_generator
import sqlite3
from pathlib import Path
from enum import Enum
from wand.image import Image
import data as Data

YT_DLP_SONG_INSTALL_OPTS: yt_dlp._Params = {
        "outtmpl": "lol",
        "format": "mp3/bestaudio/best",
        # "extractor_args": {"youtube": {"player_client": "android"}},
        "postprocessors": [{
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3"
        }]
}

YT_DLP_THUMBNAIL_INSTALL_OPTS: yt_dlp._Params = {
        "outtmpl": "lol",
        "writethumbnail": True,
        "skip_download": "True"
}

# TODO: Load the config from the file
config: dict[str, int | float | str | bool] = {
        "embed_lrc_files": False,
        "generate_cache": True
}

sqlite_connection: sqlite3.Connection | None = None
sqlite_cursor: sqlite3.Cursor | None = None

def song_install(songs: list[Song]) -> None:
    global config
    global sqlite_connection
    global sqlite_cursor

    for s in songs:
        if Path(Util.Path.installed_song(s.file_name)).exists(): continue
        current_opts: yt_dlp._Params = YT_DLP_SONG_INSTALL_OPTS
        current_opts["outtmpl"] = Util.Path.installed_song(s.file_name).replace(".mp3", ".%(ext)s")
        ydl: yt_dlp.YoutubeDL = yt_dlp.YoutubeDL(current_opts)
        ydl.download(s.link)


def thumbnail_install(thumbnails: list[Thumbnail]) -> None:
    global config
    global sqlite_connection
    global sqlite_cursor

    for t in thumbnails:
        if Path(Util.Path.installed_thumbnail(t.file_name)).exists(): continue
        current_opts: yt_dlp._Params = YT_DLP_THUMBNAIL_INSTALL_OPTS
        current_opts["outtmpl"] = Util.Path.installed_thumbnail(t.file_name).replace(".webp", ".%(ext)s")
        ydl: yt_dlp.YoutubeDL = yt_dlp.YoutubeDL(current_opts)
        ydl.download(t.link)


def song_convert(songs: list[Song]) -> None:
    global config
    global sqlite_connection
    global sqlite_cursor
    
    command: ffmpeg_generator.FFmpegCommand = ffmpeg_generator.FFmpegCommand()
    command.hide_banner = True

    cache_buffer: list[str] = []

    for s in songs:
        if sqlite_cursor != None and s.has_cache(sqlite_cursor):
            print("SONG \"{}\" SKIPPED DUE TO CACHE".format(s.title))
            cache_buffer.append(s.get_cache_command(sqlite_cursor))
            continue

        print("SONG CONVERSION: \"{}\"".format(s.title))

        lyrics: str | None = None
        if s.has_lyrics == True and config["embed_lrc_files"] == True and Path(Util.Path.lyrics()).exists():
            lyrics = open(Util.Path.lyrics(s.file_name), "r").read()

        command.inputs.clear()
        if s.begin_cut != None:
            command.inputs.append(ffmpeg_generator.FFmpegCommand.Input(Util.Path.installed_song(s.file_name), 0, Util.time_to_str(s.begin_cut), Util.time_to_str(s.get_final_song_duration())))
        else:
            command.inputs.append(ffmpeg_generator.FFmpegCommand.Input(Util.Path.installed_song(s.file_name), 0))

        if s.thumbnail_name != None:
            command.inputs.append(ffmpeg_generator.FFmpegCommand.Input(Util.Path.finished_thumbnail(s.thumbnail_name), 1))

        command.metadata = s.get_metadata_dict()
        if lyrics != None and config["embed_lrc_files"] == True:
            command.metadata["lyrics"] = lyrics
        
        command.output = Util.Path.finished_song(s.file_name)
            
        if sqlite_cursor != None:
            cache_buffer.append(s.get_cache_command(sqlite_cursor))

        command_string: str | None = command.get_command()
        if command_string != None:
            os.system(command_string)

    if sqlite_cursor != None and sqlite_connection != None:
        sqlite_cursor.execute("DELETE FROM SONG")
        for c in cache_buffer:
            sqlite_cursor.execute(c)
        sqlite_connection.commit()


def thumbnail_convert(thumbnails: list[Thumbnail]) -> None:
    global config
    global sqlite_connection
    global sqlite_cursor

    for t in thumbnails:
        if Path(Util.Path.finished_thumbnail(t.file_name)).exists():
            continue
    
        with Image(filename=Util.Path.installed_thumbnail(t.file_name)) as img:
            img.crop(left=280, width=720, height=720)
            img.save(filename=Util.Path.finished_thumbnail(t.file_name))


def generate_empty_lrc(songs: list[Song]) -> None:
    for s in songs:
        if Path(Util.Path.lyrics(s.file_name)).exists() or s.has_lyrics == False:
            continue
        file = open(Util.Path.lyrics(s.file_name), "w")

        file_content: str = "[ti: {}]\n[ar: {}]\n[length: {}]".format(s.title, s.get_artists_as_string(";"), Util.time_to_str(s.get_final_song_duration()))
        if s.album != None:
            file_content += "\n[al: {}]".format(s.album.value)
        file_content += "\n[offset: 0]\n\n" # Last for asthetic reasons :D
        file.write(file_content)
        file.close()


def main(argv: list[str]) -> None:
    global config
    global sqlite_connection
    global sqlite_cursor

    if not os.path.exists(Util.Path.installed_song()): os.mkdir(Util.Path.installed_song() + "/")
    if not os.path.exists(Util.Path.installed_thumbnail()): os.mkdir(Util.Path.installed_thumbnail() + "/")
    if not os.path.exists(Util.Path.finished_song()): os.mkdir(Util.Path.finished_song() + "/")
    if not os.path.exists(Util.Path.finished_thumbnail()): os.mkdir(Util.Path.finished_thumbnail() + "/")
    if not os.path.exists(Util.Path.lyrics()): os.mkdir(Util.Path.lyrics() + "/")

    config = Data.get_config()

    sqlite_connection = sqlite3.connect("cache.db")
    if config["generate_cache"] == True and not "-ic" in argv:
        sqlite_cursor = sqlite_connection.cursor()

    if sqlite_cursor != None:
        sqlite_cursor.execute("CREATE table IF NOT EXISTS SONG(LINK TEXT, TITLE TEXT, ARTIST TEXT, THUMBNAIL_NAME TEXT, ALBUM TEXT, TRACK INT, START_CUT INT, END_CUT INT, GENRE TEXT, FILE_NAME TEXT, HAS_LYRICS INT)")

    if "-is" in argv:
        song_install(Data.get_songs())
    if "-it" in argv:
        thumbnail_install(Data.get_thumbnails())
    if "-ct" in argv:
        thumbnail_convert(Data.get_thumbnails())
    if "-cs" in argv:
        song_convert(Data.get_songs())
    if "-gl" in argv:
        generate_empty_lrc(Data.get_songs())


class Util:
    @classmethod
    def to_snake_case(cls, text: str):
        return re.sub("\\s+", "_", re.sub("[^\\d\\w\\s]", "", re.sub("[-+!]", " ", text)).strip()).lower()

    @classmethod
    def time_to_str(cls, time: int) -> str:
        milliseconds: int = time%1000
        seconds: int = math.floor(time/1000)
        minutes: int = math.floor(seconds/60)
        hours: int = math.floor(minutes/60)

        seconds %= 60
        minutes %= 60

        return "{}:{}:{}.{}".format(hours, minutes, seconds, str(milliseconds).replace(".", ""))

    class Path():
        @classmethod
        def installed_song(cls, file_name: str | None = None, include_type: bool = True) -> str:
            return os.getcwd() + "/output/installed_songs" + ("/{}".format(file_name) if file_name != None else "") + (".mp3" if file_name != None and include_type == True else "")
        @classmethod
        def installed_thumbnail(cls, file_name: str | None = None, include_type: bool = True) -> str:
            return os.getcwd() + "/output/installed_thumbnails" + ("/{}".format(file_name) if file_name != None else "") + (".webp" if file_name != None and include_type == True else "")
        @classmethod
        def finished_song(cls, file_name: str | None = None, include_type: bool = True) -> str:
            return os.getcwd() + "/output/finished_songs" + ("/{}".format(file_name) if file_name != None else "") + (".mp3" if file_name != None and include_type == True else "")
        @classmethod
        def finished_thumbnail(cls, file_name: str | None = None, include_type: bool = True) -> str:
            return os.getcwd() + "/output/finished_thumbnails" + ("/{}".format(file_name) if file_name != None else "") + (".webp" if file_name != None and include_type == True else "")
        @classmethod
        def lyrics(cls, file_name: str | None = None, include_type: bool = True) -> str:
            return os.getcwd() + "/output/lyrics" + ("/{}".format(file_name) if file_name != None else "") + (".lrc" if file_name != None and include_type == True else "")


class Album(Enum):
    HOLLOW_KNIGHT_MUSICAL = "Hollow Knight Musical Bytes"
    UNDERTALE_GENOCIDE_PACKAGE = "Undertale Genocide Package"
    UNDERTALE_THE_MUSICAL = "Undertale The Musical"
    DELTARUNE_THE_NOT_MUSICAL = "Deltarune The (not) Musical"
    RAISED_BY_ALIENS = "Raised by Aliens"
    REBIRTH = "Rebirth"
    FORGIVE_ME_PLEASE = "Forgive Me Please"
    OUR_SUMMER_DREAMS = "Our Summer Dreams"
    ULTRAKILL_OST = "Ultrakill OST"
    THE_TALE_OF_A_CRUEL_WORLD_CALAMITY_OST = "The Tale of a Cruel World (Calamity Original Game Soundtrack)"


class Song:
    link: str = ""
    title: str = ""
    artists: list[str] = []
    thumbnail_name: str | None = None
    album: Album | None = None
    track: int | None = None
    begin_cut: int = 0 # In ms
    end_cut: int = 0 # In ms
    genre: str | None = None
    file_name: str = ""
    has_lyrics: bool = True
    year: int | None = None

    def __init__(self, link: str, title: str, artists: list[str] | str, thumbnail: str | None = None, album: Album | None = None, track: int | None = None, **kwargs):
        for i in kwargs:
            if hasattr(self, i):
                setattr(self, i, kwargs[i]);

        self.link = link
        self.title = title
        if type(artists) == list:
            self.artists = artists
        elif type(artists) == str:
            self.artists = [artists]
        self.thumbnail_name = thumbnail
        self.album = album
        self.track = track
        if self.file_name == "":
            self.file_name = self.get_default_file_name()

    def get_artists_as_string(self, separator: str) -> str:
        return separator.join(self.artists)

    def get_default_file_name(self) -> str:
        return Util.to_snake_case(self.title) + "_" + Util.to_snake_case(self.artists[0])

    def get_metadata_dict(self) -> dict[str, str]:
        ret_dict: dict[str, str] = {}
        ret_dict["title"] = self.title
        ret_dict["artist"] = self.get_artists_as_string(";")
        if self.album != None:
            ret_dict["album"] = self.album.value
        if self.track != None:
            ret_dict["track"] = str(self.track)
        if self.genre != None:
            ret_dict["genre"] = self.genre

        return ret_dict

    def has_cache(self, cursor: sqlite3.Cursor) -> bool:
        ret = cursor.execute(
                'SELECT * FROM SONG WHERE LINK = "{}" AND TITLE = "{}" AND ARTIST = "{}" AND THUMBNAIL_NAME = "{}" AND ALBUM = "{}" AND TRACK = {} AND START_CUT = {} AND END_CUT = {} AND GENRE = "{}" AND FILE_NAME = "{}" AND HAS_LYRICS = {}'.format(
                    self.link,
                    self.title,
                    self.get_artists_as_string(";"),
                    self.thumbnail_name if self.thumbnail_name != None else "",
                    self.album if self.album != None else "",
                    self.track if self.track != None else 0,
                    self.begin_cut,
                    self.end_cut,
                    self.genre if self.genre != None else "",
                    self.file_name,
                    0 if self.has_lyrics == False else 1
                    )
                )
        return ret.fetchone() != None

    def get_cache_command(self, cursor: sqlite3.Cursor) -> str:
        return 'INSERT INTO SONG(LINK, TITLE, ARTIST, THUMBNAIL_NAME, ALBUM, TRACK, START_CUT, END_CUT, GENRE, FILE_NAME, HAS_LYRICS) VALUES ("{}", "{}", "{}", "{}", "{}", "{}", {}, {}, "{}", "{}", {})'.format(
                self.link,
                self.title,
                self.get_artists_as_string(";"),
                self.thumbnail_name if self.thumbnail_name != None else "",
                self.album if self.album != None else "",
                self.track if self.track != None else 0,
                self.begin_cut,
                self.end_cut,
                self.genre if self.genre != None else "",
                self.file_name,
                (1 if self.has_lyrics == True else 0)
                )

    def get_song_duration(self) -> int:
        DURATION_CHECK_COMMAND: str = 'ffprobe -i {} -show_entries format=duration -v quiet -of csv=p=0'.format(Util.Path.installed_song(self.file_name))
        string_time = str(subprocess.check_output(DURATION_CHECK_COMMAND.split(" "))).split("'")[1].replace("\\n", "")

        milliseconds: int = int(string_time.split(".")[1][:3])
        seconds: int = int(string_time.split(".")[0])
        final_time: float = milliseconds + seconds*1000

        return final_time

    def get_final_song_duration(self) -> int:
        return self.get_song_duration() - self.begin_cut - self.end_cut


class Thumbnail:
    link: str = ""
    file_name: str = ""

    def __init__(self, link: str, file_name: str) -> None:
        self.link = link
        self.file_name = file_name


if __name__ == "__main__":
    args: list[str] = sys.argv
    args.pop(0)
    main(args)
