from typing import ClassVar

from connection_data import area_doors_unpackable
from door_logic import canOpen
from item_data import items_unpackable
from loadout import Loadout
from logicInterface import AreaLogicType, LocationLogicType, LogicInterface
from logic_shortcut import LogicShortcut

# TODO: There are a bunch of places where where Expert logic needed energy tanks even if they had Varia suit.
# Need to make sure everything is right in those places.
# (They will probably work right when they're combined like this,
#  but they wouldn't have worked right when casual was separated from expert.)

# TODO: There are also a bunch of places where casual used icePod, where expert only used Ice. Is that right?

(
    CraterR, SunkenNestL, RuinedConcourseBL, RuinedConcourseTR, CausewayR,
    SporeFieldTR, SporeFieldBR, OceanShoreR, EleToTurbidPassageR, PileAnchorL,
    ExcavationSiteL, WestCorridorR, FoyerR, ConstructionSiteL, AlluringCenoteR,
    FieldAccessL, TransferStationR, CellarR, SubbasementFissureL,
    WestTerminalAccessL, MezzanineConcourseL, VulnarCanyonL, CanyonPassageR,
    ElevatorToCondenserL, LoadingDockSecurityAreaL, ElevatorToWellspringL,
    NorakBrookL, NorakPerimeterTR, NorakPerimeterBL, VulnarDepthsElevatorEL,
    VulnarDepthsElevatorER, HiveBurrowL, SequesteredInfernoL,
    CollapsedPassageR, MagmaPumpL, ReservoirMaintenanceTunnelR, IntakePumpR,
    ThermalReservoir1R, GeneratorAccessTunnelL, ElevatorToMagmaLakeR,
    MagmaPumpAccessR, FieryGalleryL, RagingPitL, HollowChamberR, PlacidPoolR,
    SporousNookL, RockyRidgeTrailL, TramToSuziIslandR
) = area_doors_unpackable

(
    Missile, Super, PowerBomb, Morph, Springball, Bombs, HiJump,
    GravitySuit, Varia, Wave, SpeedBooster, Spazer, Ice, Grapple,
    Plasma, Screw, Charge, SpaceJump, Energy, Reserve, Xray, SMB
) = items_unpackable


exitSpacePort = LogicShortcut(lambda loadout: (
    True
    # TODO: Why did one definition have somethings different?
    # (Morph in loadout) or (Missile in loadout) or (Super in loadout) or (Wave in loadout)
))
canIBJ = LogicShortcut(lambda loadout: (
    (Morph in loadout) and
    (Bombs in loadout)
))
canUseBombs = LogicShortcut(lambda loadout: (
    (Morph in loadout) and
    ((Bombs in loadout) or (PowerBomb in loadout))
))

canFly = LogicShortcut(lambda loadout: (
    (canIBJ in loadout) or
    (SpaceJump in loadout)
))
canUsePB = LogicShortcut(lambda loadout: (
    (Morph in loadout) and
    (PowerBomb in loadout)
))
pinkDoor = LogicShortcut(lambda loadout: (
    (Missile in loadout) or
    (Super in loadout)
))
warpZone = LogicShortcut(lambda loadout: (
    (Super in loadout) or
    (
        (Morph in loadout) and
        (pinkDoor in loadout) and
        (canUseBombs in loadout)
        )
))
canKillBT = LogicShortcut(lambda loadout: (
    (Morph in loadout) and
    (pinkDoor in loadout) and
    (Bombs in loadout)
))
brinstarMain = LogicShortcut(lambda loadout: (
    (warpZone in loadout) and
    (pinkDoor in loadout)
))
lowerWaterMaze = LogicShortcut(lambda loadout: (
    (warpZone in loadout) and
    (
        (HiJump in loadout) or
        (GravitySuit in loadout)
        )
))
upperWaterMaze = LogicShortcut(lambda loadout: (
    (lowerWaterMaze in loadout) and
    (canUsePB in loadout)
))
phantoon = LogicShortcut(lambda loadout: (
    (warpZone in loadout) and
    (canUseBombs in loadout) and
    (Missile in loadout)
))
lowerNorfair = LogicShortcut(lambda loadout: (
    (warpZone in loadout) and
    (Varia in loadout) and
    (Super in loadout) and
    (canUsePB in loadout) and
    (SpeedBooster in loadout)
))
underwaterSpeed = LogicShortcut(lambda loadout: (
    (GravitySuit in loadout) and
    (SpeedBooster in loadout)
))
draygon = LogicShortcut(lambda loadout: (
    (upperWaterMaze in loadout) and
    (Super in loadout) and
    (
        (Grapple in loadout) or
        (GravitySuit in loadout)
        ) and
    (
        (Charge in loadout) or
        (Grapple in loadout)
        )
))
ridley = LogicShortcut(lambda loadout: (
    (lowerNorfair in loadout) and
    (Energy in loadout) and
    (Charge in loadout) and
    (
        (Wave in loadout) or
        (Spazer in loadout) or
        (Plasma in loadout)
        )
))
secretSpore = LogicShortcut(lambda loadout: (
    (canUsePB in loadout) and
    (Missile in loadout) and
    (Super in loadout) and
    (Charge in loadout) and
    (GravitySuit in loadout) and
    (Varia in loadout) and
    (Plasma in loadout)
))

