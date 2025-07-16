print("BIENVENIDO AL HOTEL EL BOSQUE")
def MenuOpciones():
  print("1. 🛌 Registro de Habitación")
  print("2. 🛌 Consultar disponibilidad de Habitaciones")
  print("3. 🙋 Registro Huespedes")
  print("4. 📅 Realizar Reserva")
  print("5. 🛎️ Registro Ingreso (Check-In)")
  print("6. ➡️ Registro Salida (Check-Out)")
  print("7. 📊 Administración")
  print("8. Graficos")
  print("9. Salir")

Habitaciones = {}
Huespedes = {}
Reservas = {}
Disponible = {}

import pandas as pd

def RegistrodeHabitacion(codigo):
  print("🛌Ingresó a la función Registro de Habitación")
  print("🛌Registro de Habitación")
  codigo = input("Número de la Habitación: ")
  if codigo in Habitaciones:
    print("El número ya existe.")
    return

  Tipo = input("Ingrese el tipo de habitación (Sencilla, Doble, Familiar, Suite): ")
  Capacidad = input("Ingrese la capacidad (Número de personas): ")
  Costo = float(input("Ingrese el costo por noche por persona: "))
  Estado = "Disponible"

  Habitaciones[codigo] = {
      "Tipo": Tipo,
      "Capacidad": Capacidad,
      "Costo de la Habitación": Costo,
      "Estado": "Disponible"
      }

  Disponible[codigo] = Habitaciones[codigo]

  # Convert the dictionary to a DataFrame and save to CSV
  df_habitacion = pd.DataFrame([Habitaciones[codigo]])
  df_habitacion.to_csv("Habitaciones.csv", mode="a", header=False, index=False)

  print ("🛌 Habitación registrada exitosamente.")

def ActualizarHabitacion(codigo):
  print("🛌 Actualizar Habitaciones")
  codigo = input("Número de la Habitación: ")
  if codigo not in Habitaciones:
    print("❌ La habitación no existe.")


  Tipo = input("Ingrese el tipo de habitación (Sencilla, Doble, Familiar, Suite): ")
  Capacidad = input("Ingrese la capacidad (Número de personas): ")
  Costo = float(input("Ingrese el costo por noche por persona: "))
  Estado = "Disponible"

  Habitaciones[codigo] = {
      "Tipo": Tipo,
      "Capacidad": Capacidad,
      "Costo de la Habitación": valor_habitacion,
      "Estado": "Disponible"
      }

  print("🛌 Habitación actualizada exitosamente.")
  return

def valor_habitacion ():

  print("🛌 Tipo de Habitación")
  Tipo = input("Ingrese el tipo de habitación (Sencilla, Doble, Familiar, Suite): ")
  valor_habitacion = 0
  if Tipo.lower() == "sencilla":
    valor_habitacion = 50000
  elif Tipo.lower() == "doble":
    valor_habitacion = 60000
  elif Tipo.lower() == "familiar":
    valor_habitacion = 80000
  elif Tipo.lower() == "suite":
    valor_habitacion = 90000
  return valor_habitacion

def consultardisponibilidaddeHabitaciones():

 print("🏨 Habitaciones Disponibles:")
 if not Disponible:
    print("❎ No hay habitaciones disponibles.")
 else:
   for codigo, datos in Disponible.items():
    if datos["Estado"] == "Disponible":
      print(f"Habitación {codigo} - Tipo: {datos['Tipo']} - Capacidad: {datos['Capacidad']}")

import re

def validar_documento(doc):
    if not doc.isdigit():
        print("❌ El documento debe contener solo números.")
        return False
    if not (3 <= len(doc) <= 15):
        print("❌ El documento debe tener entre 3 y 15 dígitos.")
        return False
    return True

