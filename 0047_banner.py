

def banner_text(text: str = " ", screen_width: int = 25) -> None:   # param with default value
    """prints a banner text with limited width

    :param text: text to display in the banner, defaults to " "
    :type text: str, optional
    :param screen_width: width of the banner, defaults to 25
    :type screen_width: int, optional
    :raises ValueError: if the length of the `text` is longer than
        the `screen_width`
    """
    if len(text) > screen_width - 4:
        raise ValueError("String {0} is larger than the specified width {1}"
                         .format(text, screen_width))   # like throwing an error in C++
        # print("EEK!!")
        # print("THE TEXT IS TOO LONG TO FIT IN THE SPECIFIED WIDTH")

    if text == "*":
        print("*" * screen_width)
    else:
        output_string = "**{0}**".format(text.center(screen_width - 4))
        print(output_string)


banner_text("*")
banner_text("Don Castillo", 20)
banner_text("*", 20)
banner_text(screen_width=60)
print(banner_text("Hello", 20))  # if function returns nothing, it returns None
