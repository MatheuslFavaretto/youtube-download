## youtube-download


# Descrição
Um script com funcionalidade de demosntara a utilização da biblioteca Pytube.

- download de videos youtbue de maneira facil e simplificada



#### para realizar o download :

```python
from pytube import YouTube

def Download(link):
    ytObjeto = YouTube(link)
    ytObjeto = ytObjeto.streams.get_highest_resolution()

    try:
        ytObjeto.download()
    except:
        print("Ocorreu um erro!")
    print("Download completado com sucesso!!")


link = input("Coloque o URL do video Youtube: ")
Download(link)

```


## imagens de demonstração:

![image](https://user-images.githubusercontent.com/116848225/210183467-fe8f96b6-075e-472b-b32b-200f3e11f88d.png)
![image](https://user-images.githubusercontent.com/116848225/210183478-7e938eb0-1bef-4f7c-80e7-007be6a42411.png)

