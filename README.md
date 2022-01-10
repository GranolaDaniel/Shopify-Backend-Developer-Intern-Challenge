1. Why I chose to CASCADE on deletion
2. Tests
3. Model/DB architecture
4. How-to
5. Things to add in the future/how extendable is your current code?

## How to

Start by cloning the repo from Github:

1. Run 

Then, create a secret key for Django to use:

1. Create a file called `secret.py` in the same folder as the cloned repo
2. Add a variable holding the secret as a string. E.g. `secret = '<SECRET>'`
3. Save the file