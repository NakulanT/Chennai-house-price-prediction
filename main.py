import pandas as pd
import pickle
from sklearn.ensemble import GradientBoostingRegressor

# Load the model
with open('model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

# Dictionaries for categorical features
Area = {0: 'Karapakam', 1: 'AnnaNagar', 2: 'Adyar', 3: 'Velachery', 4: 'Chrompet', 5: 'KKNagar', 6: 'TNagar'}
Parking = {1: 'Yes', 0: 'No'}
Distance_from_main_road = {1: 'Near', 2: 'Mid', 3: 'Far'}

# Function to get user input for features
def get_user_input():
    print("📌 Dictionary:\n", Area)

    while True:
        area_input = input(f"Enter Area ({', '.join(Area.values())}): ").strip().title()
        if area_input in Area.values():
            break
        else:
            print("Invalid Area. Please enter a valid value.")

    AREA = next(key for key, value in Area.items() if value.lower() == area_input.lower())

    # Remaining input as before
    INT_SQFT = int(input("Enter INT_SQFT: "))
    DIST_MAINROAD = int(input("Enter DIST_MAINROAD: "))
    N_BEDROOM = float(input("Enter N_BEDROOM: "))
    N_BATHROOM = float(input("Enter N_BATHROOM: "))
    N_ROOM = float(input("Enter N_ROOM: "))
    PARK_FACIL = int(input("Enter PARK_FACIL (0 for No, 1 for Yes): "))

    # Create a DataFrame with user input
    user_data = pd.DataFrame({
        'AREA': [AREA],
        'INT_SQFT': [INT_SQFT],
        'DIST_MAINROAD': [DIST_MAINROAD],
        'N_BEDROOM': [N_BEDROOM],
        'N_BATHROOM': [N_BATHROOM],
        'N_ROOM': [N_ROOM],
        'PARK_FACIL': [PARK_FACIL]
    })

    return user_data


# Function to make predictions
def predict_sales_price(user_data):
    prediction = model.predict(user_data)
    return prediction[0]

# Main function
def main():
    # Get user input
    user_data = get_user_input()

    # Display the input data
    print("\nInput Data:")
    print(user_data)

    # Make predictions
    predicted_sales_price = predict_sales_price(user_data)

    # Display the predicted sales price
    print("\nPredicted Sales Price:", predicted_sales_price)

if __name__ == "__main__":
    main()
