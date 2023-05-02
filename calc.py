import tkinter as tk


class Calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("375x667")
        self.window.title("Calculator")
        self.window.resizable(1,1)

        self.total_expression = "0"
        self.current_expression ="0"

        self.display_frame = self.create_display_frame()
        self.display_button = self.create_button_frame()
        self.color_object = self.create_color_object()

    def create_color_object(self):
        self.LIGHT_GRAY = "#F5F5F5"

    def create_display_frame(self):
        frame = tk.Frame(self.window, height=221, bg=self.LIGHT_GRAY)
        frame.pack(expand =True, fill="both")
        return frame

    def create_button_frame(self):
        frame = tk.Frame(self.window)
        frame.pack(explan=True, fill="both")
        return frame

    def run(self):
        self.window.mainloop()

if __name__=="__main__":
    calc = Calculator()
    calc.run()