A student wants to learn about a certain topic through a web application learning platform. Using this site, the student wants to gain a relatively clear understanding of the topic, given that their experience level is already at a set amount. You will be given the student's requested topic, their level of proficiency, and the total number of weeks that they want to learn the topic in.

[topic] = {topic}
[proficiency] = {proficiency}
[num_weeks] = {num_weeks}


Using the above information, generate a [num_weeks]-week lesson plan that will give the student a clear understanding of the topic, considering their current level of proficiency. To create this lesson plan, let's think step-by-step.

First, consider the requested topic at hand. What aspects of [topic] do you need to know about to be considered knowledgeable about it? What lessons in the [topic] is the student required to know to do more complex problems later on? Ensure that each of these lessons provide some sort of content knowledge to the student, rather than giving them a "project" or "case study" to conduct. Create a relevant course title and course description for this topic.

Once you have created a list of these lessons, consider the most effective ordering of these lessons to allow a student to learn the content most efficiently. What is the best way to order these lessons to learn the topic in 10 weeks, with basic lessons in at the beginning of the course plan and the complex lessons at the end of the course plan. When creating this course plan, make sure to consider that the student's proficiency level is [proficiency], and adjust the starting content and pace accordingly.

Finally, create basic descriptions for each week of the course plan, detailing what lessons the student will learn each week in 2-3 sentences. Supplement these descriptions with exact terms and definitions that the student should know at the end of that week.

To sum up your tasks:
<steps>
1. Create a title and a description for the course plan based on the student's requested topic.
2. Create a [num_weeks]-week course plan that will maximize a student's knowledge of the requested topic.
3. Create 2-3 sentence descriptions for each week of the course plan, with detailed terms that the student should know/comprehend after than week.
</steps>

Once all this content has been gathered, return your new course plan in the following string format, with n being [num_weeks]:
<output>
Course Title: *generated course title*
Course Description: *generated course description*
Weekly Course Outline:
[
  [
    week_1_lesson: *generated week 1 lesson title*,
    week_1_description: *generated week 1 lesson description*
  ],
  [
    week_2_lesson: *generated week 2 lesson title*,
    week_2_description: *generated week 2 lesson description*
  ],
  [
    week_3_lesson: *generated week 3 lesson title*,
    week_3_description: *generated week 3 lesson description*
  ],
  ...,
  [
    week_n_lesson: *generated week n lesson title*,
    week_n_description: *generated week n lesson description*
  ]
]
</output>