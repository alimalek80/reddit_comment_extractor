**Reddit Comment Extractor**
----------------------------

This Python script extracts all comments (including replies) from a given Reddit post URL using the PRAW library.

**Features:**

*   Fetches comments recursively, including nested replies.
    
*   Calculates the total time taken to extract comments.
    
*   Displays the total number of comments extracted.
    

**Requirements:**

*   Python 3
    
*   PRAW library (pip install praw)
    

**Instructions:**

1.  **Obtain Reddit API Credentials:**
    
    *   Visit the Reddit developer portal: [https://www.reddit.com/r/developer/](https://www.reddit.com/r/developer/)
        
    *   Create a new app and select "script" as the app type.
        
    *   Provide a name and description for your app.
        
    *   Copy the **client ID**, **client secret**, and **create a user agent** for your script.
        
2.  **Update Credentials:**
    
    *   Replace _YOUR\_CLIENT\_ID_, _YOUR\_CLIENT\_SECRET_, and _YOUR\_USER\_AGENT_ placeholders in the code with your obtained credentials.
        
    *   **Do not commit these credentials to your public GitHub repository!** Consider using a .env file or environment variables to store them securely.
        
3.  **Run the Script:**
    
    *   Save the script as a Python file (e.g., reddit\_comment\_extractor.py).
        
    *   Run the script from your terminal: python reddit\_comment\_extractor.py
        
    *   You will be prompted to enter the URL of the Reddit post.
        
    *   The script will display the time taken, total comments extracted, and each comment with its indentation level.
        

**License:**

No license.

**Disclaimer:**

This script is for educational purposes only. Please use it responsibly and adhere to Reddit's API terms of use.
