import time

# time since UNIX epoch (01.01.1970)
epoch_time: float = time.time()

# format time {:,.4f}/{:,.2e}
# The comma (,) character serves as the thousands separator.
# The . character indicates the start of the precision specifier.
# The 4 specifies the number of decimal places.
# The f indicates the number should be formatted as a floating-point value.
# The e indicates scientific notation
# Without f or e we get the scientific notation

# print in the desired format
print(f"Seconds since January 1, 1970: {'{:,.4f}'.format(epoch_time)} or "
      f"{'{:,.2e}'.format(epoch_time)} in scientific notation")

print(time.strftime("%B %d %Y"))
