Antes de rodar o programa precisa conferir se há instalação para funcionar:
Python 3.13 - 
ffmpeg -
pip install yt_dlp


No Windows:

Acesse https://www.gyan.dev/ffmpeg/builds/.
Baixe o arquivo ffmpeg-release-full.7z (ou a versão mais recente disponível).
Extraia o arquivo com um programa como 7-Zip ou WinRAR.
Dentro da pasta extraída, procure por uma subpasta chamada bin. Essa pasta contém ffmpeg.exe, ffprobe.exe, etc.
Use o caminho dessa pasta bin (ex.: C:\caminho\para\ffmpeg\bin) no comando do seu programa. Por exemplo:
bashyt-dlp --ffmpeg-location C:\caminho\para\ffmpeg\bin\ffmpeg.exe <URL_DO_VÍDEO>

Opcional: Adicione o caminho da pasta bin às variáveis de ambiente (como explicado antes) para usar o ffmpeg sem especificar o caminho toda vez.

Verifique a instalação:

Abra um novo terminal e digite ffmpeg -version para confirmar.


Voces podem fazer algumas alteraçoes:

'preferredcodec': 'mp3',      # Converte para MP3, pode ser alterado para mp4 e baixar em formato de video.
'preferredquality': '320',    # Qualidade do MP3 (192 kbps é padrao mas usei 320 para melhor qualidade).
'noplaylist': False,  # Não baixa playlists, apenas vídeos individuais -> ao mudar o valor para True, ele consegue fazer downloads de playlist.

abaixo vou deixar o treço completo do codigo.

# Configurações para o yt-dlp
        ydl_opts = {
            'format': 'bestaudio/best',  # Seleciona o melhor formato de áudio
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',  # Usa FFmpeg para extrair áudio
                'preferredcodec': 'mp3',      # Converte para MP3
                'preferredquality': '320',    # Qualidade do MP3 (192 kbps)
            }],
            'outtmpl': f'{output_path}/%(title)s.%(ext)s',  # Template do nome do arquivo
            'noplaylist': False,  # Não baixa playlists, apenas vídeos individuais 
        }

