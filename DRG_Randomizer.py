import random #random number generator

#Dictionaries and Lists

#CLASS_TYPE_NAME_Mods = {11: "", 12: "", 13: "", 21: "", 22: "", 23: "", 31: "", 32: "", 33: "", 41: "", 42: "", 43: "", 51: "", 52: "", 53: ""} (Blank Dictionary For Speed)

#Overclock Range
OC_Min = 0
OC_Max = 0

#Driller Equipment

Driller_Primaries = {1: "CRSPR Flamethrower", 2: "Cryo Cannon", 3: "Corrosive Sludge Pump"}
Driller_Secondary = {1: "Subata 120", 2: "Experimental Plasma Charger"}
Driller_Throwables = {1: "Impact Axe", 2: "High Explosive Grenade", 3: "Neurotoxin Grenade"}
Driller_Equipment = ['Reinforced Power Drills', 'Satchel Charge', '"Mole" Armor Rig']

#Driller Primary Mods (Fist Number is tier, Second Number is the mod)

Driller_Pri_Flame_Mods = {11: "High Capacity Tanks", 12: "High Pressure Ejector",
                          21: "Unfiltered Fuel", 22: "Triple Filtered Fuel", 23: "Sticky Flame Duration",
                          31: "Oversized Valves", 32: "Sticky Flame Slowdown", 33: "More Fuel",
                          41: "It Burns!", 42: "Sticky Flame Duration", 43: "More Fuel",
                          51: "Heat Radiance", 52: "Targets Explode"}

Driller_Pri_Cryo_Mods = {11: "Larger Pressure Chamber", 12: "Faster Turbine Spinup", 13: "Stronger Cooling Unit",
                         21: "Larger Reserve Tank", 22: "Overclocked Ejection Turbine", 23: "Bypassed Integrity Check",
                         31: "Improved Pump", 32: "Increased Flow Volume",
                         41: "Hard Mixture", 42: "Supercooling Mixture", 43: "Larger Reserve Tank",
                         51: "Fragile", 52: "Cold Radiance"}

Driller_Pri_Sludge_Mods = {11: "High Capacity Tanks", 12: "Better Air Pressurizer", 13: "Air Sensitive Compound",
                           21: "Dyse Nozzle", 22: "Atomizer Nozzle", 23: "Potent Goo Mix",
                           31: "Supersaturation", 32: "More Goo Canisters",
                           41: "Spillback Extension", 42: "Improved Spooling Mechanism",
                           51: "Protein Disruption Mix", 52: "Fluoroantimonic Acid", 53: "Ingredient X"}

#Driller Secondary Mods (Fist Number is tier, Second Number is the mod)

Driller_Sec_Sub_Mods = {11: "Improved Alignment	", 12: "High Capacity Magazine", 13: "Quickfire Ejector",
                        21: "Expanded Ammo Bags", 22: "Increased Caliber Rounds",
                        31: "Improved Propellant", 32: "Recoil Compensator", 33: "Expanded Ammo Bags",
                        41: "Hollow-Point Bullets", 42: "High Velocity Rounds",
                        51: "Volatile Bullets", 52: "Mactera Toxin-coating"}

Driller_Sec_EPC_Mods = {11: "Increased Particle Density", 12: "Larger Battery", 13: "Higher Charged Plasma Energy",
                        21: "Heat Shield", 22: "Overcharged Plasma Accelerator",
                        31: "Improved Charge Efficiency", 32: "Crystal Capacitors", 33: "Tweaked Radiator",
                        41: "Expanded Plasma Splash", 42: "High Density Battery", 43: "Reactive Shockwave",
                        51: "Flying Nightmare", 52: "Thin Containment Field", 53: "Plasma Burn"}

#Driller Support Equipment Mods (Fist Number is tier, Second Number is the mod)

Driller_Sup_Drill_Mods = {11: "Barbed Drills", 12: "Hardened Drill Tips", 13: "Expanded Fuel Tanks",
                          21: "Magnetic Refrigeration", 22: "Streamlined Integrity Check",
                          31: "Supercharged Motor",
                          41: "Increased Tank Pressure", 42: "Bloody Cold Drills"}

Driller_Sup_C4_Mods = {11: "Fragmentary Shell", 12: "Extra Satchel Charge", 13: "Bigger Charge",
                       21: "Kill Switch",
                       31: "Extra Satchel Charge", 32: "Volatile Compound",
                       41: "Big Bang", 42: "Concussive Blast", 43: "Rock Mover"}

Driller_Sup_Armor_Mods = {11: "Improved Generator", 12: "Boosted Converter", 13: "Bigger Mineral Bag",
                          21: "Overcharger", 22: "Healthy",
                          31: "Temperature Insulation",
                          41: "Shockwave", 42: "Static Discharge", 43: "Breathing Room"}

#Engineer Equipment

Engineer_Primaries = {1: '"Warthog" Auto 210', 2: '"Stubby" Voltaic SMG', 3: "LOK-1 Smart Rifle"}
Engineer_Secondary = {1: "Deepcore 40mm PGL", 2: "Breach Cutter"}
Engineer_Throwables = {1: "L.U.R.E.", 2: "Plasma Burster", 3: "Proximity Mine"}
Engineer_Equipment = ['Platform Gun', 'LMG Gun Platform', '"Owl" Armor Rig']

#Engineer Primary Mods (Fist Number is tier, Second Number is the mod)

Engineer_Pri_Warthog_Mods = {11: "Supercharged Feed Mechanism", 12: "Overstuffed Magazine",
                             21: "Expanded Ammo Bags", 22: "Loaded Shells", 23: "Choke",
                             31: "Recoil Dampener", 32: "Quickfire Ejector", 33: "High Capacity Magazine",
                             41: "Tungsten Coated Buckshot", 42: "Bigger Pellets",
                             51: "Turret Whip", 52: "Miner Adjustments"}

Engineer_Pri_Stubby_Mods = {11: "Increased Caliber Rounds", 12: "Upgraded Capacitors", 13: "Expanded Ammo Bags",
                            21: "High Capacity Magazine", 22: "Recoil Dampener", 23: "Improved Gas System",
                            31: "High Velocity Rounds", 32: "Expanded Ammo Bags",
                            41: "Hollow-Point Bullets", 42: "Conductive Bullets",
                            51: "Magazine Capacity Tweak", 52: "Electric Arc"}

Engineer_Pri_Loki_Mods = {11: "Increased Caliber Rounds", 12: "Expanded Ammo Bags",
                          21: "Macro Lens", 22: "CCD Array Add-On", 23: "Zoom Lens",
                          31: "Electro-Chemical Rounds", 32: "SMЯT Targeting Software™", 33: "Super Blowthrough Rounds",
                          41: "Shutter Speed Sensor", 42: "Aperture Extension",
                          51: "Electric Generator Mod", 52: "Unstable Lock Mechanism", 53: "Fear Frequency"}

#Engineer Secondary Mods (Fist Number is tier, Second Number is the mod)

Engineer_Sec_Deepcore_Mods = {11: "Fragmentary Shell", 12: "Extra Ammo", 13: "HE Compound",
                              21: "Expanded Ammo Bags", 22: "Larger Payload",
                              31: "Incendiary Compound", 32: "Pressure Wave", 33: "High Velocity Grenades",
                              41: "Homebrew Explosive", 42: "Nails + Tape", 43: "Concussive Blast",
                              51: "Proximity Trigger", 52: "Spiky Grenade", 53: "Disabled Inertia Inhibitor"}

Engineer_Sec_Cutter_Mods = {11: "Prolonged Power Generation", 12: "High Capacity Magazine",
                            21: "Expanded Ammo Bags", 22: "Condensed Plasma", 23: "Loosened Node Cohesion",
                            31: "Quick Deploy", 32: "Improved Case Ejector",
                            41: "Armor Breaking", 42: "Disruptive Frequency Tuning",
                            51: "Explosive Goodbye", 52: "Plasma Trail", 53: "Triple Split Line"}

