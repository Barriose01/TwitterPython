while True:

		print("Elige una opcion:")
		print("(1): Registro")
		print("(2): Login")
		print("(3): Salir")
		opcion = input("")
		
		if opcion.strip() == "1":
			print("\n")
			perfil = ""
			correo = input("Correo: ")
			nombre = input("Nombre: ")
			clave = input("Clave: ")
			
			perfil += correo + " " + clave + "\n"
			archivo = "usuario.txt"
			with open(archivo) as file_object:
				interior_archivo = file_object.read()
			
			if perfil in interior_archivo:
				print("\nUsuario ya registrado. Por favor ingresar nuevo nombre o contraseña\n")
				
			else:
				with open(archivo, "a") as file_object:
					file_object.write(perfil)
				print("\nRegistro exitoso\n")
			
		elif opcion.strip() == "2":
			print("\n")
			intento = ""
			correo_2 = input("Correo: ")
			clave_2 = input("Clave: ")
			intento += correo_2 + " " + clave_2 + "\n"
			archivo = "usuario.txt"
			with open(archivo) as file_object:
				contenido = file_object.read()
				
			if intento in contenido:
				print("\nBienvenido, " + correo_2 + "\n")
				tweets = []
				while True:
					
					print("\nElige: ")
					print("(1): Escribir post")
					print("(2): Ver posts")
					print("(3): Ver posts(de mas antiguo a mas reciente)")
					print("(4): Borrar un determinado post")
					print("(5): Borrar todos los posts")
					print("(6): Cerrar sesion")
					
					opciones = input("")
					if opciones.strip() == "1":
						
						print("\n")
						publicacion = ""
						post = input("Escribe un post: ")
						publicacion += post + "\n"
						archivo2 = "tweets.txt"
						with open(archivo2, "a") as file_object:
							file_object.write(publicacion)
						print("\n")
						print("-" + post)
						print("\n")
					
					if opciones.strip() == "2":
						print("\n")
						tweets.clear()
						archivo2 = "tweets.txt"
						with open(archivo2) as file_object:
							contenido = file_object.readlines()
						for linea in contenido:
							tweets.append(linea)
						if len(tweets) == 0:
							print("No hay posts para mostrar\n")
						else:
							for tweet in reversed(tweets):
								print("-" + tweet + "\n")
							
					if opciones.strip() == "3":
						print("\n")
						if len(tweets) == 0:
							print("No hay posts para mostrar\n")
						else:
							for tweet in tweets:
								print("-" + tweet + "\n")
		
					if opciones.strip() == "4":
						print("\n")
						if len(tweets) == 0:
							print("No hay posts para eliminar\n")
						else:
							while True:
								print("Ingrese el indice del post que desea eliminar\n")
								i = 1
								for tweet in reversed(tweets):
									print("-" + tweet + "(" + str(i) + ")\n")
									i+= 1
								print("(q): Volver")
								try:
									indice_tweet = input()
									tweets.reverse()
									if indice_tweet.lower().strip() == "q":
										tweets.reverse()
										break
									if int(indice_tweet.strip()) == 0 or int(indice_tweet.strip()) < 0:
										print("\nDebe ingresar un numero indicando el indice del post\n")
										tweets.reverse()
										continue
									else:
										indice_eliminado = tweets.pop(int(indice_tweet) - 1)
										print("\nPost eliminado\n")
										tweets.reverse()
										with open(archivo2) as file_object:
											lineas = file_object.readlines()
										file_object.close()
										with open(archivo2, "w") as file_object:
											for linea in lineas:
												if linea != indice_eliminado:
													file_object.write(linea)
										file_object.close() 
										tweets.clear()
										break
								except:
									print("\nDebe ingresar un numero indicando el indice del post\n")
									tweets.reverse()
										
					if opciones.strip() == "5":
						print("\n")
						tweets.clear()
						with open(archivo2) as file_object:
							lineas = file_object.readlines()
						file_object.close()
						for linea in lineas:
							tweets.append(linea)
						if len(tweets) == 0:
							print("No hay posts para eliminar\n")
						else:
							with open(archivo2, "w") as file_object:
								file_object.write("")
							file_object.close()
							tweets.clear()
							print("Todos los posts han sido borrados\n")
	
					if opciones.strip() == "6":
						print("\n")
						break
			
			else:
				print("\nNombre o clave incorrecta. Intentelo nuevamente\n")
				
		elif opcion == "3":
			print("\n")
			break	
