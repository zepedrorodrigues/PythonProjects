import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os

# Assuming the functions from BlackJack.py are in the same directory
from BlackJack import deck_make, draw, score_check, check_winner

class BlackjackGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Blackjack Game")
        self.root.geometry("800x600")

        self.deck = deck_make()
        self.player_hand = []
        self.computer_hand = []
        self.player_display = []
        self.computer_display = []

        self.card_images = {}  # Dictionary to store card images
        self.load_images()  # Load all card images

        self.setup_ui()

    def load_images(self):
        suits = ['clubs', 'hearts', 'spades', 'diamonds']
        numbers = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'j', 'q', 'k', 'a']

        for suit in suits:
            for number in numbers:
                card_name = f"{number}_of_{suit}".lower()
                image_path = os.path.join("cards", f"{card_name}.png")
                image = Image.open(image_path).resize((80, 120))  # Resize the images if needed
                self.card_images[card_name] = ImageTk.PhotoImage(image)
    def setup_ui(self):
        self.player_label = tk.Label(self.root, text="Player's Cards:", font=("Helvetica", 16))
        self.player_label.pack()
        self.player_frame = tk.Frame(self.root)
        self.player_frame.pack()
        self.player_score_label = tk.Label(self.root, text="Score: 0", font=("Helvetica", 14))
        self.player_score_label.pack()

        self.computer_label = tk.Label(self.root, text="Computer's Cards:", font=("Helvetica", 16))
        self.computer_label.pack()
        self.computer_frame = tk.Frame(self.root)
        self.computer_frame.pack()
        self.computer_score_label = tk.Label(self.root, text="Score: 0", font=("Helvetica", 14))
        self.computer_score_label.pack()

        self.buttons_frame = tk.Frame(self.root)
        self.buttons_frame.pack(pady=20)

        self.hit_button = tk.Button(self.buttons_frame, text="Hit", command=self.player_hit)
        self.hit_button.pack(side=tk.LEFT, padx=20)
        self.stand_button = tk.Button(self.buttons_frame, text="Stand", command=self.player_stand)
        self.stand_button.pack(side=tk.LEFT, padx=20)

        self.start_game()

    def start_game(self):
        self.deck = deck_make()
        self.player_hand = []
        self.computer_hand = []
        self.player_display = []
        self.computer_display = []

        draw(2, self.player_hand, self.player_display, self.deck)
        draw(1, self.computer_hand, self.computer_display, self.deck)

        self.update_ui()

        if score_check(self.player_hand) == 21:
            messagebox.showinfo("Blackjack!", "Player has Blackjack! Let's see what the computer gets.")
            self.computer_playing()

    def update_ui(self):
        for widget in self.player_frame.winfo_children():
            widget.destroy()
        for widget in self.computer_frame.winfo_children():
            widget.destroy()

        for card_name in self.player_display:
            card_image = self.card_images.get(card_name.lower())
            if card_image:
                card_label = tk.Label(self.player_frame, image=card_image)
                card_label.image = card_image  # Keep a reference to avoid garbage collection
                card_label.pack(side=tk.LEFT, padx=5)
            else:
                print(f"Card image not found for {card_name}")

        for card_name in self.computer_display:
            card_image = self.card_images.get(card_name.lower())
            if card_image:
                card_label = tk.Label(self.computer_frame, image=card_image)
                card_label.image = card_image  # Keep a reference to avoid garbage collection
                card_label.pack(side=tk.LEFT, padx=5)
            else:
                print(f"Card image not found for {card_name}")

        self.player_score_label.config(text=f"Score: {score_check(self.player_hand)}")
        self.computer_score_label.config(text=f"Score: {score_check(self.computer_hand)}")

    def player_hit(self):
        draw(1, self.player_hand, self.player_display, self.deck)
        self.update_ui()

        if score_check(self.player_hand) > 21:
            messagebox.showinfo("Busted!", "Player busted! You lose.")
            self.start_game()

    def player_stand(self):
        self.computer_playing()

    def computer_playing(self):
        while score_check(self.computer_hand) < 17:
            draw(1, self.computer_hand, self.computer_display, self.deck)
            self.update_ui()

        if score_check(self.computer_hand) > 21:
            messagebox.showinfo("Busted!", "Computer busted! Player wins!")
        else:
            result = check_winner(score_check(self.computer_hand), score_check(self.player_hand))
            messagebox.showinfo("Game Over", result)

        self.start_game()

if __name__ == "__main__":
    root = tk.Tk()
    app = BlackjackGUI(root)
    root.mainloop()
