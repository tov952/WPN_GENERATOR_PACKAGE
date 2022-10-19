import enum


class GPTypes(enum.Enum):
    BRRL = 1
    TRGR_GRD = 2
    TRGGR = 3
    GRIP = 4
    MGZN = 5
    MGWL = 6
    HDGRD = 8
    CHMBR = 9
    MZZL = 10
    CRRY_HNDLE = 11
    REAR_SGHT = 12
    FRNT_SGHT = 13
    BFFR_TUBE = 14
    CHRG_HNDLE = 15
    STCK = 16
    BUTT_PLT = 17
    RCVR = 18


GPTypesNiceName = {GPTypes.BRRL: "Barrel",
                   GPTypes.TRGR_GRD: "TriggerGuard",
                   GPTypes.TRGGR: "Trigger",
                   GPTypes.GRIP: "Grip",
                   GPTypes.MGZN: "Magazine",
                   GPTypes.MGWL: "Magwell",
                   GPTypes.HDGRD: "Handguard",
                   GPTypes.CHMBR: "Chamber",
                   GPTypes.MZZL: "Muzzle",
                   GPTypes.CRRY_HNDLE: "CarryingHandle",
                   GPTypes.REAR_SGHT: "RearSight",
                   GPTypes.FRNT_SGHT: "FrontSight",
                   GPTypes.BFFR_TUBE: "BufferTube",
                   GPTypes.CHRG_HNDLE: "ChargingHandle",
                   GPTypes.STCK: "Stock",
                   GPTypes.BUTT_PLT: "ButtPlate",
                   GPTypes.RCVR: "Receiver"}


class shapeType(enum.Enum):
    C = 0   #Cylindrical
    F = 1   #Flat


shapeTypeNiceNames = {shapeType.C : "Cylindrical",
                      shapeType.F : "Flat"}

class parmType(enum.IntEnum):
    GROUP = 0
    GUNPART = 1
    CUTOUT = 2