from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES

# Create translator object once (better performance)
translator = Translator()

# ---------------- FUNCTION ---------------- #

def translate_text():
    try:
        # Get selected languages from dropdown
        src_lang = comb_sor.get()
        dest_lang = comb_dest.get()

        # Get input text
        text = source_text.get(1.0, END)

        # Convert language names → language codes (important)
        src_code = [code for code, lang in LANGUAGES.items() if lang.lower() == src_lang.lower()][0]
        dest_code = [code for code, lang in LANGUAGES.items() if lang.lower() == dest_lang.lower()][0]

        # Translate text
        translated = translator.translate(text, src=src_code, dest=dest_code)

        # Show output
        dest_text.delete(1.0, END)
        dest_text.insert(END, translated.text)

    except Exception as e:
        dest_text.delete(1.0, END)
        dest_text.insert(END, "Error: " + str(e))


# ---------------- GUI ---------------- #

root = Tk()
root.title("Language Translator")

# Better window size (clean look)
root.geometry("600x500")
root.config(bg="lavender")

# Center window on screen
root.eval('tk::PlaceWindow . center')

# Title
Label(root, text="Translator", font=("Times New Roman", 24, "bold"),
      bg="yellow").place(x=180, y=10)

# Source Label
Label(root, text="Source Text", font=("Times New Roman", 14, "bold"),
      bg="lavender").place(x=60, y=60)

# Source Text Box
source_text = Text(root, font=("Times New Roman", 12), wrap=WORD)
source_text.place(x=60, y=90, height=100, width=480)

# Language list (from googletrans)
lang_list = list(LANGUAGES.values())

# Source Dropdown
comb_sor = ttk.Combobox(root, values=lang_list, state="readonly")
comb_sor.place(x=60, y=210, width=150)
comb_sor.set("english")

# Destination Dropdown
comb_dest = ttk.Combobox(root, values=lang_list, state="readonly")
comb_dest.place(x=390, y=210, width=150)
comb_dest.set("hindi")

# Translate Button
Button(root, text="Translate", command=translate_text,
       bg="lightblue").place(x=250, y=210, width=100)

# Destination Label
Label(root, text="Translated Text", font=("Times New Roman", 14, "bold"),
      bg="lavender").place(x=60, y=260)

# Destination Text Box
dest_text = Text(root, font=("Times New Roman", 12), wrap=WORD)
dest_text.place(x=60, y=290, height=100, width=480)

root.mainloop()