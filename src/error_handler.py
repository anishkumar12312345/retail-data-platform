try:
    result = 10 / 0
    print(result)

except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

except Exception as e:
    print("Unexpected Error:", e)

finally:
    print("Program Finished.")