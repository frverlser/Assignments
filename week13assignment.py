import requests

def get_data(artist, title):
    url = f"https://api.lyrics.ovh/v1/{artist}/{title}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            print("\nLyrics not found or API error.")
    except:
        print("\nSomething went wrong. Please check your internet or input.")
    return None

def process_data(data):
    if data and 'lyrics' in data:
        return data['lyrics']
    return None

def display_data():
    while True:
        artist = input("Enter artist name: ").strip()
        title = input("\nEnter song title: ").strip()
        if not artist:
            print("\nArtist name cannot be empty. Please try again.")
            continue
        if not title:
            print("\nSong title cannot be empty. Please try again.")
            continue
        break

    data = get_data(artist, title)
    lyrics = process_data(data)

    if data and 'lyrics' in data:
        lyrics = data['lyrics']
        print("\n--- Lyrics Found! ---\n")
        print(lyrics)

        with open("your_lyrics.txt", "a") as f:
            f.write(f"\n{artist} - {title}\n=======================\n{lyrics}\n\n\n")

display_data()