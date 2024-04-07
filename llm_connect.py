import pandas as pd
import os
from llama_index.core.query_engine import PandasQueryEngine
from prompts import new_prompt, instruction_str, context
from dotenv import load_dotenv

from note_engine import note_engine, save_note
from llama_index.core.tools import QueryEngineTool, ToolMetadata
from llama_index.core.agent import ReActAgent

# from llama_index.llms import openai
# from openai import OpenAI
from llama_index.llms.openai.base import OpenAI


"""
NOTES
    * it is quite frustrating to find the right balance between the instructions and the query needed.
      have to be ask specifically most of the time in order not to hit any of the restrictions for basic info.
   
Issues - TODOS
    * -solved- The Financial Data shows there is unnecessary white spaces in column headers. ex. ' Units Sold '   
    * Receiving different results for the same questions asked to the chatbox regards to restrctions_str  
    * Exception handling - not exactly displaying it the way i want it too.
        * doesnt always hit Exceptions
        * dont need to see so many errors 
"""
try:
    # grabs key from .env file
    load_dotenv()

    # Load and refactor column headers in financial data so it is preloaded to be processed to the agent
    financial_path = os.path.join("data", "Financials.csv")
    financial_data_frame = pd.read_csv(financial_path)
    financial_data_frame.columns = financial_data_frame.columns.str.strip()

    # query engine
    financial_query_engine = PandasQueryEngine(df=financial_data_frame,
                                               verbose=True,
                                               instruction_str=instruction_str)

    financial_query_engine.update_prompts({"pandas_prompt": new_prompt})
    # financial_query_engine.query("How many Government Segments are there?")  # Pandas Output: 300
    # print(financial_data_frame.head())

    tools = [
        note_engine,
        QueryEngineTool(query_engine=financial_query_engine,
                        metadata=ToolMetadata(name="financial_data",
                                              description="This gives information on the financial data"
                                              ))]

    llm = OpenAI(model="gpt-3.5-turbo")

    # will pick the best tool for the job
    agent = ReActAgent.from_tools(tools, llm=llm, verbose=True, context=context)
    # :llm: the ai model being used
    # :verbose: an explanation of the ai agents actions
    # :context: a general role for the agent used.

    # >=Python3.8 Assignment Expression (Walrus Operator)
    # writes a note for the result of every prompt entered
    while (prompt := input("Enter a prompt ('q' to quit): ")) != "q":
        result = agent.query(prompt)
        print(result)
        save_note(str(result))


except KeyError as key_error:
    print(f"Column not found in DataFrame: {key_error}")
    save_note(str(key_error), "Negative Note")
    # raise Exception(f"THIS IS KEY ERROR: {key_error}")

except SyntaxError as syntax_error:
    print(f"syntax error: {syntax_error}")
    save_note(str(syntax_error), "Negative Note")
    # raise SyntaxError(f"THIS IS SYNTAX ERROR: {syntax_error}")

except ValueError as value_error:
    print(f"value error: {value_error}")
    save_note(str(value_error), "Negative Note")
    # raise ValueError(f"THIS IS VALUE ERROR: {value_error}")

except Exception as e:
    save_note(str(e), "Negative Note")
    print(f"We have an error: {e}")
    # raise Exception(f"Error Detected: {e}")