#Engineer Support Equipment Mods (Fist Number is tier, Second Number is the mod)

Engineer_Sup_Platform_Mods = {11: "Supercharged Feed Mechanism", 12: "Expanded Ammo Bags", 13: "High Capacity Magazine",
                             21: "Plastcrete MKII",
                             31: "Expanded Ammo Bags", 32: "Repellant Additive", 33: "Disabled Inertia Inhibitor"}

Engineer_Sup_Turret_Mods = {11: "Gemini System", 12: "LMG MKII",
                           21: "Expanded Ammo Bags", 22: "Quick Deploy", 23: "Widemouth Refill Port",
                           31: "Hardened Rounds", 32: "Stun", 33: "Expanded Ammo Capacity",
                           41: "Defender System", 42: "Hawkeye System"}

Engineer_Sup_Armor_Mods = {11: "Improved Generator", 12: "Boosted Converter", 13: "Bigger Mineral Bag",
                           21: "Overcharger", 22: "Healthy",
                           31: "Hazmat System",
                           41: "Shockwave", 42: "Static Discharge", 43: "Breathing Room"}

#Gunner Equipment

Gunner_Primaries = {1: '"Lead Storm" Powered Minigun', 2: '"Thunderhead" Heavy Autocannon', 3: '"Hurricane" Guided Rocket System'}
Gunner_Secondary = {1: '"Bulldog" Heavy Revolver', 2: "BRT7 Burst Fire Gun"}
Gunner_Throwables = {1: "Sticky Grenade", 2: "Incendiary Grenade", 3: "Cluster Grenade"}
Gunner_Equipment = ['Zipline Launcher', 'Shield Generator', '"Barracuda" Armor Rig']

#Gunner Primary Mods (Fist Number is tier, Second Number is the mod)

Gunner_Pri_Leadstorm_Mods = {11: "Magnetic Refrigeration", 12: "Improved Motor", 13: "Improved Platform Stability",
                             21: "Oversized Drum", 22: "High Velocity Rounds",
                             31: "Hardened Rounds", 32: "Improved Stun", 33: "Blowthrough Rounds",
                             41: "Variable Chamber Pressure", 42: "Lighter Barrel Assembly", 43: "Magnetic Bearings",
                             51: "Aggressive Venting", 52: "Cold As The Grave", 53: "Hot Bullets"}

Gunner_Pri_Thunderhead_Mods = {11: "Increased Caliber Rounds", 12: "High Capacity Magazine", 13: "Expanded Ammo Bags",
                               21: "Tighter Barrel Alignment", 22: "Improved Gas System", 23: "Lighter Barrel Assembly",
                               31: "Supercharged Feed Mechanism", 32: "Loaded Rounds", 33: "High Velocity Rounds",
                               41: "Hardened Rounds", 42: "Shrapnel Rounds",
                               51: "Feedback Loop", 52: "Suppressive Fire", 53: "Damage Resistance At Full RoF"}

Gunner_Pri_Hurricane_Mods = {11: "Missile Belt", 12: "Pressurized Gas Cylinders", 13: "Increased Blast Radius",
                             21: "Bigger Jet Engine", 22: "Anti-Tank Missiles",
                             31: "Nano Missles", 32: "Improved Feed Mechanism",
                             41: "Shrapnel Load", 42: "Zip Fuel",
                             51: "Napalm-Infused Rounds", 52: "Uncontrolled Decompression", 53: "Nitroglycerin Rounds"}

#Gunner Secondary Mods (Fist Number is tier, Second Number is the mod)

Gunner_Sec_Bulldog_Mods = {11: "Quickfire Ejector", 12: "Perfect Weight Balance",
                           21: "Increased Caliber Rounds", 22: "Floating Barrel", 23: "Expanded Ammo Bags",
                           31: "Super Blowthrough Rounds", 32: "Explosive Rounds", 33: "Hollow-Point Bullets",
                           41: "Expanded Ammo Bags", 42: "High Velocity Rounds",
                           51: "Dead-Eye", 52: "Neurotoxin Coating"}

Gunner_Sec_Burst_Mods = {11: "High Velocity Rounds", 12: "Floating Barrel", 13: "Blowthrough Rounds",
                         21: "Recoil Dampener", 22: "Quickfire Ejector", 23: "Disabled Safety",
                         31: "High Capacity Magazine", 32: "Increased Caliber Rounds",
                         41: "Hardened Rounds", 42: "Expanded Ammo Bags", 43: "Hollow-Point Bullets",
                         51: "Burst Stun", 52: "Longer Burst"}

#Gunner Support Equipment Mods (Fist Number is tier, Second Number is the mod)

Gunner_Sup_Zipline_Mods = {11: "Expanded Ammo Bags", 12: "Upgraded Connection Joint", 13: "Reinforced Anchor",
                           21: "Reinforced Cable",
                           31: "Disconnection Protection", 32: "Increased Motor Traction"}

Gunner_Sup_Shield_Mods = {11: "Streamlined Integrity Check", 12: "Improved Projector",
                          21: "Fast Charging Capacitors", 22: "Larger Capacitors",
                          31: "Supercharged Coils", 32: "Lasting Effect", 33: "Improved Efficiency"}

Gunner_Sup_Armor_Mods = {11: "Improved Generator", 12: "Boosted Converter", 13: "Bigger Mineral Bag",
                         21: "Overcharger", 22: "Healthy",
                         31: "Reactive Armor",
                         41: "Shockwave", 42: "Static Discharge", 43: "Breathing Room"}

#Scout Equipment

Scout_Primaries = {1: 'Deepcore GK2', 2: 'M1000 Classic', 3: 'DRAK-25 Plasma Carbine'}
Scout_Secondary = {1: 'Jury-Rigged Boomstick', 2: "Zhukov NUK17"}
Scout_Throwables = {1: "Inhibitor-Field Generator", 2: "Cryo Grenade", 3: "Pheromone Canister"}
Scout_Equipment = ['Grappling Hook', 'Flare Gun', '"Fox" Armor Rig']

#Scout Primary Mods (Fist Number is tier, Second Number is the mod)

Scout_Pri_Deepcore_Mods = {11: "Gyro Stabilisation", 12: "Supercharged Feed Mechanism",
                           21: "Increased Caliber Rounds", 22: "Expanded Ammo Bags",
                           31: "Floating Barrel", 32: "Improved Propellant", 33: "High Capacity Magazine",
                           41: "Hollow-Point Bullets", 42: "Hardened Rounds", 43: "Improved Gas System",
                           51: "Battle Frenzy", 52: "Battle Cool", 53: "Stun"}

Scout_Pri_M1000_Mods = {11: "Expanded Ammo Bags", 12: "Increased Caliber Rounds",
                        21: "Fast-Charging Coils", 22: "Better Weight Balance", 23: "Hardened Rounds",
                        31: "Killer Focus", 32: "Extended Clip",
                        41: "Super Blowthrough Rounds", 42: "Hollow-Point Bullets",
                        51: "Hitting Where it Hurts", 52: "Precision Terror", 53: "Killing Machine"}

Scout_Pri_Carbine_Mods = {11: "High-Volume Plasma Field", 12: "Heat Shield", 13: "Stronger Plasma Accelerator",
                          21: "Larger Battery", 22: "Increased Caliber Rounds",
                          31: "Custom Coil Alignment", 32: "Gen 2 Cooling System", 33: "Hot Feet",
                          41: "Overcharged PCF", 42: "Plasma Splash", 43: "Destructive Resonance AMP",
                          51: "Manual Heat Dump", 52: "Thermal Feedback Loop"}

#Scout Secondary Mods (Fist Number is tier, Second Number is the mod)

