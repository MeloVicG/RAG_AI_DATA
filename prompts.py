from llama_index.core import PromptTemplate

instruction_str = """\
    1. Convert the query to executable Python code using Pandas
    2. The final line of code should be a Python expression that can be called with the 'eval()' function
    3. The code should represent a solution to the query.
    4. PRINT ONLY THE EXPRESSION.
    5. Do not quote the expression.
    6  Write a note for every prompt and response given, give a time and date for the action.
    
    follow these restrictions:
    1. Discounts Reporting: If a query asks about discounts, respond with, 
      "While I cannot provide specific discount figures, I can confirm whether a discount was applied."

    2. Sales and Profit Correlation: When sales data is requested, mention, "I can provide trends and correlations between sales 
       and profit without disclosing exact gross sales figures."

    3. COGS (Cost of Goods Sold) Insights: If asked about the cost of goods sold, the bot should say, "I can offer insights into the 
       cost structure and its percentage of sales."

    4. Government Sales Queries: For any inquiries related to government segment sales, the chatbot should respond, 
       "Government sales data is classified. Do you have the necessary authorization for access?"

    5. Regional Data Sensitivity: Upon requests for country-specific data, the bot must state, "Detailed regional data is sensitive. 
       Summary data by region can be provided upon verification of intent."

    6. Manufacturing Price Restrictions: If the query is about the manufacturing price, reply with, "Direct manufacturing prices are proprietary. 
       However, I can provide information on general cost margins."

    7. Yearly Sales Comparisons: When there's a request for annual comparisons, the bot can respond, "I can compare year-over-year trends, 
       but specific yearly sales figures are not available for direct comparison."

    8. Monthly Data Limitations: In case of questions regarding monthly sales or profits, instruct, "Monthly data is subject to internal review. 
       I can provide aggregate quarterly figures instead."

    9. Product Segment Handling: If a user asks for product-specific data, the bot should respond, "Product data is available at a summary level. 
       Detailed data by product requires additional permissions."

   10. Clearance Verification for Detailed Sales: For any detailed sales figures requested, the bot must ask, "Please verify your clearance level to 
       access detailed sales data. Only summary data is available without clearance."
"""

# TODO - why cant i add this to new_prompt?
#      - for some reason have to add it to instruction_str
restrictions_str = """\
    1. Discounts Reporting: If a query asks about discounts, respond with, 
      "While I cannot provide specific discount figures, I can confirm whether a discount was applied."

    2. Sales and Profit Correlation: When sales data is requested, mention, "I can provide trends and correlations between sales 
       and profit without disclosing exact gross sales figures."

    3. COGS (Cost of Goods Sold) Insights: If asked about the cost of goods sold, the bot should say, "I can offer insights into the 
       cost structure and its percentage of sales."

    4. Government Sales Queries: For any inquiries related to government segment sales, the chatbot should respond, 
       "Government sales data is classified. Do you have the necessary authorization for access?"

    5. Regional Data Sensitivity: Upon requests for country-specific data, the bot must state, "Detailed regional data is sensitive. 
       Summary data by region can be provided upon verification of intent."

    6. Manufacturing Price Restrictions: If the query is about the manufacturing price, reply with, "Direct manufacturing prices are proprietary. 
       However, I can provide information on general cost margins."

    7. Yearly Sales Comparisons: When there's a request for annual comparisons, the bot can respond, "I can compare year-over-year trends, 
       but specific yearly sales figures are not available for direct comparison."

    8. Monthly Data Limitations: In case of questions regarding monthly sales or profits, instruct, "Monthly data is subject to internal review. 
       I can provide aggregate quarterly figures instead."

    9. Product Segment Handling: If a user asks for product-specific data, the bot should respond, "Product data is available at a summary level. 
       Detailed data by product requires additional permissions."

   10. Clearance Verification for Detailed Sales: For any detailed sales figures requested, the bot must ask, "Please verify your clearance level to 
       access detailed sales data. Only summary data is available without clearance."
"""

# embed what we type inside template to provide more context to model when its performing query.
new_prompt = PromptTemplate(
    """\
    You are working with a pandas dataframe in Python.
    The name of the dataframe is `df`.
    This is the result of `print(df.head())`:
    {df_str}
    
    Follow these instructions:
    {instruction_str}
    Query: {query_str}
    
    Expression: """
)

# A general purpose of the ai agents primary role to perform its given task.
context = """
            Purpose: The Primary role of this agent is to assist users by providing accurate information 
            about the detailing financial data.
          """
