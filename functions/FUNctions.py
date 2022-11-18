


def describe_city(city, country='USA'):
    print("{} is located in {}".format(city.title(), format(country.title())))


describe_city('charlotte')
describe_city('boston')
describe_city('london', 'UK')


def make_album(artist_name, album_title, number_of_songs=None):
    album = {'artist name': artist_name, 'album_title': album_title}

    if number_of_songs:
        album['number of songs'] = number_of_songs
    return album


musician1 = make_album('Kanye west', 'Ye')
print(musician1)
musician2 = make_album('Tyson', 'Knock Out')
print(musician2)
musician3 = make_album('Obama', 'Care')
print(musician3)
musician = make_album('Kanye west', 'Ye', number_of_songs=13)
print(musician)