import pygame
import random
import os
class Game:
    def __init__(self, gesture_queue, game_running):
        os.environ['SDL_VIDEO_WINDOW_POS'] = "0,100"
        pygame.init()
        self._init_game_window()
        self._init_game_variables()
        self._init_snake()
        self._init_apple()
        self._init_display_elements()
        self.gesture_queue = gesture_queue
        self.game_running_flag = game_running

    def _init_game_window(self):
        """Initialisation de la fenêtre de jeu"""
        pygame.display.set_caption("Snake")
        self.screen = pygame.display.set_mode((720, 480))
        self.clock = pygame.time.Clock()
        self.FPS = 10

    def _init_game_variables(self):
        """Initialisation des variables de jeu"""
        self.running = True
        self.score = 0
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.GREEN = (0, 255, 0)
        self.RED = (255, 0, 0)
        self.GAME_BOUNDS = {
            'left': 70,    
            'right': 660,
            'top': 30,     
            'bottom': 420
        }

    def _init_snake(self):
        """Initialisation des variables du serpent"""
        self.snake_position_x = 200
        self.snake_position_y = 200
        self.snake_direction_x = 0
        self.snake_direction_y = 0
        self.snake_body = 10
        self.snake_positions = [[200, 200]]
        self.snake_size = 1

    def _init_apple(self):
        """Initialisation de la pomme"""
        self.apple_body = 10
        self._respawn_apple()

    def _init_display_elements(self):
        """Initialisation des éléments d'affichage"""
        self.font = pygame.font.Font(None, 50)
        self.score_font = pygame.font.Font(None, 24)

    def _respawn_apple(self):
        """Replace la pomme à une position aléatoire"""
        min_x = self.GAME_BOUNDS['left'] + 10
        max_x = self.GAME_BOUNDS['right'] - 10
        min_y = self.GAME_BOUNDS['top'] + 10
        max_y = self.GAME_BOUNDS['bottom'] - 10

        possible_x = range(min_x, max_x + 1, 10)
        possible_y = range(min_y, max_y + 1, 10)
        
        self.apple_position_x = random.choice(list(possible_x))
        self.apple_position_y = random.choice(list(possible_y))

    def _handle_events(self):
        """Gestion des événements"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.game_running_flag.clear()
            if event.type == pygame.KEYDOWN:
                self._handle_keyboard_input(event.key)

        try:
            while not self.gesture_queue.empty():
                gesture = self.gesture_queue.get_nowait()
                print(f"Geste reçu: {gesture}")
                self._handle_gesture(gesture)
        except:
            pass

    def _handle_keyboard_input(self, key):
        """Gestion des entrées clavier"""
        if key == pygame.K_RIGHT and self.snake_direction_x != -10:
            self.snake_direction_x = 10
            self.snake_direction_y = 0
        elif key == pygame.K_LEFT and self.snake_direction_x != 10:
            self.snake_direction_x = -10
            self.snake_direction_y = 0
        elif key == pygame.K_DOWN and self.snake_direction_y != -10:
            self.snake_direction_x = 0
            self.snake_direction_y = 10
        elif key == pygame.K_UP and self.snake_direction_y != 10:
            self.snake_direction_x = 0
            self.snake_direction_y = -10

    def _handle_gesture(self, gesture_id):
        """Gestion des gestes"""
        if gesture_id == 5 :  # RIGHT
            self.snake_direction_x = 10
            self.snake_direction_y = 0
        elif gesture_id == 4:  # LEFT
            self.snake_direction_x = -10
            self.snake_direction_y = 0
        elif gesture_id == 2 :  # DOWN
            self.snake_direction_x = 0
            self.snake_direction_y = 10
        elif gesture_id == 3 :  # UP
            self.snake_direction_x = 0
            self.snake_direction_y = -10
        # elif gesture_id == 0:  # STOP
        #     self.snake_direction_x = 0
        #     self.snake_direction_y = 0

    def _update_snake_position(self):
        """Mise à jour de la position du serpent"""
        self.snake_position_x += self.snake_direction_x
        self.snake_position_y += self.snake_direction_y
        
        self.snake_head = [self.snake_position_x, self.snake_position_y]
        self.snake_positions.append(self.snake_head)
        if len(self.snake_positions) > self.snake_size:
            self.snake_positions.pop(0)

    def _check_collisions(self):
        """Vérification des collisions"""
        if (self.snake_position_x >= self.GAME_BOUNDS['right'] or 
            self.snake_position_x < self.GAME_BOUNDS['left'] or 
            self.snake_position_y >= self.GAME_BOUNDS['bottom'] or 
            self.snake_position_y < self.GAME_BOUNDS['top']):
            self.running = False

        if (self.apple_position_x == self.snake_position_x and 
            self.apple_position_y == self.snake_position_y):
            self._respawn_apple()
            self.snake_size += 1
            self.score += 10

        # for segment in self.snake_positions[:-1]:
        #     if segment == self.snake_head:
        #         self.running = False

    def _draw_game(self):
        """Dessin des éléments du jeu"""
        self.screen.fill(self.BLACK)
        
        for part in self.snake_positions:
            pygame.draw.rect(
                self.screen,
                self.GREEN,
                (part[0], part[1], self.snake_body, self.snake_body)
            )
        
        pygame.draw.rect(
            self.screen,
            self.RED,
            (self.apple_position_x, self.apple_position_y, 
             self.apple_body, self.apple_body)
        )
        
        self._draw_game_limits()
        self._draw_score()
        
        pygame.display.flip()

    def _draw_game_limits(self):
        """Dessin des limites du terrain"""
        pygame.draw.rect(
            self.screen,
            self.WHITE,
            (self.GAME_BOUNDS['left'], 
             self.GAME_BOUNDS['top'],
             600,
             400),
            2
        )

    def _draw_score(self):
        """Affichage du score"""
        score_text = self.score_font.render(
            f'Score: {self.score}',
            True,
            self.WHITE
        )
        self.screen.blit(score_text, (13, 13))

    def show_game_over(self):
        """Affichage de l'écran de game over"""
        self.screen.fill(self.BLACK)
        
        game_over_text = self.font.render('Game Over', True, self.WHITE)
        text_rect = game_over_text.get_rect(
            center=(self.screen.get_width()/2, self.screen.get_height()/2 - 33)
        )
        self.screen.blit(game_over_text, text_rect)
        
        final_score_text = self.score_font.render(
            f'Score final: {self.score}',
            True,
            self.WHITE
        )
        score_rect = final_score_text.get_rect(
            center=(self.screen.get_width()/2, self.screen.get_height()/2 + 33)
        )
        self.screen.blit(final_score_text, score_rect)
        
        pygame.display.flip()
        pygame.time.wait(2000)

    def game_running(self):
        """Boucle principale du jeu"""
        clock = pygame.time.Clock()
        while self.running:
            self._handle_events()
            self._update_snake_position()
            self._check_collisions()
            self._draw_game()
            clock.tick(self.FPS)

            if not self.running:
                self.show_game_over()