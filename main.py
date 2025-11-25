from kivy.app import App
from kivy.clock import Clock
from kivy.uix.label import Label
from kivy.utils import platform
import requests
import threading
from datetime import datetime

class SimpleBackgroundMonitor(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.monitoring_active = False
        self.last_network = None
        self.BOT_TOKEN = "7961552454:AAHIpIcmYQoT1VG-KR3OUNjzOt2BWa59VS4"
        self.CHAT_ID = "7683896497"

    def build(self):
        self.title = 'Network Monitor'
        return Label(text='Monitoring active\nYou can minimize app')

    def on_start(self):
        self.monitoring_active = True
        current_network = self.get_network_state()
        self.last_network = current_network
        self.send_notification(f"Monitoring started\n{current_network}")
        Clock.schedule_interval(self.check_network, 5)

    def check_network(self, dt):
        if not self.monitoring_active: return
        current_network = self.get_network_state()
        if current_network != self.last_network:
            timestamp = datetime.now().strftime("%H:%M:%S")
            self.send_notification(f"Network changed ({timestamp}):\n{current_network}")
            self.last_network = current_network

    def get_network_state(self):
        try:
            if platform == "android":
                from jnius import autoclass
                Context = autoclass('android.content.Context')
                ConnectivityManager = autoclass('android.net.ConnectivityManager')
                PythonActivity = autoclass('org.kivy.android.PythonActivity')
                activity = PythonActivity.mActivity
                connectivity_manager = activity.getSystemService(Context.CONNECTIVITY_SERVICE)
                network_info = connectivity_manager.getActiveNetworkInfo()
                if network_info and network_info.isConnected():
                    if network_info.getType() == ConnectivityManager.TYPE_WIFI:
                        return "Connected to WI-FI"
                    elif network_info.getType() == ConnectivityManager.TYPE_MOBILE:
                        return "Connected to mobile network"
                    else: return "Connected to network"
                else: return "No connection"
            else: return "Test (not Android)"
        except Exception as e: return f"Error: {str(e)}"

    def send_notification(self, message):
        def send_telegram_message():
            try:
                url = f"https://api.telegram.org/bot{self.BOT_TOKEN}/sendMessage"
                data = {"chat_id": self.CHAT_ID, "text": message}
                requests.post(url, data=data, timeout=10)
            except Exception as e: print(f"Send error: {e}")
        threading.Thread(target=send_telegram_message, daemon=True).start()

    def on_pause(self): return True

if __name__ == '__main__':
    SimpleBackgroundMonitor().run()
