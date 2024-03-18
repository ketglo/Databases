import os
import psycopg2
from dotenv import load_dotenv

# Load .env file from the same directory
def get_env_file_name():
    current_directory = os.getcwd()
    env_files = [filename for filename in os.listdir(current_directory) if filename.endswith(".env")]
    
    if env_files:
        return env_files[0]  # Assuming there's only one .env file
    else:
        return None  # No .env file found in the current directory

if __name__ == "__main__":
    env_file_name = get_env_file_name()
    #if env_file_name:
        #print(f"The name of the environment file in the current directory is: {env_file_name}")
    #else:
        #print("No .env file found in the current directory.")
    
load_dotenv(env_file_name)

# Get the connection string from the environment variable
connection_string = os.getenv('DATABASE_URL')

# Connect to the Postgres database
conn = psycopg2.connect(connection_string)
# Create a cursor object
cur = conn.cursor()
# Execute SQL commands to retrieve the current time and version from PostgreSQL
cur.execute('SELECT NOW();')
time = cur.fetchone()[0]
cur.execute('SELECT version();')
version = cur.fetchone()[0]
# Close the cursor and connection
cur.close()
conn.close()
# Print the results
print('Current time:', time)
print('PostgreSQL version:', version)
