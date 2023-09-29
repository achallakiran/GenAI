import openai

# Define your OpenAI API key
api_key = "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"

# Function to generate SQL SELECT statement
def generate_select_statement(table_name, columns):
    prompt = f"Generate a SQL SELECT statement for the {table_name} table to retrieve {', '.join(columns)}."
    return generate_sql_statement(prompt)

# Function to generate SQL INSERT statement
def generate_insert_statement(table_name, values):
    prompt = f"Generate a SQL INSERT statement for the {table_name} table with values {', '.join(values)}."
    return generate_sql_statement(prompt)

# Function to generate SQL statement using OpenAI API
def generate_sql_statement(prompt):
    openai.api_key = api_key
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=50,  # Adjust max_tokens as needed for your use case
        n=1,  # Number of completions to generate
        stop=None,  # Optional stop sequences
        temperature=0.7,  # Controls randomness (adjust as needed)
    )

    return response.choices[0].text.strip()

# Example usage:
if __name__ == "__main__":
    table_name = "my_table"
    columns = ["column1", "column2", "column3"]
    values = ["value1", "value2", "value3"]

    select_statement = generate_select_statement(table_name, columns)
    insert_statement = generate_insert_statement(table_name, values)

    print("Generated SQL SELECT statement:")
    print(select_statement)

    print("\nGenerated SQL INSERT statement:")
    print(insert_statement)

