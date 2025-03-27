import streamlit as st

def calculate_additional_5_star_reviews(current_reviews, current_rating, target_rating):
    # Calculate the current total rating score
    current_total_score = current_rating * current_reviews
    
    # Define X as the number of new 5-star reviews needed
    X = 0  # Start with zero additional reviews
    
    while True:
        new_total_reviews = current_reviews + X
        new_total_score = current_total_score + (5 * X)
        new_average_rating = new_total_score / new_total_reviews
        
        if new_average_rating >= target_rating:
            return X  # Return the number of additional 5-star reviews needed
        
        X += 1  # Increment X and check again

# Streamlit UI
st.title("⭐ Amazon Rating Calculator")
st.write("Calculate how many additional 5-star reviews you need to reach your target rating!")

# User input
current_reviews = st.number_input("Current Number of Reviews:", min_value=1, step=1)
current_rating = st.number_input("Current Rating (out of 5):", min_value=1.0, max_value=5.0, step=0.1)
target_rating = st.number_input("Target Rating (out of 5):", min_value=1.0, max_value=5.0, step=0.1)

if st.button("Calculate"):
    if target_rating <= current_rating:
        st.warning("Target rating must be higher than current rating.")
    else:
        additional_reviews = calculate_additional_5_star_reviews(current_reviews, current_rating, target_rating)
        st.success(f"You need approximately {additional_reviews} more 5-star reviews to reach a {target_rating} rating.")
