from dao_planc import DaoPlanC
from mod_PlanC import planC

class CtrPlanc:
    def __init__(self, plan=None):  
        self.planes = plan
    
    def consulta(self, buscar):
        objDaoplan = DaoPlanC()
        return objDaoplan.consultar(buscar)
    
    def ingresar(self, plan):
        objDaoplan = DaoPlanC()
        return objDaoplan.ingresar(plan)
    
    def modificar(self, plan):
        objDaoplan = DaoPlanC()
        return objDaoplan.modificar(plan)
    
    def eliminar(self, plan):
        objDaoplan = DaoPlanC()
        return objDaoplan.eliminar(plan)
        
    
""" plan = planC(0,'02',1,'banco','D',True)
ctr = CtrPlanc()
#ingresar un grupo
ctr.ingresar(plan)
planes = ctr.consulta("")
print(planes)
for plan in planes:
    print(plan[0], plan[1], plan[2], plan[3], plan[4], plan[5])  """