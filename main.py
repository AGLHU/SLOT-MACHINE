import random


MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winnings_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winnings_lines.append(line + 1)

    return winnings, winnings_lines

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    # Iterating through a dictionary, .items gives key and value associated with a dictionary
    for symbol, symbol_count in symbols.items():
        # _ is an anonymous variable, when you do not care about the count value
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    
    columns = []   # Define a reels list
    for _ in range(cols):    # Generate a column for each column we have, e.g. 3 cols, this runs 3 times
        # Pick random value for each row in our column
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")

        print()

# Collects user input for amount of money they wish to deposit
def deposit():
    # Continue to ask for deposit until there is enough money to play
    while True:
        deposit_amount = input("How much would you like to deposit? $")
        if deposit_amount.isdigit():
            deposit_amount = int(deposit_amount)
            if deposit_amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number.")

    return deposit_amount

def get_number_of_lines():
    # Pick a number from 1 to 3
    while True:
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Number must be between 1 and 3.")
        else:
            print("Please enter a number.")

    return lines


def get_bet():
    while True:
        deposit_amount = input("How much would you like to bet on each line? $")
        if deposit_amount.isdigit():
            deposit_amount = int(deposit_amount)
            if MIN_BET <= deposit_amount <= MAX_BET:
                break
            else:
                print(f"AMount must be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Please enter a number.")

    return deposit_amount
        

def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(
                f"You do not have enough to bet that amount, your current balance is ${balance}")
        else:
            break

    print(
        f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}.")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}!")
    print(f"You won on lines:", *winning_lines)
    return winnings - total_bet

def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press enter to play (q to quit).")
        if answer == "q":
            break
        balance += spin(balance)

    print(f"You left with ${balance}")

main()