Scout_Sec_Boomstick_Mods = {11: "Expanded Ammo Bags", 12: "Double-Sized Buckshot",
                            21: "Double Trigger", 22: "Quickfire Ejector",
                            31: "Improved Stun", 32: "Expanded Ammo Bags", 33: "High Capacity Shells",
                            41: "Super Blowthrough Rounds", 42: "Tungsten Coated Buckshot", 43: "Improved Blast Wave",
                            51: "Auto Reload", 52: "Fear The Boomstick", 53: "White Phosphorous Shells"}

Scout_Sec_Zhukov_Mods = {11: "Expanded Ammo Bags", 12: "High Velocity Rounds",
                         21: "High Capacity Magazine", 22: "Supercharged Feed Mechanism", 23: "Quickfire Ejector",
                         31: "Increased Caliber Rounds", 32: "Better Weight Balance",
                         41: "Blowthrough Rounds", 42: "Hollow-Point Bullets", 43: "Expanded Ammo Bags",
                         51: "Conductive Bullets", 52: "Get In, Get Out"}

#Scout Support Equipment Mods (Fist Number is tier, Second Number is the mod)

Scout_Sup_Hook_Mods = {11: "Improved Recharger", 12: "Longer Cable",
                       21: "Greater Cable Stretch",
                       31: "High Velocity Ejection System", 32: "Overcharged Winch",
                       41: "Safety First", 42: "Momentum", 43: "Bypassed Integrity Check"}

Scout_Sup_Flare_Mods = {11: "Expanded Ammo Bags", 12: "Thicker Core",
                        21: "Supercharged Feed Mechanism", 22: "High Capacity Magazine",
                        31: "Auto Reload", 32: "Expanded Ammo Bags", 33: "Magnesium Core"}

Scout_Sup_Armor_Mods = {11: "Improved Generator", 12: "Boosted Converter", 13: "Bigger Mineral Bag",
                        21: "Overcharger", 22: "Healthy",
                        31: "Shock Absorbers",
                        41: "Shockwave", 42: "Static Discharge", 43: "Breathing Room"}

#Perks

Active_Perks = ["Beast Master", "Berzerker", "Dash", "Field Medic", "Heightened Senses", "Hover Boots", "Iron Will", "See You In Hell", "Shield Link"]
Passive_Perks = ["Born Ready", "Deep Pockets", "Elemental Insulation", "Friendly", "It's a Bug Thing", "Resupplier", "Second Wind", "Strong Arm", "Sweet Tooth", "Thorns", "Unstoppable", "Vampire", "Veteran Depositor"]

#Randomizer Code

#Gathers input and sorts it alphabetically
print(f'{"-" * 94}\nInput the following classes you have all items unlocked on. (Driller, Engineer, Gunner, Scout)\n{" " * 19}!CASE SENSITIVE! Place ONLY Spaces inbetween each class.{" " * 19}\n{"-" * 94}')
print("Example: Driller Engineer Gunner Scout\n\n")
Intial_Input = input()

Player_Classes = Intial_Input.split()
Player_Classes.sort()
#Checks for any Errors in the list before continuing
Input_Loops = len(Player_Classes)
Input_Index = 0
Loop_Input = ""

while True:
    while Input_Loops > 0:
        if Input_Loops > 4: #Checks if there are too many values.
            print(f'\n\n{"-" * 77}\nERROR: Input has too many values, or not enough values! Enter in a new input.\n{"-" * 77}\n\n')
            Loop_Input = "E"
        elif Player_Classes[Input_Index] == "Driller" or Player_Classes[Input_Index] == "Engineer" or Player_Classes[Input_Index] == "Gunner" or Player_Classes[Input_Index] == "Scout": #Checks for Class strings
            Input_Index += 1
            Input_Loops -= 1
        else: # Responds to a string that isn't a class
            print(f'\n\n{"-" * 135}\nERROR: Input does not contain one of the following: Driller Engineer Gunner Scout. Or it is formatted improperly. Enter in a new input.\n{"-" * 135}\n\n')
            Loop_Input = "E"
            
        if Loop_Input == "E": #Allows the user to stay in a loop until they have an acceptable input
            print(f'{"-" * 94}\nInput the following classes you have all items unlocked on. (Driller, Engineer, Gunner, Scout)\n{" " * 20}!CASE SENSITIVE! Place ONLY Spaces inbetween each class.{" " * 20}\n{"-" * 94}')
            print("Example: Driller Engineer Gunner Scout\n\n")
            Intial_Input = input()
            Player_Classes = Intial_Input.split()
            Player_Classes.sort()
            Input_Loops = len(Player_Classes)
            Input_Index = 0
            Loop_Input = ""
    else:
        break

#Random Loadout Builder
Chosen_Class = random.choice(Player_Classes)