def validar_nombre(nombre):
    nombre = nombre.strip()
    if len(nombre) < 3:
        print("❌ El nombre debe tener al menos 3 letras.")
        return False
    if not re.match(r"^[A-Za-zÁÉÍÓÚÑáéíóúñ\s]+$", nombre):
        print("❌ No se permiten números ni caracteres especiales.")
        return False
    return True

def validar_apellidos(apellidos):
    apellidos = apellidos.strip()
    if len(apellidos) < 3:
        print("❌ El apellido debe tener al menos 3 letras.")
        return False
    if not re.match(r"^[A-Za-zÁÉÍÓÚÑáéíóúñ\s]+$", apellidos):
        print("❌ No se permiten números ni caracteres especiales.")
        return False
    return True

def validar_telefono(telefono):
    if not telefono.isdigit():
        print("❌ El teléfono solo debe contener números.")
        return False
    if not (7 <= len(telefono) <= 10):
        print("❌ El teléfono debe tener entre 7 y 10 dígitos.")
        return False
    return True

def validar_correo(correo):
    if not re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", correo):
        print("❌ Correo electrónico inválido. Debe contener '@' y un dominio.")
        return False
    return True

def RegistroHuespedes():
       while True:
        print("🙋 Registro de Huésped")
        tipodedocumento = input("Tipo de documento (CC, TI, CE, etc.): ")

        documento = input("Documento de identidad del Huésped: ")
        if documento in Huespedes:
            print("🙋 El huésped ya está registrado.")
            actualizar = input("¿Desea actualizar la información del huésped? (S/N): ").lower()
            if actualizar != "s":
                return

        while not validar_documento(documento):
            documento = input("Documento de identidad del Huésped: ")

        nombre = input("Nombre: ")
        while not validar_nombre(nombre):
            nombre = input("Nombre: ")

        apellidos = input("Apellidos: ")
        while not validar_apellidos(apellidos):
            apellidos = input("Apellidos: ")

        telefono = input("Teléfono: ")
        while not validar_telefono(telefono):
            telefono = input("Teléfono: ")

        correo = input("Correo electrónico: ")
        while not validar_correo(correo):
            correo = input("Correo electrónico: ")


        Huespedes[documento] = {
            "Tipo de documento": tipodedocumento,
            "Documento": documento,
            "Nombre": nombre,
            "Apellidos": apellidos,
            "Teléfono": telefono,
            "Correo electrónico": correo
        }

        print("✅🙋 Huésped registrado exitosamente.")

        DfHuespedes=pd.DataFrame([Huespedes[documento]])
        DfHuespedes.to_csv("Huespedes.csv")

        otro = input("¿Desea registrar otro huésped? (S/N): ").lower()
        if otro != "s":
            break

from ast import Try
#Reserva

from datetime import datetime, timedelta

