from player import Player

Romil = Player("Romil")
print(Romil.name)
print(Romil.lives)
Romil.lives -= 1
print(Romil)

Romil.lives -= 1
print(Romil)

Romil.lives -= 1
print(Romil)

Romil.lives -= 1
print(Romil)
Romil._lives = 9
print(Romil)

Romil.level = 2
print(Romil)
Romil.level += 5
print(Romil)
Romil.level = 3
print(Romil)

Romil.score = 500
print(Romil)
