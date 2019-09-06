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
        return random.choice(["amphibious","avian","fish-like","insectoid","hairy and fanged","lizardlike","fat and many-legged","made of wholly alien elements"])


    def get_body_plan(self):
        return random.choice(["humanoid","quadruped","many-legged","bulbous","amorphous"])

    def get_poison(self):
        return random.choice(["death","paralysis","recuring damage","convulsion","blindness","hallucination"])


    def __init__(self):
        self.basic_animal_feature = self.get_basic_animal_feature()
        if random.randint(1,11) > 9:
            while True:
                new_animal_feature = self.get_basic_animal_feature()
                if self.basic_animal_feature != new_animal_feature:
                    break

            self.basic_animal_feature += " and " + self.get_basic_animal_feature()
        
        self.body_plan = self.get_body_plan()
        if random.randint(1,6) > 4:
            self.body_plan += " and " + self.get_body_plan()

        self.limb_novelty = random.choice(["wings","many jointed limbs","tentacles","opposable thumbs","retractable limbs","varying sized limbs"])
        self.skin_novelty = random.choice(["a hard shell","an exoskeleton","an odd body texture","to molt regularly","skin harmful to touch","wet or slimy skin"])
        self.main_weapon = random.choice(["teeth or mandibles","claws","poison","harmful discharge","pincers","horns"])
        self.size = random.choice(["cat-sized","wolf-sized","bull-sized","hippo-sized","elephant-sized"])
        self.behavior = random.choice(["hunts in kin-group packs","favors ambush attacks", "criples prey and waits for their death", "its pack supports the alpha","lures or drives prey into danger","hunts alone", "is only a predator at certian times","mindlessly attacks humans","moves in vigilant heards","exists in small family groups","teams up on a single foe","goes berserk when near death","is violent in certian seasons","is vicious if threatened","has symbiotic creatures protect them","breeds at tremendous rates","never attacks unwounded prey","uses other beasts as harriers","always flees if it is significantly hurt","poisons its prey, waits for it to die","disguises itself as its prey","is remarkably stealthy","summons predators to weak prey","steals prey from weaker predators"])
        
        if "harmful discharge" in self.main_weapon:
            self.harmful_discharge = random.choice(["an acidic spew doing its damage on hit","a toxic spittle or cloud","a sonic drill or other disabling noise","a natural laser or plasma discharge","a nauseating stench or disabling chemcial","an quipment-melting corrosive fluid","explosive pellets or chemical catalyts."])
            if "toxic" in self.harmful_discharge:
                self.poison = self.get_poison()
                self.onset = random.choice(["instantly","in moments","in less than a minute","in about a minute","in a few minuts", "in an hour"])

                self.main_weapon = "%s that causes %s in %s and lasts for %s" % (self.harmful_discharge, self.poison, self.onset, self.durration)

                if "death" not in self.poison:
                    self.main_weapon += " and lasts for " + random.choice(["less than a minute","about a minute","about ten minutes","about an hour", "a few hours","a few days"])
            
            self.main_weapon = self.harmful_discharge
        elif "poison" in self.main_weapon:
            self.main_weapon = self.get_poison() + "causiong poison"

        self.monster = "You run into a fucking %s %s %s creature with %s and it has %s. It %s and uses fucking %s to attack." % (self.size, self.basic_animal_feature, self.body_plan, self.limb_novelty, self.skin_novelty, self.behavior, self.main_weapon)