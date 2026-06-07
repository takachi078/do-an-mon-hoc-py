
import pygame
import sys

pygame.init()

# Kích thước màn hình
WIDTH = 1280
HEIGHT = 720

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Platform Game")

clock = pygame.time.Clock()

# Font
font = pygame.font.SysFont("Arial", 50)

# Load background
menu_bg = pygame.image.load("data/images/background.png").convert()
menu_bg = pygame.transform.scale(menu_bg, (WIDTH, HEIGHT))

# Màu
WHITE = (255, 255, 255)
BLUE = (50, 150, 255)

# Hàm vẽ text
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect(center=(x, y))
    surface.blit(textobj, textrect)

# Hàm game chính
def game():
    running = True

    while running:
        screen.fill((0, 0, 0))

        draw_text("GAME STARTED", font, WHITE, screen, WIDTH // 2, HEIGHT // 2)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        clock.tick(60)

# Main Menu
def main_menu():
    while True:

        # Vẽ background
        screen.blit(menu_bg, (0, 0))

        # Tiêu đề
        draw_text("PLATFORM GAME", font, WHITE, screen, WIDTH // 2, 120)

        # Button
        start_rect = pygame.Rect(540, 250, 200, 60)
        option_rect = pygame.Rect(540, 350, 200, 60)
        quit_rect = pygame.Rect(540, 450, 200, 60)

        pygame.draw.rect(screen, BLUE, start_rect, border_radius=10)
        pygame.draw.rect(screen, BLUE, option_rect, border_radius=10)
        pygame.draw.rect(screen, BLUE, quit_rect, border_radius=10)

        draw_text("START", font, WHITE, screen, WIDTH // 2, 280)
        draw_text("OPTION", font, WHITE, screen, WIDTH // 2, 380)
        draw_text("QUIT", font, WHITE, screen, WIDTH // 2, 480)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:

                mouse_pos = pygame.mouse.get_pos()

                # START
                if start_rect.collidepoint(mouse_pos):
                    game()

                # OPTION
                if option_rect.collidepoint(mouse_pos):
                    print("OPTION")

                # QUIT
                if quit_rect.collidepoint(mouse_pos):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()
        clock.tick(60)

# Chạy menu
main_menu()