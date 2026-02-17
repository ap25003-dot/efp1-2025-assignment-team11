
from datetime import datetime, date


def parse_date(date_str):
    try:
        return datetime.strptime(date_str, "%Y-%m-%d").date()
    except ValueError:
        return None




        choice = input("Επιλογή: ")



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