if Chosen_Class == "Driller": #Driller Class Builder
    
    #Selects a random number to pull from the primary weapon table.
    Primary_Weapon = random.randrange(1, 4)
    Primary_Weapon = Driller_Primaries[Primary_Weapon]

    
    #Selects a random number to pull from the secondary weapon table.
    Secondary_Weapon = random.randrange(1, 3)
    Secondary_Weapon = Driller_Secondary[Secondary_Weapon]
    
    #Selects a random number to pull from the throwable weapon table.
    Throwable = random.randrange(1, 4)
    Throwable = Driller_Throwables[Throwable]

    #Primary Weapons

    #CRSPR Flamethrower Mods
    if Primary_Weapon == "CRSPR Flamethrower":
        Pri_Mod_Tier_One = random.randrange(11, 13)
        Pri_Mod_Tier_One = Driller_Pri_Flame_Mods[Pri_Mod_Tier_One]
        Pri_Mod_Tier_Two = random.randrange(21, 24)
        Pri_Mod_Tier_Two = Driller_Pri_Flame_Mods[Pri_Mod_Tier_Two]
        Pri_Mod_Tier_Three = random.randrange(31, 34)
        Pri_Mod_Tier_Three = Driller_Pri_Flame_Mods[Pri_Mod_Tier_Three]
        Pri_Mod_Tier_Four = random.randrange(41, 44)
        Pri_Mod_Tier_Four = Driller_Pri_Flame_Mods[Pri_Mod_Tier_Four]
        Pri_Mod_Tier_Five = random.randrange(51, 53)
        Pri_Mod_Tier_Five = Driller_Pri_Flame_Mods[Pri_Mod_Tier_Five]

    #Cryo Cannon Mods
    if Primary_Weapon == "Cryo Cannon":
        Pri_Mod_Tier_One = random.randrange(11, 14)
        Pri_Mod_Tier_One = Driller_Pri_Cryo_Mods[Pri_Mod_Tier_One]
        Pri_Mod_Tier_Two = random.randrange(21, 24)
        Pri_Mod_Tier_Two = Driller_Pri_Cryo_Mods[Pri_Mod_Tier_Two]
        Pri_Mod_Tier_Three = random.randrange(31, 33)
        Pri_Mod_Tier_Three = Driller_Pri_Cryo_Mods[Pri_Mod_Tier_Three]
        Pri_Mod_Tier_Four = random.randrange(41, 44)
        Pri_Mod_Tier_Four = Driller_Pri_Cryo_Mods[Pri_Mod_Tier_Four]
        Pri_Mod_Tier_Five = random.randrange(51, 53)
        Pri_Mod_Tier_Five = Driller_Pri_Cryo_Mods[Pri_Mod_Tier_Five]
        

    #Corrosive Sludge Pump Mods
    if Primary_Weapon == "Corrosive Sludge Pump":
        Pri_Mod_Tier_One = random.randrange(11, 14)
        Pri_Mod_Tier_One = Driller_Pri_Sludge_Mods[Pri_Mod_Tier_One]
        Pri_Mod_Tier_Two = random.randrange(21, 24)
        Pri_Mod_Tier_Two = Driller_Pri_Sludge_Mods[Pri_Mod_Tier_Two]
        Pri_Mod_Tier_Three = random.randrange(31, 33)
        Pri_Mod_Tier_Three = Driller_Pri_Sludge_Mods[Pri_Mod_Tier_Three]
        Pri_Mod_Tier_Four = random.randrange(41, 43)
        Pri_Mod_Tier_Four = Driller_Pri_Sludge_Mods[Pri_Mod_Tier_Four]
        Pri_Mod_Tier_Five = random.randrange(51, 54)
        Pri_Mod_Tier_Five = Driller_Pri_Sludge_Mods[Pri_Mod_Tier_Five]

    #Overclock Selection for Primary
    OC_Max = int(input(f'\nInput how many Overclocks you have for the {Primary_Weapon}:\n'))
    if OC_Max == 0:
        OC_Min = 0
    elif OC_Max < 0:
        while True:
            print("ERROR: You cannot have negative over clocks.")
            OC_Max = int(input(f'\nInput how many Overclocks you have for the {Primary_Weapon}:\n'))
            if OC_Max > -1:
                break
    else:
        OC_Min = 1
        OC_Max += 1
    
    if OC_Max != 0:
        Pri_OC = random.randrange(OC_Min, OC_Max)
    else:
        Pri_OC = 0

    #Secondary Weapons

    #Subata 120 Mods
    if Secondary_Weapon == "Subata 120":
        Sec_Mod_Tier_One = random.randrange(11, 14)
        Sec_Mod_Tier_One = Driller_Sec_Sub_Mods[Sec_Mod_Tier_One]
        Sec_Mod_Tier_Two = random.randrange(21, 23)
        Sec_Mod_Tier_Two = Driller_Sec_Sub_Mods[Sec_Mod_Tier_Two]
        Sec_Mod_Tier_Three = random.randrange(31, 34)
        Sec_Mod_Tier_Three = Driller_Sec_Sub_Mods[Sec_Mod_Tier_Three]
        Sec_Mod_Tier_Four = random.randrange(41, 43)
        Sec_Mod_Tier_Four = Driller_Sec_Sub_Mods[Sec_Mod_Tier_Four]
        Sec_Mod_Tier_Five = random.randrange(51, 53)
        Sec_Mod_Tier_Five = Driller_Sec_Sub_Mods[Sec_Mod_Tier_Five]

    #Experimental Plasma Charger Mods
    if Secondary_Weapon == "Experimental Plasma Charger":
        Sec_Mod_Tier_One = random.randrange(11, 14)
        Sec_Mod_Tier_One = Driller_Sec_EPC_Mods[Sec_Mod_Tier_One]
        Sec_Mod_Tier_Two = random.randrange(21, 23)
        Sec_Mod_Tier_Two = Driller_Sec_EPC_Mods[Sec_Mod_Tier_Two]
        Sec_Mod_Tier_Three = random.randrange(31, 34)
        Sec_Mod_Tier_Three = Driller_Sec_EPC_Mods[Sec_Mod_Tier_Three]
        Sec_Mod_Tier_Four = random.randrange(41, 44)
        Sec_Mod_Tier_Four = Driller_Sec_EPC_Mods[Sec_Mod_Tier_Four]
        Sec_Mod_Tier_Five = random.randrange(51, 54)
        Sec_Mod_Tier_Five = Driller_Sec_EPC_Mods[Sec_Mod_Tier_Five]

    #Overclock Selection for Secondary
    OC_Max = int(input(f'\nInput how many Overclocks you have for the {Secondary_Weapon}:\n'))
    if OC_Max == 0:
        OC_Min = 0
    elif OC_Max < 0:
        while True:
            print("ERROR: You cannot have negative over clocks.")
            OC_Max = int(input(f'\nInput how many Overclocks you have for the {Secondary_Weapon}:\n'))
            if OC_Max > -1:
                break
    else:
        OC_Min = 1
        OC_Max += 1
    
    if OC_Max != 0:
        Sec_OC = random.randrange(OC_Min, OC_Max)
    else:
        Sec_OC = 0

    #Support Equipment

    #Reinforced Power Drills Mods
    Support_One = "Reinforced Power Drills"  
    Sup_One_Mod_Tier_One = random.randrange(11, 14)
    Sup_One_Mod_Tier_One = Driller_Sup_Drill_Mods[Sup_One_Mod_Tier_One]
    Sup_One_Mod_Tier_Two = random.randrange(21, 23)
    Sup_One_Mod_Tier_Two = Driller_Sup_Drill_Mods[Sup_One_Mod_Tier_Two]
    Sup_One_Mod_Tier_Three = Driller_Sup_Drill_Mods[31]
    Sup_One_Mod_Tier_Four = random.randrange(41, 43)
    Sup_One_Mod_Tier_Four = Driller_Sup_Drill_Mods[Sup_One_Mod_Tier_Four]

    #Satchel Charge Mods
    Support_Two = "Satchel Charge"
    Sup_Two_Mod_Tier_One = random.randrange(11, 14)
    Sup_Two_Mod_Tier_One = Driller_Sup_C4_Mods[Sup_Two_Mod_Tier_One]
    Sup_Two_Mod_Tier_Two = Driller_Sup_C4_Mods[21]
    Sup_Two_Mod_Tier_Three = random.randrange(31, 33)
    Sup_Two_Mod_Tier_Three = Driller_Sup_C4_Mods[Sup_Two_Mod_Tier_Three]
    Sup_Two_Mod_Tier_Four = random.randrange(41, 44)
    Sup_Two_Mod_Tier_Four = Driller_Sup_C4_Mods[Sup_Two_Mod_Tier_Four]

    #"Mole" Armor Rig Mods
    Armor = '"Mole" Armor Rig'
    Armor_Mod_Tier_One = random.randrange(11, 14)
    Armor_Mod_Tier_One = Driller_Sup_Armor_Mods[Armor_Mod_Tier_One]
    Armor_Mod_Tier_Two = random.randrange(21, 23)
    Armor_Mod_Tier_Two = Driller_Sup_Armor_Mods[Armor_Mod_Tier_Two]
    Armor_Mod_Tier_Three = Driller_Sup_Armor_Mods[31]
    Armor_Mod_Tier_Four = random.randrange(41, 44)
    Armor_Mod_Tier_Four = Driller_Sup_Armor_Mods[Armor_Mod_Tier_Four]


