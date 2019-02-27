monsters = ["Cat","Commoner","Hyena","Jackal","Scorpion","Vulture","Bandit","Camel","Flying Snake","Guard","Kobold","Mule","Poisonous Snake","Stirge","Tribal Warrior","Constrictor Snake","Giant Lizard","Giant Poisonous Snake","Giant Wolf Spider","Pseudodragon","Winged Kobold","Dust Mephit","Gnoll","Hobgoblin","Jackalwere","Scout","Swarm of Insects","Death Dog","Giant Hyena","Giant Spider","Giant Toad","Giant Vulture","Half-ogre","Lion","Thri-kreen","Yuan-ti Pureblood","Bandit Captain","Berserker","Druid","Giant Constrictor Snake","Gnoll Pack Lord","Ogre","Giant Scorpion","Hobgoblin Captain","Mummy","Phase Spider","Wight","Yuan-ti Malison","Couatl","Gnoll Fang of Yeenoghu","Lamia","Weretiger","Air Elemental","Fire Elemental","Revenant","Cyclops","Hobgoblin Warlord","Medusa","Young Brass Dragon","Yuan-ti Abomination","Young Blue Dragon","Guardian Naga","Efreeti","Gynosphinx","Roc","Adult Brass Dragon","Mummy Lord","Purple Worm","Adult Blue Dragon","Adult Blue Dracolich","Androsphinx","Ancient Brass Dragon","Ancient Blue Dragon"]
sorted_monsters = list()
for index in range(len(monsters)):
    if (index % 2 == 0):
        sorted_monsters.reverse()

    sorted_monsters.append(monsters[index])

monsters_with_intelience = list()
final_monster_list = list()

for monster in sorted_monsters:
    short_monster_list = list()
    short_monster_list.append(monster)
    short_monster_list.append(1)
    final_monster_list.append(short_monster_list)


print(final_monster_list)