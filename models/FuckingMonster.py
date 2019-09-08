import random

class FuckingMonster:
    basic_animal_feature = ""
    body_plan = ""
    limb_novelty = ""
    skin_novelty = ""
    main_weapon = ""
    size = ""
    behavior = ""
    behavior_trait = ""
    harmful_discharge = ""
    poison = ""
    onset = ""
    durration = ""
    monster = ""

    def get_basic_animal_feature(self):
        return random.choice(["amphibious","avian","fish-like","insectoid","fanged, hairy","lizardlike","burly and many-legged","wholly alien"])


    def get_body_plan(self):
        return random.choice(["humanoid","quadrupedal","many-legged","bulbous","amorphous"])

    def get_poison(self):
        return random.choice(["death","paralysis","recuring damage","convulsion","blindness","hallucination"])


    def __init__(self):
        self.basic_animal_feature = self.get_basic_animal_feature()
        if random.randint(1,11) > 9:
            while True:
                new_animal_feature = self.get_basic_animal_feature()
                if self.basic_animal_feature != new_animal_feature:
                    break

            self.basic_animal_feature += ", " + new_animal_feature
        
        self.body_plan = self.get_body_plan()
        if random.randint(1,6) > 4:
            while True:
                new_body_plan = self.get_body_plan()
                if self.body_plan != new_body_plan:
                    break
            self.body_plan += ", " + new_body_plan

        self.limb_novelty = random.choice(["wings","many-jointed limbs","tentacles","opposable thumbs","retractable limbs","varying sized limbs"])
        self.skin_novelty = random.choice(["a hard shell","an exoskeleton","an odd body texture","to molt regularly","skin harmful to touch","wet or slimy skin"])
        self.main_weapon = random.choice(["teeth or mandibles","claws","poison","harmful discharge","pincers","horns"])
        self.size = random.choice(["small","medium sized","large","huge","gargantuan"])
        self.behavior = random.choice(["hunt in kin-group packs","favor ambush attacks", "criple prey and wait for their death", "support the alpha while pack hunting","lure or drive prey into danger","hunt alone", "are only predators at certian times","mindlessly attacks humans","move in vigilant heards","exist in small family groups","team up on a single foe","go berserk when near death","are violent in certian seasons","are vicious if threatened","have symbiotic creatures protect them","breed at tremendous rates","never attack unwounded prey","use other beasts as harriers","always flee if it is significantly hurt","poison thier prey, and wait for it to die","disguise themselves as prey","are remarkably stealthy","summon predators to weak prey","steal prey from weaker predators"])
        
        if "harmful discharge" in self.main_weapon:
            self.harmful_discharge = random.choice(["acidic spews doing its damage on hit","toxic spittle or clouds","sonic drills or other disabling noises","natural lasers or plasma discharges","nauseating stenches or disabling chemcials","equipment-melting corrosive fluids","explosive pellets or chemical catalyts"])
            if "toxic" in self.harmful_discharge:
                self.poison = self.get_poison()
                self.onset = random.choice(["instantly","in moments","in less than a minute","in about a minute","in a few minuts", "in an hour"])

                self.main_weapon = "%s that causes %s in %s and lasts for %s" % (self.harmful_discharge, self.poison, self.onset, self.durration)

                if "death" not in self.poison:
                    self.main_weapon += " and lasts for " + random.choice(["less than a minute","about a minute","about ten minutes","about an hour", "a few hours","a few days"])
            
            self.main_weapon = self.harmful_discharge
        elif "poison" in self.main_weapon:
            self.main_weapon = self.get_poison() + "-causing poison"

        self.monster = "You run into a fucking %s %s %s creature with %s and it has %s. They %s and use fucking %s to attack." % (self.size, self.basic_animal_feature, self.body_plan, self.limb_novelty, self.skin_novelty, self.behavior, self.main_weapon)