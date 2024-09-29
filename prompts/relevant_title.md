A student is looking for a relevant course on a prominent/popular e-learning platform, such as Udemy, edX, or Coursera. However, this student frequently uses internet slang, incomplete phrases, and questions to search for certain courses, rather than using clear keywords arguments that will assist him in his search. He also might search for specific lessons within a broader course, when he should be searching for the course instead. Using your knowledge of correct keyword search syntax and English grammar/spelling, take in the student's keyword and generate a clear course title that the student can then use to get relevant results. Please note that in some cases, a student may have a correctly-worded or genuinely correct keyword search that requires no modification. In that case, you may just return the keyword search in exactly the format that the student typed it in.

[keyword_search] = {keyword_search}

Below are some examples of what a student might search, and what your correct output should be:
<examples>
example #  |   student_keyword_search                               |  correct_generated_output               |
-----------|--------------------------------------------------------|-----------------------------------------|
    1      | "I dont know what lin alg is"                          | "Introduction to Linear Algebra"        |
    2      | "What are dangling modifiers"                          | "Basics of English Grammar/Syntax"      |
    3      | "How to solve first-order differential equations?"     | "Intermediate Differential Equations"   |
    4      | "Functional groups and uses in AP Chemistry"           | "Short Tutorial in Organic Chemistry"   |
    5      | "wat prompt engineering?"                              | "Introduction to Prompt Engineering"    |
    6      | "Physics for Electricity and Magnetism"                | "Physics for Electricity and Magnetism" |
</examples>

Based on the above examples of potential keyword searches and correct generated outputs, output your result in the following string format.
<output>
*generated output*
</output>
Under no circumstances should you include any other descriptors or reasoning for your answer in your output. The only output you should include is your corrected course title (if applicable).