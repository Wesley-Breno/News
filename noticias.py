import requests
import re
from bs4 import BeautifulSoup


def noticia(site):
    lista = []

    if site == 0:
        url = r'https://g1.globo.com/tecnologia/'
        dados = requests.get(url)
        html = BeautifulSoup(dados.text, 'html.parser')

        titulos = html.select('.feed-post-link.gui-color-primary.gui-color-hover')
        descricao = html.select('.feed-post-body-resumo')
        data = html.select('.feed-post-datetime')
        videos_image = html.select('.bstn-fd-picture-image')
        fotos = html.select('.bstn-fd-picture-image')

        links = []
        videos = []
        fotos_links = []

        for titulo in titulos:
            a = str(titulo)
            links.append(re.findall(r'https://g1.globo.com/[a-z\d]*_*-*\.*/[a-z\d]*_*-*\.*/[a-z\d]*_*-*\.*/[a-z\d]*_*-*\.*/*[a-z\d]*_*-*\.*/*[a-z\d]*_*-*\.*/*[a-z\d]*_*-*\.*\#*\,*[a-z\d]*_*-*\.*\#*\,*[a-z\d]*_*-*\.*\#*\,*[a-z\d]*_*-*\.*\#*\,*[a-z\d]*_*-*\.*\#*\,*[a-z\d]*_*-*\.*\#*\,*[a-z\d]*_*-*\.*\#*\,*[a-z\d]*_*-*\.*\#*\,*[a-z\d]*_*-*\.*\#*\,*[a-z\d]*_*-*\.*\#*\,*[a-z\d]*_*-*\.*\#*\,*[a-z\d]*_*-*\.*\#*\,*[a-z\d]*_*-*\.*\#*\,*[a-z\d]*_*-*\.*\#*\,*[a-z\d]*_*-*\.*\#*\,*[a-z\d]*_*-*\.*\#*\,*[a-z\d]*_*-*\.*\#*\,*[a-z\d]*_*-*\.*\#*\,*[a-z\d]*_*-*\.*\#*\,*[a-z\d]*_*-*\.*\#*\,*[a-z\d]*_*-*\.*\#*\,*[a-z\d]*_*-*\.*\#*\,*[a-z\d]*_*-*\.*\#*\,*[a-z\d]*_*-*\.*\#*\,*[a-z\d]*_*-*\.*\#*\,*[a-z\d]*_*-*\.*\#*\,*[a-z\d]*_*-*\.*\#*\,*[a-z\d]*_*-*\.*\#*\,*[a-z\d]*_*-*\.*\#*\,*[a-z\d]*_*-*\.*\#*\,*[a-z\d]*_*-*\.*\#*\,*[a-z\d]*_*-*\.*\#*\,*[a-z\d]*_*-*\.*\#*\,*[a-z\d]*_*-*\.*\#*\,*[a-z\d]*_*-*\.*\#*\,*[a-z\d]*_*-*\.*\#*\,*[a-z\d]*_*-*\.*\#*\,*[a-z\d]*_*-*\.*\#*\,*[a-z\d]*_*-*\.*\#*\,*[a-z\d]*_*-*\.*\#*\,*[a-z\d]*_*-*\.*\#*\,*[a-z\d]*_*-*\.*\#*\,*[a-z\d]*_*-*\.*\#*\,*[a-z\d]*_*-*\.*\#*\,*[a-z\d]*_*-*\.*\#*\,*[a-z\d]*_*-*\.*\#*\,*[a-z\d]*_*-*\.*\#*\,*', a, re.I))

        for video in videos_image:
            a = str(video)
            videos.append(re.findall(
                r'https://s2.glbimg.com/-*[a-z\d]*_*-*[a-z\d]*_*-*[a-z\d]*_*-*[a-z\d]*_*-*[a-z\d]*_*-*[a-z\d]*_*=/[\d]{3}x[\d]{3}/top/smart/filters:max_age\(3600\)/https://s01.video.glbimg.com/deo/vi/\d*/\d*/\d*',
                a, re.I))

        for foto in fotos:
            a = str(foto)
            fotos_links.append(re.findall(
                r'https://s2.glbimg.com/-*[a-z\d]*_*-*[a-z\d]*_*-*[a-z\d]*_*-*[a-z\d]*_*-*[a-z\d]*_*-*[a-z\d]*_*=/[\d]{3}x[\d]{3}/top/smart/https://i.s3.glbimg.com/v1/-*[a-z\d]*_*-*[a-z\d]*_*-*[a-z\d]*_*-*[a-z\d]*_*-*[a-z\d]*_*-*[a-z\d]*_*/-*[a-z\d]*_*-*[a-z\d]*_*/-*[a-z\d]*_*/-*[a-z\d]*_*/-*[a-z\d]*_*/-*[a-z\d]*_*/-*[a-z\d]*_*-*[a-z\d]*_*/-*[a-z\d]*_*-*[a-z\d]*_*-*[a-z\d]*_*-*[a-z\d]*_*-*[a-z\d]*_*-*[a-z\d]*_*-*[a-z\d]*_*-*[a-z\d]*_*-*[a-z\d]*_*-*[a-z\d]*_*-*[a-z\d]*_*-*[a-z\d]*_*-*[a-z\d]*_*-*[a-z\d]*_*\.\w+',
                a, re.I))

        cont = 0
        noticias = dict()

        while cont != 8:
            try:
                noticias[cont] = {"titulo": titulos[cont].text, "descricao": descricao[cont].text,
                                  "data": data[cont].text,
                                  'link': links[cont][0], 'fonte': url, 'video': videos[cont][0]}
                cont += 1
            except:
                try:
                    noticias[cont] = {"titulo": titulos[cont].text, "descricao": descricao[cont].text,
                                      "data": data[cont].text,
                                      'link': links[cont][0], 'fonte': url, 'video': fotos_links[cont][0]}
                    cont += 1
                except:
                    try:
                        noticias[cont] = {"titulo": titulos[cont].text, "descricao": descricao[cont].text,
                                          "data": data[cont].text,
                                          'link': links[cont][0], 'fonte': url, 'video': 'https://www.observatoriodaimprensa.com.br/wp-content/uploads/2019/10/8-6-540x304.jpg'}
                        cont += 1
                    except:
                        noticias[cont] = {"titulo": titulos[cont].text, "descricao": descricao[cont].text,
                                          "data": data[cont].text,
                                          'link': 'https://g1.globo.com/tecnologia/', 'fonte': url,
                                          'video': 'https://www.observatoriodaimprensa.com.br/wp-content/uploads/2019/10/8-6-540x304.jpg'}
                        cont += 1

        for noticia in noticias.values():
            lista.append(noticia)

    elif site == 1:
        url = r'https://olhardigital.com.br/editorias/noticias/'
        dados = requests.get(url)
        html = BeautifulSoup(dados.text, 'html.parser')

        titulos = html.select('.post-title')
        descricao = html.select('.post-excerpt')
        images = html.select('.attachment-popular.size-popular.wp-post-image')
        enderecos = html.select('.card-post.type8.img-effect1')

        links = []
        imagens = []

        for link in enderecos:
            links.append(re.findall('href=\"(https://olhardigital.com.br/\d*/\d*/\d*/-*[a-z\d]*_*-*[a-z\d]*_*-*[a-z\d]*_*-*[a-z\d]*_*-*[a-z\d]*_*/-*[a-z\d]*_*-*[a-z\d]*_*-*[a-z\d]*_*-*[a-z\d]*_*-*[a-z\d]*_*-*[a-z\d]*_*-*[a-z\d]*_*-*[a-z\d]*_*-*[a-z\d]*_*-*[a-z\d]*_*-*[a-z\d]*_*-*[a-z\d]*_*-*[a-z\d]*_*-*[a-z\d]*_*-*[a-z\d]*_*-*[a-z\d]*_*-*[a-z\d]*_*-*[a-z\d]*_*-*[a-z\d]*_*-*[a-z\d]*_*/)\"', str(link), re.I))

        for image in images:
            imagens.append(re.findall(r'src=\"(https://img.olhardigital.com.br/wp-content/uploads/\d*/\d*/-*\.*[a-z\d]*_*-*\.*[a-z\d]*_*-*\.*[a-z\d]*_*-*\.*[a-z\d]*_*-*\.*[a-z\d]*_*-*\.*[a-z\d]*_*-*\.*[a-z\d]*_*-*\.*[a-z\d]*_*-*\.*[a-z\d]*_*-*\.*[a-z\d]*_*-*\.*[a-z\d]*_*-*\.*[a-z\d]*_*-*\.*[a-z\d]*_*-*\.*\w*)\"', str(image), re.I))

        cont = 0
        noticias = dict()

        while cont != 8:
            try:
                noticias[cont] = {"titulo": titulos[cont].text, "descricao": descricao[cont].text,
                                          "data": 'Recentemente',
                                          'link': links[cont][0], 'fonte': url, 'video': imagens[cont][0]}
                cont += 1
            except:
                noticias[cont] = {"titulo": titulos[cont].text, "descricao": descricao[cont].text,
                                  "data": 'Recentemente',
                                  'link': links[cont][0], 'fonte': url, 'video': 'https://www.observatoriodaimprensa.com.br/wp-content/uploads/2019/10/8-6-540x304.jpg'}
                cont += 1

        for noticia in noticias.values():
            lista.append(noticia)

    return lista


if __name__ == "__main__":
    noticia(0)
