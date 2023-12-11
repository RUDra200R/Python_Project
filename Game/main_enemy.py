from enemy import Enemy, Troll, Vampyre, VampyreKing
# for enemy class
# random_monster = Enemy("Basic enemy", 12, 1)
# print(random_monster)
#
# random_monster.take_damage(4)
# print(random_monster)
#
# random_monster.take_damage(8)
# print(random_monster)
#
# random_monster.take_damage(9)
# print(random_monster)

# for troll class
ugly_troll = Troll("pug")
print("Ugly troll - {}".format(ugly_troll))
another_troll = Troll("Ug")
print("Another_troll - {}".format(another_troll))
brother = Troll("Ugr")
print(brother)


# part 2 for troll class grunt method
ugly_troll.grunt()
another_troll.grunt()
brother.grunt()
monster = Troll("Basic enemy")
monster.grunt()

# for vampyre class
vamp = Vampyre("vamp")
print(vamp)
vamp.take_damage(5)
print(vamp)
print("-" * 80)
another_troll.take_damage(30)
print(another_troll)
#
# while vamp.alive:
#     vamp.take_damage(1)
#     # print(vamp)

vamp._lives = 0
vamp._hit_points = 1
print(vamp)
# for Vampyreking class
dracula = VampyreKing("Dracula")
print(dracula)
dracula.take_damage(12)
print(dracula)
