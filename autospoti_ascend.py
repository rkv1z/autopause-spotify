import asyncio
from winrt.windows.media.control import GlobalSystemMediaTransportControlsSessionManager
from winrt.windows.media.control import GlobalSystemMediaTransportControlsSessionPlaybackStatus
import time

vid_now = 1

async def check_sessions(vid_now):
    spoti = None
    other_play = False
    sessions = await GlobalSystemMediaTransportControlsSessionManager.request_async()
    sessions1 = sessions.get_sessions()
    for j in sessions1:
        ses_name = j.source_app_user_model_id
        ses_stat = j.get_playback_info().playback_status

        if "Spotify.exe" in ses_name:
            spoti = j
            spoti_now = ses_stat
        elif ses_stat == GlobalSystemMediaTransportControlsSessionPlaybackStatus.PLAYING:
            other_play = True

    if spoti:

        if other_play and vid_now == 1 and spoti_now == GlobalSystemMediaTransportControlsSessionPlaybackStatus.PLAYING:
            await spoti.try_pause_async()
            vid_now = 0

        elif not other_play and vid_now == 0 and spoti_now == GlobalSystemMediaTransportControlsSessionPlaybackStatus.PAUSED:
            await spoti.try_play_async()
            vid_now = 1

        return vid_now
    else:        
        return vid_now

while True:
    vid_now = asyncio.run(check_sessions(vid_now))
    time.sleep(2)  