area_logic: AreaLogicType = {
    "Early": {
        # using SunkenNestL as the hub for this area, so we don't need a path from every door to every other door
        # just need at least a path with sunken nest to and from every other door in the area
        ("CraterR", "SunkenNestL"): lambda loadout: (
            True
        ),
        ("SunkenNestL", "CraterR"): lambda loadout: (
            True
        ),
        ("SunkenNestL", "RuinedConcourseBL"): lambda loadout: (
            True
        ),
        ("SunkenNestL", "RuinedConcourseTR"): lambda loadout: (
            True
            # TODO: Expert needs energy and casual doesn't? And Casual can do it with supers, but expert can't?
        ),   
    },
}


location_logic: LocationLogicType = {
    "Right Sky Super": lambda loadout: (
        (warpZone in loadout) and
        (
            (SpeedBooster in loadout) or
            (
                (canFly in loadout) and
                (Morph in loadout)
                )
            )
    ),
    "Bomb Torizo": lambda loadout: (
        (Morph in loadout) and
        (pinkDoor in loadout) and
        (Bombs in loadout)
    ),
    "Morph Ball": lambda loadout: (
        True
    ),
    "Alpha Missile": lambda loadout: (
        (Morph in loadout)
    ),
    "Plasma Beam": lambda loadout: (
        (Morph in loadout) and
        (Springball in loadout) and
        (SpeedBooster in loadout) and
        (
            (canUseBombs in loadout) or
            (Wave in loadout) or
            (Spazer in loadout)
            )
    ),
    "Landing Site Power Bomb": lambda loadout: (
        (canUsePB in loadout)
    ),
    "Missile Parlor Tunnel": lambda loadout: (
        (canUseBombs in loadout)
    ),
    "Bombs Alternate": lambda loadout: (
        (Morph in loadout) and
        (pinkDoor in loadout)
    ),
    "Missile Maze Wall": lambda loadout: (
        (warpZone in loadout) and
        (
            (canIBJ in loadout) or
            (
                (Morph in loadout) and
                (Springball in loadout)
                )
            )
    ),
    "Right Sky Missile": lambda loadout: (
        (warpZone in loadout) and
        (
            (canIBJ in loadout) or
            (
                (Morph in loadout) and
                (Springball in loadout)
                )
            )
    ),
    "Sky Tripper Power Bomb": lambda loadout: (
        (warpZone in loadout) and
        (canUsePB in loadout)
    ),
    "Energy Grapple Hidden": lambda loadout: (
        (warpZone in loadout) and
        (Grapple in loadout) and
        (Morph in loadout)
    ),
    "Missile Reservoir Sky": lambda loadout: (
        (warpZone in loadout) and
        (canUseBombs in loadout)
    ),
    "High Mushroom Missile": lambda loadout: (
        (Morph in loadout) and
        (Super in loadout) and
        (
            (canFly in loadout) or
            (Ice in loadout) or
            (SpeedBooster in loadout)
            )
    ),
    "Mushroom Energy Tank": lambda loadout: (
        (brinstarMain in loadout)
    ),
    "Crateria Reserve": lambda loadout: (
        (brinstarMain in loadout) and
        (SpeedBooster in loadout)
    ),
    "Climb Super": lambda loadout: (
        (Morph in loadout) and
        (Super in loadout) and
        (SpeedBooster in loadout) and
        (canUsePB in loadout) and
        (Springball in loadout)
    ),
    "Missile Outside Maze": lambda loadout: (
        (brinstarMain in loadout)
    ),
    "Missile Inside Maze": lambda loadout: (
        (brinstarMain in loadout) and
        (Super in loadout) and
        (Morph in loadout) and
        (canUseBombs in loadout)
    ),
    "Spazer": lambda loadout: (
        (brinstarMain in loadout) and
        (Super in loadout)
    ),
    "Power Bomb Xray Maze": lambda loadout: (
        (brinstarMain in loadout) and
        (Super in loadout) and
        (canUsePB in loadout) and
        (Bombs in loadout) and
        (Springball in loadout)
        
    ),
    "Walljump Missile": lambda loadout: (
        (brinstarMain in loadout)
    ),
    "Charge Beam": lambda loadout: (
        (brinstarMain in loadout) and
        (Morph in loadout) and
        (Wave in loadout)
    ),
    "Crumble Missile": lambda loadout: (
        (brinstarMain in loadout) and
        (SpeedBooster in loadout) and
        (Super in loadout) and
        (Morph in loadout)
    ),
    "Crumble Power Bomb": lambda loadout: (
        (brinstarMain in loadout) and
        (SpeedBooster in loadout) and
        (Super in loadout) and
        (canUseBombs in loadout) and
        (Springball in loadout)
    ),
    "Double Flower Missile": lambda loadout: (
        (brinstarMain in loadout) and
        (SpeedBooster in loadout)
    ),
    "Brin-Crat Elevator Speed Missile": lambda loadout: (
        (brinstarMain in loadout) and
        (SpeedBooster in loadout)
    ),
    "Energy Tank Open Pink": lambda loadout: (
        (brinstarMain in loadout) and
        (
            (Energy in loadout) or
            (SpaceJump in loadout) or
            (Grapple in loadout) or
            (Varia in loadout)
            )
    ),
    "HiJump Energy Tank": lambda loadout: (
        (brinstarMain in loadout) and
        (Super in loadout) and
        (canUseBombs in loadout)
    ),
    "HiJump": lambda loadout: (
        (brinstarMain in loadout) and
        (pinkDoor in loadout) and
        (canUseBombs in loadout)
    ),
    "Crateria Wave Beam": lambda loadout: (
        (Morph in loadout) and
        (pinkDoor in loadout) and
        (SpeedBooster in loadout) and
        (canUseBombs in loadout) and
        (Springball in loadout)
    ),
    "Speed Maze Missile": lambda loadout: (
        (brinstarMain in loadout) and
        (SpeedBooster in loadout) and
        (canUsePB in loadout)
    ),
    "Super Gate Super": lambda loadout: (
        (brinstarMain in loadout) and
        (SpeedBooster in loadout) and
        (Morph in loadout) and
        (Super in loadout)
    ),
    "Puyo Tide Missile": lambda loadout: (
        (brinstarMain in loadout) and
        (canUseBombs in loadout) and
        (
            (SpeedBooster in loadout) or
            (HiJump in loadout) or
            (GravitySuit in loadout)
            )
        
    ),
    "Right Missile From Water Maze": lambda loadout: (
        (brinstarMain in loadout) and
        (canUsePB in loadout)
        
    ),
    "Waver High Missile": lambda loadout: (
        (brinstarMain in loadout) and
        (canUsePB in loadout) and
        (
            (canFly in loadout) or
            (Ice in loadout) or
            (SpeedBooster in loadout)
            )
    ),
    "Waver High Energy Tank": lambda loadout: (
        (brinstarMain in loadout) and
        (
            (canFly in loadout) or
            (Ice in loadout) or
            (SpeedBooster in loadout)
            )
    ),
    "False Wall Elevator Reserve": lambda loadout: (
        (SpeedBooster in loadout) and
        (
            (
                (brinstarMain in loadout) and
                (Super in loadout)
                ) or
                (
                    (warpZone in loadout) and
                    (
                        (Varia in loadout) or
                        (Energy in loadout)
                        )
                    )
            )
    ),
    "False Wall Elevator Missile": lambda loadout: (
        (
            (brinstarMain in loadout) and
            (Super in loadout)
            ) or
        (
            (warpZone in loadout) and
            (
                (Varia in loadout) or
                (Energy in loadout)
                )
            )
    ),
    "Table Energy Tank": lambda loadout: (
        (brinstarMain in loadout)
    ),
    "Robot Ride Super": lambda loadout: (
        (phantoon in loadout) and
        (SpeedBooster in loadout)
    ),
    "SECRET Screw Attack Norfair Left": lambda loadout: (
        (secretSpore in loadout)
    ),
    "SECRET Space Jump Water Maze Tube": lambda loadout: (
        (secretSpore in loadout)
    ),
    "SECRET Gravity Suit Parlor": lambda loadout: (
        (secretSpore in loadout)
    ),
    "Lava Wall Missile": lambda loadout: (
        (warpZone in loadout) and
        (
            (Varia in loadout) or
            (loadout.count(Energy) + loadout.count(Reserve) >= 2)
            )
    ),
    "Super Nova Core": lambda loadout: (
        (warpZone in loadout) and
        (
            (Varia in loadout) or
            (loadout.count(Energy) + loadout.count(Reserve) >= 3)
            ) and
        (Super in loadout) and
        (Morph in loadout)
    ),
    "Shoutout to Crumble Shaft": lambda loadout: (
        (warpZone in loadout) and
        (
            (Varia in loadout) or
            (loadout.count(Energy) + loadout.count(Reserve) >= 3)
            ) and
        (
            (Super in loadout) or
            (canUsePB in loadout)
            )
    ),
    "Lil Grapple Bump Missile": lambda loadout: (
        (warpZone in loadout) and
        (
            (Varia in loadout) or
            (loadout.count(Energy) + loadout.count(Reserve) >= 4)
            ) and
        (Super in loadout)
    ),
    "Norfair Reserve": lambda loadout: (
        (warpZone in loadout) and
        (
            (Varia in loadout) or
            (loadout.count(Energy) + loadout.count(Reserve) >= 3)
            ) and
        (Super in loadout) and
        (canUseBombs in loadout)
    ),
    "Norf-Warp Elevator Spark Missile": lambda loadout: (
        (warpZone in loadout) and
        (Energy in loadout) and
        (SpeedBooster in loadout)
    ),
    "Lil Grapple Bump Power Bomb": lambda loadout: (
        (warpZone in loadout) and
        (
            (Varia in loadout) or
            (loadout.count(Energy) + loadout.count(Reserve) >= 4)
            ) and
        (Super in loadout) and
        (Morph in loadout)
    ),
    "Croc Power Bomb": lambda loadout: (
        (warpZone in loadout) and
        (
            (Varia in loadout) or
            (loadout.count(Energy) + loadout.count(Reserve) >= 5)
            ) and
        (Super in loadout)
    ),
    "Trapeze Power Bomb": lambda loadout: (
        (warpZone in loadout) and
        (Varia in loadout) and
        (canUseBombs in loadout) and
        (Springball in loadout)
    ),
    "Trapeze Energy": lambda loadout: (
        (warpZone in loadout) and
        (Varia in loadout) and
        (canUseBombs in loadout)
    ),
    "Pink Orb Farm Stash": lambda loadout: (
        (warpZone in loadout) and
        (
            (Varia in loadout) or
            (Energy in loadout)
            ) and
        (canUsePB in loadout)
    ),
    "Water Maze Reserve": lambda loadout: (
        (lowerWaterMaze in loadout) and
        (Super in loadout) and
        (
            (Ice in loadout) or
            (canFly in loadout)
            )
    ),
    "Speedball Super": lambda loadout: (
        (upperWaterMaze in loadout) and
        (Springball in loadout) and
        (SpeedBooster in loadout) and
        (GravitySuit in loadout)
    ),
    "Crumble Cage Missile": lambda loadout: (
        (warpZone in loadout) and
        (
            (Varia in loadout) or
            (loadout.count(Energy) + loadout.count(Reserve) >= 4)
            ) and
        (Morph in loadout)
    ),
    "LN Open Energy Tank": lambda loadout: (
        (lowerNorfair in loadout) 
    ),
    "Speed Booster": lambda loadout: (
        (warpZone in loadout) and
        (
            (Varia in loadout) or
            (loadout.count(Energy) + loadout.count(Reserve) >= 4)
            ) and
        (canUsePB in loadout)
    ),
    "Norfair Blue Gate Missile": lambda loadout: (
        (warpZone in loadout) and
        (
            (Varia in loadout) or
            (loadout.count(Energy) + loadout.count(Reserve) >= 4)
            ) and
        (Morph in loadout) and
        (Wave in loadout)
    ),
    "Norfair Wave Beam": lambda loadout: (
        (warpZone in loadout) and
        (
            (Varia in loadout) or
            (loadout.count(Energy) + loadout.count(Reserve) >= 6)
            ) and
        (Super in loadout) and
        (canIBJ in loadout)
    ),
    "Pink Gate Super": lambda loadout: (
        (warpZone in loadout) and
        (
            (Varia in loadout) or
            (loadout.count(Energy) + loadout.count(Reserve) >= 5)
            ) and
        (Morph in loadout) and
        (pinkDoor in loadout)
    ),
    "Speed Ramp Missile": lambda loadout: (
        (warpZone in loadout) and
        (
            (Varia in loadout) or
            (loadout.count(Energy) + loadout.count(Reserve) >= 4)
            ) and
        (SpeedBooster in loadout)
    ),
    "LN Retro Ped Missile": lambda loadout: (
        (lowerNorfair in loadout)
    ),
    "Norf-Crat Elevator Missile": lambda loadout: (
        (canUsePB in loadout)
        
    ),
    "Norf-Crat Elevator Energy Tank": lambda loadout: (
        (SpeedBooster in loadout) and
        (canUsePB in loadout)
    ),
    "LN First Spark Missile": lambda loadout: (
        (lowerNorfair in loadout) and
        (SpeedBooster in loadout)
    ),
    "LN Double Spark Missile": lambda loadout: (
        (lowerNorfair in loadout) and
        (SpeedBooster in loadout)
    ),
    "Space Jump": lambda loadout: (
        (ridley in loadout)
    ),
    "LN Power Bomb": lambda loadout: (
        (lowerNorfair in loadout)
    ),
    "Water Maze Screw Attack": lambda loadout: (
        (lowerNorfair in loadout) and
        (SpeedBooster in loadout) and
        (Springball in loadout) and
        (GravitySuit in loadout)
    ),
    "Metroid Gauntlet Missile": lambda loadout: (
        (SpeedBooster in loadout) and
        (pinkDoor in loadout)
    ),
    "Speed Steps Missile": lambda loadout: (
        (SpeedBooster in loadout) and
        (Super in loadout) and
        (Morph in loadout) #softlock protection
    ),
    "Grapple Beam": lambda loadout: (
        (Morph in loadout) and
        (Super in loadout)
    ),
    "Grapple Missile": lambda loadout: (
        (canUsePB in loadout) and
        (Super in loadout) 
    ),
    "Gravity Suit": lambda loadout: (
        (brinstarMain in loadout) and
        (canUsePB in loadout) and
        (Super in loadout) and
        (
            (Missile in loadout) or
            (Charge in loadout)
            )
    ), #behind kraid fight
    "Climb Speed Missile": lambda loadout: (
        (Morph in loadout) and
        (pinkDoor in loadout) and
        (SpeedBooster in loadout)
    ),
    "Water Maze Screw Missile": lambda loadout: (
        (lowerNorfair in loadout) and
        (SpeedBooster in loadout) and
        (Springball in loadout)
    ),
    "Goober Race Power Bomb": lambda loadout: (
        (warpZone in loadout) and
        (canUsePB in loadout) and
        (Wave in loadout) and
        (Ice in loadout)
        
    ),
    "WS Shinespark Puzzle Super": lambda loadout: (
        (warpZone in loadout) and
        (canUseBombs in loadout) and
        (SpeedBooster in loadout) and
        (HiJump in loadout)
    ),
    "Crumble Trippers Missile": lambda loadout: (
        (warpZone in loadout) and
        (canUseBombs in loadout) and
        (Springball in loadout)
    ),
    "Lava Dive Energy Tank": lambda loadout: (
        (warpZone in loadout) and
        (canUseBombs in loadout) and
        (Varia in loadout) and
        (Grapple in loadout)
    ),
    "Goober Super": lambda loadout: (
        (brinstarMain in loadout) and
        (canUseBombs in loadout)
    ),
    "Spore Spawn Super": lambda loadout: (
        (brinstarMain in loadout) and
        (Morph in loadout)
    ),
    "Conveyors Missile": lambda loadout: (
        (warpZone in loadout) and
        (canUseBombs in loadout) and
        (Springball in loadout)
    ),
    "Crown Energy Tank": lambda loadout: (
        (phantoon in loadout) and
        (Wave in loadout)
    ),
    "Bowling Missile": lambda loadout: (
        (phantoon in loadout) and
        (canUsePB in loadout) and
        (SpeedBooster in loadout)
    ),
    "Moat Missile": lambda loadout: (
        (warpZone in loadout) and
        (
            (SpeedBooster in loadout) or
            (GravitySuit in loadout)
            )
    ),
    "WS Right Side Speed Missile": lambda loadout: (
        (Super in loadout) and
        (SpeedBooster in loadout)
    ),
    "WS Right Side Energy Tank": lambda loadout: (
        (Super in loadout) and
        (
            (canUseBombs in loadout) or
            (SpeedBooster in loadout) or
            (Screw in loadout)
            )
    ),
    "WS Speed Chozo Missile": lambda loadout: (
        (phantoon in loadout) and
        (SpeedBooster in loadout)
    ),
    "Varia Suit": lambda loadout: (
        (phantoon in loadout) and
        (Super in loadout) and
        (
            (Energy in loadout) or
            (Varia in loadout) or
            (Grapple in loadout) or
            (SpaceJump in loadout) or
            ((canUsePB in loadout) and (SpeedBooster in loadout))
            )
    ),
    "SECRET Speed Booster Top Green": lambda loadout: (
        (secretSpore in loadout)
    ),
    "SECRET Springball WS Left": lambda loadout: (
        (secretSpore in loadout)
    ),
    "SECRET Ice Beam Top Norfair": lambda loadout: (
        (secretSpore in loadout)
    ),
    "Metal Pirates Missile": lambda loadout: (
        (upperWaterMaze in loadout) and
        (Super in loadout)
    ),
    "Tube Pirates Missile": lambda loadout: (
        (lowerWaterMaze in loadout) and
        (canUseBombs in loadout)
    ),
    "Pre-Botwoon Missile": lambda loadout: (
        (lowerWaterMaze in loadout)
    ),
    "Beach Missile": lambda loadout: (
        (upperWaterMaze in loadout) and
        (canUsePB in loadout)
    ),
    "Metal Pirates Power Bomb": lambda loadout: (
        (upperWaterMaze in loadout) and
        (Super in loadout) and
        (
            (
                (Wave in loadout) and
                (Charge in loadout) and
                (Plasma in loadout)
                ) or
            (SpeedBooster in loadout)
            ) # x-factor?
    ),
    "Top Water Maze Nook Missile": lambda loadout: (
        (upperWaterMaze in loadout) and
        (Morph in loadout) and
        (Super in loadout)
    ),
    "Ice Beam": lambda loadout: (
        (lowerWaterMaze in loadout) and
        (Energy in loadout) and
        (Charge in loadout) and
        (Super in loadout) and
        (
            (Grapple in loadout) or
            (Ice in loadout)
            ) #not sure about jumping up
    ),
    "Final Tourian Missile": lambda loadout: (
        (phantoon in loadout) and
        (draygon in loadout) and
        (ridley in loadout) and
        (SpeedBooster in loadout) and
        (Springball in loadout) and
        (Ice in loadout) and
        (Reserve in loadout) and
        (Xray in loadout)
    ),
    "Left Sand Pit ~ Right Missile": lambda loadout: (
        (lowerWaterMaze in loadout) and
        (canUseBombs in loadout)
    ),
    "Left Sand Pit Super": lambda loadout: (
        (lowerWaterMaze in loadout) and
        (canUseBombs in loadout)
    ),
    "Left Sand Pit ~ Left Missile": lambda loadout: (
        (lowerWaterMaze in loadout) and
        (canUseBombs in loadout)
    ),
    "Left Sand Pit Power Bomb": lambda loadout: (
        (lowerWaterMaze in loadout) and
        (canUseBombs in loadout)
    ),
    "Above Sand Pit Missile": lambda loadout: (
        (lowerWaterMaze in loadout) and
        (underwaterSpeed in loadout)
    ),
    "Sand Showers Energy Tank": lambda loadout: (
        (upperWaterMaze in loadout) and
        (
            (GravitySuit in loadout) or
            (Grapple in loadout)
            )
    ),
    "Right Sand Pit Energy Tank": lambda loadout: (
        (upperWaterMaze in loadout) and
        (Super in loadout)
    ),
    "Middle Sand Pit Energy Tank": lambda loadout: (
        (lowerWaterMaze in loadout)
    ),
    "Flying Speedball Missile": lambda loadout: (
        (upperWaterMaze in loadout) and
        (underwaterSpeed in loadout) and
        (Morph in loadout)
    ),
    "Speedball Shortcut Missile": lambda loadout: (
        (lowerWaterMaze in loadout) and
        (underwaterSpeed in loadout) and
        (Morph in loadout)
    ),
    "Oum Missile": lambda loadout: (
        (upperWaterMaze in loadout) and
        (Super in loadout) and
        (
            (Grapple in loadout) or
            (GravitySuit in loadout)
            )
    ),
    "Springball": lambda loadout: (
        (draygon in loadout)
    ),
    "WS Grapple Puzzle Power Bomb": lambda loadout: (
        (warpZone in loadout) and
        (SpeedBooster in loadout) and
        (Morph in loadout) and
        (
            (Grapple in loadout) or
            (SpaceJump in loadout)
            )
    ),
    "Tourian Screw Attack": lambda loadout: (
        (phantoon in loadout) and
        (draygon in loadout) and
        (ridley in loadout)
    ),
    "X-Ray Scope": lambda loadout: (
        (brinstarMain in loadout) and
        (canUsePB in loadout) and
        (
            (Grapple in loadout) or
            (canFly in loadout) or
            (Ice in loadout)
            )
    ),
    "WS Grapple Fish": lambda loadout: (
        (warpZone in loadout) and
        (canUseBombs in loadout) and
        (GravitySuit in loadout) and
        (Grapple in loadout)
    ),
    "X-Ray Into Wall Missile": lambda loadout: (
        (brinstarMain in loadout) and
        (Morph in loadout) and
        (pinkDoor in loadout) and
        (Xray in loadout)
    ),
    "Secret Area Shinespark Missile": lambda loadout: (
        (secretSpore in loadout) and
        (SpeedBooster in loadout)
    ),
    
}


class Expert(LogicInterface):
    area_logic: ClassVar[AreaLogicType] = area_logic
    location_logic: ClassVar[LocationLogicType] = location_logic

    @staticmethod
    def can_fall_from_spaceport(loadout: Loadout) -> bool:
        return True
