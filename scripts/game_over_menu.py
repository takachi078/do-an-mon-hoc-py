import pygame
import sys

def game_over_menu(game):

    bg = pygame.image.load(
        r'data/images/game_over_bg.png'
    ).convert()

    bg = pygame.transform.scale(
        bg,
        (320, 240)
    )

    while True:

        game.display.blit(bg, (0, 0))

        # FONT
        title_font = pygame.font.SysFont("Arial", 45)
        button_font = pygame.font.SysFont("Arial", 30)

        # ===== TITLE =====
        title = title_font.render(
            "GAME OVER",
            True,
            (255, 0, 0)
        )

        game.display.blit(title, (55, 50))

        # ===== BUTTONS =====
        continue_rect = pygame.Rect(60, 120, 200, 50)

        back_rect = pygame.Rect(60, 190, 200, 50)

        pygame.draw.rect(
            game.display,
            (60, 60, 60),
            continue_rect,
            border_radius=10
        )

        pygame.draw.rect(
            game.display,
            (60, 60, 60),
            back_rect,
            border_radius=10
        )

        # ===== BUTTON TEXT =====
        continue_text = button_font.render(
            "CONTINUE",
            True,
            (255, 255, 255)
        )

        back_text = button_font.render(
            "BACK",
            True,
            (255, 255, 255)
        )

        game.display.blit(continue_text, (82, 132))

        game.display.blit(back_text, (125, 202))

        # SCALE
        scaled_display = pygame.transform.scale(
            game.display,
            game.screen.get_size()
        )

        game.screen.blit(scaled_display, (0, 0))

        # ===== EVENTS =====
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:

                # SCALE MOUSE
                mx, my = event.pos

                mx /= 2
                my /= 2

                # CONTINUE
                if continue_rect.collidepoint((mx, my)):

                    game.load_level(game.level)

                    return

                # BACK TO MENU
                if back_rect.collidepoint((mx, my)):

                    return

        pygame.display.update()

        game.clock.tick(60)