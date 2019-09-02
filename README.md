# JSON Schema Transformer

So just last week, I was faced with a problem wherein some of our JSON data may need to change field names. Basically it's like mapping to a new JSON Schema.

So in Java, we have the Jolt Transformation to do this easily, but Jolt doesn't have a Python version of its code (or maybe there is but I just wasn't able to find it).

## JSONBender

Here comes the solution.

While trying to search the web or what tools can be used to transform a JSON data to a different schema, there were actually a lot that shown but seems a bit complicated.

Then I stumbled upon this [JSONBender](https://github.com/Onyo/jsonbender) library, where I can just define the schema I want to transform to as a dictionary, and pass the JSONBender functions for iterating to my source JSON.

I find it really easy to work with, plus transformation is easy with not much of hassle.

## AJT Project

I am not using the actual JSONBender library, but it helped gave me the idea on how to transform a JSON object to a different schema.

A schema YAML file is being used to define the mapping transformation.

**Format**

fields:
 newfield1: oldfield1
 newfield2: oldfield2
 newfield3: oldfield3
 nested: <-- (Used if the next field contains a JSON object)
  newfield4:
   oldfield4:
    newfield5: oldfield5 <-- (techinically this part is an object under field #4)
 
## Limitations

1. The words 'fields' and 'nested' in here are reserved keywords, and can't be part of your original JSON object.

2. This is only good for 1 to 1 mapping of fields, and can't handle complicated mapping like flattening of nested objects or combining 2 fields to a single field.

** If you need to handle complicated mapping, then best to use existing libraries out there. **

## TODO

1. Handle more complicated transformations
