import tkinter as tk
from tkinter import ttk, messagebox
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class NQueensVisualizer:

    def __init__(self, root):
        self.root = root
        self.root.title("N-Queens Backtracking Visualizer")
        self.root.geometry("1200x750")
        self.root.minsize(1000, 650)

        # Algorithm variables
        self.n = 4
        self.board = []
        self.steps = []
        self.step_index = 0
        self.solutions = []
        self.current_solution = []
        self.nodes_explored = 0

        # Animation control
        self.animation_running = False
        self.animation_job = None

        self.create_interface()

    # ==========================================================
    # CREATE GUI
    # ==========================================================

    def create_interface(self):

        # ---------------- TOP TITLE ----------------

        title = tk.Label(
            self.root,
            text="N-QUEENS BACKTRACKING VISUALIZER",
            font=("Arial", 22, "bold"),
            fg="#17365D"
        )

        title.pack(pady=10)

        subtitle = tk.Label(
            self.root,
            text="Interactive visualization of the Backtracking Algorithm",
            font=("Arial", 11),
            fg="#555555"
        )

        subtitle.pack()

        # ---------------- CONTROL FRAME ----------------

        control_frame = tk.Frame(
            self.root,
            bg="#EAF2F8",
            bd=1,
            relief="solid"
        )

        control_frame.pack(
            fill="x",
            padx=15,
            pady=12
        )

        tk.Label(
            control_frame,
            text="Number of Queens (N):",
            font=("Arial", 11, "bold"),
            bg="#EAF2F8"
        ).pack(side="left", padx=10, pady=10)

        self.n_entry = tk.Entry(
            control_frame,
            width=6,
            font=("Arial", 12)
        )

        self.n_entry.insert(0, "4")

        self.n_entry.pack(
            side="left",
            padx=5
        )

        self.start_button = tk.Button(
            control_frame,
            text="Start",
            command=self.start_algorithm,
            bg="#2874A6",
            fg="white",
            font=("Arial", 10, "bold"),
            width=10
        )

        self.start_button.pack(
            side="left",
            padx=5
        )

        self.previous_button = tk.Button(
            control_frame,
            text="Previous",
            command=self.previous_step,
            width=10
        )

        self.previous_button.pack(
            side="left",
            padx=5
        )

        self.next_button = tk.Button(
            control_frame,
            text="Next Step",
            command=self.next_step,
            width=10
        )

        self.next_button.pack(
            side="left",
            padx=5
        )

        self.auto_button = tk.Button(
            control_frame,
            text="Auto Play",
            command=self.auto_play,
            bg="#239B56",
            fg="white",
            font=("Arial", 10, "bold"),
            width=10
        )

        self.auto_button.pack(
            side="left",
            padx=5
        )

        self.reset_button = tk.Button(
            control_frame,
            text="Reset",
            command=self.reset,
            width=10
        )

        self.reset_button.pack(
            side="left",
            padx=5
        )

        # ---------------- MAIN AREA ----------------

        main_frame = tk.Frame(self.root)

        main_frame.pack(
            fill="both",
            expand=True,
            padx=15,
            pady=5
        )

        # ---------------- BOARD AREA ----------------

        board_frame = tk.LabelFrame(
            main_frame,
            text="Chessboard",
            font=("Arial", 12, "bold")
        )

        board_frame.pack(
            side="left",
            fill="both",
            expand=True,
            padx=5
        )

        self.figure, self.ax = plt.subplots(
            figsize=(6, 6)
        )

        self.canvas = FigureCanvasTkAgg(
            self.figure,
            master=board_frame
        )

        self.canvas.get_tk_widget().pack(
            fill="both",
            expand=True
        )

        # ---------------- INFORMATION AREA ----------------

        info_frame = tk.LabelFrame(
            main_frame,
            text="Algorithm Information",
            font=("Arial", 12, "bold"),
            width=330
        )

        info_frame.pack(
            side="right",
            fill="y",
            padx=5
        )

        info_frame.pack_propagate(False)

        self.status_label = tk.Label(
            info_frame,
            text="Ready",
            font=("Arial", 13, "bold"),
            fg="#2874A6"
        )

        self.status_label.pack(
            pady=15
        )

        # Current step

        self.step_label = tk.Label(
            info_frame,
            text="Step: 0 / 0",
            font=("Arial", 11)
        )

        self.step_label.pack(
            pady=5
        )

        # Queen positions

        self.position_label = tk.Label(
            info_frame,
            text="Queen Positions: []",
            font=("Arial", 11),
            wraplength=300
        )

        self.position_label.pack(
            pady=10
        )

        # Nodes explored

        self.nodes_label = tk.Label(
            info_frame,
            text="Nodes Explored: 0",
            font=("Arial", 11)
        )

        self.nodes_label.pack(
            pady=5
        )

        # Solutions

        self.solution_label = tk.Label(
            info_frame,
            text="Solutions Found: 0",
            font=("Arial", 11)
        )

        self.solution_label.pack(
            pady=5
        )

        # Explanation

        tk.Label(
            info_frame,
            text="Algorithm Status",
            font=("Arial", 11, "bold")
        ).pack(
            pady=(25, 5)
        )

        self.explanation = tk.Text(
            info_frame,
            height=10,
            width=35,
            font=("Arial", 10),
            wrap="word",
            state="disabled"
        )

        self.explanation.pack(
            padx=10,
            pady=5
        )

        # Complexity

        complexity_text = (
            "Complexity\n\n"
            "Time: O(N!)\n"
            "Space: O(N)\n\n"
            "Technique:\n"
            "Backtracking"
        )

        tk.Label(
            info_frame,
            text=complexity_text,
            font=("Arial", 10, "bold"),
            fg="#555555",
            justify="left"
        ).pack(
            pady=15
        )

        # Draw initial board
        self.draw_board([])

    # ==========================================================
    # N-QUEENS ALGORITHM
    # ==========================================================

    def is_safe(self, row, col, board):

        for previous_row in range(row):

            previous_col = board[previous_row]

            # Same column
            if previous_col == col:
                return False

            # Same diagonal
            if abs(previous_row - row) == abs(
                previous_col - col
            ):
                return False

        return True

    def generate_steps(self):

        self.steps = []
        self.solutions = []
        self.nodes_explored = 0

        board = [-1] * self.n

        def backtrack(row):

            # Solution found
            if row == self.n:

                solution = board.copy()

                self.solutions.append(solution)

                self.steps.append({
                    "board": solution.copy(),
                    "type": "solution",
                    "row": row,
                    "col": -1,
                    "message":
                        f"Solution {len(self.solutions)} found!"
                })

                return

            # Try every column
            for col in range(self.n):

                self.nodes_explored += 1

                # ---------------- VALID ----------------

                if self.is_safe(row, col, board):

                    board[row] = col

                    self.steps.append({
                        "board": board.copy(),
                        "type": "place",
                        "row": row,
                        "col": col,
                        "message":
                            f"Place queen at "
                            f"Row {row + 1}, "
                            f"Column {col + 1}"
                    })

                    backtrack(row + 1)

                    # ---------------- BACKTRACK ----------------

                    self.steps.append({
                        "board": board.copy(),
                        "type": "backtrack",
                        "row": row,
                        "col": col,
                        "message":
                            f"Backtrack: remove queen "
                            f"from Row {row + 1}, "
                            f"Column {col + 1}"
                    })

                    board[row] = -1

                # ---------------- INVALID ----------------

                else:

                    self.steps.append({
                        "board": board.copy(),
                        "type": "invalid",
                        "row": row,
                        "col": col,
                        "message":
                            f"Invalid placement at "
                            f"Row {row + 1}, "
                            f"Column {col + 1} — "
                            f"branch pruned"
                    })

        backtrack(0)

    # ==========================================================
    # START
    # ==========================================================

    def start_algorithm(self):

        self.stop_animation()

        try:
            n = int(self.n_entry.get())

        except ValueError:

            messagebox.showerror(
                "Invalid Input",
                "Please enter a valid integer."
            )

            return

        if n < 1 or n > 10:

            messagebox.showwarning(
                "Invalid N",
                "Please enter N between 1 and 10."
            )

            return

        self.n = n

        self.step_index = 0

        self.generate_steps()

        self.status_label.config(
            text="Algorithm Ready",
            fg="#2874A6"
        )

        self.update_display()

    # ==========================================================
    # NEXT STEP
    # ==========================================================

    def next_step(self):

        if not self.steps:
            return

        if self.step_index < len(self.steps):

            self.step_index += 1

            self.update_display()

    # ==========================================================
    # PREVIOUS STEP
    # ==========================================================

    def previous_step(self):

        if not self.steps:
            return

        if self.step_index > 1:

            self.step_index -= 1

            self.update_display()

        elif self.step_index == 1:

            self.step_index = 0

            self.update_display()

    # ==========================================================
    # AUTO PLAY
    # ==========================================================

    def auto_play(self):

        if not self.steps:

            messagebox.showinfo(
                "Start First",
                "Click Start before using Auto Play."
            )

            return

        if self.animation_running:
            return

        self.animation_running = True

        self.animate()

    def animate(self):

        if not self.animation_running:
            return

        if self.step_index >= len(self.steps):

            self.animation_running = False

            self.status_label.config(
                text="Completed",
                fg="#239B56"
            )

            return

        self.step_index += 1

        self.update_display()

        self.animation_job = self.root.after(
            700,
            self.animate
        )

    def stop_animation(self):

        self.animation_running = False

        if self.animation_job is not None:

            self.root.after_cancel(
                self.animation_job
            )

            self.animation_job = None

    # ==========================================================
    # RESET
    # ==========================================================

    def reset(self):

        self.stop_animation()

        self.steps = []
        self.solutions = []
        self.step_index = 0
        self.nodes_explored = 0

        self.status_label.config(
            text="Ready",
            fg="#2874A6"
        )

        self.step_label.config(
            text="Step: 0 / 0"
        )

        self.position_label.config(
            text="Queen Positions: []"
        )

        self.nodes_label.config(
            text="Nodes Explored: 0"
        )

        self.solution_label.config(
            text="Solutions Found: 0"
        )

        self.update_explanation(
            "Enter N and click Start to begin."
        )

        self.draw_board([])

    # ==========================================================
    # UPDATE DISPLAY
    # ==========================================================

    def update_display(self):

        if not self.steps:

            self.draw_board([])

            return

        if self.step_index == 0:

            board = [-1] * self.n

            self.draw_board(board)

            return

        current = self.steps[
            self.step_index - 1
        ]

        board = current["board"]

        step_type = current["type"]

        message = current["message"]

        self.draw_board(
            board,
            current["row"],
            current["col"],
            step_type
        )

        self.step_label.config(
            text=
            f"Step: {self.step_index} / "
            f"{len(self.steps)}"
        )

        positions = []

        for col in board:

            if col != -1:
                positions.append(col + 1)

        self.position_label.config(
            text=
            f"Queen Positions: {positions}"
        )

        self.nodes_label.config(
            text=
            f"Nodes Explored: "
            f"{self.nodes_explored}"
        )

        # Count solutions up to current point

        solution_count = 0

        for i in range(
            self.step_index
        ):

            if self.steps[i]["type"] == "solution":
                solution_count += 1

        self.solution_label.config(
            text=
            f"Solutions Found: "
            f"{solution_count}"
        )

        # Status colors

        if step_type == "place":

            self.status_label.config(
                text="Valid Placement",
                fg="#239B56"
            )

            self.update_explanation(
                message +
                "\n\nThe position is safe, so "
                "the algorithm recursively moves "
                "to the next row."
            )

        elif step_type == "invalid":

            self.status_label.config(
                text="Invalid / Pruned",
                fg="#C0392B"
            )

            self.update_explanation(
                message +
                "\n\nThe queen conflicts with "
                "another queen in the same column "
                "or diagonal. This branch is "
                "pruned."
            )

        elif step_type == "backtrack":

            self.status_label.config(
                text="Backtracking",
                fg="#8E44AD"
            )

            self.update_explanation(
                message +
                "\n\nThe current choice did not "
                "lead to a solution. The algorithm "
                "returns to the previous decision "
                "and tries another column."
            )

        elif step_type == "solution":

            self.status_label.config(
                text="Solution Found!",
                fg="#D68910"
            )

            self.update_explanation(
                message +
                "\n\nAll N queens have been placed "
                "without conflicts."
            )

    # ==========================================================
    # EXPLANATION TEXT
    # ==========================================================

    def update_explanation(self, text):

        self.explanation.config(
            state="normal"
        )

        self.explanation.delete(
            "1.0",
            tk.END
        )

        self.explanation.insert(
            tk.END,
            text
        )

        self.explanation.config(
            state="disabled"
        )

    # ==========================================================
    # DRAW CHESSBOARD
    # ==========================================================

    def draw_board(
        self,
        board,
        highlight_row=-1,
        highlight_col=-1,
        step_type=""
    ):

        self.ax.clear()

        self.ax.set_xlim(
            0,
            self.n
        )

        self.ax.set_ylim(
            0,
            self.n
        )

        self.ax.set_aspect("equal")

        # Draw squares
        for row in range(self.n):

            for col in range(self.n):

                # Chessboard colors
                if (row + col) % 2 == 0:

                    color = "#F0D9B5"

                else:

                    color = "#B58863"

                # Highlight current position
                if (
                    row == highlight_row
                    and col == highlight_col
                ):

                    if step_type == "invalid":

                        color = "#E74C3C"

                    elif step_type == "backtrack":

                        color = "#9B59B6"

                    elif step_type == "place":

                        color = "#2ECC71"

                    elif step_type == "solution":

                        color = "#F1C40F"

                self.ax.add_patch(
                    plt.Rectangle(
                        (col, self.n - row - 1),
                        1,
                        1,
                        facecolor=color,
                        edgecolor="black"
                    )
                )

        # Draw queens
        for row in range(self.n):

            if (
                row < len(board)
                and board[row] != -1
            ):

                col = board[row]

                x = col + 0.5

                y = (
                    self.n
                    - row
                    - 0.5
                )

                self.ax.text(
                    x,
                    y,
                    "♛",
                    fontsize=32,
                    ha="center",
                    va="center",
                    color="#17202A"
                )

        # Row labels
        for row in range(self.n):

            self.ax.text(
                -0.25,
                self.n - row - 0.5,
                str(row + 1),
                ha="center",
                va="center",
                fontsize=10,
                fontweight="bold"
            )

        # Column labels
        for col in range(self.n):

            self.ax.text(
                col + 0.5,
                -0.25,
                str(col + 1),
                ha="center",
                va="center",
                fontsize=10,
                fontweight="bold"
            )

        self.ax.set_title(
            f"N-Queens Board (N = {self.n})",
            fontsize=14,
            fontweight="bold"
        )

        self.ax.axis("off")

        self.figure.tight_layout()

        self.canvas.draw()


# ==============================================================
# RUN APPLICATION
# ==============================================================

if __name__ == "__main__":

    root = tk.Tk()

    app = NQueensVisualizer(root)

    root.mainloop()
