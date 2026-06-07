import streamlit as st
from pathlib import Path

# --- FOLDER SETUP ---
# Ek alag folder banate hain jahan saari files save hongi
BASE_DIR = Path("MyFiles")
BASE_DIR.mkdir(exist_ok=True) # Agar folder nahi hai, to bana dega

# Helper function: Folder ke andar ki saari files ki list lane ke liye
def get_file_list():
    return [f.name for f in BASE_DIR.iterdir() if f.is_file()]

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="File Handler", page_icon="📁", layout="centered")

# --- HEADER ---
st.title("📁 Modern File Handler")
st.markdown("A simple, responsive UI for managing your local files.")
st.divider()

# --- NAVIGATION TABS ---
tab1, tab2, tab3, tab4 = st.tabs(["Create ➕", "Read 📖", "Update 🔄", "Delete ❌"])

# --- TAB 1: CREATE ---
with tab1:
    st.subheader("Create a New File")
    c_name = st.text_input("Enter file name (e.g., text.txt):", key="c_name")
    c_content = st.text_area("Enter file content:", key="c_content", height=150)
    
    if st.button("Create File", type="primary"):
        if c_name:
            path = BASE_DIR / c_name
            if not path.exists():
                try:
                    with open(path, "w") as f:
                        f.write(c_content)
                    st.success(f"File '{c_name}' created successfully in 'MyFiles' folder!")
                except Exception as err:
                    st.error(f"An error occurred: {err}")
            else:
                st.error("Error! File already exists.")
        else:
            st.warning("Please provide a file name.")

# --- TAB 2: READ ---
with tab2:
    st.subheader("Read an Existing File")
    files = get_file_list()
    
    if not files:
        st.info("No files available. Please create a file first.")
    else:
        # User ko list dikhane ke liye selectbox ka use
        r_name = st.selectbox("Select file to read:", files, key="r_name")
        
        if st.button("Read File"):
            path = BASE_DIR / r_name
            try:
                with open(path, "r") as f:
                    content = f.read()
                st.info(f"Viewing: {r_name}")
                st.code(content, language="text")
            except Exception as err:
                st.error(f"An error occurred: {err}")

# --- TAB 3: UPDATE ---
with tab3:
    st.subheader("Update a File")
    files = get_file_list()
    
    if not files:
        st.info("No files available to update.")
    else:
        u_name = st.selectbox("Select file to update:", files, key="u_name")
        
        update_action = st.radio(
            "Choose update operation:",
            ("Rename File", "Append Content", "Overwrite Content"),
            horizontal=True
        )

        path = BASE_DIR / u_name

        # Sub-logic for Renaming
        if update_action == "Rename File":
            new_name = st.text_input("Enter new file name:", key="new_name")
            if st.button("Rename"):
                if new_name:
                    new_path = BASE_DIR / new_name
                    if not new_path.exists():
                        try:
                            path.rename(new_path)
                            st.success(f"Renamed '{u_name}' to '{new_name}' successfully!")
                        except Exception as err:
                            st.error(f"An error occurred: {err}")
                    else:
                        st.error(f"Error! The file '{new_name}' already exists.")
                else:
                    st.warning("Please provide a new file name.")

        # Sub-logic for Appending
        elif update_action == "Append Content":
            append_data = st.text_area("Content to append:", key="append_data")
            if st.button("Append"):
                try:
                    with open(path, "a") as f:
                        f.write("\n" + append_data)
                    st.success("Content appended successfully!")
                except Exception as err:
                    st.error(f"An error occurred: {err}")

        # Sub-logic for Overwriting
        elif update_action == "Overwrite Content":
            overwrite_data = st.text_area("New content to overwrite:", key="overwrite_data")
            if st.button("Overwrite"):
                try:
                    with open(path, "w") as f:
                        f.write(overwrite_data)
                    st.success("File overwritten successfully!")
                except Exception as err:
                    st.error(f"An error occurred: {err}")

# --- TAB 4: DELETE ---
with tab4:
    st.subheader("Delete a File")
    files = get_file_list()
    
    if not files:
        st.info("No files available to delete.")
    else:
        d_name = st.selectbox("Select file to delete:", files, key="d_name")
        st.warning("⚠️ Warning: This action cannot be undone.")
        
        if st.button("Delete File", type="primary"): 
            path = BASE_DIR / d_name
            try:
                path.unlink()
                st.success(f"File '{d_name}' deleted successfully!")
            except Exception as err:
                st.error(f"An error occurred: {err}")

# --- FOOTER ---
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: gray; padding: 10px;'>Created by Divyakant</div>",
    unsafe_allow_html=True
)