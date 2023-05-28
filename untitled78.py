import streamlit as st
def main():
    st.title("My Streamlit App")
    
    # Add your Streamlit app content here
    st.write("Welcome to my app!")
    
    # Example of adding a button to the app
    if st.button("Click me!"):
        st.write("Button clicked!")
    
    # Example of adding a selectbox to the app
    options = ["Option 1", "Option 2", "Option 3"]
    selected_option = st.selectbox("Choose an option", options)
    st.write("You selected:", selected_option)
    
if __name__ == "__main__":
    main()
