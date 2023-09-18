class Netflix:
    def __init__(self):
        # Kullanıcıları ve profilleri saklamak için boş sözlükler oluşturuyoruz.
        self.users = {}
    
    def create_user(self, username, password):
        # Yeni bir kullanıcı oluşturur ve sözlüğe ekler.
        if username not in self.users:
            self.users[username] = {'password': password, 'profiles': {}}
            print(f'{username} kullanıcısı oluşturuldu.')
        else:
            print(f'{username} zaten mevcut.')

    def login(self, username, password):
        # Kullanıcı adı ve şifreyi kontrol ederek giriş yapar.
        if username in self.users and self.users[username]['password'] == password:
            print(f'{username} giriş yaptı.')
        else:
            print('Geçersiz kullanıcı adı veya şifre.')

    def create_profile(self, username, profile_name):
        # Kullanıcının yeni bir profil oluşturmasına izin verir.
        if username in self.users:
            profiles = self.users[username]['profiles']
            if profile_name not in profiles:
                profiles[profile_name] = {'watchlist': []}
                print(f'{profile_name} profil oluşturuldu.')
            else:
                print(f'{profile_name} zaten mevcut.')

    def search_content(self, keyword):
        # Belirli bir anahtar kelimeye göre içerik arar.
        # Bu örnekte içeriklerin bir listesi varsayılmıştır.
        content_list = ['The Irishman', 'Stranger Things', 'Bird Box', 'The Witcher', 'Extraction']
        matching_content = [content for content in content_list if keyword.lower() in content.lower()]
        return matching_content

    def add_to_watchlist(self, username, profile_name, content):
        # İzleme listesine içerik ekler.
        if username in self.users and profile_name in self.users[username]['profiles']:
            watchlist = self.users[username]['profiles'][profile_name]['watchlist']
            watchlist.append(content)
            print(f'{content} izleme listesine eklendi.')
        else:
            print('Kullanıcı veya profil bulunamadı.')

# Netflix sınıfını kullanarak örnek işlemler:
netflix = Netflix()
netflix.create_user('Firengiz', '123456')
netflix.login('Firengiz', '123456')
netflix.create_profile('Firengiz', 'Firengiz Profili')
netflix.add_to_watchlist('Firengiz', 'Firengiz Profili', 'The Irishman')
search_results = netflix.search_content('The Irishman')
print('Arama Sonuçları:', search_results)
