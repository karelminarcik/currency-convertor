from tkinter import *
import requests


# Barvy
main_color = "#158B8F"

# Okno
window = Tk()
window.minsize(400, 120)
window.resizable(False, False)
window.title("Currency Converter")
window.config(bg=main_color)
window.iconbitmap("img/currency.ico")

def convert():
    try:
        currency_from = drop_down_from.get()
        currency_to = drop_down_to.get()
        amount = int(user_input.get())

        url = f"https://api.apilayer.com/exchangerates_data/convert?to={currency_to}&from={currency_from}&amount={amount}"

        payload = {}
        headers = {
            "apikey": "DzcYowfNkZ89WX7gcrMTu5baIDtnjJp1"
        }

        response = requests.request("GET", url, headers=headers, data=payload)

        response.raise_for_status()
        data_result = response.json()
        result_label.config(text=round(data_result["result"], 2))
        notification_label.config(text="")

    except:
        notification_label.config(text="Please insert amount")




# uzivatelsky vstup
user_input = Entry(width=20, font=("Arial", 12), justify=CENTER)
user_input.insert(0, "0")
user_input.grid(row=0, column=0, padx=10,pady=(10,0))

# Roletka -z jake meny
drop_down_from = StringVar(window)
drop_down_from.set("CZK")  #vychozi hodnota
drop_down_from_options = OptionMenu(window, drop_down_from, "EUR", "USD", "CZK", "PLN")
drop_down_from_options.grid(row=0, column=1, padx=10, pady=(10,0))

# Roletka na jakou menu
drop_down_to = StringVar(window)
drop_down_to.set("CZK") # vychozi hodnota
drop_down_to_options = OptionMenu(window, drop_down_to, "EUR", "USD", "CZK", "PLN")
drop_down_to_options.grid(row=1, column=1, padx=10, pady=(10,0))

# Tlacitko prepoctu
count_button = Button(text="Convert", font=("Ariel" , 12), command=convert)
count_button.grid(row=0, column=3, padx=10, pady=(10,0))

# Label pro zobrazeni vysledku prevodu
result_label = Label(text="0", bg=main_color, font=("Arial", 12))
result_label.grid(row=1,column=0)

# notification label
notification_label = Label(window,bg=main_color, font=("Arial", 12))
notification_label.grid(row=2, column=0)

# hlavni cyklus
window.mainloop()