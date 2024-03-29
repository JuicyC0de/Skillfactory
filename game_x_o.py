def new_game(): #Функция новой игры
    arena = [[' ', 1, 2, 3],
             [1, '-', '-', '-'],
             [2, '-', '-', '-'],
             [3, '-', '-', '-']]    #Создаем чистое поле
    return arena, 0, False, False    #Возвращаем чистое поле


def display():  #Функция отображения поля в консоли
    for i in range(4):
        print(*game_arena[i])


def check_win(arena, gamer):    #Функция проверки на победу, берем само состояние поля и какой игрок, для присваивания ему победы
    arena_lines = [[arena[i][j] for i in range(1, 4)] for j in range(1, 4)] #Создаем варианты направлений победы - здесь столбцы
    arena_lines.append([arena[i][i] for i in range(1, 4)])  #Здесь одна диагональ
    arena_lines.append([arena[i][-1 * (i - 4)] for i in range(1, 4)])   #Здесь другая
    for i in range(1, 4):
        arena_lines.append(arena[i][1:])    #Добавляем так же строки
    if any(arena_lines[i].count(gamer) == 3 for i in range(len(arena_lines))):  #Ну и проверяем собственно на победу (3 одинаковых символа в каком либо списке из вариантов)
        print(f'Игра окончена. Победил игрок -{gamer.upper()}-!')   #Сообщение о победе
        return True #Возврат тру для смены статуса игры


def game_step(arena, gamer):    #Функция самого хода, берем для записи хода само поле и какой игрок ходит
    can_do = ('1', '2', '3')    #Допустимые для ввода данные
    while True: #Создаем цикл пока игрок не введет допустимые значения
        step = list(map(str, input(f'Игрок -{gamer}-, Введите координаты x_y: ').split()))  #Записываем ход игрока в формате строки, что бы не словить ошибку если введено не число
        if len(step) != 2 or not all(i in can_do for i in step):    #Проверяем что бы введенные данные соответствоали тому, что мы ждем
            print(f'Введите координаты в виде 2-х чисел в диапазоне от 1 до 3, разделенных пробелом')   #Уточняем, что мы хотим
            continue    #Если введено что то не то, начинаем цикл снова с ввода данных
        step = list(map(int, step)) #Ошибок нет, преобразуем данные в числовые координаты
        if arena[step[1]][step[0]] == '-':  #Проверяем по координатам, не заняты ли уже они
            arena[step[1]][step[0]] = gamer.lower() #Записываем сам ход в поле
            break   #Завершаем цикл хода
        else:
            print('Данная ячейка уже занята, сделайте другой ход') #Если ячейка занята ходим снова по циклу


win = x = bool  #состояние окончания игры в случае победы или заполненности поля, выбор игрока - игроков может быть только два, поэтому тоже булевый тип для переключения
takt = int  #подсчет ходов, что бы не делать лишние проверки на победу раньше 5 хода и завершить игру, когда ходов уже 9
game_arena, takt, win, x = new_game() #Создаем новую игру
while not win:  #цикл игры
    display() #отображение поля
    x = not x   #переключение игрока
    game_step(game_arena, 'X' if x else 'O')    #шаг игры
    takt += 1   #плюс к подсчету ходов
    if takt > 4:    #начинаем проверку на победу с 5-го хода, когда хотя бы у одного есть 3 хода
        win = check_win(game_arena,  'x' if x else 'o') #Статус игры победа или нет
    if takt == 9:   #заполенность поля - заканчиваем игру
        win = True
        print(f'Игра окончена. Ничья!')
    if win: #если игра окончена предлагаем сиграть еще раз
        if input(f'Если хотите поиграть еще, введите "y" и нажмите enter: ') == 'y':
            game_arena, takt, win, x = new_game()
        else:
            print(f'Good By !!!')
