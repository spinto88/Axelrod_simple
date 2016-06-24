#!/bin/bash
# -*- ENCODING: UTF-8 -*-

ffmpeg -start_number 0 -r 5.0 -i opinion%d.png -vcodec mpeg4 opinion_Q100phi_0.00001_opcion2bis.avi
ffmpeg -start_number 0 -r 5.0 -i vaccinated%d.png -vcodec mpeg4 vaccinated_Q100phi_0.00001_opcion2bis.avi

zip -r Q100phi_0.00001_databis.zip opinion*.txt
zip -r Q100phi_0.00001_graphbis.zip opinion*.png
zip -r Q100phi_0.00001_databis.zip vaccinated*.txt
zip -r Q100phi_0.00001_graphbis.zip vaccinated*.png

rm -f opinion*.png
rm -f opinion*.txt
rm -f vaccinated*.png
rm -f vaccinated*.txt
# Con esta linea en la terminal o ejecutando ./movie.sh toma todos los archivos de la carpeta en la que estoy con el nombre file_n con n empezando desde 0 y arma un archivo .avi con la secuencia de graficos
