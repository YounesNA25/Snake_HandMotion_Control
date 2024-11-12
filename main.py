import pygame
import threading
from queue import Queue
from src.gestures_manager import gesture_detection_process
from src.game import Game

def main():
    gesture_queue = Queue()
    game_running = threading.Event()
    game_running.set()

    # Créer et démarrer le thread de détection des gestes
    gesture_thread = threading.Thread(
        target=gesture_detection_process,
        args=(gesture_queue, game_running)
    )
    gesture_thread.start()

    # Démarrer le jeu dans le thread principal
    game = Game(gesture_queue, game_running)
    game.game_running()

    # Nettoyage
    game_running.clear()
    gesture_thread.join()
    pygame.quit()

if __name__ == '__main__':
    main()