import os
from dotenv import load_dotenv
from langchain_community.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SimpleSequentialChain
from langchain.agents import AgentType, initialize_agent, load_tools


# Load environment variables from .env file
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Initialize OpenAI with the API key
llm = OpenAI(openai_api_key=OPENAI_API_KEY)

# Define the prompt template correctly with 'input_variables'
prompt_template_name = PromptTemplate(
    input_variables=["technology"],  # 'input_variables' should be used instead of 'input_variable'
    template="I want to make an AI-{technology} Company Startup. Please help me identify areas I should focus on to maximize seed fundings.",
)

# Create the LLMChain
tech_chain = LLMChain(llm=llm, prompt=prompt_template_name)

# Define the prompt template correctly with 'input_variables'
prompt_template_name = PromptTemplate(
    input_variables=["company_name"],  # 'input_variables' should be used instead of 'input_variable'
    template="Suggest me some {company_name} for my Ai Sartup",
)

name_chain = LLMChain(llm=llm, prompt=prompt_template_name)

chain = SimpleSequentialChain(chains = [tech_chain, name_chain])
# response = chain.run("Machine Learning")
# print(response)

# Uing LLM Agent 

tools = load_tools(["wikipedia", "llm-math"], llm=llm)
initialize_agent