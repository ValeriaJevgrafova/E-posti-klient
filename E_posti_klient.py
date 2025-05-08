import tkinter as tk
from tkinter import filedialog, messagebox
import smtplib
from email.message import EmailMessage
import os

# Переменная для хранения пути к вложению
attached_file = ""

# Функция выбора файла
def lisa_fail():
    global attached_file
    attached_file = filedialog.askopenfilename()
    attach_label.config(text=attached_file)

# Функция отправки письма
def saada_email():
    try:
        msg = EmailMessage()
        msg['From'] = 'valeria.jevgrafova@gmail.com'  # Gmail отправителя
        msg['To'] = email_entry.get()
        msg['Subject'] = subject_entry.get()
        msg.set_content(body_text.get("1.0", tk.END))

        # Добавляем вложение, если оно есть
        if attached_file:
            with open(attached_file, 'rb') as f:
                file_data = f.read()
                file_name = os.path.basename(attached_file)
                msg.add_attachment(file_data, maintype='application',
                                   subtype='octet-stream', filename=file_name)

        # Отправка письма через SMTP
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login('valeria.jevgrafova@gmail.com', 'TEIE_RAKENDUSE_SALASÕNA')
            smtp.send_message(msg)

        messagebox.showinfo("Edu", "Kiri on saadetud!")  # Уведомление об успехе
    except Exception as e:
        messagebox.showerror("Viga", str(e))  # Уведомление об ошибке

# Интерфейс
root = tk.Tk()
root.title("E-kirja saatmine")
root.geometry("600x400")

labels_frame = tk.Frame(root, bg="darkgreen")
labels_frame.pack(side=tk.LEFT, fill=tk.Y)

inputs_frame = tk.Frame(root)
inputs_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

# Метки
for txt in ["E-POST:", "TEEMA:", "LISA:", "KIRI:"]:
    label = tk.Label(labels_frame, text=txt, fg="lightgreen", bg="darkgreen", font=("Arial", 14))
    label.pack(anchor="w", padx=10, pady=10)

# Ввод email, тема, файл, текст
email_entry = tk.Entry(inputs_frame, font=("Arial", 14), fg="green", width=40)
email_entry.pack(pady=10)
email_entry.insert(0, "valeria.jevgrafova@gmail.com")

subject_entry = tk.Entry(inputs_frame, font=("Arial", 14), fg="green", width=40)
subject_entry.pack(pady=10)
subject_entry.insert(0, "Ilus mesilane")

attach_label = tk.Label(inputs_frame, text="", font=("Arial", 10), fg="gray")
attach_label.pack()

body_text = tk.Text(inputs_frame, height=8, font=("Arial", 14), fg="green")
body_text.pack(pady=10)
body_text.insert(tk.END, "Tere!\nVaata kui ilus mesilane!\nPäikest!")

# Кнопки
buttons_frame = tk.Frame(inputs_frame)
buttons_frame.pack(pady=10)

add_button = tk.Button(buttons_frame, text="LISA PILT", bg="darkgreen", fg="lightgreen",
                       font=("Arial", 14), command=lisa_fail)
add_button.pack(side=tk.LEFT, padx=10)

send_button = tk.Button(buttons_frame, text="SAADA", bg="darkgreen", fg="lightgreen",
                        font=("Arial", 14), command=saada_email)
send_button.pack(side=tk.LEFT, padx=10)

root.mainloop()

