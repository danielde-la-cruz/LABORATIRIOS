Algoritmo ejercicio_4_4puntos
	escribir "ingrese el precio de compra"
	leer A
	Dma=A*0.1
	Dme=A*0.05
	si A>3000 Entonces
		escribir"el precio con descuento es: ", (A-Dma)
	SiNo
		escribir "el precio con descuento seria: ", A-Dme
	FinSi
FinAlgoritmo
