import streamlit as st

st.title('Password Checker')

password = st.text_input(label="Password", placeholder="Enter your password", type="password")

def validate(password):
    if not password:
        st.warning("Please enter a password")
        return
    strength = 0
    lower_case = upper_case = digit = white_space = special_char = 0
    for char in list(password):
        if char.islower():
            lower_case += 1
        elif char.isupper():
            upper_case += 1
        elif char.isdigit():
            digit += 1
        elif char.isspace():
            white_space += 1
        else:
            special_char += 1
    
    if lower_case > 0:
        strength += 1
    if upper_case > 0:
        strength += 1
    if digit > 0:
        strength += 1  
    if special_char > 0:
        strength += 1
    if white_space == 0:
        strength += 1
    if len(password) >= 8:
        strength += 1

    return strength, lower_case, upper_case, digit, white_space, special_char

if st.button("Check"):
    strength, lower_case, upper_case, digit, white_space, special_char = validate(password)

    if strength == 1:
        st.error("Password Strength: Very Weak")
    elif strength == 2:
        st.warning("Password Strength: Weak")
    elif strength == 3:
        st.info("Password Strength: Medium")
    elif strength == 4:
        st.success("Password Strength: Strong")
    elif strength == 5:
        st.success("Password Strength: Very Strong")
    else: 
        st.balloons()
        st.success("Password Strength: Excellent")
    
    st.write(
        f"Password contains:\n"
        f"- {len(password)} characters\n"
        f"- {lower_case} lowercase\n"
        f"- {upper_case} uppercase\n"
        f"- {digit} digits\n"
        f"- {special_char} special characters\n"
        f"- {white_space} spaces"
    )

    if strength < 4:
        st.info("Tips to improve your password:\n"
                "- Use a mix of uppercase and lowercase letters\n"
                "- Include numbers and special characters\n"
                "- Avoid spaces\n"
                "- Make it at least 8 characters long")
    elif strength >= 4 and strength < 6:
        st.success("Great! Your password is strong.")
    else:
        st.success("Fantastic! Your password is unhackable(^_^).")