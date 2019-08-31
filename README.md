# JSON Schema Transformer

So just last week, I was faced with a problem wherein some of our JSON data may need to change field names. Basically it's like mapping to a new JSON Schema.

So in Java, we have the Jolt Transformation to do this easily, but Jolt doesn't have a Python version of its code (or maybe there is but I just wasn't able to find it).

## JSONBender

Here comes the solution.

While trying to search the web or what tools can be used to transform a JSON data to a different schema, there were actually a lot that shown but seems a bit complicated.

Then I stumbled upon this JSONBender library, where I can just define the schema I want to transform to as a dictionary, and pass the JSONBender functions for iterating to my source JSON.

I find it really easy to work with, plus transformation is easy with much of hassle.

## AJT Project

I am not using the actual JSONBender library, but it helped gave me the idea on how to transform a JSON object to a different schema.

A schema YAML file is being used to define the mapping transformation.

**Format**

fields:
 newfield1: oldfield1
 newfield2: oldfield2
 newfield3: oldfield3
 array: <-- (Used if the next field contains a JSON object)
  newfield4:
   oldfield4:
    newfield5: oldfield5 <-- (techinically this part is an object under field #4)
 
## TODO

1. Handle multiple files