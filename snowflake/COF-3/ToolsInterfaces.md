### Snowflake Cortex Overview

Snowflake Cortex is Snowflake’s built-in AI and LLM platform that allows you to use Generative AI, search, summarization, document extraction, and conversational analytics directly inside Snowflake using SQL, Python, and APIs.

Main components:

AI SQL Functions
Cortex Search
Cortex Analyst
Document AI


### AI SQL Functions

### AI_COMPLETE

**AI_COMPLETE**: Generates a completion for a given text string or image using a selected LLM. Use this function for most generative AI tasks.

**AI_COMPLETE** is the updated version of COMPLETE (SNOWFLAKE.CORTEX).

```sql
--- Single string 
AI_COMPLETE(
    <model>, <prompt> [ , <model_parameters>, <response_format>, <show_details> ] )

SELECT AI_COMPLETE('snowflake-arctic', 'What are large language models?');

SELECT AI_COMPLETE(
    'mistral-large',
        CONCAT('Critique this review in bullet points: <review>', content, '</review>')
) FROM reviews LIMIT 10;

--- Single file

SELECT AI_COMPLETE('claude-sonnet-4-6',
    'Extract the kitchen appliances identified in this image. Respond in JSON only with the identified appliances.',
    TO_FILE('@myimages', 'kitchen.png'));
--- 
SELECT AI_COMPLETE('claude-sonnet-4-6',
  PROMPT('Are both image {0} and image {1} pictures of cats?',
    TO_FILE('@myimages', 'sleepingcat.png'), TO_FILE('@myimages', 'jumpingcat.png'))) AS image_classification;
```


### AI_CLASSIFY
Classifies text, images, or documents into categories that you specify.

```sql

AI_CLASSIFY( <input> , <list_of_categories> [, <config_object> ] [, <return_error_details> ] )

SELECT AI_CLASSIFY('One day I will see the world', ['travel', 'cooking']);

--- output 
'{
  "labels": ["travel"]
 }';

SELECT AI_CLASSIFY(
  'One day I will see the world and learn to cook my favorite dishes',
  ['travel', 'cooking', 'reading', 'driving'],
  {'output_mode': 'multi'}
);

```

### AI_FILTER
Classifies free-form prompt inputs into a boolean. Currently supports both text and image filtering.

```sql

AI_FILTER( <input> [, <return_error_details> ] )
AI_FILTER( <predicate> , <input> [, <return_error_details> ] )
AI_FILTER( PROMPT('<template_string>',  <col_1>, … ) [, <return_error_details> ] )


SELECT AI_FILTER('Is Canada in North America?');

---
WITH reviews AS (

SELECT 'Wow... Loved this place.' AS review
UNION ALL SELECT 'The pizza is not good.'
)
SELECT * FROM reviews
WHERE AI_FILTER(PROMPT('The reviewer enjoyed the restaurant: {0}', review));

```

## AI_AGG
Reduces a column of text data using a natural language instruction.

```sql
AI_AGG( <expr>, <instruction> )

SELECT AI_AGG('[Excellent, Excellent, Great, Mediocre]',
              'Summarize the product ratings for a blog post targeting consumers');

```

## AI_EMBED
Creates an embedding vector from text or an image.

```sql
SELECT AI_EMBED('snowflake-arctic-embed-l-v2.0', 'hello world');

SELECT AI_EMBED('voyage-multimodal-3',
        TO_FILE ('@my_images', 'CITY_WALKING1.PNG'));

``

## AI_EXTRACT
Extracts information from an input string or file.

```sql
AI_EXTRACT( <text>, <responseFormat> )

SELECT AI_EXTRACT(
  file => TO_FILE('@db.schema.files', 'document.pdf'),
  responseFormat => {'name': 'What is the last name of the employee?', 'date': 'What is the inspection date?'},
  scores => TRUE
);

```

## AI_SENTIMENT
Returns overall and category sentiment in the given input text.

```sql

SELECT AI_SENTIMENT('A tourist\'s delight, in low urban light,
    Recommended gem, a pizza night sight. Swift arrival, a pleasure so right,
    Yet, pockets felt lighter, a slight pricey bite. 💰🍕🚀');

SELECT
  AI_SENTIMENT(
    review_content,
    ['concept', 'performance', 'script', 'cinematography', 'soundtrack']
  ),
  review_content
  FROM reviews LIMIT 10;

```

## AI_SIMILARITY
Computes a similarity score based on the vector cosine similarity value of the inputs’ embedding vectors. Currently supports both text and image similarity computation.

```sql
AI_SIMILARITY( <input1>, <input2> )
AI_SIMILARITY( <input1>, <input2>, <config_object> )

SELECT AI_SIMILARITY('I like this dish', 'This dish is very good');

SELECT
    review
FROM restaurant_reviews
ORDER BY AI_SIMILARITY(review, 'I love the food here!');

```

## AI_SUMMARIZE_AGG
Summarizes a column of text data.

```sql
SELECT AI_SUMMARIZE_AGG('The restaurant was excellent. I especially enjoyed the pizza and ice cream. My grandma didnt like it though.');
```

## SUMMARIZE (SNOWFLAKE.CORTEX)
Summarizes the given English-language input text.

```sql
SNOWFLAKE.CORTEX.SUMMARIZE(<text>)
SELECT SNOWFLAKE.CORTEX.SUMMARIZE(review_content) FROM reviews LIMIT 10;
```

## AI_TRANSCRIBE
AI_TRANSCRIBE is a fully managed SQL function that transcribes audio and video files stored in a stage, extracting text, timestamps, and speaker information

```sql
AI_TRANSCRIBE( <audio_file> [ , <options> ] [, <return_error_details> ] )

SELECT AI_TRANSCRIBE(TO_FILE(
    '@financial_consultation', 'consultation.wav'));

```

## AI_TRANSLATE

Translates the given input text from one supported language to another.

```sql
AI_TRANSLATE(
    <text>, <source_language>, <target_language> [, <return_error_details> ] )

SELECT AI_TRANSLATE(review_content, 'en', 'de') FROM reviews LIMIT 10;
```

## AI_REDACT
Detects and redacts personally identifiable information (PII) from unstructured text data.

```sql
AI_TRANSCRIBE( <audio_file> [ , <options> ] [, <return_error_details> ] )
```

## AI_PARSE_DOCUMENT
Returns the extracted content from a document on a Snowflake stage as a JSON-formatted string

```sql
AI_PARSE_DOCUMENT( <file_object> [, <options> ] [, <return_error_details> ] )

SELECT AI_PARSE_DOCUMENT (
    TO_FILE('@docs.doc_stage','research-paper-example.pdf'),
    {'mode': 'LAYOUT' , 'page_split': true}) AS research_paper_example;
```
