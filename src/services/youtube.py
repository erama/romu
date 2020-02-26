import requests
import time
import random, string

from random import randint
from bs4 import BeautifulSoup as beautiful_soup

from .credentials import Credentials
from .env import Env

class Youtube:
    VIDEO_ID = Env.video_id()
    CHANNEL_ID = Env.channel_id()
    TEXT_FILE = Env.text_file()

    NO_CACHE_HEADER = { 
        "Cache-Control": "no-cache",
        "Expires": "Thu, 01 Jan 1970 00:00:00 GMT",
        "Pragma": "no-cache"
    }

    def comment_video(self, youtube, video_id, message="", channel_id=CHANNEL_ID):
        youtube.commentThreads().insert(
        
            part="snippet",
            body=dict(
                snippet=dict(
                    channelId=channel_id,
                    videoId=video_id,
                    topLevelComment=dict(
                        snippet=dict(
                            textOriginal=message
                        )
                    )
                )
            )
        ).execute()

    def run(self):
        try:
            credentials = Credentials.build()

            with open(self.TEXT_FILE) as erama:
                for eramaline in erama:
                    comment = eramaline +" Gracias ! " + "Romu -> "+str(randint(2,303))
                    self.comment_video(credentials, self.VIDEO_ID, comment  )
                    #self.like_video(credentials, latest_video_id)
                    print("Comentario publicado: " + comment)
                    #self.run()
                    time.sleep(randint(2,33))

            self.run()
        except KeyboardInterrupt:
            print("Finalizado por el usuario")
        except Exception as e:
            print("Algo salió mal! ;) {e}".format(e=e))
            self.run()
        