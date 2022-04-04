class Boleta():
    def __init__(self, categoria, horas_extra, tardanza):
        self.categoria = categoria
        self.horas_extra = horas_extra
        self.tardanza = tardanza
               
    def sueldo(self, sueldob):
        self.sueldob = sueldob
        if self.categoria == "A":
            self.sueldob = 3000
        elif self.categoria== "B":
            self.sueldob = 2500
        elif self.categoria == "C":
            self.sueldob = 2000

    def descuento (self, desc_tard):
        self.desc_tard = desc_tard
        self.desc_tard = ((self.sueldob/240)/60)*self.tardanza
        
    def pago_extra (self, pag_ext):
        self.pag_ext = pag_ext
        self.pag_ext = (self.sueldob/240)*self.horas_extra
        
        
    def pago_total (self, sueldo_neto):
        self.sueldo_neto = sueldo_neto
        self.sueldo_neto = (self.sueldob+self.pag_ext)-self.desc_tard
        
   
