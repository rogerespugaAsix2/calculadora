import streamlit as st

def calculate_combinations(password_length, charset_lengths):
    """
    Calculate the total number of password combinations given the password length and the lengths of the selected character sets.
   
    Args:
    password_length (int): The desired length of the password.
    charset_lengths (list): The lengths of the character sets selected by the user.
   
    Returns:
    int: The total number of possible combinations.
    """
    total_combinations = 1
    for length in charset_lengths:
        total_combinations *= length
    return total_combinations ** password_length

def main():
    # Streamlit interface setup
    st.title("Calculadora de Fuerza Bruta de Contraseñas")
   
    # User inputs
    password_length = st.number_input("Longitud de la contraseña", min_value=1, max_value=20, value=1)
    charset_options = ("Solo números", "Solo letras minúsculas", "Solo letras mayúsculas",
                       "Letras minúsculas y mayúsculas", "Alfanumérico", "Alfanumérico con símbolos")
    selected_charsets = st.multiselect("Conjuntos de caracteres", charset_options)
   
    # Define charset lengths
    charset_lengths = {
        "Solo números": 10,  # 0-9
        "Solo letras minúsculas": 26,  # a-z
        "Solo letras mayúsculas": 26,  # A-Z
        "Letras minúsculas y mayúsculas": 52,  # a-z + A-Z
        "Alfanumérico": 62,  # a-z + A-Z + 0-9
        "Alfanumérico con símbolos": 92  # a-z + A-Z + 0-9 + punctuation
    }
   
    # Get lengths of selected charsets
    selected_charset_lengths = [charset_lengths[option] for option in selected_charsets]
   
    # Calculate combinations
    total_combinations = calculate_combinations(password_length, selected_charset_lengths)
   
    # Display results
    st.write(f"Total de combinaciones posibles: {total_combinations:,}")

if __name__ == "__main__":
    main()

