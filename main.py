from trabajador import Trabajador
from boleta import Boleta

class Main(Trabajador,Boleta):
    def __init__(self,nombre,categoria, horas_extra, tardanza):
        self.nombre = nombre
        self.categoria = categoria
        self.horas_extra = horas_extra
        self.tardanza = tardanza
        
    def entrada_de_datos(self):
        print("\n***ENTRADA DE DATOS***")
        print("Trabajador:         ", self.nombre)    
        print("Categoria:          ", self.categoria)
        print("Horas extra:        ", self.horas_extra)
        print("Tardanza(minutos):  ", self.tardanza)
  
    def boleta_de_pagos (self):
        print("\n***BOLETA DE PAGOS***")
        print("Categoría:                  ", self.categoria)
        print("Sueldo básico:             $", self.sueldob)
        print("Descuento por tardanza:    $", round(self.desc_tard,2))
        print("Pago extra:                $",round(self.pag_ext,2))
        print("Sueldo neto:               $", round(self.sueldo_neto,2))


