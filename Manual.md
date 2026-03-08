# FinCLI User Manual

## 1. Income Records

The **Income Records** section allows you to record and organize your income transactions. When using this section, **FinCLI** will prompt you for several inputs. Each prompt collects important information about the transaction and ensures that the data recorded remains accurate and consistent.

Below is an explanation of each prompt, its purpose, how to use it, and the rules enforced by the system.

1. **Income Transaction Prompt:** 
    - **Purpose:** This prompt records the **amount of money you received** from an income transaction such as salary, business profit, or freelance payment.
    - **Usage Information:** Enter the amount of money you received. If the amount includes cents or paise, you can include decimal values.
    - **Rules:**  The value must be numeric. The value must be positive. Since most of currencies operate with two decimal places so only value with two decimal places are allowed.
2. **Income Source Prompt:**   
    - **Purpose:** This prompt categorizes where your income came from so you can later analyze your main sources of income.
    - **Usage Information:** Choose the appropriate category from the menu by entering the number shown. If you select **Other Sources**, you will be able to enter a custom income source.
    - **Rules:** The input must be numeric. The number must correspond to one of the menu options. Should you leave the custom source blank, the system will automatically record it as "Other Sources".
3. **Transaction Date Prompt:**  
    - **Purpose:** This prompt records **when the income transaction occurred**.
    - **Usage Information:** You will be presented with two options:
        1. **Today** – records the current date automatically.
        2. **Custom Date** – allows you to manually enter the date of the transaction.
        
        If you choose a custom date, you will be asked to provide the **year**, **month**, and **day** of the transaction.
        
    - **Rules:** All inputs must be **numeric**. The **year** must be between **2000 and the current year**. If the year entered is the **current year**, the month cannot exceed the current month. If the year entered is **earlier than the current year**, any month between **January and December** is allowed. If the selected month is the **current month**, the day cannot exceed the current day. The system automatically validates: **correct number of days in each month**, **leap years** &  prevention of **future dates.**
4. **Transaction Account Prompt:** 
    - **Purpose:** This prompt records **which account received the income**. Tracking the account allows FinCLI to later calculate **account-wise balances and overall net worth**.
    - **Usage Information:** Enter the name of the account where the income was credited. Exmaples include: Salary Account, Business Account, Merchant Account, Cash.
    - **Rules:** The name must contain **between 1 and 20 Characters.** The input can contain **letters and numbers**. If left blank, the system will use the default value "bank".
5. **Transaction Note:**  
    - **Purpose:** This prompt allows you to record a short note describing the reason for the transaction. Notes help you remember **why the transaction occurred** , which can be useful for reviewing your financial history later.
    - **Usage Information:** Enter a short description of the transaction. Examples include: Client Payment, Salary, Refund received.
    - **Rules:**  The note must contain **between 1 and 50 characters**. Longer notes are not allowed to keep transaction records concise.

**Important Note:** If any rule is violated, **FinCLI will repeatedly prompt you until valid input is provided**. This ensures that all financial records remain **accurate, consistent, and reliable** for future tracking and analysis.