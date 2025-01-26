import tkinter as tk
from tkinter import ttk
from googletrans import Translator  # Importing the Translator module from googletrans for text translation

# Function to translate text
def traduire_texte():
    # Retrieve the text to be translated from the input field
    texte_a_traduire = texte_entree.get()
    # Retrieve the target language code (e.g., 'en' for English, 'fr' for French) from the input field
    langue_cible = langue_cible_entree.get()

    # Create an instance of the Translator
    traducteur = Translator()

    # Translate the text to the target language
    traduction = traducteur.translate(texte_a_traduire, dest=langue_cible)

    # Update the label to display the translated text
    texte_traduit.configure(text=traduction.text)

# Create the main window
fenetre = tk.Tk()
fenetre.title("Translator")  # Set the window title
fenetre.geometry("800x500")  # Set the window size

# Customize the theme for a better appearance
style = ttk.Style()
style.theme_use("clam")  # Use the "clam" theme for widgets

# Create widgets with a personalized style
frame = ttk.Frame(fenetre)  # Main frame for the layout
frame.pack(padx=10, pady=10)

# Label for the text to be translated
label_texte = ttk.Label(frame, text="Text to translate:")
label_texte.grid(row=0, column=0, padx=5, pady=5, sticky="w")

# Entry widget for inputting the text to translate
texte_entree = ttk.Entry(frame, width=40)
texte_entree.grid(row=0, column=1, padx=5, pady=5)

# Label for the target language code
label_langue_cible = ttk.Label(frame, text="Target language:")
label_langue_cible.grid(row=1, column=0, padx=5, pady=5, sticky="w")

# Entry widget for inputting the target language code
langue_cible_entree = ttk.Entry(frame, width=10)
langue_cible_entree.grid(row=1, column=1, padx=5, pady=5)

# Button to trigger the translation
bouton_traduire = ttk.Button(frame, text="Translate", command=traduire_texte)
bouton_traduire.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

# Label to display the translated text
texte_traduit = ttk.Label(frame, text="", wraplength=300, foreground="blue")
texte_traduit.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

# Start the main loop for the graphical user interface
fenetre.mainloop()