elif Chosen_Class == "Engineer": #Engineer Class Builder
    
    #Selects a random number to pull from the primary weapon table.
    Primary_Weapon = random.randrange(1, 4)
    Primary_Weapon = Engineer_Primaries[Primary_Weapon]

    
    #Selects a random number to pull from the secondary weapon table.
    Secondary_Weapon = random.randrange(1, 3)
    Secondary_Weapon = Engineer_Secondary[Secondary_Weapon]
    
    #Selects a random number to pull from the throwable weapon table.
    Throwable = random.randrange(1, 4)
    Throwable = Engineer_Throwables[Throwable]

    #Primary Weapons

    #"Warthog" Auto 210 Mods
    if Primary_Weapon == '"Warthog" Auto 210':
        Pri_Mod_Tier_One = random.randrange(11, 13)
        Pri_Mod_Tier_One = Engineer_Pri_Warthog_Mods[Pri_Mod_Tier_One]
        Pri_Mod_Tier_Two = random.randrange(21, 24)
        Pri_Mod_Tier_Two = Engineer_Pri_Warthog_Mods[Pri_Mod_Tier_Two]
        Pri_Mod_Tier_Three = random.randrange(31, 34)
        Pri_Mod_Tier_Three = Engineer_Pri_Warthog_Mods[Pri_Mod_Tier_Three]
        Pri_Mod_Tier_Four = random.randrange(41, 43)
        Pri_Mod_Tier_Four = Engineer_Pri_Warthog_Mods[Pri_Mod_Tier_Four]
        Pri_Mod_Tier_Five = random.randrange(51, 53)
        Pri_Mod_Tier_Five = Engineer_Pri_Warthog_Mods[Pri_Mod_Tier_Five]

    #"Stubby" Voltaic SMG Mods
    if Primary_Weapon == '"Stubby" Voltaic SMG':
        Pri_Mod_Tier_One = random.randrange(11, 14)
        Pri_Mod_Tier_One = Engineer_Pri_Stubby_Mods[Pri_Mod_Tier_One]
        Pri_Mod_Tier_Two = random.randrange(21, 24)
        Pri_Mod_Tier_Two = Engineer_Pri_Stubby_Mods[Pri_Mod_Tier_Two]
        Pri_Mod_Tier_Three = random.randrange(31, 33)
        Pri_Mod_Tier_Three = Engineer_Pri_Stubby_Mods[Pri_Mod_Tier_Three]
        Pri_Mod_Tier_Four = random.randrange(41, 43)
        Pri_Mod_Tier_Four = Engineer_Pri_Stubby_Mods[Pri_Mod_Tier_Four]
        Pri_Mod_Tier_Five = random.randrange(51, 53)
        Pri_Mod_Tier_Five = Engineer_Pri_Stubby_Mods[Pri_Mod_Tier_Five]
        

    #LOK-1 Smart Rifle Pump Mods
    if Primary_Weapon == "LOK-1 Smart Rifle":
        Pri_Mod_Tier_One = random.randrange(11, 13)
        Pri_Mod_Tier_One = Engineer_Pri_Loki_Mods[Pri_Mod_Tier_One]
        Pri_Mod_Tier_Two = random.randrange(21, 24)
        Pri_Mod_Tier_Two = Engineer_Pri_Loki_Mods[Pri_Mod_Tier_Two]
        Pri_Mod_Tier_Three = random.randrange(31, 34)
        Pri_Mod_Tier_Three = Engineer_Pri_Loki_Mods[Pri_Mod_Tier_Three]
        Pri_Mod_Tier_Four = random.randrange(41, 43)
        Pri_Mod_Tier_Four = Engineer_Pri_Loki_Mods[Pri_Mod_Tier_Four]
        Pri_Mod_Tier_Five = random.randrange(51, 54)
        Pri_Mod_Tier_Five = Engineer_Pri_Loki_Mods[Pri_Mod_Tier_Five]

    #Overclock Selection for Primary
    OC_Max = int(input(f'\nInput how many Overclocks you have for the {Primary_Weapon}:\n'))
    if OC_Max == 0:
        OC_Min = 0
    elif OC_Max < 0:
        while True:
            print("ERROR: You cannot have negative over clocks.")
            OC_Max = int(input(f'\nInput how many Overclocks you have for the {Primary_Weapon}:\n'))
            if OC_Max > -1:
                break
    else:
        OC_Min = 1
        OC_Max += 1
    
    if OC_Max != 0:
        Pri_OC = random.randrange(OC_Min, OC_Max)
    else:
        Pri_OC = 0

    #Secondary Weapons

    #Deepcore 40mm PGL Mods
    if Secondary_Weapon == "Deepcore 40mm PGL":
        Sec_Mod_Tier_One = random.randrange(11, 14)
        Sec_Mod_Tier_One = Engineer_Sec_Deepcore_Mods[Sec_Mod_Tier_One]
        Sec_Mod_Tier_Two = random.randrange(21, 23)
        Sec_Mod_Tier_Two = Engineer_Sec_Deepcore_Mods[Sec_Mod_Tier_Two]
        Sec_Mod_Tier_Three = random.randrange(31, 34)
        Sec_Mod_Tier_Three = Engineer_Sec_Deepcore_Mods[Sec_Mod_Tier_Three]
        Sec_Mod_Tier_Four = random.randrange(41, 44)
        Sec_Mod_Tier_Four = Engineer_Sec_Deepcore_Mods[Sec_Mod_Tier_Four]
        Sec_Mod_Tier_Five = random.randrange(51, 54)
        Sec_Mod_Tier_Five = Engineer_Sec_Deepcore_Mods[Sec_Mod_Tier_Five]

    #Breach Cutter Mods
    if Secondary_Weapon == "Breach Cutter":
        Sec_Mod_Tier_One = random.randrange(11, 13)
        Sec_Mod_Tier_One = Engineer_Sec_Cutter_Mods[Sec_Mod_Tier_One]
        Sec_Mod_Tier_Two = random.randrange(21, 24)
        Sec_Mod_Tier_Two = Engineer_Sec_Cutter_Mods[Sec_Mod_Tier_Two]
        Sec_Mod_Tier_Three = random.randrange(31, 33)
        Sec_Mod_Tier_Three = Engineer_Sec_Cutter_Mods[Sec_Mod_Tier_Three]
        Sec_Mod_Tier_Four = random.randrange(41, 43)
        Sec_Mod_Tier_Four = Engineer_Sec_Cutter_Mods[Sec_Mod_Tier_Four]
        Sec_Mod_Tier_Five = random.randrange(51, 54)
        Sec_Mod_Tier_Five = Engineer_Sec_Cutter_Mods[Sec_Mod_Tier_Five]

    #Overclock Selection for Secondary
    OC_Max = int(input(f'\nInput how many Overclocks you have for the {Secondary_Weapon}:\n'))
    if OC_Max == 0:
        OC_Min = 0
    elif OC_Max < 0:
        while True:
            print("ERROR: You cannot have negative over clocks.")
            OC_Max = int(input(f'\nInput how many Overclocks you have for the {Secondary_Weapon}:\n'))
            if OC_Max > -1:
                break
    else:
        OC_Min = 1
        OC_Max += 1
    
    if OC_Max != 0:
        Sec_OC = random.randrange(OC_Min, OC_Max)
    else:
        Sec_OC = 0

    #Support Equipment

    #Platform Gun Mods
    Support_One = "Platform Gun"  
    Sup_One_Mod_Tier_One = random.randrange(11, 14)
    Sup_One_Mod_Tier_One = Engineer_Sup_Platform_Mods[Sup_One_Mod_Tier_One]
    Sup_One_Mod_Tier_Two = Engineer_Sup_Platform_Mods[21]
    Sup_One_Mod_Tier_Three = random.randrange(31, 34)
    Sup_One_Mod_Tier_Three = Engineer_Sup_Platform_Mods[Sup_One_Mod_Tier_Three]

    #LMG Gun Platform Mods
    Support_Two = "LMG Gun Platform"
    Sup_Two_Mod_Tier_One = random.randrange(11, 13)
    Sup_Two_Mod_Tier_One = Engineer_Sup_Turret_Mods[Sup_Two_Mod_Tier_One]
    Sup_Two_Mod_Tier_Two = random.randrange(21, 24)
    Sup_Two_Mod_Tier_Two = Engineer_Sup_Turret_Mods[Sup_Two_Mod_Tier_Two]
    Sup_Two_Mod_Tier_Three = random.randrange(31, 34)
    Sup_Two_Mod_Tier_Three = Engineer_Sup_Turret_Mods[Sup_Two_Mod_Tier_Three]
    Sup_Two_Mod_Tier_Four = random.randrange(41, 43)
    Sup_Two_Mod_Tier_Four = Engineer_Sup_Turret_Mods[Sup_Two_Mod_Tier_Four]

    #"Owl" Armor Rig Mods
    Armor = '"Owl" Armor Rig'
    Armor_Mod_Tier_One = random.randrange(11, 14)
    Armor_Mod_Tier_One = Engineer_Sup_Armor_Mods[Armor_Mod_Tier_One]
    Armor_Mod_Tier_Two = random.randrange(21, 23)
    Armor_Mod_Tier_Two = Engineer_Sup_Armor_Mods[Armor_Mod_Tier_Two]
    Armor_Mod_Tier_Three = Engineer_Sup_Armor_Mods[31]
    Armor_Mod_Tier_Four = random.randrange(41, 44)
    Armor_Mod_Tier_Four = Engineer_Sup_Armor_Mods[Armor_Mod_Tier_Four]

