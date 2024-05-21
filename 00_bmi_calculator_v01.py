from tkinter import *
from functools import partial  # To prevent unwanted windows


class Converter:

    @staticmethod
    def round_ans(val):
        var_rounded = "{:.1f}".format(val)
        return var_rounded

    # convert height and weight inputs to bmi value
    def bmi_calculate(self):

        height = self.check_height()
        weight = self.check_weight()

        if height == "amount":
            answer = "Please enter a height higher than 0cm"
        elif weight == "amount":
            answer = "Please enter a weight higher than 0kg"
        elif height == "number" or weight == "number":
            answer = "Please make sure both entries are numbers"
        else:
            self.output_answer()
            answer = (weight / (height * height)) * 10000
            answer = self.round_ans(answer)

        self.output_label.config(text=answer)

    def check_height(self):

        has_error = "no"

        height_response = self.height_entry.get()

        try:
            height_response = float(height_response)

            if height_response <= 0:
                has_error = "amount"

        except ValueError:
            has_error = "number"

        if has_error == "no":
            return height_response
        else:
            return has_error

    def check_weight(self):

        has_error = "no"

        weight_response = self.weight_entry.get()

        try:
            weight_response = float(weight_response)

            if weight_response < 0:
                has_error = "amount"

        except ValueError:
            has_error = "number"

        if has_error == "no":
            return weight_response
        else:
            return has_error

    def output_answer(self):
        has_errors = self.height_entry.get()

        if has_errors == "no":

            has_errors = self.check_weight()

            if has_errors == "no":

                self.output_label.config(fg="#004C00")
                self.height_entry.config(bg="#FFFFFF")
                self.weight_entry.config(bg="#FFFFFF")

        else:

            self.output_label.config(fg="#9C0000")
            self.height_entry.config(bg="#F8CECC")
            self.weight_entry.config(bg="#F8CECC")

    def __init__(self):
        # Initialise variables (such as the feedback variable)
        self.var_feedback = StringVar()
        self.var_feedback.set("")

        self.var_has_error = StringVar()
        self.var_has_error.set("no")

        # common format for all buttons
        # Arial size 14 bold, with white text
        button_font = ("Arial", "12", "bold")
        button_fg = "#FFFFFF"

        # set up GUI frame
        self.bmi_frame = Frame()
        self.bmi_frame.grid()

        self.bmi_heading = Label(self.bmi_frame,
                                 text="BMI CALCULATOR",
                                 font=("Arial", "16", "bold")
                                 )
        self.bmi_heading.grid(row=0)

        instructions = "Enter your height, weight and age below in the allocated input" \
                       " boxes and then press calculate to be given your current BMI " \
                       "status."
        self.bmi_instructions = Label(self.bmi_frame,
                                      text=instructions,
                                      wraplength=250, width=40,
                                      justify="left")
        self.bmi_instructions.grid(row=1, column=0)

        # Conversion, help and history / export buttons
        self.button_frame = Frame(self.bmi_frame)
        self.button_frame.grid(row=4)

        self.output_label = Label(self.bmi_frame, text="",
                                  fg="#9C0000")
        self.output_label.grid(row=3)

        self.height_entry = Entry(self.button_frame,
                                  font=("Arial", "14"),
                                  width=12
                                  )
        self.height_entry.grid(row=0, column=1, padx=10, pady=10)

        self.weight_entry = Entry(self.button_frame,
                                  font=("Arial", "14"),
                                  width=12
                                  )
        self.weight_entry.grid(row=1, column=1, padx=10, pady=10)

        self.age_entry = Entry(self.button_frame,
                               font=("Arial", "14"),
                               width=12
                               )
        self.age_entry.grid(row=2, column=1, padx=10, pady=10)

        self.height_label = Label(self.button_frame,
                                  text="HEIGHT:",
                                  justify="right",
                                  font=("Arial", "14"),
                                  width=12
                                  )
        self.height_label.grid(row=0, column=0, padx=5, pady=10)

        self.weight_label = Label(self.button_frame,
                                  text="WEIGHT:",
                                  justify="right",
                                  font=("Arial", "14"),
                                  width=12
                                  )
        self.weight_label.grid(row=1, column=0, padx=5, pady=10)

        self.age_label = Label(self.button_frame,
                               text="AGE:",
                               justify="right",
                               font=("Arial", "14"),
                               width=12
                               )
        self.age_label.grid(row=2, column=0, padx=5, pady=10)

        self.to_history_button = Button(self.button_frame,
                                        text="History / Export",
                                        bg="#004C99",
                                        fg=button_fg,
                                        font=button_font,
                                        width=12,
                                        state=DISABLED
                                        )
        self.to_history_button.grid(row=0, column=2, padx=5, pady=5)

        self.to_help_button = Button(self.button_frame,
                                     text="Help / Info",
                                     bg="#CC6600",
                                     fg=button_fg,
                                     font=button_font,
                                     width=12,
                                     command=self.to_help)
        self.to_help_button.grid(row=1, column=2, padx=5, pady=5)

        self.to_calculate_button = Button(self.bmi_frame,
                                          text="Calculate",
                                          bg="#CC6600",
                                          fg=button_fg,
                                          font=button_font,
                                          width=36,
                                          command=lambda: self.bmi_calculate()
                                          )
        self.to_calculate_button.grid(row=5, padx=5, pady=5)

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

        self.information_frame = Frame(self.help_frame,
                                       width=500,
                                       pady=20,
                                       bg=background)
        self.information_frame.grid(row=3)

        self.help_heading_label = Label(self.help_frame, bg=background,
                                        text="Help / Info",
                                        font=("Arial", "14", "bold"),
                                        pady=15)
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
                                     font=("Arial", "9"),
                                     pady=10)
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
                                       text="Inform Me",
                                       command=lambda: self.inform_me())
        self.inform_me_button.grid(row=0, column=2)

        self.dismiss_button = Button(self.help_frame,
                                     font=("Arial", "12", "bold"),
                                     text="Dismiss", bg="#CC6600",
                                     fg="#FFFFFF",
                                     command=partial(self.close_help,
                                                     partner))
        self.dismiss_button.grid(row=4, padx=10, pady=10)

        self.value_label = Label(self.information_frame,
                                 font=("Arial", "16", "bold"),
                                 bg=background,
                                 padx=50)

        self.information_label = Label(self.information_frame,
                                       font=("Arial", "9"),
                                       wraplength=400,
                                       bg=background,
                                       padx=25)

    def information_check(self):

        bmi_value = self.bmi_entry.get()
        bmi_value = float(bmi_value)

        if bmi_value < 18.5:
            text = "You are underweight. Consider taking measures " \
                   "such as increasing caloric intake and maintaining " \
                   "a solid exercise regimen. If you are " \
                   "worried about your weight, it might be best " \
                   "to visit a doctor for a more comprehensive " \
                   "analysis and professional advice."

        elif 18.5 <= bmi_value <= 24.9:
            text = "You are a relatively healthy weight. It is " \
                   "unlikely you have or will have any issues " \
                   "regarding your weight. This does not mean " \
                   "you are necessarily of perfect health, " \
                   "if you are worried about any aspect of your " \
                   "health, do not hesitate to visit a doctor."

        elif 24.9 < bmi_value <= 29.9:
            text = "You are overweight. You could consider measures " \
                   "such as increasing caloric intake and/or increasing " \
                   "your amount of exercise per week. If you feel as though " \
                   "your excess of weight is affecting your life, it would " \
                   "not be ill-advised to visit your local doctor."

        elif 29.9 < bmi_value <= 39.9:
            text = "You are considered obese. You could consider measures " \
                   "such as decreasing caloric intake and/or increasing " \
                   "your amount of exercise per week. It would be highly " \
                   "recommended that you vist a doctor and seek remedial " \
                   "treatment as soon as possible."

        elif bmi_value > 39.9:
            text = "You are considered morbidly obese. It is likely that " \
                   "your weight has a relatively large affect on your life. " \
                   "You are prone to issues such as sleep apnea, heart disease " \
                   "and various others. See a doctor urgently to receive a plan " \
                   "on normalising your weight."
        else:
            text = "Nothing"

        return text

    def check_bmi(self):

        has_error = "no"

        bmi_response = self.bmi_entry.get()

        try:
            weight_response = float(bmi_response)

            if weight_response < 0:
                has_error = "amount"

        except ValueError:
            has_error = "number"

        if has_error == "no":
            return bmi_response
        else:
            return has_error

    # informs user about BMI value
    def inform_me(self):
        bmi_value = self.check_bmi()
        information_text = self.information_check()

        self.value_label.grid(column=0, row=0)
        self.value_label.config(text=bmi_value)
        self.information_label.grid(column=1, row=0)
        self.information_label.config(text=information_text)

    # closes help dialogue (used by button and x at top of dialogue)
    def close_help(self, partner):
        # Put help button back to normal...
        partner.to_help_button.config(state=NORMAL)
        self.help_box.destroy()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    Converter()
    root.mainloop()
