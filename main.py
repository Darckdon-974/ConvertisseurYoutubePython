from pytube import YouTube
import shutil

user_link_input = input("Mettez votre  lien YouTube : ")

def download(link):
    yt = YouTube(link)
    print (user_link_input)
    print ("Nombre de vues : ", yt.views )
    print ("Durée : ", yt.length, " Secondes")
    print("Téléchargement ...")
    yt.streams.get_highest_resolution().download()
    shutil.move('./*.mp4', './youtube')
    print("Téléchargement terminé ! :)")
    return yt

def main():
    download(user_link_input)

main()