elif Chosen_Class == "Gunner": #Gunner Class Builder
    
    #Selects a random number to pull from the primary weapon table.
    Primary_Weapon = random.randrange(1, 4)
    Primary_Weapon = Gunner_Primaries[Primary_Weapon]

    
    #Selects a random number to pull from the secondary weapon table.
    Secondary_Weapon = random.randrange(1, 3)
    Secondary_Weapon = Gunner_Secondary[Secondary_Weapon]
    
    #Selects a random number to pull from the throwable weapon table.
    Throwable = random.randrange(1, 4)
    Throwable = Gunner_Throwables[Throwable]

    #Primary Weapons

    #"Lead Storm" Powered Minigun Mods
    if Primary_Weapon == '"Lead Storm" Powered Minigun':
        Pri_Mod_Tier_One = random.randrange(11, 14)
        Pri_Mod_Tier_One = Gunner_Pri_Leadstorm_Mods[Pri_Mod_Tier_One]
        Pri_Mod_Tier_Two = random.randrange(21, 23)
        Pri_Mod_Tier_Two = Gunner_Pri_Leadstorm_Mods[Pri_Mod_Tier_Two]
        Pri_Mod_Tier_Three = random.randrange(31, 34)
        Pri_Mod_Tier_Three = Gunner_Pri_Leadstorm_Mods[Pri_Mod_Tier_Three]
        Pri_Mod_Tier_Four = random.randrange(41, 44)
        Pri_Mod_Tier_Four = Gunner_Pri_Leadstorm_Mods[Pri_Mod_Tier_Four]
        Pri_Mod_Tier_Five = random.randrange(51, 54)
        Pri_Mod_Tier_Five = Gunner_Pri_Leadstorm_Mods[Pri_Mod_Tier_Five]

    #"Thunderhead" Heavy Autocannon Mods
    if Primary_Weapon == '"Thunderhead" Heavy Autocannon':
        Pri_Mod_Tier_One = random.randrange(11, 14)
        Pri_Mod_Tier_One = Gunner_Pri_Thunderhead_Mods[Pri_Mod_Tier_One]
        Pri_Mod_Tier_Two = random.randrange(21, 24)
        Pri_Mod_Tier_Two = Gunner_Pri_Thunderhead_Mods[Pri_Mod_Tier_Two]
        Pri_Mod_Tier_Three = random.randrange(31, 34)
        Pri_Mod_Tier_Three = Gunner_Pri_Thunderhead_Mods[Pri_Mod_Tier_Three]
        Pri_Mod_Tier_Four = random.randrange(41, 43)
        Pri_Mod_Tier_Four = Gunner_Pri_Thunderhead_Mods[Pri_Mod_Tier_Four]
        Pri_Mod_Tier_Five = random.randrange(51, 53)
        Pri_Mod_Tier_Five = Gunner_Pri_Thunderhead_Mods[Pri_Mod_Tier_Five]
        

    #"Hurricane" Guided Rocket System Mods
    if Primary_Weapon == '"Hurricane" Guided Rocket System':
        Pri_Mod_Tier_One = random.randrange(11, 14)
        Pri_Mod_Tier_One = Gunner_Pri_Hurricane_Mods[Pri_Mod_Tier_One]
        Pri_Mod_Tier_Two = random.randrange(21, 23)
        Pri_Mod_Tier_Two = Gunner_Pri_Hurricane_Mods[Pri_Mod_Tier_Two]
        Pri_Mod_Tier_Three = random.randrange(31, 33)
        Pri_Mod_Tier_Three = Gunner_Pri_Hurricane_Mods[Pri_Mod_Tier_Three]
        Pri_Mod_Tier_Four = random.randrange(41, 43)
        Pri_Mod_Tier_Four = Gunner_Pri_Hurricane_Mods[Pri_Mod_Tier_Four]
        Pri_Mod_Tier_Five = random.randrange(51, 54)
        Pri_Mod_Tier_Five = Gunner_Pri_Hurricane_Mods[Pri_Mod_Tier_Five]

    #Overclock Selection for Primary
    OC_Max = int(input(f'\nInput how many Overclocks you have for the {Primary_Weapon}:\n'))
    if OC_Max == 0:
        OC_Min = 0
    elif OC_Max < 0:
        while True:
            print("ERROR: You cannot have negative over clocks.")
            OC_Max = int(input(f'\nInput how many Overclocks you have for the {Primary_Weapon}:\n'))
            if OC_Max > -1:
                break
    else:
        OC_Min = 1
        OC_Max += 1
    
    if OC_Max != 0:
        Pri_OC = random.randrange(OC_Min, OC_Max)
    else:
        Pri_OC = 0

    #Secondary Weapons

    #"Bulldog" Heavy Revolver Mods
    if Secondary_Weapon == '"Bulldog" Heavy Revolver':
        Sec_Mod_Tier_One = random.randrange(11, 13)
        Sec_Mod_Tier_One = Gunner_Sec_Bulldog_Mods[Sec_Mod_Tier_One]
        Sec_Mod_Tier_Two = random.randrange(21, 24)
        Sec_Mod_Tier_Two = Gunner_Sec_Bulldog_Mods[Sec_Mod_Tier_Two]
        Sec_Mod_Tier_Three = random.randrange(31, 34)
        Sec_Mod_Tier_Three = Gunner_Sec_Bulldog_Mods[Sec_Mod_Tier_Three]
        Sec_Mod_Tier_Four = random.randrange(41, 43)
        Sec_Mod_Tier_Four = Gunner_Sec_Bulldog_Mods[Sec_Mod_Tier_Four]
        Sec_Mod_Tier_Five = random.randrange(51, 53)
        Sec_Mod_Tier_Five = Gunner_Sec_Bulldog_Mods[Sec_Mod_Tier_Five]

    #BRT7 Burst Fire Gun Mods
    if Secondary_Weapon == "BRT7 Burst Fire Gun":
        Sec_Mod_Tier_One = random.randrange(11, 14)
        Sec_Mod_Tier_One = Gunner_Sec_Burst_Mods[Sec_Mod_Tier_One]
        Sec_Mod_Tier_Two = random.randrange(21, 24)
        Sec_Mod_Tier_Two = Gunner_Sec_Burst_Mods[Sec_Mod_Tier_Two]
        Sec_Mod_Tier_Three = random.randrange(31, 33)
        Sec_Mod_Tier_Three = Gunner_Sec_Burst_Mods[Sec_Mod_Tier_Three]
        Sec_Mod_Tier_Four = random.randrange(41, 44)
        Sec_Mod_Tier_Four = Gunner_Sec_Burst_Mods[Sec_Mod_Tier_Four]
        Sec_Mod_Tier_Five = random.randrange(51, 53)
        Sec_Mod_Tier_Five = Gunner_Sec_Burst_Mods[Sec_Mod_Tier_Five]

    #Overclock Selection for Secondary
    OC_Max = int(input(f'\nInput how many Overclocks you have for the {Secondary_Weapon}:\n'))
    if OC_Max == 0:
        OC_Min = 0
    elif OC_Max < 0:
        while True:
            print("ERROR: You cannot have negative over clocks.")
            OC_Max = int(input(f'\nInput how many Overclocks you have for the {Secondary_Weapon}:\n'))
            if OC_Max > -1:
                break
    else:
        OC_Min = 1
        OC_Max += 1
    
    if OC_Max != 0:
        Sec_OC = random.randrange(OC_Min, OC_Max)
    else:
        Sec_OC = 0

    #Support Equipment

    #Zipline Launcher Drills Mods
    Support_One = 'Zipline Launcher'  
    Sup_One_Mod_Tier_One = random.randrange(11, 14)
    Sup_One_Mod_Tier_One = Gunner_Sup_Zipline_Mods[Sup_One_Mod_Tier_One]
    Sup_One_Mod_Tier_Two = Gunner_Sup_Zipline_Mods[21]
    Sup_One_Mod_Tier_Three = random.randrange(31, 33)
    Sup_One_Mod_Tier_Three = Gunner_Sup_Zipline_Mods[Sup_One_Mod_Tier_Three]


    #Shield Generator Mods
    Support_Two = "Shield Generator"
    Sup_Two_Mod_Tier_One = random.randrange(11, 13)
    Sup_Two_Mod_Tier_One = Gunner_Sup_Shield_Mods[Sup_Two_Mod_Tier_One]
    Sup_Two_Mod_Tier_Two = random.randrange(21, 23)
    Sup_Two_Mod_Tier_Two = Gunner_Sup_Shield_Mods[Sup_Two_Mod_Tier_Two]
    Sup_Two_Mod_Tier_Three = random.randrange(31, 34)
    Sup_Two_Mod_Tier_Three = Gunner_Sup_Shield_Mods[Sup_Two_Mod_Tier_Three]

    #"Barracuda" Armor Rig
    Armor = '"Barracuda" Armor Rig'
    Armor_Mod_Tier_One = random.randrange(11, 14)
    Armor_Mod_Tier_One = Gunner_Sup_Armor_Mods[Armor_Mod_Tier_One]
    Armor_Mod_Tier_Two = random.randrange(21, 23)
    Armor_Mod_Tier_Two = Gunner_Sup_Armor_Mods[Armor_Mod_Tier_Two]
    Armor_Mod_Tier_Three = Gunner_Sup_Armor_Mods[31]
    Armor_Mod_Tier_Four = random.randrange(41, 44)
    Armor_Mod_Tier_Four = Gunner_Sup_Armor_Mods[Armor_Mod_Tier_Four]

