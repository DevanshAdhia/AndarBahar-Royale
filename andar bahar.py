from tkinter import *
from tkinter import messagebox
import random

class AndarBaharGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Andar Bahar Card Game")
        self.root.geometry("900x700")
        self.root.configure(bg="#1a5f1a")
        
        # Game variables
        self.deck = []
        self.joker = None
        self.andar_cards = []
        self.bahar_cards = []
        self.game_active = False
        self.bet_choice = None
        self.balance = 1000
        self.bet_amount = 100
        
        # Card suits and values
        self.suits = ['♠', '♥', '♦', '♣']
        self.values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        
        self.create_widgets()
        
    def create_widgets(self):
        # Title
        title_label = Label(self.root, text="🃏 ANDAR BAHAR 🃏", 
                              font=("Arial", 28, "bold"), 
                              bg="#1a5f1a", fg="white")
        title_label.pack(pady=10)
        
        # Balance and bet frame
        info_frame = Frame(self.root, bg="#1a5f1a")
        info_frame.pack(pady=10)
        
        self.balance_label = Label(info_frame, text=f"Balance: ₹{self.balance}", 
                                     font=("Arial", 16, "bold"), 
                                     bg="#1a5f1a", fg="gold")
        self.balance_label.pack(side=LEFT, padx=20)
        
        self.bet_label = Label(info_frame, text=f"Bet: ₹{self.bet_amount}", 
                                 font=("Arial", 16, "bold"), 
                                 bg="#1a5f1a", fg="white")
        self.bet_label.pack(side=LEFT, padx=20)
        
        # Joker card display
        joker_frame = Frame(self.root, bg="#1a5f1a")
        joker_frame.pack(pady=15)
        
        Label(joker_frame, text="Joker Card:", 
                font=("Arial", 14, "bold"), 
                bg="#1a5f1a", fg="white").pack()
        
        self.joker_label = Label(joker_frame, text="", 
                                   font=("Arial", 48, "bold"), 
                                   bg="white", fg="black",
                                   width=4, height=2,
                                   relief=RAISED, bd=3)
        self.joker_label.pack(pady=5)
        
        # Cards display frame
        cards_frame = Frame(self.root, bg="#1a5f1a")
        cards_frame.pack(pady=20, fill=BOTH, expand=True)
        
        # Andar side
        andar_frame = Frame(cards_frame, bg="#1a5f1a")
        andar_frame.pack(side=LEFT, padx=20, fill=BOTH, expand=True)
        
        Label(andar_frame, text="ANDAR (Inside)", 
                font=("Arial", 16, "bold"), 
                bg="#1a5f1a", fg="yellow").pack()
        
        self.andar_display = Label(andar_frame, text="", 
                                     font=("Arial", 12), 
                                     bg="#2d7a2d", fg="white",
                                     justify=LEFT, anchor="nw",
                                     width=20, height=12,
                                     relief=SUNKEN, bd=2)
        self.andar_display.pack(pady=10, fill=BOTH, expand=True)
        
        # Bahar side
        bahar_frame = Frame(cards_frame, bg="#1a5f1a")
        bahar_frame.pack(side=RIGHT, padx=20, fill=BOTH, expand=True)
        
        Label(bahar_frame, text="BAHAR (Outside)", 
                font=("Arial", 16, "bold"), 
                bg="#1a5f1a", fg="yellow").pack()
        
        self.bahar_display = Label(bahar_frame, text="", 
                                     font=("Arial", 12), 
                                     bg="#2d7a2d", fg="white",
                                     justify=LEFT, anchor="nw",
                                     width=20, height=12,
                                     relief=SUNKEN, bd=2)
        self.bahar_display.pack(pady=10, fill=BOTH, expand=True)
        
        # Betting buttons
        bet_frame = Frame(self.root, bg="#1a5f1a")
        bet_frame.pack(pady=10)
        
        self.andar_btn = Button(bet_frame, text="Bet on ANDAR", 
                                   font=("Arial", 14, "bold"),
                                   bg="#4CAF50", fg="white",
                                   width=15, height=2,
                                   command=lambda: self.place_bet("Andar"))
        self.andar_btn.pack(side=LEFT, padx=10)
        
        self.bahar_btn = Button(bet_frame, text="Bet on BAHAR", 
                                   font=("Arial", 14, "bold"),
                                   bg="#2196F3", fg="white",
                                   width=15, height=2,
                                   command=lambda: self.place_bet("Bahar"))
        self.bahar_btn.pack(side=LEFT, padx=10)
        
        # Control buttons
        control_frame = Frame(self.root, bg="#1a5f1a")
        control_frame.pack(pady=10)
        
        Button(control_frame, text="New Game", 
                 font=("Arial", 12, "bold"),
                 bg="#FF9800", fg="white",
                 width=12,
                 command=self.new_game).pack(side=LEFT, padx=5)
        
        Button(control_frame, text="Change Bet (₹50/100/200)", 
                 font=("Arial", 12, "bold"),
                 bg="#9C27B0", fg="white",
                 width=20,
                 command=self.change_bet).pack(side=LEFT, padx=5)
        
    def create_deck(self):
        self.deck = []
        for suit in self.suits:
            for value in self.values:
                self.deck.append(f"{value}{suit}")
        random.shuffle(self.deck)
        
    def get_card_value(self, card):
        return card[:-1]  # Remove suit symbol
        
    def new_game(self):
        if self.balance < 50:
            messagebox.showwarning("Insufficient Balance", "You don't have enough balance to play!")
            return
            
        self.create_deck()
        self.joker = self.deck.pop(0)
        self.andar_cards = []
        self.bahar_cards = []
        self.game_active = True
        self.bet_choice = None
        
        # Display joker
        self.joker_label.config(text=self.joker)
        color = "red" if self.joker[-1] in ['♥', '♦'] else "black"
        self.joker_label.config(fg=color)
        
        self.andar_display.config(text="")
        self.bahar_display.config(text="")
        
        self.andar_btn.config(state=NORMAL)
        self.bahar_btn.config(state=NORMAL)
        
    def place_bet(self, choice):
        if not self.game_active:
            messagebox.showwarning("No Game", "Please start a new game first!")
            return
            
        if self.balance < self.bet_amount:
            messagebox.showwarning("Insufficient Balance", "You don't have enough balance for this bet!")
            return
            
        self.bet_choice = choice
        self.balance -= self.bet_amount
        self.update_display()
        
        self.andar_btn.config(state=DISABLED)
        self.bahar_btn.config(state=DISABLED)
        
        messagebox.showinfo("Bet Placed", f"You bet ₹{self.bet_amount} on {choice}!")
        self.root.after(500, self.play_game)
        
    def play_game(self):
        joker_value = self.get_card_value(self.joker)
        turn = 0  # 0 for Andar, 1 for Bahar
        
        while self.deck:
            card = self.deck.pop(0)
            
            if turn == 0:
                self.andar_cards.append(card)
            else:
                self.bahar_cards.append(card)
                
            self.update_card_display()
            self.root.update()
            self.root.after(300)
            
            if self.get_card_value(card) == joker_value:
                winner = "Andar" if turn == 0 else "Bahar"
                self.end_game(winner)
                return
                
            turn = 1 - turn  # Alternate between Andar and Bahar
            
    def update_card_display(self):
        andar_text = "\n".join([f"{i+1}. {card}" for i, card in enumerate(self.andar_cards)])
        bahar_text = "\n".join([f"{i+1}. {card}" for i, card in enumerate(self.bahar_cards)])
        
        self.andar_display.config(text=andar_text)
        self.bahar_display.config(text=bahar_text)
        
    def end_game(self, winner):
        self.game_active = False
        
        if winner == self.bet_choice:
            winnings = self.bet_amount * 2
            self.balance += winnings
            messagebox.showinfo("You Won!", 
                              f"{winner} won!\nYou won ₹{winnings}!\nNew balance: ₹{self.balance}")
        else:
            messagebox.showinfo("You Lost!", 
                              f"{winner} won!\nYou lost ₹{self.bet_amount}.\nNew balance: ₹{self.balance}")
        
        self.update_display()
        
    def change_bet(self):
        bets = [50, 100, 200]
        current_index = bets.index(self.bet_amount)
        self.bet_amount = bets[(current_index + 1) % len(bets)]
        self.update_display()
        
    def update_display(self):
        self.balance_label.config(text=f"Balance: ₹{self.balance}")
        self.bet_label.config(text=f"Bet: ₹{self.bet_amount}")

if __name__ == "__main__":
    root = Tk()
    game = AndarBaharGame(root)
    root.mainloop()