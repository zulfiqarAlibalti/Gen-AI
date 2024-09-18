import os
from dotenv import load_dotenv
from langchain_community.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SimpleSequentialChain

# Load environment variables from .env file
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Initialize OpenAI with the API key
llm = OpenAI(openai_api_key=OPENAI_API_KEY)

# Function to generate startup name and focus areas based on tech_name
def generate_tech_Startup_name(tech_name):
    # Define the prompt template for identifying target areas
    prompt_template_area = PromptTemplate(
        input_variables=["technology"],
        template="I want to make an AI-{technology} Company Startup. Please help me identify areas I should focus on to maximize seed fundings."
    )

    # Define the prompt template for suggesting a startup name
    prompt_template_name = PromptTemplate(
        input_variables=["company_name"],
        template="Suggest me some {company_name} names for my AI startup."
    )

    # Create the LLM chains
    tech_chain = LLMChain(llm=llm, prompt=prompt_template_area)
    name_chain = LLMChain(llm=llm, prompt=prompt_template_name)

    # Create a SimpleSequentialChain that links the two prompts
    chain = SimpleSequentialChain(chains=[tech_chain, name_chain])

    # Run the chain with the selected technology
    response = chain.run(tech_name)

    # For simplicity, the response will return the startup name and target area suggestion
    return {
        'tech_startup_name': response.split('\n')[0],  # Assuming the first line is the name
        'target_area': response  # The entire response will include target areas
    }
