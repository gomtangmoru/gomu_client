from shit.shell import shell
import webbrowser

class wireguard:
    def __init__(self):
        self.wireguard_installer_for_windows = "https://download.wireguard.com/windows-client/wireguard-installer.exe"

    def is_wiregurad(self):
        result = shell.run("wg")
        if result is None:
            return False
        return True

    def wireguard_installer(self):
        webbrowser.open(self.wireguard_installer_for_windows)


wireguard = wireguard()