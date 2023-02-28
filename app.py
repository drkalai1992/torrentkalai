from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    from torrentp import TorrentDownloader
    for i in range(1):
        torrent_file = TorrentDownloader(input(), '.')
        torrent_file.start_download()
hello()
