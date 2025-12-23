import json

with open('1.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

users = data['users']

print("Содержимое файла 1.json:")
print("=" * 60)
for user in users:
    for key, value in user.items():
        print(f"{key} → {value}")
    print("-" * 60)

def find_users_by_surname_prefix(users, prefix):
    prefix = prefix.lower()
    found = [user for user in users if user['surname'].lower().startswith(prefix)]
    
    print(f"\nПоиск пользователей с фамилией на '{prefix.upper()}':")
    if found:
        for user in found:
            print(f"  {user['name']} {user['surname']} (ID: {user['id']})")
    else:
        print("  Не найдено")
    return found

def calculate_average_age(users):
    avg_age = sum(user['age'] for user in users) / len(users)
    print(f"\nСредний возраст пользователей: {avg_age:.1f} лет")
    return avg_age

def count_users_by_language(users):
    languages = {}
    for user in users:
        lang = user['language']
        languages[lang] = languages.get(lang, 0) + 1
    
    print("\nКоличество пользователей по языкам:")
    for lang, count in languages.items():
        print(f"  {lang}: {count}")
    return languages

def save_filtered_data(filtered_users, filename='out.json'):
    output_data = {'filtered_users': filtered_users}
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(output_data, f, indent=2, ensure_ascii=False)
    print(f"\nОтфильтрованные данные сохранены в {filename}")

print("\n" + "=" * 60)
print("АНАЛИЗ ДАННЫХ")
print("=" * 60)

filtered = find_users_by_surname_prefix(users, 'Smi')

calculate_average_age(users)
count_users_by_language(users)

save_filtered_data(filtered)
