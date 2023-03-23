from datetime import datetime, timedelta

class Venta():
    
    def __init__(self,pCodigoArticulo,pVendedor,pSucursal,pImporte):
        self.importe = pImporte
        self.sucursal = pSucursal
        self.vendedor = pVendedor
        self.codigoArticulo = pCodigoArticulo
        self.fecha = datetime.now().strftime("%d/%m/%Y")