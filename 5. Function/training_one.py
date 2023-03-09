#Тренажер 1
def discriminant(a, b, c):
    """
    функция для нахождения дискриминанта
    """
    return b ** 2 - 4 * a * c



def solution(a, b, c):
    """
    функция для нахождения корней уравнения
    """
    if discriminant(a, b, c) > 0:
        x1 = ((-b + (discriminant(a, b, c) ** 0.5)) / (2 * a))
        x2 = ((-b - (discriminant(a, b, c) ** 0.5)) / (2 * a))
        print(x1, x2)
    elif discriminant(a, b, c) == 0:
        x = -b / (2 * a)
        print(x)
    else:
        print('корней нет')    
    

if __name__ == '__main__':
    solution(1, 8, 15) 
    solution(1, -13, 12)
    solution(-4, 28, -49)
    solution(1, 1, 1)