def RealizarReserva():
    print("📅 Realizar Reserva de Habitación")

    documento = input("Ingrese el documento del huésped: ")
    if documento not in Huespedes:
        print("❌ El huésped no está registrado. No se puede realizar la reserva.")
        return

    nombre_huesped = Huespedes[documento]['Nombre'] + " " + Huespedes[documento]['Apellidos']

    tipo = input("Ingrese el tipo de habitación a reservar (Sencilla, Doble, Familiar, Suite): ").capitalize()
    if tipo not in ["Sencilla", "Doble", "Familiar", "Suite"]:
        print("❌ Tipo de habitación no válido.")
        return
    disponibles = [codigo for codigo, datos in Habitaciones.items()
                   if datos["Tipo"].lower() == tipo.lower() and datos["Estado"] == "Disponible"]

    if not disponibles:
        print(f"❌ No hay habitaciones disponibles del tipo {tipo}.")
        return

    print("Habitaciones disponibles:", disponibles)
    habitacion = input("Ingrese el número de habitación a reservar: ")
    if habitacion not in disponibles:
        print("❌ Habitación no disponible o no existe.")
        return

    try:
        fecha_ingreso = input("Ingrese la fecha de ingreso (AAAA-MM-DD): ")
        fecha_ingreso_dt = datetime.strptime(fecha_ingreso, "%Y-%m-%d")
        noches = int(input("Ingrese el número de noches de estancia: "))
        if noches <= 0:
            print("❌ El número de noches debe ser mayor a cero.")
            return
    except ValueError:
        print("❌ Fecha o número de noches inválidos.")
        return

    fecha_salida_dt = fecha_ingreso_dt + timedelta(days=noches)

    if tipo.lower() == "sencilla":
        costo_noche = 50000
    elif tipo.lower() == "doble":
        costo_noche = 60000
    elif tipo.lower() == "familiar":
        costo_noche = 80000
    elif tipo.lower() == "suite":
        costo_noche = 90000
    else:
      print("❌ Tipo de habitación inválido.")
      return

    try:
      capacidad = int(Habitaciones[habitacion]['Capacidad'])

    except:
      print("❌ Error al leer la capacidad de la habitación.")
      return

    try:
      personas = int(input(f"Ingrese número de personas (máx {capacidad}): "))
      if personas <= 0 or personas > capacidad:
        print("❌ Número de personas inválido.")
        return
    except ValueError:
      print("❌ Ingrese un número válido de personas.")
      return

    total = costo_noche * personas * noches


    # Guardar solo la reserva (sin cambiar estado aún)
    Reservas[documento] = {
        "Nombre": nombre_huesped,
        "Tipo": tipo,
        "Habitacion": habitacion,
        "Ingreso": fecha_ingreso_dt,
        "Salida": fecha_salida_dt,
        "Noches": noches,
        "Costo": total,
        "CheckIn": False  # Aún no ha hecho ingreso
    }

    print("📅 Reserva registrada exitosamente. Comprobante:")
    print("==============================================")
    print(f"Nombre del huésped: {nombre_huesped}")
    print(f"Tipo de habitación: {tipo}")
    print(f"Número de habitación: {habitacion}")
    print(f"Fecha de ingreso: {fecha_ingreso_dt.date()}")
    print(f"Fecha de salida: {fecha_salida_dt.date()}")
    print(f"Número de noches: {noches}")
    print(f"Costo total estimado: ${total:,.0f}")
    print("==============================================")

    DfReservas=pd.DataFrame([Reservas[documento]])
    DfReservas.to_csv("Reservas.csv")


#Registro de Ingreso

def RegistrodeIngreso():
    print("🛎️ Registro de Ingreso (Check-In)")

    documento = input("Ingrese el documento del huésped: ")
    if documento not in Reservas:
        print("❌ No existe una reserva registrada para este documento.")
        return

    reserva = Reservas[documento]
    if reserva["CheckIn"]:
        print("⚠️ El huésped ya ha realizado el check-in previamente.")
        return

    habitacion = reserva["Habitacion"]
    if Habitaciones[habitacion]["Estado"] == "Ocupada":
        print("❌ La habitación ya está ocupada.")
        return

    # Actualizar estado
    reserva["CheckIn"] = True
    Habitaciones[habitacion]["Estado"] = "Ocupada"

    print("✅🛎️ Check-In realizado exitosamente.")
    print("--------------------------------------")
    print(f"Nombre del huésped: {reserva['Nombre']}")
    print(f"Habitación asignada: {habitacion}")
    print(f"Fecha de ingreso: {reserva['Ingreso'].date()}")
    print("--------------------------------------")


#Registro de salida


from datetime import datetime

