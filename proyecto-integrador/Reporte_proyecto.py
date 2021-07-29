nom_arch= "Reporte.txt"
arch= open(nom_arch,"w")
arch.write("Tus resultados finales han sido los siguientes\n")

arch.write(f"Prueba:\nAritmetica: {marc} preguntas correctas\nAlgebra: {} preguntas correctas\nGeometria: {} preguntas correctas\nProbabilidad: {} preguntas correctas")
arch.write(f"Tu puntaje final fue de {}\n")

arch.close()