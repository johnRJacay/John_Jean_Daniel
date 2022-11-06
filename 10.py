print("En una tienda compre una mochila, una cartuchera y un borrador")
print("precio de la mochila = $45")
print("precio de la cartuchera = $15")
print("precio del borrador = $2 ")
print("se me aplico IGV")
mochila= 45
cartuchera= 15
borrador= 2
IGV= 0.18
PrecioSubtotal= mochila + cartuchera + borrador
PrecioIGV= PrecioSubtotal * IGV
precioTotal= PrecioSubtotal + PrecioIGV
print("EL precio total con todo IGV seria")
print(precioTotal)