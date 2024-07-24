import os
import webbrowser

dir_path = os.path.dirname(os.path.realpath(__file__))
html = os.path.join(dir_path, "player.html")

def open_html_file(file_path):
    # Verifica se o arquivo HTML existe no caminho especificado
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"O arquivo HTML não foi encontrado no caminho especificado: {file_path}")
    
    # Converte o caminho do arquivo para uma URL de arquivo
    file_url = f'file:///{os.path.abspath(file_path)}'
    
    # Abre o arquivo HTML no navegador padrão
    webbrowser.open(file_url)

print('PLAYER TORRENT By Joel')
print('\n')
magnet = input('COLE O MAGNET LINK: ')
if 'magnet' in magnet:
    with open(html, 'w', encoding='utf-8') as f:
        page = '''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Webtor.io Player</title>
            <style>
                html, body {{
                    margin: 0;
                    padding: 0;
                    width: 100%;
                    height: 100%;
                    overflow: hidden;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    background-color: #000; /* Plano de fundo da página preto */
                }}
                #player {{
                    width: 80%; /* Ajuste a largura conforme necessário */
                    height: 80%; /* Ajuste a altura conforme necessário */
                    max-width: 800px; /* Limita a largura máxima do player */
                    max-height: 600px; /* Limita a altura máxima do player */
                    background-color: #000; /* Plano de fundo do player preto */
                }}
            </style>
        </head>
        <body>
            <!-- Container for the Webtor player -->
            <div id="player"></div>

            <!-- Include the Webtor.io script -->
            <script src="https://cdn.jsdelivr.net/npm/@webtor/embed-sdk-js/dist/index.min.js"></script>
            <script>
                // Initialize the Webtor player
                window.webtor = window.webtor || [];
                window.webtor.push({{
                    id: 'player',
                    magnet: '{}', // Replace with your torrent magnet link
                    on: function(e) {{
                        if (e.name == window.webtor.TORRENT_FETCHED) {{
                            console.log('Torrent fetched!', e.data);
                        }}
                        if (e.name == window.webtor.TORRENT_ERROR) {{
                            console.log('Torrent error!');
                        }}
                    }},
                    poster: 'https://wallpapers.com/images/hd/overlapping-fine-neon-green-matrix-dvfxd08moa4d5hy8.jpg', // Optional poster image
                    title: 'Torrent Player' // Optional title
                }});
            </script>
        </body>
        </html>
        '''.format(magnet)
        f.write(page)
        open_html_file(html)
