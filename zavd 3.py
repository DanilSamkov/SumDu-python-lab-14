import json
import matplotlib.pyplot as plt

# Завантажуємо дані з JSON файлу
def load_data_from_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data['students']

# Підраховуємо кількість хлопців і дівчат у списку учнів
def count_genders(students):
    boys = sum(1 for student in students if student['стать'] == 'чоловіча')
    girls = sum(1 for student in students if student['стать'] == 'жіноча')
    return boys, girls

# Побудова кругової діаграми для розподілу статей учнів
def plot_gender_distribution(boys, girls):
    labels = ['Хлопці', 'Дівчата']
    sizes = [boys, girls]
    colors = ['#ff9999', '#66b3ff']

    plt.figure(figsize=(7, 7))
    plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
    plt.axis('equal')
    plt.title('Розподіл статей учнів у класі')
    plt.show()


def main():
    file_path = 'students.json'

    students = load_data_from_json(file_path)

    boys, girls = count_genders(students)

    plot_gender_distribution(boys, girls)


if __name__ == "__main__":
    main()
