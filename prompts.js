const { GoogleGenerativeAI } = require("@google/generative-ai");
const { HumanMessagePromptTemplate } = require("@langchain/core/prompts");
const fs = require('fs');
require('dotenv').config();

async function fetchAndFormatMarkdown(prompt_filepath) {
  let text;

  text = fs.readFileSync(prompt_filepath, 'utf-8');

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

const return_get_course = async (prompt_filepath, course) => {
  const message = await fetchAndFormatMarkdown(prompt_filepath);
  const formatted = await message.format({ course: course });
  return formatted;
}

let generate_search = async (keyword_search) => {
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

let generate_careers = async (course) => {
  try {
    const genAI = new GoogleGenerativeAI(process.env.GEMINI_API_KEY);
    const model = genAI.getGenerativeModel({
      model: "gemini-1.5-flash",
    });

    const formatted = await return_get_course("./prompts/generate_top_majors.md", course)

    const result = await model.generateContent(formatted.content.toString());
    const response = await result.response
    return response.text();
  } catch (error) {
    console.error('Error executing prompt:', error);
    return error;
  }
};

let generate_lessonplan = async (topic, proficiency, num_weeks) => {
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

module.exports = {
  generate_search: generate_search,
  generate_careers: generate_careers,
  generate_lessonplan: generate_lessonplan
}