# JSON Schema Transformer

So just last week, I was faced with a problem wherein some of our JSON data may need to change field names. Basically it's like mapping to a new JSON Schema.

So in Java, we have the Jolt Transformation to do this easily, but Jolt doesn't have a Python version of its code (or maybe there is but I just wasn't able to find it).

## JSONBender

Here comes the solution.

While trying to search the web or what tools can be used to transform a JSON data to a different schema, there were actually a lot that shown but seems a bit complicated.

Then I stumbled upon this [JSONBender](https://github.com/Onyo/jsonbender) library, where I can just define the schema I want to transform to as a dictionary, and pass the JSONBender functions for iterating to my source JSON.

I find it really easy to work with, plus transformation is easy with not much of hassle.

## AJT Project

This project is using JSONBender to transform my schema to a different one.

Currently, it only supports a Simple JSON format, no arrays or whatever complicated shizz.

To make it more dynamic, I am defining a YML file the contains all the fields you want to transform.

**Format**

fields:
 newfield1: oldfield1
 newfield2: oldfield2
 newfield3: oldfield3
 
## TODO

1. Handle nested JSON format
2. Handle multiple files
