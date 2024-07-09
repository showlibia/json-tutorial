import gdb

class PrintLoopValues(gdb.Command):
    """Print values of i, c->json[i-1], and literal[i] in the while loop."""

    def __init__(self):
        super(PrintLoopValues, self).__init__("print_values", gdb.COMMAND_USER)

    def invoke(self, arg, from_tty):
        frame = gdb.selected_frame()
        while True:
            try:
                # Evaluate variables
                i = gdb.parse_and_eval("i")
                c_json = gdb.parse_and_eval("c->json[i-1]")
                literal = gdb.parse_and_eval("literal[i]")

                # Print their values
                print(f"i = {i}, c->json[i-1] = {c_json}, literal[i] = {literal}")

                # Execute next iteration
                gdb.execute("next")  # Move to the next line in the loop
            except gdb.error as e:
                # If any error occurs (e.g., when the loop ends), break the loop
                print(f"Error: {e}")
                break

PrintLoopValues()
