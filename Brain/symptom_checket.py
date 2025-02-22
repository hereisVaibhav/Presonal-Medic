def swap_salaries():
    alice_salary = int(input())
    bob_salary = float(input())

    print("Initial salaries:")
    print(f"Alice's salary = {alice_salary}")
    print(f"Bob's salary = {bob_salary}")

    # Swap salaries
    temp_salary = alice_salary
    alice_salary = bob_salary
    bob_salary = temp_salary

    print("New salaries after swapping")  # No newline here!
    print(f"Alice's salary = {alice_salary}")
    print(f"Bob's salary = {bob_salary}")

swap_salaries()