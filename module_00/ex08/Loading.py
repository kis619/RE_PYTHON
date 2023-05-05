import os


def print_progress(iterable, idx, elements_count, bar_size, progress_step):
    """Prints the progress of an iterable in the terminal

    Args:
        iterable: iterable to print progress of
        idx: current index of iterable
        elements_count: total number of elements in iterable
        bar_size: len of the bar
        progress_step: progress step based off of terminal window size
    """
    # string representation of progress as fraction
    progress_fraction = f"{idx}/{elements_count}"

    # string representation of progress as percentage
    progress_percent = f"{int(idx / elements_count * 100)}%"

    # string representation of progress as bar
    progress_bar = '█' * (progress_step)

    # string representation of empty bar
    empty_bar = " " * (bar_size - progress_step - 1)

    # concatenate progress bar and empty bar
    bar = progress_bar + empty_bar

    print(f"\r{progress_percent}|{bar}| {progress_fraction}", end="")


def ft_tqdm(iterable):
    """_summary_

    Yields:
        _type_: _description_
    """
    # get terminal size
    terminal_size = os.get_terminal_size().columns

    # get iterable length
    elements_count = len(iterable)

    # calculate bar size by substracting the len of the progress percentage
    # the len of the progress fraction and the len of other symbol
    # from the terminal size
    bar_size = terminal_size - \
        len(f"{elements_count} / {elements_count}") - len("100%") - len("| |")

    # calculate progress factor based off of bar size
    progress_factor = bar_size / elements_count

    for idx, elem in enumerate(iterable):
        yield elem
        # calculate progress step
        progress_step = int(idx * progress_factor)

        # print progress
        print_progress(iterable, idx + 1, elements_count,
                       bar_size, progress_step)
