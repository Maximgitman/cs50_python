def camel_to_snake(camel_case):
        
    snake_case = ""
    for char in camel_case:
        if char.islower():
            snake_case += char
        else:
            snake_case += f"_{char.lower()}"
    return snake_case

if __name__ == "__main__":
    camel = input("camelCase: ")
    print(camel_to_snake(camel))