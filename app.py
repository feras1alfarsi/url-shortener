import tkinter as tk
import requests

def shorten_url(long_url):
    if long_url == "":
        return "❌ Error: Please enter a URL"
    response = requests.get(f"https://tinyurl.com/api-create.php?url={long_url}")
    if response.status_code == 200:
        return response.text
    else:
        return "❌ Error: Could not shorten URL"

window = tk.Tk()
window.title("URL Shortener")
window.geometry("500x400")

label = tk.Label(window, text="Enter your long URL:")
label.pack(pady=10)

entry = tk.Entry(window, width=50)
entry.pack(pady=5)



def on_click():
    long_url = entry.get().strip()
    short_url = shorten_url(long_url)
    result_label.config(text=short_url)
    copy_button.config(text="Copy URL")

def copy_to_clipboard():
    window.clipboard_clear()
    window.clipboard_append(result_label.cget("text"))
    copy_button.config(text="✅ Copied!")

result_label = tk.Label(window, text="")
result_label.pack(pady=10)

button = tk.Button(window, text="Shorten URL", command=on_click)
button.pack(pady=10)

copy_button = tk.Button(window, text="Copy URL", command=copy_to_clipboard)
copy_button.pack(pady=5)
window.mainloop()