def RegistrodeSalida():
    print("🚪 Registro de Salida (Check-Out)")

    documento = input("Ingrese el documento del huésped: ")
    if documento not in Reservas:
        print("❌ No se encontró ninguna reserva con ese documento.")
        return

    reserva = Reservas[documento]

    if not reserva.get("CheckIn", False):
        print("❌ El huésped no ha realizado el check-in.")
        return

    habitacion = reserva["Habitacion"]
    tipo = reserva["Tipo"]
    fecha_ingreso = reserva["Ingreso"]
    fecha_salida_str = input("Ingrese la fecha de salida (AAAA-MM-DD): ")


    fecha_salida_dt = datetime.strptime(fecha_salida_str, "%Y-%m-%d")
    if fecha_salida_dt <= fecha_ingreso:
        print("❌ La fecha de salida debe ser posterior a la de ingreso.")
        return

    noches = (fecha_salida_dt - fecha_ingreso).days
    print(f"🌙 Noches de estancia: {noches}")
    if noches < 1:
      noches = 1

    print(f"📅 Fecha de ingreso: {fecha_ingreso.date()}")
    print(f"📅 Fecha de salida: {fecha_salida_dt.date()}")


    if tipo.lower() == "sencilla":
        costo_noche = 50000
    elif tipo.lower() == "doble":
        costo_noche = 60000
    elif tipo.lower() == "familiar":
        costo_noche = 80000
    elif tipo.lower() == "suite":
        costo_noche = 90000
    else:
        print("❌ Tipo de habitación inválido.")

    try:
      capacidad = int(Habitaciones[habitacion]['Capacidad'])

    except:
        print("❌ Error al leer la capacidad de la habitación.")

    try:
      personas = int(input(f"Ingrese número de personas (máx {capacidad}): "))
      if personas <= 0 or personas > capacidad:
        print("❌ Número de personas inválido.")

    except ValueError:
      print("❌ Ingrese un número válido de personas.")


    total = costo_noche * personas * noches

    # Factura
    print("🧾 Factura de Estancia")
    print("===================================")
    print(f"Nombre completo: {reserva['Nombre']}")
    print(f"Documento: {documento}")
    print(f"Tipo de habitación: {tipo}")
    print(f"Número de habitación: {habitacion}")
    print(f"Fecha de ingreso: {fecha_ingreso.date()}")
    print(f"Fecha de salida: {fecha_salida_dt.date()}")
    print(f"Número total de noches: {noches}")
    print(f"Valor por noche: ${costo_noche:,.0f}")
    print(f"Total a pagar: ${total:,.0f}")
    print("===================================")
    print("Gracias por su visita!")

    # Actualizar habitación y limpiar reserva

    Habitaciones[habitacion]["Estado"] = "Disponible"
    reserva["CheckOut"] = fecha_salida_dt
    reserva["CobroReal"] = total
    reserva["NochesReales"] = noches

#Administración

def crear_archivo_admins():
    try:
        with open("admins.txt", "x") as f:  # "x" solo crea si no existe
            f.write("admin1,clave123")
            f.write("admin2,password456")
            print("✅ Archivo admins.txt creado con usuarios por defecto.")
    except FileExistsError:
        print("📂 El archivo admins.txt ya existe.")

crear_archivo_admins()


import pandas as pd

def cargar_admins():
    try:
        df = pd.read_csv("admins.txt", header=None, names=["usuario", "contraseña"])
        return df
    except FileNotFoundError:
        print("❌ Archivo de administradores no encontrado.")
        return pd.DataFrame(columns=["usuario", "contraseña"])

def login_admin():
    admins = cargar_admins()
    usuario = input("👤 Usuario de administrador: ")
    clave = input("🔒 Contraseña: ")

    match = admins[(admins["usuario"] == usuario) & (admins["contraseña"] == clave)]
    if not match.empty:
        print("✅ Acceso concedido al módulo de administración.")
        return True
    else:
        print("❌ Usuario o contraseña incorrectos.")
        return False



