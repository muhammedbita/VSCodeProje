from time import sleep
from win10toast import ToastNotifier

def sayac(Mesaj,Saniye):
    if Mesaj == "":
        Mesaj="Kalan Saniye"
    for i in range(Saniye):
        print(f"{Mesaj}: {Saniye-i}")
        sleep(1)

def bildirim(Mesaj,Saniye):
    bildiri = ToastNotifier()
    bildiri.show_toast(title="BİTA",msg=f"{Mesaj}",icon_path=None,duration=Saniye)