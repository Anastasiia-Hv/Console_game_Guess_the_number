import random

def guess_the_number():
    min_number = 1
    max_number = 100
    max_attempts = 8
    
    # Генерація випадкового числа
    secret_number = random.randint(min_number, max_number)
    attempts = 0
    
    print(f"Вгадайте число від {min_number} до {max_number}. У вас {max_attempts} спроб!")
    
    # Основний цикл гри
    while attempts < max_attempts:
        try:
            guess = int(input(f"Спроба {attempts + 1}. Ваше число: "))
        except ValueError:
            print("Будь ласка, введіть ціле число!")
            continue
        
        attempts += 1
        
        if guess < secret_number:
            print("Занадто маленьке!")
        elif guess > secret_number:
            print("Занадто велике!")
        else:
            print(f"Вітаємо! Ви вгадали число {secret_number} за {attempts} спроб!")
            return
    
    # Якщо спроби закінчились
    print(f"На жаль, ви не вгадали. Загадане число було {secret_number}.")

# Запуск гри
if __name__ == "__main__":
    guess_the_number()