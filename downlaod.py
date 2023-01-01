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
