
// Funcion de intercambio //    
void swap(int *px, int *py)
{
	int temp;
	temp = *px; /* guarda el valor de la direccion x */
	*px = *py; /* pone y en x */
	*py = temp; /* pone x en y */
}

