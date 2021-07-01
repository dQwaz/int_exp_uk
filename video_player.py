"""A video player class."""

from video_library import VideoLibrary
import random
import constant

class VideoPlayer:
    """A class used to represent a Video Player."""
    playlists = []
    playlist = []

    def __init__(self, data=None):
        self._video_library = VideoLibrary()
        self._playlists = data if not data is None else []
        self._playlist = data if not data is None else []

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        """Returns all videos."""
        print('Showing all videos : \n')
        for videos in self._video_library.get_all_videos():
            print(videos)

    def play_video(self, video_id):

        """Plays the respective video.
        Args:
            video_id: The video_id to be played.
        """

        if video_id == "funny_dogs_video_id":
            playing_video = video_id
            if constant.PLAYING:
                print("Stopping Video:", constant.VIDEO_ID)
                print("Playing Video:", playing_video)
            else:
                constant.PLAYING = True
                constant.VIDEO_ID = playing_video
                playing_video = "Playing Video: Funny Dogs"
                print(playing_video)
                return constant.PLAYING, constant.VIDEO_ID

        elif video_id == "amazing_cats_video_id":
            playing_video = video_id
            if constant.PLAYING:
                print("Stopping Video:", constant.VIDEO_ID)
                print("Playing Video:", playing_video)
            else:
                constant.PLAYING = True
                constant.VIDEO_ID = playing_video
                playing_video = "Playing Video: Amazing Cats"
                print(playing_video)
                return constant.PLAYING, constant.VIDEO_ID

        elif video_id == "another_cat_video_id":
            playing_video = video_id
            if constant.PLAYING:
                print("Stopping Video:", constant.VIDEO_ID)
                print("Playing Video:", playing_video)
            else:
                constant.PLAYING = True
                constant.VIDEO_ID = playing_video
                playing_video = "Playing Video: Another Cat Video"
                print(playing_video)
                return constant.PLAYING, constant.VIDEO_ID

        elif video_id == "life_at_google_video_id":
            playing_video = video_id
            if constant.PLAYING:
                print("Stopping Video:", constant.VIDEO_ID)
                print("Playing Video:", playing_video)
            else:
                constant.PLAYING = True
                constant.VIDEO_ID = playing_video
                playing_video = "Playing Video: Life at Google"
                print(playing_video)
                return constant.PLAYING, constant.VIDEO_ID

        elif video_id == "nothing_video_id":
            playing_video = video_id
            if constant.PLAYING:
                print("Stopping Video:", constant.VIDEO_ID)
                print("Playing Video:", playing_video)
            else:
                constant.PLAYING = True
                constant.VIDEO_ID = playing_video
                playing_video = "Playing Video: Video about nothing"
                print(playing_video)
                return constant.PLAYING, constant.VIDEO_ID

        else:
            print("Cannot play video: Video does not exist")

    def stop_video(self):
        """Stops the current video."""

        print("stop_video needs implementation")

    def play_random_video(self):
        """Plays a random video from the video library."""
        id_list = ['funny_dogs_video_id', 'amazing_cats_video_id', 'another_cat_video_id',
                   'life_at_google_video_id', 'nothing_video_id']
        self.play_video(random.choice(id_list))
        print('Playing a random video')

    def pause_video(self):
        """Pauses the current video."""

        print("pause_video needs implementation")

    def continue_video(self):
        """Resumes playing the current video."""

        print("continue_video needs implementation")

    def show_playing(self):
        """Displays video currently playing."""

        print("show_playing needs implementation")

    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.
        Args:
            playlist_name: The playlist name.
        """
        global playlists
        global playlist
        playlist = playlist_name
        self.playlists.append(playlist)
        playlist = []
        print(f"{playlist}" ' playlist was created')

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.
        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        # Debug this I think it's assigning bad values
        if playlist_name in self.playlists:
            self._playlist.append(video_id)
            print(self._playlist)

        else:
            print('Playlist does not exist')

    def show_all_playlists(self):
        """Display all playlists."""
        print(self.playlists)

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.
        Args:
            playlist_name: The playlist name.
        """
        # have to run check against playlist name if it exists and showing deleted items
        print(self._playlist)

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.
        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        # not working properly
        if str(video_id) not in self.playlist:
            print('Video is not in playlist')
            print(self.playlist)
        else:
            ind = self.playlist.index(str(video_id))
            self.playlist.remove(ind)
            print(f"{video_id}" ' was removed from your playlist')
            print(self.playlist)

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.
        Args:
            playlist_name: The playlist name.
        """
        self._playlist[:]
        print(f"{playlist_name}" ' playlist was wiped of data')
        print(self._playlist)

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.
        Args:
            playlist_name: The playlist name.
        """
        print(self.playlists)
        print(self.playlists.index(playlist_name))
        # print(f"{playlist_name}" ' was removed')
        print(self.playlists)
    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.
        Args:
            search_term: The query to be used in search.
        """
        print("search_videos needs implementation")

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.
        Args:
            video_tag: The video tag to be used in search.
        """
        print("search_videos_tag needs implementation")

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.
        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        print("flag_video needs implementation")

    def allow_video(self, video_id):
        """Removes a flag from a video.
        Args:
            video_id: The video_id to be allowed again.
        """
        print("allow_video needs implementation")
