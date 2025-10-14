import os
from supabase import create_client, Client
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def main():
    """
    Main function to interact with the Supabase backend.
    """
    url: str = os.environ.get("SUPABASE_URL")
    key: str = os.environ.get("SUPABASE_KEY")

    if not url or not key:
        print("Error: SUPABASE_URL and SUPABASE_KEY environment variables are not set.")
        print("Please create a .env file in the 'backend' directory and add them.")
        return

    supabase: Client = create_client(url, key)

    print("Successfully connected to Supabase.")

    # Example usage:
    # 1. Sign in a user (replace with actual user credentials)
    # try:
    #     user_response = supabase.auth.sign_in_with_password({
    #         "email": "mp.constituency.a@example.com",
    #         "password": "some-password"
    #     })
    #     print("User signed in successfully.")
    # except Exception as e:
    #     print(f"Error signing in: {e}")
    #     return


    # 2. Fetch data from the summary views
    # RLS policies will automatically filter the data based on the logged-in user.
    try:
        print("\nFetching county summary (public data)...")
        county_response = supabase.table('county_summary').select('*').execute()
        print("County Data:", county_response.data)

        # The following calls will likely return empty lists if RLS is enabled
        # and you are not authenticated as an MP.
        print("\nFetching constituency summary (MP-specific data)...")
        constituency_response = supabase.table('constituency_summary').select('*').execute()
        print("Constituency Data:", constituency_response.data)


        print("\nFetching ward summary (MP-specific data)...")
        ward_response = supabase.table('ward_summary').select('*').execute()
        print("Wards Data:", ward_response.data)

    except Exception as e:
        print(f"An error occurred while fetching data: {e}")


if __name__ == "__main__":
    main()
