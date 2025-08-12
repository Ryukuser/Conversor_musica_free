# Conversor_musica_free
Crie um conversor de musica ou vide se quiserem chamar assim. Ele pega links do youtube como input e baixa numa versão mp3 para sua maquina. Intuito do codigo foi criado para evitar usarem sites web para essa função.


Antes de rodar o programa precisa conferir se há instalação para funcionar:
Python 3.13 
ffmpeg
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