elif Chosen_Class == "Scout": #Scout Class Builder
    
    #Selects a random number to pull from the primary weapon table.
    Primary_Weapon = random.randrange(1, 4)
    Primary_Weapon = Scout_Primaries[Primary_Weapon]

    
    #Selects a random number to pull from the secondary weapon table.
    Secondary_Weapon = random.randrange(1, 3)
    Secondary_Weapon = Scout_Secondary[Secondary_Weapon]
    
    #Selects a random number to pull from the throwable weapon table.
    Throwable = random.randrange(1, 4)
    Throwable = Scout_Throwables[Throwable]

    #Primary Weapons

    #Deepcore GK2 Mods
    if Primary_Weapon == "Deepcore GK2":
        Pri_Mod_Tier_One = random.randrange(11, 13)
        Pri_Mod_Tier_One = Scout_Pri_Deepcore_Mods[Pri_Mod_Tier_One]
        Pri_Mod_Tier_Two = random.randrange(21, 23)
        Pri_Mod_Tier_Two = Scout_Pri_Deepcore_Mods[Pri_Mod_Tier_Two]
        Pri_Mod_Tier_Three = random.randrange(31, 34)
        Pri_Mod_Tier_Three = Scout_Pri_Deepcore_Mods[Pri_Mod_Tier_Three]
        Pri_Mod_Tier_Four = random.randrange(41, 44)
        Pri_Mod_Tier_Four = Scout_Pri_Deepcore_Mods[Pri_Mod_Tier_Four]
        Pri_Mod_Tier_Five = random.randrange(51, 54)
        Pri_Mod_Tier_Five = Scout_Pri_Deepcore_Mods[Pri_Mod_Tier_Five]

    #M1000 Classic Mods
    if Primary_Weapon == "M1000 Classic":
        Pri_Mod_Tier_One = random.randrange(11, 13)
        Pri_Mod_Tier_One = Scout_Pri_M1000_Mods[Pri_Mod_Tier_One]
        Pri_Mod_Tier_Two = random.randrange(21, 24)
        Pri_Mod_Tier_Two = Scout_Pri_M1000_Mods[Pri_Mod_Tier_Two]
        Pri_Mod_Tier_Three = random.randrange(31, 33)
        Pri_Mod_Tier_Three = Scout_Pri_M1000_Mods[Pri_Mod_Tier_Three]
        Pri_Mod_Tier_Four = random.randrange(41, 43)
        Pri_Mod_Tier_Four = Scout_Pri_M1000_Mods[Pri_Mod_Tier_Four]
        Pri_Mod_Tier_Five = random.randrange(51, 54)
        Pri_Mod_Tier_Five = Scout_Pri_M1000_Mods[Pri_Mod_Tier_Five]
        

    #DRAK-25 Plasma Carbine Pump Mods
    if Primary_Weapon == "DRAK-25 Plasma Carbine":
        Pri_Mod_Tier_One = random.randrange(11, 14)
        Pri_Mod_Tier_One = Scout_Pri_Carbine_Mods[Pri_Mod_Tier_One]
        Pri_Mod_Tier_Two = random.randrange(21, 23)
        Pri_Mod_Tier_Two = Scout_Pri_Carbine_Mods[Pri_Mod_Tier_Two]
        Pri_Mod_Tier_Three = random.randrange(31, 34)
        Pri_Mod_Tier_Three = Scout_Pri_Carbine_Mods[Pri_Mod_Tier_Three]
        Pri_Mod_Tier_Four = random.randrange(41, 44)
        Pri_Mod_Tier_Four = Scout_Pri_Carbine_Mods[Pri_Mod_Tier_Four]
        Pri_Mod_Tier_Five = random.randrange(51, 53)
        Pri_Mod_Tier_Five = Scout_Pri_Carbine_Mods[Pri_Mod_Tier_Five]

    #Overclock Selection for Primary
    OC_Max = int(input(f'\nInput how many Overclocks you have for the {Primary_Weapon}:\n'))
    if OC_Max == 0:
        OC_Min = 0
    elif OC_Max < 0:
        while True:
            print("ERROR: You cannot have negative over clocks.")
            OC_Max = int(input(f'\nInput how many Overclocks you have for the {Primary_Weapon}:\n'))
            if OC_Max > -1:
                break
    else:
        OC_Min = 1
        OC_Max += 1
    
    if OC_Max != 0:
        Pri_OC = random.randrange(OC_Min, OC_Max)
    else:
        Pri_OC = 0

    #Secondary Weapons

    #Jury-Rigged Boomstick Mods
    if Secondary_Weapon == "Jury-Rigged Boomstick":
        Sec_Mod_Tier_One = random.randrange(11, 13)
        Sec_Mod_Tier_One = Scout_Sec_Boomstick_Mods[Sec_Mod_Tier_One]
        Sec_Mod_Tier_Two = random.randrange(21, 23)
        Sec_Mod_Tier_Two = Scout_Sec_Boomstick_Mods[Sec_Mod_Tier_Two]
        Sec_Mod_Tier_Three = random.randrange(31, 34)
        Sec_Mod_Tier_Three = Scout_Sec_Boomstick_Mods[Sec_Mod_Tier_Three]
        Sec_Mod_Tier_Four = random.randrange(41, 44)
        Sec_Mod_Tier_Four = Scout_Sec_Boomstick_Mods[Sec_Mod_Tier_Four]
        Sec_Mod_Tier_Five = random.randrange(51, 54)
        Sec_Mod_Tier_Five = Scout_Sec_Boomstick_Mods[Sec_Mod_Tier_Five]

    #Zhukov NUK17 Mods
    if Secondary_Weapon == "Zhukov NUK17":
        Sec_Mod_Tier_One = random.randrange(11, 13)
        Sec_Mod_Tier_One = Scout_Sec_Zhukov_Mods[Sec_Mod_Tier_One]
        Sec_Mod_Tier_Two = random.randrange(21, 24)
        Sec_Mod_Tier_Two = Scout_Sec_Zhukov_Mods[Sec_Mod_Tier_Two]
        Sec_Mod_Tier_Three = random.randrange(31, 33)
        Sec_Mod_Tier_Three = Scout_Sec_Zhukov_Mods[Sec_Mod_Tier_Three]
        Sec_Mod_Tier_Four = random.randrange(41, 44)
        Sec_Mod_Tier_Four = Scout_Sec_Zhukov_Mods[Sec_Mod_Tier_Four]
        Sec_Mod_Tier_Five = random.randrange(51, 53)
        Sec_Mod_Tier_Five = Scout_Sec_Zhukov_Mods[Sec_Mod_Tier_Five]

    #Overclock Selection for Secondary
    OC_Max = int(input(f'\nInput how many Overclocks you have for the {Secondary_Weapon}:\n'))
    if OC_Max == 0:
        OC_Min = 0
    elif OC_Max < 0:
        while True:
            print("ERROR: You cannot have negative over clocks.")
            OC_Max = int(input(f'\nInput how many Overclocks you have for the {Secondary_Weapon}:\n'))
            if OC_Max > -1:
                break
    else:
        OC_Min = 1
        OC_Max += 1
    
    if OC_Max != 0:
        Sec_OC = random.randrange(OC_Min, OC_Max)
    else:
        Sec_OC = 0

    #Support Equipment

    #Grappling Hook Mods
    Support_One = "Grappling Hook"  
    Sup_One_Mod_Tier_One = random.randrange(11, 13)
    Sup_One_Mod_Tier_One = Scout_Sup_Hook_Mods[Sup_One_Mod_Tier_One]
    Sup_One_Mod_Tier_Two = Scout_Sup_Hook_Mods[21]
    Sup_One_Mod_Tier_Three = random.randrange(31, 33)
    Sup_One_Mod_Tier_Three = Scout_Sup_Hook_Mods[Sup_One_Mod_Tier_Three]
    Sup_One_Mod_Tier_Four = random.randrange(41, 44)
    Sup_One_Mod_Tier_Four = Scout_Sup_Hook_Mods[Sup_One_Mod_Tier_Four]

    #Flare Gun Mods
    Support_Two = "Flare Gun"
    Sup_Two_Mod_Tier_One = random.randrange(11, 13)
    Sup_Two_Mod_Tier_One = Scout_Sup_Flare_Mods[Sup_Two_Mod_Tier_One]
    Sup_Two_Mod_Tier_Two = random.randrange(21, 23)
    Sup_Two_Mod_Tier_Two = Scout_Sup_Flare_Mods[Sup_Two_Mod_Tier_Two]
    Sup_Two_Mod_Tier_Three = random.randrange(31, 34)
    Sup_Two_Mod_Tier_Three = Scout_Sup_Flare_Mods[Sup_Two_Mod_Tier_Three]

    #"Fox" Armor RigMods
    Armor = '"Fox" Armor Rig'
    Armor_Mod_Tier_One = random.randrange(11, 14)
    Armor_Mod_Tier_One = Scout_Sup_Armor_Mods[Armor_Mod_Tier_One]
    Armor_Mod_Tier_Two = random.randrange(21, 23)
    Armor_Mod_Tier_Two = Scout_Sup_Armor_Mods[Armor_Mod_Tier_Two]
    Armor_Mod_Tier_Three = Scout_Sup_Armor_Mods[31]
    Armor_Mod_Tier_Four = random.randrange(41, 44)
    Armor_Mod_Tier_Four = Scout_Sup_Armor_Mods[Armor_Mod_Tier_Four]



