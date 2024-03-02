from pytube import YouTube

# Função para baixar vídeo
def baixar_video(url):
    try:
        yt = YouTube(url)
        video = yt.streams.filter(progressive=True, file_extension='mp4').first()
        video.download()
        print("Download completo!")
    except Exception as e:
        print("Ocorreu um erro durante o download:", str(e))

# URL do vídeo
url_video = "https://youtube.com/whatch?v=GtP-P44VMyk"

# Chamada da função para baixar o vídeo
baixar_video(url_video)