def Administracion():
    if not login_admin():
        return

    while True:
        print("\n📊 MÓDULO DE ADMINISTRACIÓN")
        print("1. Total de huéspedes registrados")
        print("2. Total de habitaciones ocupadas")
        print("3. Total de habitaciones disponibles")
        print("4. Ingresos generados por reservas")
        print("5. Tiempo promedio de estancia por huésped")
        print("6. Lista de huéspedes con historial de reservas")
        print("7. Huésped con más noches")
        print("8. Huésped con menos noches")
        print("9. Volver al menú principal")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print(f"Total huéspedes registrados: {len(Huespedes)}")

        elif opcion == "2":
            ocupadas = sum(1 for h in Habitaciones.values() if h["Estado"] == "Ocupada")
            print(f"Total habitaciones ocupadas: {ocupadas}")

        elif opcion == "3":
            disponibles = sum(1 for h in Habitaciones.values() if h["Estado"] == "Disponible")
            print(f"Total habitaciones disponibles: {disponibles}")

        elif opcion == "4":
            total_ingresos = sum(r.get("CobroReal", 0) for r in Reservas.values() if r.get("CheckOut"))
            print(f"💰 Ingresos totales: ${total_ingresos:,.0f}")

        elif opcion == "5":
            total_noches = sum(r.get("NochesReales", 0) for r in Reservas.values() if r.get("CheckOut"))
            total_personas = len([r for r in Reservas.values() if r.get("CheckOut")])
            promedio = total_noches / total_personas if total_personas else 0
            print(f"📏 Estancia promedio: {promedio:.2f} noches")

        elif opcion == "6":
            print("📋 Lista de huéspedes con historial:")
            for doc, res in Reservas.items():
                print(f"- {res['Nombre']} (Documento: {doc})")

        elif opcion == "7":
            maximo = max(Reservas.items(), key=lambda x: x[1].get("NochesReales", 0))
            print(f"🏆 Huésped con más noches: {maximo[1]['Nombre']} ({maximo[1].get('NochesReales', 0)} noches)")

        elif opcion == "8":
            minimo = min((r for r in Reservas.values() if r.get("CheckOut")), key=lambda x: x.get("NochesReales", float('inf')))
            print(f"📉 Huésped con menos noches: {minimo['Nombre']} ({minimo.get('NochesReales', 0)} noches)")

        elif opcion == "9":
            break

        else:
            print("❌ Opción inválida.")

#Graficos

import matplotlib.pyplot as plt

