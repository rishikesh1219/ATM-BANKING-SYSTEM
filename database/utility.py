from database.databaseConnection import cursor, database_config


# 1. Function to get amount from database
def getAmountFromDB(account_no: int):
    try:
        # Changed 'USERS' to 'accounts' and 'AMOUNT' to 'BALANCE' to match your SQL
        get_amount_query = """SELECT BALANCE \
                              FROM accounts
                              WHERE ACCOUNT_NO = %s;"""
        cursor.execute(get_amount_query, (account_no,))
        result = cursor.fetchone()

        if result:
            return result[0]
        return 0
    except Exception as e:
        return f"Something wrong in database/utility.getAmountFromDB: {e}"


# 2. Function to update amount in database
def setAmountInDB(account_no: int, amount: int, trans_amount: int, transaction_type: str = None):
    try:
        # Changed 'USERS' to 'accounts' and 'AMOUNT' to 'BALANCE'
        update_amount_query = """UPDATE accounts \
                                 SET BALANCE = %s
                                 WHERE ACCOUNT_NO = %s;"""
        cursor.execute(update_amount_query, (amount, account_no))

        # Updating transaction table
        if transaction_type:
            insert_transaction_query = """INSERT INTO TRANSACTIONS
                                              (ACCOUNT_NUMBER, TRANSACTION_TYPE, AMOUNT)
                                          VALUES (%s, %s, %s);"""
            cursor.execute(insert_transaction_query, (account_no, transaction_type, trans_amount))

        database_config.commit()
    except Exception as e:
        return f"Something wrong in database/utility.setAmountInDB: {e}"


# 3. Function to check account status (EXISTENCE CHECK)
def checkAccountStatus(account_no):
    """Checks if an account exists in the database."""
    try:
        # Using the cursor imported at the top instead of connectToDB()
        query = "SELECT ACCOUNT_NO FROM accounts WHERE ACCOUNT_NO = %s"
        cursor.execute(query, (account_no,))
        result = cursor.fetchone()

        return result is not None
    except Exception as e:
        print(f"Error in checkAccountStatus: {e}")
        return False