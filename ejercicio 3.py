import tkinter as tk
from tkinter import messagebox

def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32


def convertir_temperatura():
    try:
        celsius = float(entry_temp.get())
        fahrenheit = celsius_a_fahrenheit(celsius)
        messagebox.showinfo("Resultado", f"{celsius}°C = {fahrenheit:.2f}°F")
    except ValueError:
        messagebox.showerror("Error", "Introduce un número válido")


def tabla_multiplicar():
    try:
        numero = int(entry_tabla.get())
        resultado = "\n".join([f"{numero} x {i} = {numero * i}" for i in range(1, 11)])
        messagebox.showinfo(f"Tabla del {numero}", resultado)
    except ValueError:
        messagebox.showerror("Error", "Introduce un número entero válido")

def mostrar_menu():
    limpiar_ventana()
    titulo = tk.Label(ventana, text="=== MENÚ PRINCIPAL ===", font=("Segoe UI", 13, "bold"), bg="#F2F2F2")
    titulo.pack(pady=20)

    btn_temp = tk.Button(ventana, text="Conversión de temperatura 🌡️", width=25, bg="#D0E7FF",
                         fg="#003366", relief="flat", command=mostrar_conversion)
    btn_temp.pack(pady=10)

    btn_tabla = tk.Button(ventana, text="Tabla de multiplicar ✖️", width=25, bg="#DFFFD6",
                          fg="#004400", relief="flat", command=mostrar_tabla)
    btn_tabla.pack(pady=10)

    btn_salir = tk.Button(ventana, text="Salir 🚪", width=25, bg="#FFD6D6",
                          fg="#660000", relief="flat", command=ventana.destroy)
    btn_salir.pack(pady=20)


def mostrar_conversion():
    limpiar_ventana()
    tk.Label(ventana, text="Conversión de temperatura", font=("Segoe UI", 12, "bold"), bg="#F2F2F2").pack(pady=10)
    tk.Label(ventana, text="Introduce grados Celsius:", bg="#F2F2F2").pack()
    
    global entry_temp
    entry_temp = tk.Entry(ventana, relief="flat", bg="#FFFFFF", width=15, justify="center")
    entry_temp.pack(pady=5)

    tk.Button(ventana, text="Convertir", bg="#CCE5FF", fg="#003366", relief="flat",
              command=convertir_temperatura).pack(pady=5)
    tk.Button(ventana, text="⬅ Volver al menú", bg="#EAEAEA", relief="flat", command=mostrar_menu).pack(pady=10)


def mostrar_tabla():
    limpiar_ventana()
    tk.Label(ventana, text="Tabla de multiplicar", font=("Segoe UI", 12, "bold"), bg="#F2F2F2").pack(pady=10)
    tk.Label(ventana, text="Introduce un número entero:", bg="#F2F2F2").pack()
    
    global entry_tabla
    entry_tabla = tk.Entry(ventana, relief="flat", bg="#FFFFFF", width=15, justify="center")
    entry_tabla.pack(pady=5)
    tk.Button(ventana, text="Mostrar tabla", bg="#DFFFD6", fg="#004400", relief="flat",
              command=tabla_multiplicar).pack(pady=5)
    tk.Button(ventana, text="⬅ Volver al menú", bg="#EAEAEA", relief="flat", command=mostrar_menu).pack(pady=10)

def limpiar_ventana():
    """Elimina todos los widgets actuales de la ventana"""
    for widget in ventana.winfo_children():
        widget.destroy()

ventana = tk.Tk()
ventana.title("Menú interactivo")
ventana.geometry("350x300")
ventana.config(bg="#F2F2F2")  
ventana.resizable(False, False)

mostrar_menu()

ventana.mainloop()
