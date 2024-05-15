from tkinter import *
from functools import partial  # To prevent unwanted windows


class Converter:

    def __init__(self):
        # common format for al l buttons
        # Arial size 14 bold, with white text
        button_font = ("Arial", "12", "bold")
        button_fg = "#FFFFFF"

        # set up GUI frame
        self.temp_frame = Frame(padx=10, pady=10)
        self.temp_frame.grid()

        # Conversion, help and history / export buttons
        self.button_frame = Frame(padx=30, pady=30)
        self.button_frame.grid(row=0)

        self.to_help_button = Button(self.button_frame,
                                     text="Help / Info",
                                     bg="#CC6600",
                                     fg=button_fg,
                                     font=button_font,
                                     width=12,
                                     command=self.to_help)
        self.to_help_button.grid(row=1, column=0, padx=5, pady=5)

    def to_help(self):
        DisplayHelp(self)


class DisplayHelp:

    def __init__(self, partner):

        # setup dialogue box and background colour
        background = "#ffe6cc"
        self.help_box = Toplevel()

        # disable help button
        partner.to_help_button.config(state=DISABLED)

        # If users press cross at top, closes help and
        # 'releases' help button
        self.help_box.protocol('WM_DELETE_WINDOW',
                               partial(self.close_help, partner))

        self.help_frame = Frame(self.help_box, width=500,
                                height=200,
                                bg=background)
        self.help_frame.grid()

        self.input_frame = Frame(self.help_frame,
                                 width=500,
                                 height=200,
                                 pady=20,
                                 bg=background)
        self.input_frame.grid(row=2)

        self.help_heading_label = Label(self.help_frame, bg=background,
                                        text="Help / Info",
                                        font=("Arial", "14", "bold"))
        self.help_heading_label.grid(row=0)

        help_text = "This program can be used to gauge whether or not you are " \
                    "around about a healthy weight with regards to your height. " \
                    "It should not be taken as medical advice, but rather can be" \
                    "taken as a loose guide to whether or not you should seek " \
                    "restorative measures regarding your weight. To use the " \
                    "program, simply enter your height and weight into the " \
                    "allocated entries to find be given your BMI value. Make " \
                    "to only use numbers, such as Height: 180, Weight: 80. The " \
                    "units are metric, so the height is measure in centimetres " \
                    "and the weight in kgs. After you are given you're value you " \
                    "you can enter it below to be given information about your " \
                    "height to weight ratio."
        self.help_text_label = Label(self.help_frame, bg=background,
                                     text=help_text, wraplength=500,
                                     justify="left")
        self.help_text_label.grid(row=1, padx=10)

        self.bmi_label = Label(self.input_frame,
                               bg=background,
                               font=("Arial", "16", "bold"),
                               text="Input BMI Value:")
        self.bmi_label.grid(row=0, column=0)

        self.bmi_entry = Entry(self.input_frame,
                               font=("Arial", "20"),
                               width=5)
        self.bmi_entry.grid(row=0, column=1, padx=10, pady=10)

        self.inform_me_button = Button(self.input_frame,
                                       bg="dark blue",
                                       fg="white",
                                       font=("Arial", "12", "bold"),
                                       text="Inform Me")
        self.inform_me_button.grid(row=0, column=2)

        self.dismiss_button = Button(self.help_frame,
                                     font=("Arial", "12", "bold"),
                                     text="Dismiss", bg="#CC6600",
                                     fg="#FFFFFF",
                                     command=partial(self.close_help,
                                                     partner))
        self.dismiss_button.grid(row=3, padx=10, pady=10)

    # closes help dialogue (used by button and x at top of dialogue)
    def close_help(self, partner):
        # Put help button back to normal...
        partner.to_help_button.config(state=NORMAL)
        self.help_box.destroy()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("BMI Calculator")
    Converter()
    root.mainloop()
