from igramscraper.instagram import Instagram # pylint: disable=no-name-in-module
import numpy as np
import pandas as pd
import os
import requests

# If account is public you can query Instagram without auth

instagram = Instagram()

nombre_usuario = "aceiteoleo"
numero_fotos = 10


this_file_path = os.path.abspath(__file__)
BASE_DIR = os.path.dirname(this_file_path)
images_dir = os.path.join(BASE_DIR, "Fotos_{nombre_usuario}")
os.makedirs(images_dir, exist_ok=True)


medias = instagram.get_medias(nombre_usuario, numero_fotos)
print(len(medias))

for media in medias:
    string = str(media)
    nombre = string.split()[5]
    print(nombre)
    url = string.split()[-4]
    downloaded_image_path = os.path.join(images_dir, f"{nombre}.jpg")
    r = requests.get(url)
    with open(downloaded_image_path, "wb") as f:
        f.write(r.content)

print("fin")


# labels = np.arange(1,11)
# df = pd.DataFrame(download_links, labels)


#print(df)


# df = pd.DataFrame(medias, )
# df[4]

#df.to_excel('AceiteOleo.xlsx', sheet_name= "NewSheet", index = False)

#print(df)

# print(media)
# account = media.owner
# print(account)
# print('Usernam', account.username)
# print('Full Name', account.full_name)
# print('Profile Pic Url', account.get_profile_picture_url_hd())


# If account private you should be subscribed and after auth it will be available

# username = ''
# password = ''
# session_folder = ''
# instagram = Instagram()
# instagram.with_credentials(username, password, session_folder)
# instagram = Instagram()
# instagram.login()
# instagram.get_medias('private_account', 100)
