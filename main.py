# main.py

import tkinter as tk
from tkinter import filedialog
from file_finder import FileFinder
from api_integration import APIIntegration
from text_appender import TextAppender

class Application:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Markdown File Processor")

        self.directory = ""
        self.file_finder = FileFinder()
        self.api_integration = APIIntegration()
        self.text_appender = TextAppender()

        self.create_widgets()

    def create_widgets(self):
        self.directory_label = tk.Label(self.root, text="Selected Directory:")
        self.directory_label.grid(row=0, column=0)

        self.directory_button = tk.Button(self.root, text="Select Directory", command=self.select_directory)
        self.directory_button.grid(row=1, column=0, pady=5)

        self.process_button = tk.Button(self.root, text="Process Files", command=self.process_files)
        self.process_button.grid(row=2, column=0, pady=5)

        self.send_button = tk.Button(self.root, text="Send File", command=self.send_file)
        self.send_button.grid(row=3, column=0, pady=5)

        self.append_button = tk.Button(self.root, text="Append Text", command=self.append_text)
        self.append_button.grid(row=4, column=0, pady=5)

        # Create a frame to hold the listbox and scrollbar
        self.frame = tk.Frame(self.root)
        self.frame.grid(row=5, column=0, pady=5, sticky='nsew')
        self.root.grid_rowconfigure(5, weight=1)  # Allow frame to expand vertically
        self.root.grid_columnconfigure(0, weight=1)  # Allow frame to expand horizontally

        self.file_listbox = tk.Listbox(self.frame, selectmode='multiple', width=50)  # Adjust width as required
        self.file_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.scrollbar = tk.Scrollbar(self.frame, orient=tk.VERTICAL)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.xscrollbar = tk.Scrollbar(self.frame, orient=tk.HORIZONTAL)
        self.xscrollbar.pack(side=tk.BOTTOM, fill=tk.X)

        # Configure the listbox to use the scrollbars
        self.file_listbox.config(yscrollcommand=self.scrollbar.set, xscrollcommand=self.xscrollbar.set)
        self.scrollbar.config(command=self.file_listbox.yview)
        self.xscrollbar.config(command=self.file_listbox.xview)

        self.root.mainloop()




    def select_directory(self):
        self.directory = filedialog.askdirectory()
        self.directory_label.config(text="Selected Directory: " + self.directory)

    def process_files(self):
        if self.directory:
            files = self.file_finder.find_files(self.directory)
            file_names = []  # New list to store file names
            for file in files:
                #self.send_file(file)
                file_names.append(file) # Store file names
                self.file_listbox.insert(tk.END, file)  # Add file name to listbox
        else:
            print("No directory selected.")

    # def send_file(self, file):
    #     response = self.api_integration.send_file(file)
    #     if response:
    #         self.append_text(file, response)

    def send_file(self):
        response = self.api_integration.test_gpt_openai("summarize the following text: GPT4All Chat comes with a built-in server mode allowing you to programmatically interact with any supported local LLM through a very familiar HTTP API. You can find the API documentation here.Enabling server mode in the chat client will spin-up on an HTTP server running on localhost port 4891 (the reverse of 1984). You can enable the webserver via GPT4All Chat > Settings > Enable web server.Begin using local LLMs in your AI powered apps by changing a single line of code: the base path for requests. ")
        if response:
            print("This is the response from main:" + response)

    def append_text(self, file, processed_text):
        self.text_appender.append_text(file, processed_text)

if __name__ == "__main__":
    app = Application()
