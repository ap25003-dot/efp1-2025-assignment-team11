from services import RentalSystem
from datetime import datetime, date


def parse_date(date_str):
    try:
        return datetime.strptime(date_str, "%Y-%m-%d").date()
    except ValueError:
        return None


def main():
    system = RentalSystem()
    print("Καλωσήρθατε στο σύστημα ενοικίασης οχημάτων")

    # LOGIN
    while True:
        name = input("Όνομα πελάτη: ")
        email = input("Email πελάτη: ")

        customer = system.find_customer(name, email)

        if customer:
            print(f"Καλώς ήρθες, {customer.name}!")
            break
        else:
            print("Δεν βρέθηκε πελάτης με αυτά τα στοιχεία. Προσπαθήστε ξανά.")

    while True:
        print("\n--- Μενού ---")
        print("1. Αναζήτηση οχήματος")
        print("2. Προβολή των ενοικιάσεών μου")
        print("0. Έξοδος")

        choice = input("Επιλογή: ")

        # ---------------------------------------------------
        # 1. Αναζήτηση οχήματος
        # ---------------------------------------------------
        if choice == "1":

            # Έλεγχος ημερομηνιών
            while True:
                start_str = input("Ημερομηνία έναρξης (YYYY-MM-DD): ")
                end_str = input("Ημερομηνία λήξης (YYYY-MM-DD): ")

                start_date = parse_date(start_str)
                end_date = parse_date(end_str)

                if not start_date or not end_date:
                    print("Μη έγκυρη μορφή ημερομηνίας.")
                    continue

                today = date.today()

                if start_date < today:
                    print("Η ημερομηνία έναρξης δεν μπορεί να είναι στο παρελθόν.")
                    continue

                if end_date < today:
                    print("Η ημερομηνία λήξης δεν μπορεί να είναι στο παρελθόν.")
                    continue

                if end_date < start_date:
                    print("Η ημερομηνία λήξης πρέπει να είναι μετά την έναρξη.")
                    continue

                break

            available = system.search_available_vehicles(start_date, end_date)

            if not available:
                print("Δεν υπάρχουν διαθέσιμα οχήματα.")
                continue

            print("\nΔιαθέσιμα οχήματα:")
            for v in available:
                print(v)

            # Επιλογή οχήματος με επανάληψη
            while True:
                try:
                    vehicle_id = int(input("Δώσε ID οχήματος για κράτηση: "))
                except ValueError:
                    print("Το ID πρέπει να είναι αριθμός.")
                    continue

                vehicle = system.find_vehicle_by_id(vehicle_id)

                if not vehicle:
                    print("Δεν υπάρχει όχημα με αυτό το ID.")
                    continue

                
                break

            rental = system.create_rental(customer.user_id, vehicle_id, start_str, end_str)
            print("Η κράτηση ολοκληρώθηκε:")
            print(rental)

        # ---------------------------------------------------
        # 2. Προβολή ενοικιάσεων
        # ---------------------------------------------------
        elif choice == "2":

            # Υπομενού σε loop
            while True:
                print("\n--- Ενοικιάσεις ---")
                print("a. Ολοκληρωμένες")
                print("b. Μη ολοκληρωμένες")
                print("c. Επιστροφή στο μενού")

                sub = input("Επιλογή: ")

                # Completed rentals
                if sub == "a":
                    completed = system.completed_rentals_for_customer(customer.user_id)

                    if not completed:
                        print("Δεν υπάρχουν ολοκληρωμένες ενοικιάσεις.")
                        continue

                    for r in completed:
                        print(r)

                    # Επιλογή rental_id με επανάληψη
                    while True:
                        try:
                            rental_id = int(input("Δώσε ID για αξιολόγηση: "))
                        except ValueError:
                            print("Το ID πρέπει να είναι αριθμός.")
                            continue

                        rental = next((r for r in completed if r.rental_id == rental_id), None)

                        if not rental:
                            print("Δεν υπάρχει ολοκληρωμένη ενοικίαση με αυτό το ID.")
                            continue

                        break

                    # Βαθμολογία οχήματος
                    while True:
                        try:
                            score_vehicle = int(input("Βαθμολογία οχήματος (1-5): "))
                        except ValueError:
                            print("Η βαθμολογία πρέπει να είναι αριθμός.")
                            continue

                        if not (1 <= score_vehicle <= 5):
                            print("Η βαθμολογία πρέπει να είναι από 1 έως 5.")
                            continue

                        break

                    # Βαθμολογία ιδιοκτήτη
                    while True:
                        try:
                            score_owner = int(input("Βαθμολογία ιδιοκτήτη (1-5): "))
                        except ValueError:
                            print("Η βαθμολογία πρέπει να είναι αριθμός.")
                            continue

                        if not (1 <= score_owner <= 5):
                            print("Η βαθμολογία πρέπει να είναι από 1 έως 5.")
                            continue

                        break

                    comment = input("Σχόλιο: ")

                    rating = system.submit_or_change_rating(
                        customer_id=customer.user_id,
                        rental_id=rental_id,
                        score_vehicle=score_vehicle,
                        score_owner=score_owner,
                        comment=comment
                    )

                    if rating:
                        print("Η αξιολόγηση καταχωρήθηκε:")
                        print(rating)

                    break  # ΕΠΙΣΤΡΟΦΗ ΣΤΟ ΚΕΝΤΡΙΚΟ ΜΕΝΟΥ

                # Pending rentals
                elif sub == "b":
                    rentals = system.pending_rentals_for_customer(customer.user_id)
                    if not rentals:
                        print("Δεν υπάρχουν μη ολοκληρωμένες ενοικιάσεις.")
                    else:
                        for r in rentals:
                            print(r)
                    continue

                elif sub == "c":
                    break

                else:
                    print("Μη έγκυρη επιλογή.")
                    continue

        elif choice == "0":
            print("Έξοδος από το σύστημα. Αντίο!")
            break

        else:
            print("Μη έγκυρη επιλογή.")


if __name__ == "__main__":
    main()
