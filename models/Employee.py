import smartpy as sp

class Employee(sp.Contract):

def __init__(employeeType, satisfaction, wage, memberGymId):
        self.init(employeeType           = custType,
                  satisfaction    = TNat,
                  wage        = sp.TMap(employeeType, sp.TNat),
                  isActive            = false,
                  employeeId         = self.employeeId,
                  memberGymId               = memberGymId)
                  