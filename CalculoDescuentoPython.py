def calcular_descuento(monto_total, porcentaje_descuento=10):
    descuento = monto_total * (porcentaje_descuento / 100)
    return descuento

# Llamadas a la función
monto1 = 100  # Ejemplo de monto total
descuento1 = calcular_descuento(monto1)  # Usando el porcentaje predeterminado del 10%
monto_final1 = monto1 - descuento1

monto2 = 200  # Ejemplo de monto total
descuento2 = calcular_descuento(monto2, 15)  # Usando un porcentaje de descuento del 15%
monto_final2 = monto2 - descuento2

# Resultados
print(f"Compra 1: Descuento aplicado: ${descuento1:.2f}, Monto final a pagar: ${monto_final1:.2f}")
print(f"Compra 2: Descuento aplicado: ${descuento2:.2f}, Monto final a pagar: ${monto_final2:.2f}")

