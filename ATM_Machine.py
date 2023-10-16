working_Status = True;
Balance = 0;

while working_Status:
    input_Number = int(input("Wählen Sie ihren Vorgang:\n"
                             "1. Einzahlen\n"
                             "2. Abheben\n"
                             "3. Kontostand\n"
                             "4. Beenden\n"))

    if input_Number == 1:
        deposit = int(input("Geben Sie den Betrag welchen Sie einzahlen möchten ein\n"))
        print("Sie haben erfolgreich: " + str(deposit) + " Euro auf ihr Konto eingezahlt")
        Balance += deposit;

    elif input_Number == 2:
        take_Off = int(input("Geben Sie den Betrag welchen Sie auszahlen möchten ein\n"))
        if take_Off > Balance:
            print("Sie können nur " + str(Balance) + " abheben")
        else:
            print("Sie haben erfolgreich: " + str(take_Off) + " Euro abgehoben")
            Balance -= take_Off

    elif input_Number == 3:
        print("Ihr Kontostand beträgt: " + str(Balance) + " Euro")

    elif input_Number == 4:
        working_Status = False;
        break;




