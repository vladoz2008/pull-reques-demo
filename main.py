def greet(name):
    """Функция приветствует пользователя по имени."""
    if not name:
        print("No name provided.")
    else:
        print(f"Hello {name}")

if __name__ == "__main__":
    greet("world")