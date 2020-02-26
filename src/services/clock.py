import requests
import time
import traceback

from .env import Env

from datetime import datetime as date_time

class Clock:
    CLOCK_URL = Env.clock_api_url()
    TICK_TIME = Env.clock_waiting_time()

    def __init__(self, service):
        self.service = service

    def wait_and_log(self):
        time.sleep(self.TICK_TIME)

        print("Comenzamos")

    def cron(self):
        try:
            self.wait_and_log()
            self.service().run()

            #is_ready_for_release = self.current_api_time() >= self.RELEASE_DATE

            #self.service().run() if is_ready_for_release else self.cron()
        except Exception as error:
            print(
                "Something went wrong - Clock Cron: {error} - Traceback: {trace}".format(
                    error=error,
                    trace=traceback.format_exc()
                )
            )

