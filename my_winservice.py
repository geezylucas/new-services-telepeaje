import time
from base_class_winservice import SMWinservice
from transfer import app


class NewServiceTelepeaje(SMWinservice):
    _svc_name_ = "NewServiceTelepeaje"
    _svc_display_name_ = "Python Geezy's Winservice Example"
    _svc_description_ = "That's a great winservice! :)"

    def start(self):
        self.isrunning = True

    def stop(self):
        self.isrunning = False

    def main(self):
        while self.isrunning:
            app.run()
            time.sleep(120)


if __name__ == '__main__':
    NewServiceTelepeaje.parse_command_line()
