def calcular_descuento(precio):
    if precio > 70:
        descuento = 0.12  # 12% de descuento
    elif precio > 50:
        descuento = 0.10  # 10% de descuento
    else:
        descuento = 0  # Sin descuento

    precio_final = precio - (precio * descuento)
    return precio_final


# Solicitar el precio del producto al usuario
precio_producto = float(input("Ingrese el precio del producto: "))
precio_con_descuento = calcular_descuento(precio_producto)

print(f"El precio final con descuento es: {precio_con_descuento:.2f}")