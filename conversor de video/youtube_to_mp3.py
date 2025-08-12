import yt_dlp
import os

def download_youtube_to_mp3(url, output_path="downloads"):
    try:
        # Cria o diretório de saída se não existir
        if not os.path.exists(output_path):
            os.makedirs(output_path)

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

        # Baixa e converte o vídeo para MP3
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print(f"Download concluído! Arquivo salvo em: {output_path}")

    except Exception as e:
        print(f"Ocorreu um erro: {str(e)}")

if __name__ == "__main__":
    # Solicita o link do YouTube
    youtube_url = input("Digite o link do vídeo do YouTube: ")
    download_youtube_to_mp3(youtube_url)