import time

class Scheduler:
    def init(self, interval_minutes=15):
        self.interval = interval_minutes * 60  # seconds

    def wait(self, override_delay=None):
        """
        Pauses execution for the defined time interval.
        """
        delay = override_delay if override_delay else self.interval
        print(f"\n⏳ Waiting {delay/60:.1f} minutes before next check...\n")
        time.sleep(delay)
