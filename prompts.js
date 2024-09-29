import { GoogleGenerativeAI } from '@google/generative-ai';
import {HumanMessagePromptTemplate} from '@langchain/core/prompts';
import dotenv from 'dotenv';
dotenv.config();

async function fetchAndFormatMarkdown(prompt_filepath) {
  let text;

  const response = await fetch(prompt_filepath);
  text = await response.text();

  const message = HumanMessagePromptTemplate.fromTemplate(text);

  return message;
}

const return_correct_search = async (prompt_filepath, keyword_search) => {
  const message = await fetchAndFormatMarkdown(prompt_filepath)
  const formatted = await message.format({ keyword_search: keyword_search });
  return formatted;
}

const return_get_lessons = async (prompt_filepath, topic, proficiency, num_weeks) => {
  const message = await fetchAndFormatMarkdown(prompt_filepath)
  const formatted = await message.format({ topic: topic, proficiency: proficiency, num_weeks: num_weeks });
  return formatted;
}

const generate_search = async (keyword_search) => {
  try {
    const genAI = new GoogleGenerativeAI(process.env.GEMINI_API_KEY);
    const model = genAI.getGenerativeModel({
      model: "gemini-1.5-flash",
    });

    const formatted = await return_correct_search("./prompts/relevant_title.md", keyword_search)

    const result = await model.generateContent(formatted.content.toString());
    const response = await result.response
    return response.text();
  } catch (error) {
    console.error('Error executing prompt:', error);
    return error;
  }
};

const generate_lessonplan = async (topic, proficiency, num_weeks) => {
  try {
    const genAI = new GoogleGenerativeAI(process.env.GEMINI_API_KEY);
    const model = genAI.getGenerativeModel({
      model: "gemini-1.5-flash",
    });

    const formatted = await return_get_lessons("./prompts/lesson_plan.md", topic, proficiency, num_weeks)

    const result = await model.generateContent(formatted.content.toString());
    const response = await result.response
    return response.text();
  } catch (error) {
    console.error('Error executing prompt')
    return error;
  }
}