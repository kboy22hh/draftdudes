
grade_scale = {
        'A': 4.0, 'A-': 3.7, 'B+': 3.3, 'B': 3.0, 'B-': 2.7,
        'C+': 2.3, 'C': 2.0, 'C-': 1.7, 'D+': 1.3, 'D': 1.0, 
        'D-': 0.7, 'F': 0.0
    }

def get_number_points(grade):
    scale = {
        10: 4.0, 9: 3.7, 8: 3.3, 7: 3.0, 6: 2.7,
        5: 2.3, 4: 2.0, 3: 1.7, 2: 1.3, 1: 1.0
    }
    try:
        return scale.get(int(grade), 0.0)
    except ValueError:
        return 0.0
    

total_sum = 0
num_inputs = 4

for i in range(num_inputs):
    user_input = int(input(f"Enter number {i + 1} of {num_inputs}: "))
    total_sum += user_input


average = total_sum / num_inputs

total_points = 0.0
num_inputs = 11

print("Please enter letter grades (e.g., A, B+, C-):")

for i in range(num_inputs):
    while True:
        # Get input, remove trailing spaces, and convert to uppercase
        letter = input(f"Grade {i + 1} of {num_inputs}: ").strip().upper()
        
        # Check if the entered letter grade exists in our scale dictionary
        if letter in grade_scale:
            total_points += grade_scale[letter]
            break # Valid grade entered, exit the while loop to get the next input
        else:
            print("Invalid grade. Please enter a valid letter grade (A, B, C, D, F, etc.).")

# Calculate the final GPA average
gpa_average = total_points / num_inputs

print((get_number_points(average) * 0.7) + (gpa_average * .3))
