import pygame
import sys


def checker(mas, sign):
    zeroes = 0

    for row in mas:
        zeroes += row.count(0)
        if row.count(sign) == 3:
            return sign

    for col in range(3):
        if mas[0][col] == sign and mas[1][col] == sign and mas[2][col] == sign:
            return sign

    if mas[0][0] == sign and mas[1][1] == sign and mas[2][2] == sign:
        return sign

    if mas[0][2] == sign and mas[1][1] == sign and mas[2][0] == sign:
        return sign

    if zeroes == 0:
        return 'Piece'

    return False


pygame.init()
size_block = 100
margin = 15
width = height = size_block * 3 + margin * 4

size_window = (width, height)
screen = pygame.display.set_mode(size_window)
pygame.display.set_caption('tic-tac-toe')

field_color = (64, 64, 64)
x_color = (149, 18, 182)
o_color = (16, 121, 182)
gray = (96, 96, 96)
black_gray = (64, 64, 64)
white = (250, 250, 250)

query = 0  # ++

mas = [[0] * 3 for i in range(3)]

game_over = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            x_mouse, y_mouse = pygame.mouse.get_pos()
            col = x_mouse // (size_block + margin)
            row = y_mouse // (size_block + margin)
            if mas[row][col] == 0:
                if query % 2 == 0:
                    mas[row][col] = 'x'
                else:
                    mas[row][col] = 'o'
                query += 1
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            game_over = False
            mas = [[0] * 3 for i in range(3)]
            query = 0
            screen.fill(field_color)

    if not game_over:
        for row in range(3):
            for col in range(3):
                if mas[row][col] == 'x':
                    color = x_color
                elif mas[row][col] == 'o':
                    color = o_color
                else:
                    color = gray
                x = col * size_block + (col + 1) * margin
                y = row * size_block + (row + 1) * margin
                pygame.draw.rect(screen, color, (x, y, size_block, size_block))
                if color == x_color:
                    pygame.draw.line(screen, white, (x + 5, y + 5), (x + size_block - 5, y + size_block - 5), 5)
                    pygame.draw.line(screen, white, (x + size_block - 5, y + 5), (x + 5, y + size_block - 5), 5)
                elif color == o_color:
                    pygame.draw.circle(screen, white, (x + size_block // 2, y + size_block // 2), size_block // 2 - 3, 5)

    if (query - 1) % 2 == 0:
        game_over = checker(mas, 'x')
    else:
        game_over = checker(mas, 'o')

    if game_over:
        screen.fill(field_color)
        font = pygame.font.SysFont('atxingkai', 80)
        text1 = font.render(game_over, True, white)
        text_rect = text1.get_rect()
        text_x = screen.get_width() / 2 - text_rect.width / 2
        text_y = screen.get_height() / 2 - text_rect.height / 2
        screen.blit(text1, [text_x, text_y])

    pygame.display.update()