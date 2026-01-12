class MusicAlbum:
    def __init__(self, title="", release_year=0, duration=0, is_digital=True):
        self.title = title
        self.release_year = release_year
        self.duration = duration
        self.is_digital = is_digital

    def __repr__(self):
        format_type = "Цифровой релиз" if self.is_digital else "Физический носитель"
        return f"Альбом: '{self.title}', Год: {self.release_year}, Длительность: {self.duration} мин., Формат: {format_type}"

    def export_data(self):
        return {
            'title': self.title,
            'release_year': self.release_year,
            'duration': self.duration,
            'is_digital': self.is_digital
        }


def generate_albums_collection():
    return [
        MusicAlbum("The Dark Side of the Moon", 1973, 42, True),
        MusicAlbum("Thriller", 1982, 42, False),
        MusicAlbum("Back in Black", 1980, 41, True),
        MusicAlbum("Rumours", 1977, 39, True),
        MusicAlbum("The Wall", 1979, 81, False),
        MusicAlbum("Led Zeppelin IV", 1971, 42, True),
        MusicAlbum("Abbey Road", 1969, 47, True),
        MusicAlbum("Nevermind", 1991, 49, False),
        MusicAlbum("Hotel California", 1976, 43, True),
        MusicAlbum("Born to Run", 1975, 39, True),
        MusicAlbum("Purple Rain", 1984, 43, False),
        MusicAlbum("Appetite for Destruction", 1987, 53, True),
        MusicAlbum("OK Computer", 1997, 53, True),
        MusicAlbum("The Joshua Tree", 1987, 50, True),
        MusicAlbum("A Night at the Opera", 1975, 43, False)
    ]


def display_collection(header, items):
    print(header)
    print("=" * 70)
    for item in items:
        print(item)


def sort_collection(items, key_function, sort_description):
    sorted_items = sorted(items, key=key_function)
    display_collection(f"\nСортировка по {sort_description}\n", sorted_items)
    return sorted_items


def save_to_file(filename, items):
    with open(filename, 'w', encoding='utf-8') as file:
        for item in items:
            digital_flag = 1 if item.is_digital else 0
            file.write(f"{item.title};{item.release_year};{item.duration};{digital_flag}\n")
    print(f"\nКоллекция сохранена в файл: {filename}")


def main():
    albums = generate_albums_collection()

    display_collection("\nИсходная коллекция музыкальных альбомов\n", albums)

    sort_collection(albums, lambda a: a.title, "названию альбома")
    sort_collection(albums, lambda a: a.release_year, "году выпуска")
    sort_collection(albums, lambda a: a.duration, "длительности")
    sort_collection(albums, lambda a: a.is_digital, "формату выпуска")

    print("\n>>> Экспорт данных <<<")
    save_to_file("music_albums.txt", albums)

    print("\n>>> Проверка экспортированных данных <<<")
    try:
        with open("music_albums.txt", 'r', encoding='utf-8') as file:
            content = file.read()
            if content:
                print("\nСодержимое файла music_albums.txt:")
                print("-" * 40)
                print(content)
            else:
                print("Файл пуст!")
    except FileNotFoundError:
        print("Ошибка: файл не найден!")


if __name__ == "__main__":
    main()