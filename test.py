import streamlit as st
import webbrowser
import subprocess

def index():
    website_url = "http://127.0.0.1:5000/"  # Replace with your website URL
    your_content = "Hello,\nThis is a test.\n\nHere is another line of text."  # Replace with your own content
    background_color = "lightblue"  # Replace with the desired background color
    font_color = "white"  # Replace with the desired font color

    # Install required dependencies
    pip install -r requirements.txt

    # Open fullscreen and display content
    open_fullscreen(website_url, your_content, background_color, font_color)

    return "Python script executed successfully"

def open_fullscreen(url, content, bg_color, font_color):
    import tkinter as tk
    import webbrowser

    root = tk.Tk()
    root.attributes('-fullscreen', True)
    root.wm_attributes('-topmost', True)  # Set the window to be always on top

    def exit_fullscreen(event):
        root.destroy()

    root.bind('<Control-q>', exit_fullscreen)

    # Change the background color
    root.configure(bg=bg_color)

    # Open the website
    webbrowser.open_new(url)

    # Display your content
    label = tk.Label(root, text=content, font=('Helvetica', 18), bg=bg_color, fg=font_color)
    label.pack(pady=20)

    root.mainloop()

def install_dependencies():
    st.write("Installing required dependencies...")
    subprocess.run(["pip", "install", "package1", "package2", "package3"])  # Replace package names as needed

if __name__ == '__main__':
    index()
