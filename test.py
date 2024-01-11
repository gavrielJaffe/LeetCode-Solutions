from datetime import datetime, timedelta

def next_day(input_date):
    # Convert input string to datetime object
    input_date = datetime.strptime(input_date, '%Y-%m-%d')

    # Calculate the next day by adding one day
    output_date = input_date + timedelta(days=1)

    # Convert the result back to the string format
    output_date_str = output_date.strftime('%Y-%m-%d')

    return output_date_str

# Example usage:
input_date = '2021-11-15'
output_date = next_day(input_date)
print(f"Input: {input_date}, Output: {output_date}")
