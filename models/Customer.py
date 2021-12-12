import smartpy as sp

class Customer(sp.Contract):

def __init__(custType, satisfaction, machineBuffs, trainerBuffs, isActive, memberGymId):
        self.init(custType           = custType,
                  satisfaction    = TNat,
                  machineBuffs        = sp.TMap(custType, sp.TInt),
                  trainerBuffs        = sp.TMap(custType, sp.TInt),
                  isActive            = false,
                  memberGymId         = self.memberGymId,
                  owner               = owner,
                  counterparty        = counterparty)
                  