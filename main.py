import pandas as pd
import joblib

# Load the pre-trained model
model = joblib.load('model.pkl')

# Dictionary mappings for categorical features
Area_mapping = {0: 'Karapakkam', 1: 'AnnaNagar', 2: 'Adyar', 3: 'Velachery', 4: 'Chromepet', 5: 'KKNagar', 6: 'TNagar'}
Parking_mapping = {1: 'Yes', 0: 'No'}
Distance_mapping = {1: 'Near', 2: 'Mid', 3: 'Far'}

# Function to get user input for features
def get_user_input():
    AREA = int(input(f"Enter Area (0-{len(Area_mapping) - 1}): "))
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

    # Map numerical values to categorical values
    user_data['AREA'] = user_data['AREA'].map(Area_mapping)
    user_data['PARK_FACIL'] = user_data['PARK_FACIL'].map(Parking_mapping)

    # Display the input data
    print("\nInput Data:")
    print(user_data)

    # Make predictions
    predicted_sales_price = predict_sales_price(user_data)

    # Display the predicted sales price
    print("\nPredicted Sales Price:", predicted_sales_price)

if __name__ == "__main__":
    main()