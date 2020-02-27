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
            how = ['🅶🅾🅽🆉🅰🅻🅾🆁🅰🅼🅰.🅲🅾🅼',"G̵̡̤̙̖̗̗̜̝̦̼͐̀o̶̤̖͍͗̾ń̶̰̯̯̥̥̟̎̈́̕z̶̥̱̬̘̭͖̉a̷̬̰͉͉͋̒̔́̈́̓͜l̸̪͌̽͆̿̽͐͒̑̄ö̵̢̨̢̢͚̰̻́͑̈̂̿̎͝͠R̴̳̩͛̌̅́̎̍å̶̡̨̛͚̌̋͘ͅm̶͍̹̓͋ͅā̶̙͖͉̬̹̀.̶̜̜̮̳̹͍́̅̀̄͐͗̔͌͝ͅc̸͕̝̟̠̟̑̈́̚̕͠ö̸̺̙̯̬̝́̇͒̆̾͆̾̒͜m̶̨̛̖̳͎͈͙̖͍̺̀̉̅̾̂̓͜͝͝'","🄻4🄱🅂.🄲🄾🄼",
            "𝕲𝖔𝖓𝖟𝖆𝖑𝖔𝕽𝖆𝖒𝖆.𝖈𝖔𝖒","𝙂𝙤𝙣𝙯𝙖𝙡𝙤𝙍𝙖𝙢𝙖.𝙘𝙤𝙢","Gₒₙzₐₗₒᵣₐₘₐ.cₒₘ","🅻4🅱🆂.🅲🅾🅼",
            "𝕃𝟜𝔹𝕊.𝕔𝕠𝕞","ɢᴏɴᴢᴀʟᴏʀᴀᴍᴀ.ᴄᴏᴍ","𝔾𝕠𝕟𝕫𝕒𝕝𝕠ℝ𝕒𝕞𝕒.𝕔𝕠𝕞","Ꮆㄖ几乙卂ㄥㄖ尺卂爪卂．匚ㄖ爪","𝓛4𝓑𝓢.𝓬𝓸𝓶"]
            with open(self.TEXT_FILE) as erama:
                for eramaline in erama:
                    comment = how[randint(0,11)] + "  "+ eramaline + str(randint(0,3000))
                    self.comment_video(credentials, self.VIDEO_ID, comment  )
                    #self.like_video(credentials, latest_video_id)
                    print("Comentario publicado: " + comment)
                    #self.run()
                    time.sleep(randint(33,333))

            self.run()
        except KeyboardInterrupt:
            print("Finalizado por el usuario")
        except Exception as e:
            print("Algo salió mal! ;) {e}".format(e=e))
            self.run()
        