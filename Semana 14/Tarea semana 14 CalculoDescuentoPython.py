def calcular_descuento(monto_total, porcentaje_descuento=10):
    descuento = monto_total * (porcentaje_descuento/100)
    return  descuento

if __name__=="__main__":
    compras_mensuales = 4500
    compra_moto = 3000

## Llamada Compras mensuales
    descuento1 = calcular_descuento(compras_mensuales)
    print(f"Monto de la compra mensuales es {compras_mensuales}, el descuento es {descuento1}")

## Llamada Compra de una moto
    descuento2 = calcular_descuento(compra_moto)
    print(f"Monto de la compra de la moto es {compra_moto}, el descuento es {descuento2}")