#Perk Selection

Active_Perk_One = random.choice(Active_Perks)
Active_Perk_Two = random.choice(Active_Perks)

while Active_Perk_One == Active_Perk_Two:
    Active_Perk_Two = random.choice(Active_Perks)

Passive_Perk_One = random.choice(Passive_Perks)
Passive_Perk_Two = random.choice(Passive_Perks)
Passive_Perk_Three = random.choice(Passive_Perks)

while Passive_Perk_One == Passive_Perk_Two or Passive_Perk_One == Passive_Perk_Three:
    Passive_Perk_One = random.choice(Passive_Perks)

while Passive_Perk_Two == Passive_Perk_One or Passive_Perk_Two == Passive_Perk_Three:
    Passive_Perk_Two = random.choice(Passive_Perks)

while Passive_Perk_Three == Passive_Perk_Two or Passive_Perk_Three == Passive_Perk_One:
    Passive_Perk_Three = random.choice(Passive_Perks)

#Final Print Statement
print("\n" * 30)
print(f'{"-" * 25}\nYour Randomized DRG Build\n{"-" * 25}\n')
print(f'Class: {Chosen_Class}\n')
print(f'Primary Weapon: {Primary_Weapon}\n{" " * 16}Tier 1 Mod: {Pri_Mod_Tier_One}\n{" " * 16}Tier 2 Mod: {Pri_Mod_Tier_Two}\n{" " * 16}Tier 3 Mod: {Pri_Mod_Tier_Three}\n{" " * 16}Tier 4 Mod: {Pri_Mod_Tier_Four}\n{" " * 16}Tier 5 Mod: {Pri_Mod_Tier_Five}')

#Only prints Overclock selection if it selected an overclock to begin with.
if Pri_OC != 0:
    print(f'{" " * 16}Use Overclock {Pri_OC}\n')
else:
    print("")

print(f'Secondary Weapon: {Secondary_Weapon}\n{" " * 18}Tier 1 Mod: {Sec_Mod_Tier_One}\n{" " * 18}Tier 2 Mod: {Sec_Mod_Tier_Two}\n{" " * 18}Tier 3 Mod: {Sec_Mod_Tier_Three}\n{" " * 18}Tier 4 Mod: {Sec_Mod_Tier_Four}\n{" " * 18}Tier 5 Mod: {Sec_Mod_Tier_Five}')

#Only prints Overclock selection if it selected an overclock to begin with.
if Sec_OC != 0:
    print(f'{" " * 18}Use Overclock {Sec_OC}\n')
else:
    print("")

print(f'Throwable: {Throwable}\n')
print("Support Items:\n")

#Classes have a different amount of tiers for their support items.
if Chosen_Class != "Engineer" and Chosen_Class != "Gunner":
    print(f'Support Tool 1: {Support_One}\n{" " * 16}Tier 1 Mod: {Sup_One_Mod_Tier_One}\n{" " * 16}Tier 2 Mod: {Sup_One_Mod_Tier_Two}\n{" " * 16}Tier 3 Mod: {Sup_One_Mod_Tier_Three}\n{" " * 16}Tier 4 Mod: {Sup_One_Mod_Tier_Four}\n')
else:
    print(f'Support Tool 1: {Support_One}\n{" " * 16}Tier 1 Mod: {Sup_One_Mod_Tier_One}\n{" " * 16}Tier 2 Mod: {Sup_One_Mod_Tier_Two}\n{" " * 16}Tier 3 Mod: {Sup_One_Mod_Tier_Three}\n')
if Chosen_Class != "Gunner" and Chosen_Class != "Scout":
    print(f'Support Tool 2: {Support_Two}\n{" " * 16}Tier 1 Mod: {Sup_Two_Mod_Tier_One}\n{" " * 16}Tier 2 Mod: {Sup_Two_Mod_Tier_Two}\n{" " * 16}Tier 3 Mod: {Sup_Two_Mod_Tier_Three}\n{" " * 16}Tier 4 Mod: {Sup_Two_Mod_Tier_Four}\n')
else:
    print(f'Support Tool 2: {Support_Two}\n{" " * 16}Tier 1 Mod: {Sup_Two_Mod_Tier_One}\n{" " * 16}Tier 2 Mod: {Sup_Two_Mod_Tier_Two}\n{" " * 16}Tier 3 Mod: {Sup_Two_Mod_Tier_Three}\n')

print(f'Armor: {Armor}\n{" " * 7}Tier 1 Mod: {Armor_Mod_Tier_One}\n{" " * 7}Tier 2 Mod: {Armor_Mod_Tier_Two}\n{" " * 7}Tier 3 Mod: {Armor_Mod_Tier_Three}\n{" " * 7}Tier 4 Mod: {Armor_Mod_Tier_Four}\n')
print("Active Perks:\n")
print(f'{Active_Perk_One}\n{Active_Perk_Two}\n')
print("Passive Perks:\n")
print(f'{Passive_Perk_One}\n{Passive_Perk_Two}\n{Passive_Perk_Three}')
