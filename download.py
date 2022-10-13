# ba_meta require api 7
import ba, os, _ba
# its updated
version = 1.2

def install(url: str, destination: str) -> None:
    import urllib.request
    data = urllib.request.urlopen(url)
    print("True")
    open(destination, 'w').write(str(data.read().decode()))
    print('True Again')

# ba_meta export plugin
class Plugin(ba.Plugin):
    url = 'https://raw.githubusercontent.com/imayushsaini/Bombsquad-Ballistica-Modded-Server/public-server/dist/ba_root/mods/games/running_bombs.py'
    install(url, _ba.env()["python_directory_user"] + os.sep+'running_bombs.py')
