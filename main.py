from game_of_life import GameOfLife
import time

game = GameOfLife(10, 10)

# contoh pola "blinker"
game.set_alive(4, 5)
game.set_alive(5, 5)
game.set_alive(6, 5)

for _ in range(20):
    game.display()
    game.next_generation()
    time.sleep(0.5)
