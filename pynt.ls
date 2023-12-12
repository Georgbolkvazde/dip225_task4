# ... (jūsu esošais kods)

# Pārbaudīsim un izlabosim jūsu kodu, kas lasa un apstrādā informāciju par algu
with open('salary.xlsx', 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    next(reader)  # Пропустить заголовок
    for row in reader:
        encoded_name = row[0]
        salary = row[1]
        if encoded_name in encoded_names:
            decoded_name = people[encoded_names.index(encoded_name)]
            if decoded_name == 'Jo Rivers':
                print(f'Jo Rivers kopējā alga: {salary} eur')
