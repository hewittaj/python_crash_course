# #8-6
# def city_country(city, country):
#     print(f"{city.title()}, {country.title()}")

# city_country('des moines', 'usa')
# city_country('paris', 'france')

#8-7
def make_album(artist, album, songs = None):
    if songs:
        album_info = {
            'artist name': artist, 
            'album name': album,
            'songs': songs
            }
    else:
        album_info = {
            'artist name': artist, 
            'album name': album,
            }
    print(album_info)

make_album('led zeppelin', 'album 1', songs = 20)
#8-8