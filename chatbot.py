# chatbot sobre la presion alta(hipertension)
# comunidad:nuevo padilla, tamaulipas
def mostrar_menu():
    print("\n🤖 ¡hola! soy cuida tu presion, tu asistente virtual de salud.")
    print("estoy aqui para ayudarte a cuidar tu presion arterial")
    print("que es la presion alta")
    print("causas y sintomas")
    print("consejos para prevenirla")
print("Actividades recomendadas")
print("Alimentacion saludable")
print("salir")

while True:
    mostrar_menu()
    opcion=input("\nEscribe el numero de la opcion que deseas: ")

    if opcion == "1":
        print("\n la presion arterial alta (hipertension) ocurre cuando la sangre ejerce demasiada fuerza sobre las paredes de las arterias.")
        print("Esto puede dañar el corazon, los riñones y el cerebro si no se controla.")
        print("es importante revisarla con frecuencia en tu centro de salud de nuevo padilla.")

    elif opcion == "2":
        print("\n⚠️ las principales causas en nuestra comunidad son:")
        print("-estres diario 😣")
        print("-mala alimentacion 🍟🥤")
        print("-Falta de ejercicio")
        print("-Fumar o tomar alcoho🚬🍺")
        print("-Antecedentes familiares")
        print("\n😥 los sintomas pueden incluir dolor de cabeza, mareos, cansancio o palpitaciones.")
        print("A veces no hay sintomas, por eso se le llama el 'asesino silencioso'. ")

    elif opcion == "3":
        print("\n consejos para prevenir la hipertension:")
        print("-Haz ejercicio al menos 30 minutos al dia 🚶")
        print("-Reduce el consumo de sal 🧂 y grasa")
        print("-come frutas, verduras y bebe agua 💧")
        print("-evita el estres con actividades relajantes 🧘")
        print("-Acude al medico regularmente")

    elif opcion == "4":
        print("\n🚶‍♀️ Actividades ideales para jovenes y adultos mayores:")
        print("-caminatas por el parque de padilla 🚶")
        print("-Andar en bicicleta o bailar 💃")
        print("-Ejercicios de respiracion o yoga 🧘")
        print("- Juegos al aire libre con la familia 🌲")

    elif opcion == "5":
        print("\n🍎 Alimentacion saludable para controlar la presion:")
        print("-come frutas y verduras todos los dias 🍉🥬")
        print("-Evita los refrescos, frituras y pan dulce 🚫")
        print("-prefiere pollo o pescado en lugar de carne roja")
        print("-Cocina con poca sal y bebe suficiente agua 💧")

    elif opcion == "6":
        print("\n🙏 Gracias por usar cuida tu presion.")
        print("Recuerda: pequeños cambios en tu rutina pueden mejorar tu salud.")
        print("cuida tu corazon ♥️ y comparte esta informacion en tu comunidad de nuevo padilla.")
        break

    else:
        print("\n❌ opcion no valida, intenta de nuevo por favor.")
