#!/usr/bin/python3
from random import choice
from models.DiceRoller import DiceRoller as d
import math
import string

class FuckingEncounter:
    description = ""

    def __init__(self, terrain):
        self.description = "The fucking party encounters %s near %s" % (self.get_encounter_type(terrain), self.get_nuanced_terrain(terrain))



    def get_monsters(self, terrain):
        roll = d.roll_dice(3)
        monsters = list()
        if terrain == "arctic":
            monsters = [['Nightwalker', 1],['Ancient White Dragon', 1],['Adult White Dragon', 1],['Frost Giant Everlasting One', 1],['Remorhaz', 1],['Winter Eladrin', 1],['Abominable Yeti', 0],['Shoosuva', 1],['Ancient White Dragon', 1],['Adult White Dragon', 1],['Abominable Yeti', 1],['Frost Giant', 1],['Young Remorhaz', 1],['Werebear', 1],['Yeti', 1],['Winter Wolf', 0],['Saber-toothed Tiger', 0],['Polar Bear',0 ],['Ogre', 1],['Griffon', 1],['Bandit Captain', 1],['Half-ogre', 1],['Orc', 1],['Ice Mephit', 1],['Tribal Warrior', 1],['Kobold', 1],['Owl', 0],['Commoner', 1],['Bandit', 1],['Blood Hawk', 0],['Giant Owl', 1],['Winged Kobold', 1],['Scout', 1],['Brown Bear', 0],['Berserker', 1],['Druid', 1],['Orc Eye of Gruumsh', 1],['Orog', 1],['Manticore', 1],['Veteran', 1],['Revenant', 1],['Troll', 1],['Mammoth', 0],['Young White Dragon', 1],['Remorhaz', 1],['Roc', 0],['Lost Sorrowsworn', 1],['Frost Giant', 1],['Flind', 1],['Frost Salamander', 1],['Roc', 0],['Boneclaw', 1],['Dire Troll', 1],['Storm Giant Quintessent', 1],['Elder Tempest', 1]]
        elif terrain == "coastal":
            monsters = [['Nightwalker', 1], ['Ancient White Dragon', 1], ['Adult White Dragon', 1], ['Frost Giant Everlasting One', 1], ['Dragon Turtle', 0], ['Adult Blue Dragon', 1], ['Roc', 0], ['Marid', 1], ['Young Bronze Dragon', 1], ['Cyclops', 1], ['Banshee', 1], ['Veteran', 1], ['Sahuagin Priestess', 1], ['Plesiosaurus', 1], ['Griffon', 1], ['Druid', 1], ['Harpy', 1], ['Giant Toad', 0], ['Sahuagin', 1], ['Winged Kobold', 1], ['Giant Wolf Spider', 1], ['Giant Lizard', 0], ['Poisonous Snake', 0], ['Merfolk', 1], ['Giant Crab', 0], ['Blood Hawk', 0], ['Crab', 0], ['Commoner', 1], ['Eagle', 0], ['Bandit', 1], ['Guard', 1], ['Kobold', 1], ['Stirge', 0], ['Tribal Warrior', 1], ['Pseudodragon', 1], ['Pteranodon', 1], ['Scout', 1],['Giant Eagle', 0], ['Bandit Captain', 1], ['Berserker', 1], ['Merrow', 1], ['Ogre', 1], ['Sea Hag', 1], ['Manticore', 1], ['Sahuagin Baron', 1], ['Water Elemental', 1], ['Young Blue Dragon', 1], ['Djinni', 1], ['Storm Giant', 1], ['Adult Bronze Dragon', 1], ['Ancient Bronze Dragon', 1], ['Ancient Blue Dragon', 1], ['Dire Troll', 1], ['Storm Giant Quintessent', 1], ['Elder Tempest', 1]]
        elif terrain == "desert":
            monsters = [['Ancient Brass Dragon', 1], ['Androsphinx', 1], ['Purple Worm', 0], ['Mummy Lord', 1], ['Gynosphinx', 1], ['Efreeti', 1], ['Yuan-ti Abomination', 1], ['Young Brass Dragon', 1], ['Cyclops', 1], ['Revenant', 1], ['Weretiger', 1], ['Lamia', 1], ['Yuan-ti Malison', 1], ['Wight', 1], ['Hobgoblin Captain', 1], ['Giant Scorpion', 0], ['Giant Constrictor Snake', 0], ['Druid', 1], ['Yuan-ti Pureblood', 1], ['Thri-kreen', 1], ['Giant Vulture', 0], ['Giant Toad', 0], ['Death Dog', 0], ['Swarm of Insects', 0], ['Hobgoblin', 1], ['Gnoll', 1], ['Pseudodragon', 1], ['Giant Wolf Spider', 0], ['Constrictor Snake', 0], ['Tribal Warrior', 1], ['Mule', 0], ['Kobold', 1], ['Camel', 1], ['Bandit', 1], ['Jackal', 0], ['Hyena', 0], ['Cat', 0], ['Commoner', 1], ['Scorpion', 0], ['Vulture', 0], ['Flying Snake', 0], ['Guard', 1], ['Poisonous Snake', 0], ['Stirge', 0], ['Giant Lizard', 0], ['Giant Poisonous Snake', 0], ['Winged Kobold', 1], ['Dust Mephit', 1], ['Jackalwere', 1], ['Scout', 1], ['Giant Hyena', 0], ['Giant Spider', 0], ['Half-ogre', 1], ['Lion', 0], ['Bandit Captain', 1], ['Berserker', 1], ['Gnoll Pack Lord', 1], ['Ogre', 1], ['Mummy', 1], ['Phase Spider', 0], ['Couatl', 1], ['Gnoll Fang of Yeenoghu', 1], ['Air Elemental', 1], ['Fire Elemental', 1], ['Hobgoblin Warlord', 1], ['Medusa', 1], ['Young Blue Dragon', 1], ['Guardian Naga', 1], ['Roc', 0], ['Adult Brass Dragon', 1], ['Adult Blue Dragon', 1], ['Adult Blue Dracolich', 1], ['Ancient Blue Dragon', 1]]
        elif terrain == "forest":
            pass
        elif terrain == "grassland":
            pass
        elif terrain == "hill":
            pass
        elif terrain == "mountian":
            pass
        elif terrain == "swamp":
            pass
        elif terrain == "underdark":
            pass
        elif terrain == "underwater":
            pass

        return monsters[math.floor(roll*len(monsters))]
            

    def get_encounter_type(self, terrain):
        d100 = d.roll_dice(1)
        encounter_type = ""

        if d100 < 0.17:
            encounter_type = "an empty area"
        elif d100 < 0.20:
            encounter_type = "an ungaurded treasure"
        elif d100 < 0.61:
            encounter_type = "monsters"
        elif d100 < 0.85:
            encounter_type = "monsters which have treasure"
        elif d100 < 0.89:
            encounter_type = "special"
        elif d100 < 0.97:
            encounter_type = "trap"
        else:
            encounter_type = "trap with treasure"

        if "monsters" in encounter_type:
            monster = self.get_monsters(terrain)
            behavior = self.get_behavior(monster[1])
            encounter_type = encounter_type.replace("monster", monster[0]) 
            encounter_type += " " + behavior[0]

            if behavior[1] == 1:
                other_monster = self.get_monsters(terrain)
                encounter_type += " " + other_monster[0]

        return encounter_type


    def get_nuanced_terrain(self, terrain):
        if terrain == "arctic":
            return choice(["light snow drift","glacier","snow bank","moguls","ice sheet","glacier fizzure","glacier cave","field of permafrost9","frozen carcass","frozen rocks","frozen river","frozen pond","deep, wet snow","a recently killed carcass","hard packed snow","muddy, wet snow","an abandoned cabin","some cabin ruins","waypost stones","large boulders covered in ice","snow drifts against large rocks","frozen tundra","ice flow","frozen lake","rocky river flowing into a glacier cave","tall grasses reaching up though the snow","geothermal vents near melted snow"])
        elif terrain == "coastal":
            return choice(["loose sand dunes","beach grass ","ruined pier","sea cliff","natural arch","ruined lighthouse","overturned boat on the beach","shore washed seaweed","fishing shack","ruined fishing shack","campsite","tree-lined beach","rocky beach","shallow tidal pools","stilt house","ruined stilt house","groomed trail or walkway from cliff to beach","stone pier","ruined fortress","enclosed tidal pool","ruined watch tower"])
        elif terrain == "desert":
            return choice(["scrubbs","rocky gravel","windswept sand dunes","small thorny trees growing in a dry riverbed","salt basin","rolling dunes covered in sagebrush","a flood river ripping through a small canyon","a dry riverbed in a small canyon","a fisure","tall rocky outcroppings","an oasis","a lone dead tree","rocky slopes dotted with thorny trees","salt basin","a field of sharp rocks","fields of cactus and brush","palm trees reaching out of a dry riverbed","thorny flowers growing out of a rocky outcropping","wind-eroded pillars","wind-eroded canyon","dry grassland","tall dunes of flour-fine sands","alkeline water basin","dry lakebed dotted with dead trees"])
        elif terrain == "forest":
            return choice(["a grove of tall evergreen trees","old grove with a dense understory shrubs","a trail or tracks winding through a dense grove","large trees covered in moss","moss covered deadfall","deadfall trees covered in fungus and mushrooms","a small creek winding through tall trees","a trail or tracks which fork in different directions","a gully filled with ferns and deadfall","moss covered understory","a rocky stream with a deadfall bridge","standing stones in a grove","a small clearing","a ruined cabin","an abandoned cabin","an abandoned campsite","a baren patch of dead trees","tall trees draped in vines","a rocky gulch with a river running through it ","a clearing with a pond filled with lilly pads","a forest clearing filled with wildflowers","thin young trees with twisted, winding branches","a sparse grove of trees with leaf litter","old trees draped in moss","thin young trees reaching up from purple and blue wildflowers","an old tree with a treehouse","an old twisted tree growing out of a rocky outcropping","boulders revealing an entrance to a cave"])
        elif terrain == "grassland":
            return choice(["small groups of scrubbs","tall lush grasses and reeds","a lone tree in the fields","dry gray grasses","white wildflowers","purple wildflowers","fields of wild grains and groats","a trail or animal tracks through the grasses","standing stones","a kopie","a small stream","a pond","large mounds of dirt covered in dead grass","thorny flowers in a thicket","yellow wildflowers","patches of dense scrubbs","a small grove of trees","a pond surrounded by cattails","a gully filled with small trees and scrubbs","a pair of trees in a wide field","a ruined fence or pen","a small cabin"])
        elif terrain == "hills":
            return choice(["a small cliff","a switchback path up a Hill","a rocky cliff ledge","shrubs growing out of a large pile of boulders","a washed out gully","slopes dotted with trees","rolling hills dotted with boulders","a patchwork of shrubs and small trees","standing stones on a cliff edge","standing stones on a hilltop","ruined watchtower on a hill","watchtower on a hill","moss covered cliffs","a stream running between two hills","crags and rocky outcroppings on the slope of a hill","a small cabin nestled in a gully","a single tall tree on a hill","a steep rocky slope giving way to a cave entrance"])
        elif terrain == "mountain":
            return choice(["steep rocky slopes","wind eroded gully","a deep canyon filled with fog","a river cutting between two peaks","a cascading waterfall over a rocky cliff","rolling rocky slopes dotted with trees","a line of trees following a gulley","a caldera","a pond","a deep lake surrounded by rocky slopes","a small hunting cabin","a ruined hunting cabin","an abandoned cabin","a shallow, winding, canyon","a peak reaching above the timberline","scrub and dry brush eeking out of a pile of boulders","windswept standing stones","water eroded canyon","a stone arch over a small canyon","a pond lined with evergreen trees","tall pillar rock formations","a sheer bluff","a ghrotto dotted with trees","a burbling stream through the rocks","lose rock over an undulating slope"])
        elif terrain == "swamp":
            return choice(["mangrove trees","flooded area","thick gloppy mud","thick roots burled above the murky water","algea crusted deadfall","floating plantlife in the water","tall reeds and grasses among the trees","muddy banks along a treeline","a dam of deadfall washed against some trees","tangled shrubs growing in the mud","tall trees draped over with hanging moss","mosses and ferns growing up out of the muck","a small cabin on stilts","an overturned boat lodged into a tree","a tangle of roots above the murkey waterline","tall grasses emerging from the water","depressions of muddy leaf litter nestled between some trees.","A large boulder covered over with trees and moss","an open expanse of muddy grassland with a few dead trees standing erect in the muck","a thick blanket of moss draped over some dead trees","a floating dock","an open wet area free from trees","a field of dead trees covered in mushrooms","a floating cabin lashed to a dead tree","a boggy field covered in patches of grass"])
        elif terrain == "underdark":
            return choice(["open cavern full of stalactites","and underground river","an underground stream","an underground lake","a multi-tiered glowing mushroom forest","small stalactites and stalackmites","large sharp crystals growing out of the ground","walls covered in sharp crystals","a glowing mushroom farm","a forest of tall, tube shaped mushrooms.","a deep flooded chasam","a hovel carved into stone walls","a underground pond with stalacmights thrusting upward from in it","bizzare twisting rock formations with crystals growing from their cracks.","a mist filled cavern with grags and boulders","a mysteriously glowing tree that gives off it's own light","a cracked basin filled with wet sand","a low cieling hanging with fungus","a cave in filled with boulders","multilevel tiered rock formations","a canyon covered in fungus"])
        elif terrain == "underwater":
            return choice(["a coral crag","a reef on a sheer cliff","a forest of kelp and seaweed","tall stones jutting out of the sand","tumbling stones rolled across the sand","barnacle covered rocks","a reef of large, soft corals","a sand flat","berms of bleached coral","stacked stones overgrown in sea moss","a sunken boat","an underwater cave","rocky flats dusted with sand","a sunken statue covered in filter feeders and seaweed","ruins of a submerged building","grasses and seaweed over a flat of sand","geothermal vents jutting out of rocky outcroppings","rocky crags","sand drifted rocky outcroppings"])
        # elif terrain == "Urban":
        #   return choice([])

    def get_behavior(self,isInteligent):
        inteligent_behaviors = [["who are doing something with art", 0],["who are meditating", 0],["who are performing a ritual", 0],["who are are wounded", 0],["who are willing to be diplomatic", 0],["who are toiling and laboring", 0],["who are lost or searching for something", 0],["who are fleeing or are in persuit of", 1],["who are in combat with", 1],["who are walking", 0],["who are patrolling", 0],["who are in an altered state are here", 0],["who are hunting or gathering resources", 0],["who are mating", 0],["who are resting or making camp", 0],["who are sleeping", 0]]
        animal_behaviors = [["who are sleeping", 0],["who are dying", 0],["who are mating", 0],["who are eating or being eaten by", 1],["who are patrolling", 0],["who are walking", 0],["who are strutting a territorial display", 0],["who are in combat with", 1],["who are wounded", 0],["who are walking", 0],["who are strutting a territorial display", 0],["who are resting, relaxing, or otherwise nesting", 0],["who are fleeing or in persuit of", 1],["who are hunting or gathering", 0],["who are in an altered state", 0],["who are defecating", 0]]
        roll = d.roll_dice(3)

        if isInteligent == 1:
            return inteligent_behaviors[math.floor(roll*len(inteligent_behaviors))]
        else:
            return animal_behaviors[math.floor(roll*len(animal_behaviors))]

        


        