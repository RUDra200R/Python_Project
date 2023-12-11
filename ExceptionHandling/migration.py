import Duck

flock = Duck.Flock()
donald = Duck.Duck()
daisy = Duck.Duck()
duck3 = Duck.Duck()
duck4 = Duck.Duck()
duck5 = Duck.Duck()
duck6 = Duck.Duck()
duck7 = Duck.Duck()
percy = Duck.Penguin()

flock.add_duck(donald)
flock.add_duck(daisy)
flock.add_duck(duck3)
flock.add_duck(duck4)
flock.add_duck(percy)
flock.add_duck(duck5)
flock.add_duck(duck6)
flock.add_duck(duck7)

flock.migrate()
