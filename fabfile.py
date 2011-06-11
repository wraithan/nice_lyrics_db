from fabric.api import local

def deploy():
    local('scp -P 7565 nice_lyrics_db/deploy_settings.py dotcloud@www.nicelyricsdb.dotcloud.com:~')
    local('dotcloud push nicelyricsdb.www .')