def mostrar_graficos():
    print("📊 Generando gráficos...")

    # Datos para gráficos
    tipos = ["Sencilla", "Doble", "Familiar", "Suite"]
    ocupadas = [sum(1 for h in Habitaciones.values() if h["Tipo"].lower() == tipo.lower() and h["Estado"] == "Ocupada") for tipo in tipos]
    disponibles = [sum(1 for h in Habitaciones.values() if h["Tipo"].lower() == tipo.lower() and h["Estado"] == "Disponible") for tipo in tipos]

    # 1. Gráfico de barras
    plt.figure(figsize=(10, 5))
    plt.bar(["Estándar", "Suite"], [ocupadas[0] + ocupadas[1] + ocupadas[2], ocupadas[3]], color=["blue", "purple"])
    plt.title("Comparación habitaciones estándar vs suite (ocupadas)")
    plt.xlabel("Tipo")
    plt.ylabel("Cantidad")
    plt.show()

    # 2. Pie chart ocupadas vs disponibles
    total_ocupadas = sum(ocupadas)
    total_disponibles = sum(disponibles)
    plt.pie([total_ocupadas, total_disponibles], labels=["Ocupadas", "Disponibles"], autopct="%1.1f%%", colors=["red", "green"])
    plt.title("Distribución de habitaciones")
    plt.show()

    # 3. Línea: check-out por día
    fechas_checkout = [res["CheckOut"].date() for res in Reservas.values() if "CheckOut" in res]
    if fechas_checkout:
        fechas_unicas = sorted(set(fechas_checkout))
        conteo = [fechas_checkout.count(f) for f in fechas_unicas]
        plt.plot(fechas_unicas, conteo, marker='o')
        plt.title("Check-Outs por día")
        plt.xlabel("Fecha")
        plt.ylabel("Cantidad")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    # 4. Barras horizontales: noches por huésped (Top 10)
    noches_huesped = sorted(((res["Nombre"], res.get("NochesReales", 0)) for res in Reservas.values()), key=lambda x: x[1], reverse=True)[:10]
    nombres = [x[0] for x in noches_huesped]
    noches = [x[1] for x in noches_huesped]
    plt.barh(nombres, noches, color="orange")
    plt.title("Top 10 huéspedes por noches")
    plt.xlabel("Noches")
    plt.gca().invert_yaxis()
    plt.tight_layout()
    plt.show()

    # 5. Scatter: noches vs valor pagado
    noches = [res.get("NochesReales", 0) for res in Reservas.values()]
    pagos = [res.get("CobroReal", 0) for res in Reservas.values()]
    plt.scatter(noches, pagos)
    plt.title("Relación noches vs total pagado")
    plt.xlabel("Noches")
    plt.ylabel("Valor pagado")
    plt.show()

    # 6. Pie chart: ingresos por tipo (estándar vs suite)
    ingresos_estandar = sum(res.get("CobroReal", 0) for res in Reservas.values() if res["Tipo"].lower() != "suite")
    ingresos_suite = sum(res.get("CobroReal", 0) for res in Reservas.values() if res["Tipo"].lower() == "suite")
    plt.pie([ingresos_estandar, ingresos_suite], labels=["Estándar", "Suite"], autopct="%1.1f%%")
    plt.title("Ingresos por tipo de habitación")
    plt.show()

    # 7. Histograma: duración de estancias
    noches_validas = [res.get("NochesReales", 0) for res in Reservas.values()]
    plt.hist(noches_validas, bins=range(1, max(noches_validas)+2), edgecolor="black")
    plt.title("Duración de estancias")
    plt.xlabel("Noches")
    plt.ylabel("Cantidad de huéspedes")
    plt.show()

    # 8. Combinado: ingresos diarios (barras + línea)
    ingresos_dia = {}
    for res in Reservas.values():
        if "CheckOut" in res:
            fecha = res["CheckOut"].date()
            ingresos_dia[fecha] = ingresos_dia.get(fecha, 0) + res.get("CobroReal", 0)
    fechas = sorted(ingresos_dia)
    ingresos = [ingresos_dia[f] for f in fechas]
    plt.bar(fechas, ingresos, color="lightblue", label="Ingresos")
    plt.plot(fechas, ingresos, color="darkblue", marker="o", label="Tendencia")
    plt.title("Ingresos diarios")
    plt.xlabel("Fecha")
    plt.ylabel("Ingresos ($)")
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()
    plt.show()

def menu_principal():
  while True:
    print("Menú Principal")
    MenuOpciones()
    opcion = input("Ingrese una opción: ")

    if opcion == "1":
      codigo = input("Ingrese el código de la habitación: ")
      if codigo in Habitaciones:
        print("La habitación ya existe.")
        actualizar = input("¿Desea actualizar la información de la habitación?")
        if actualizar.lower() == "s":
          ActualizarHabitacion(codigo)
        else:
          print("La habitación no se actualizará.")
      else:
        RegistrodeHabitacion(codigo)
    elif opcion == "2":
      consultardisponibilidaddeHabitaciones()
    elif opcion == "3":
      RegistroHuespedes()
    elif opcion == "4":
      RealizarReserva()
    elif opcion == "5":
      RegistrodeIngreso()
    elif opcion == "6":
      RegistrodeSalida()
    elif opcion == "7":
      Administracion()
    elif opcion == "8":
      mostrar_graficos()
    elif opcion == "Salir":
      print("¡Gracias por Visitarnos!")
    else:
      print("❌ Opción inválida. Por favor, seleccione una opción válida.")

menu_principal()
