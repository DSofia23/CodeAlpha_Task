import task1_hangman
import task2_stock_portfolio
import task4_chatbot

def main():
    while True:
        print("\n===============================")
        print("   PYTHON MINI PROJECT MENU    ")
        print("===============================")
        print("1. Hangman Game")
        print("2. Stock Portfolio Tracker")
        print("3. Basic Chatbot")
        print("4. Exit")
        print("===============================\n")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            task1_hangman.play_hangman()

        elif choice == "2":
            task2_stock_portfolio.start_portfolio_tracker()

        elif choice == "3":
            task4_chatbot.chatbot()

        elif choice == "4":
            print("Thank you for using the project!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
