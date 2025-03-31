import tkinter as tk
from tkinter import messagebox

def agregar_item():
    item = entrada_item.get().strip()
    if item:
        lista_items.insert(tk.END, item)
        entrada_item.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "Ingrese un ítem antes de añadir.")

def marcar_completado():
    try:
        seleccion = lista_items.curselection()[0]
        item = lista_items.get(seleccion)
        if not item.startswith("✔ "):
            lista_items.delete(seleccion)
            lista_items.insert(seleccion, f"✔ {item}")
    except IndexError:
        messagebox.showwarning("Advertencia", "Seleccione un ítem para marcar como completado.")

def eliminar_item():
    try:
        seleccion = lista_items.curselection()[0]
        lista_items.delete(seleccion)
    except IndexError:
        messagebox.showwarning("Advertencia", "Seleccione un ítem para eliminar.")

def salir_aplicacion():
    ventana.quit()

def agregar_con_enter(event):
    agregar_item()

def marcar_con_doble_click(event):
    marcar_completado()

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Lista de Ítems")
ventana.geometry("400x400")
ventana.resizable(False, False)

# Entrada de texto para nuevos ítems
entrada_item = tk.Entry(ventana, width=40)
entrada_item.pack(pady=10)
entrada_item.bind("<Return>", agregar_con_enter)

# Botones de control
frame_botones = tk.Frame(ventana)
frame_botones.pack(pady=10)

btn_agregar = tk.Button(frame_botones, text="Añadir Ítem", command=agregar_item)
btn_agregar.grid(row=0, column=0, padx=5)

btn_completar = tk.Button(frame_botones, text="Marcar como Completado", command=marcar_completado)
btn_completar.grid(row=0, column=1, padx=5)

btn_eliminar = tk.Button(frame_botones, text="Eliminar Ítem", command=eliminar_item)
btn_eliminar.grid(row=0, column=2, padx=5)

btn_salir = tk.Button(frame_botones, text="Salir", command=salir_aplicacion)
btn_salir.grid(row=0, column=3, padx=5)

# Lista de ítems
lista_items = tk.Listbox(ventana, width=50, height=15)
lista_items.pack(pady=10)
lista_items.bind("<Double-Button-1>", marcar_con_doble_click)

# Ejecutar la aplicación
ventana.mainloop()