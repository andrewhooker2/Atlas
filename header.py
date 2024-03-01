def header_print():
    logo = """
             /  /\          ___                      /  /\         /  /\\
            /  /::\        /  /\                    /  /::\       /  /:/_
           /  /:/\:\      /  /:/    ___     ___    /  /:/\:\     /  /:/ /\\
          /  /:/~/::\    /  /:/    /__/\   /  /\  /  /:/~/::\   /  /:/ /::\\
         /__/:/ /:/\:\  /  /::\    \  \:\ /  /:/ /__/:/ /:/\:\ /__/:/ /:/\:\\
         \  \:\/:/__\/ /__/:/\:\    \  \:\  /:/  \  \:\/:/__\/ \  \:\/:/~/:/
          \  \::/      \__\/  \:\    \  \:\/:/    \  \::/       \  \::/ /:/
           \  \:\           \  \:\    \  \::/      \  \:\        \__\/ /:/
            \  \:\           \__\/     \__\/        \  \:\         /__/:/
             \__\/                                   \__\/         \__\/
    """

    welcome_message = "Welcome to Atlas."
    conversation_start_message = "AI-driven conversations start here."
    quit_message = "Type 'quit' to end the session."
    input_prompt = "Awaiting your input..."

    cyan_color_code = "\033[36m"
    reset_code = "\033[0m"

    # Calculate the width of the ASCII art for the border
    art_width = max(len(line) for line in logo.split('\n'))

    # Create the top and bottom border based on the ASCII art width
    border = "=" * art_width

    # Print the top border
    print(cyan_color_code + border + reset_code)

    # Print the ASCII art
    print(cyan_color_code + logo + reset_code)

    # Center the welcome messages within the border
    def print_centered_message(message):
        padding = (art_width - len(message)) // 2 * " "
        print(cyan_color_code + padding + message + padding + reset_code)

    # Print each message centered
    print_centered_message(welcome_message)
    print_centered_message(conversation_start_message)
    print_centered_message(quit_message)
    print_centered_message(input_prompt)

    # Print the bottom border
    print(cyan_color_code + border + reset_code)
