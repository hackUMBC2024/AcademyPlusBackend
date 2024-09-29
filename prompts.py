import os, re
import numpy as np
from dotenv import load_dotenv
import anthropic
from langchain_core.prompts import PromptTemplate
import google.generativeai as genai
# from langchain_anthropic import ChatAnthropic

load_dotenv('./.env')

PROFICIENCIES = ["newcomer", "5-year-old", "15-year-old", "40-year-old"]
DURATION = ["1 week", "2 weeks", "1 month", "3 months"]

def init_claude() -> anthropic.Anthropic:
  client = anthropic.Anthropic(
    api_key=os.environ.get('ANTHROPIC_API_KEY'),
  )
  return client

def init_gemini() -> genai.GenerativeModel:
  genai.configure(api_key=os.environ.get('GEMINI_API_KEY'))
  return genai.GenerativeModel(model_name='gemini-1.5-flash',
                              system_instruction="You are a talented education professional, tasked with generating course outlines for new courses for a website. Using your konwledge of specific course content and efficient/useful learning techniques, you will be tasked with generating course outlines and content-specific practice problems to assist students with learning new topics.")

def call_model(client, prompt: str, output_tokens=10000) -> genai.types.GenerateContentResponse:
  response = client.generate_content(
    prompt,
    generation_config = genai.GenerationConfig(
      max_output_tokens=output_tokens,
      temperature=0.1
    )
  )
  return response

def correct_search(prompt_file_location: str, keyword_search: str) -> str:
  CLIENT = init_gemini()

  with open(prompt_file_location, 'r') as file:
    prompt_template_text = file.read()

  unformatted = PromptTemplate(
    input_variables = ["keyword_search"],
    template=prompt_template_text
  )
  prompt = unformatted.format(keyword_search=keyword_search)
  response = call_model(CLIENT, prompt, 100000)

  return response.text

def get_lessons(prompt_file_location: str, topic: str, time_duration: str, proficiency: str, num_lessons: int) -> str:
  CLIENT = init_gemini()

  with open(prompt_file_location, "r") as file:
    prompt_template_text = file.read()

  unformatted = PromptTemplate(
    input_variables=["topic", "proficiency", "num_weeks"],
    template=prompt_template_text
  )
  prompt = unformatted.format(topic=topic, proficiency=proficiency, num_weeks=num_lessons)
  response = call_model(CLIENT, prompt, 1000)

  # with open('./outputs/prompt.md', 'w') as prompt_file:
  #   prompt_file.write(prompt)

  return response.text

def get_lesson_titles(lessons: str) -> list:
  pattern = r'week_\d+_lesson:\s*"(.*?)"'
  return re.findall(pattern, lessons)

def get_youtube_links(prompt_file_location: str, lessons: str) -> list:
  CLIENT = init_gemini()

  with open(prompt_file_location, "r") as file:
    prompt_template_text = file.read()

  all_links = []
  topic_list = get_lesson_titles(lessons)

  for lesson in topic_list:
    unformatted = PromptTemplate(
      input_variables=["lesson"],
      template=prompt_template_text
    )
    prompt = unformatted.format(lesson=lesson)
    response = call_model(CLIENT, prompt, 1000)

    all_links.append(response.text.split("\n"))

  return all_links

def get_lesson_content(prompt_file_location: str, topic: str, lessons: str, proficiency: str) -> list:
  CLIENT = init_gemini()

  with open(prompt_file_location, "r") as file:
    prompt_template_text = file.read()

  all_descriptions = []
  topic_list = get_lesson_titles(lessons)

  for lesson in topic_list:
    unformatted = PromptTemplate(
      input_variables=["topic", "lesson", "proficiency"],
      template=prompt_template_text
    )
    prompt = unformatted.format(topic=topic, lesson=lesson, proficiency=proficiency)
    response = call_model(CLIENT, prompt, 10000)
    print(response.text)
    all_descriptions.append(response.text)

  return all_descriptions

print("beginning LLM calls")
new_title = correct_search('./prompts/relevant_title.md', "how to know about Python coding")
with open('./outputs/response.md', 'w') as response_file:
  response_file.write(get_lessons("./prompts/lesson_plan.md", new_title, DURATION[0], PROFICIENCIES[0], 15))

with open('./outputs/response.md', 'r') as response_file:
  # with open('./outputs/links.md', 'w') as links_file:
  #   links_file.write(str(get_youtube_links("./prompts/youtube.md", response_file.read())))
  with open('./outputs/descriptions.md', 'w') as descriptions_file:
    descriptions_file.write(str(get_lesson_content('./prompts/create_descriptions.md', new_title, response_file.read(), PROFICIENCIES[0])))
