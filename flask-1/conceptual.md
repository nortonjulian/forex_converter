### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript?
  Javascript is a scripting language that helps to create interactive
  web pages while Python is an object-oriented langauge with built in data
  structures ideal for application development

Javascript has no concept of mutable or immutable while Python has mutable and
immutable data types

Javascript uses curly brackets whereas Python uses indentation

- Given a dictionary like `{"a": 1, "b": 2}`: , list two ways you
  can try to get a missing key (like "c") _without_ your programming
  crashing.

  You can use the update() and merge operator to add to a dictionary

- What is a unit test?
  A unit test is a segment of code written to test other pieces of code

- What is an integration test?
  An integration test tests multiple components of code at the same time.

- What is the role of web application framework, like Flask?
  Flask provides the tools and libraries upon which you can build an application
  in Python

- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?
  The first one uses a form in "request.form" where a form is set up in a template
  while the second uses the query string in "request.args". It depends on what type
  of application. If it's just searching for something in a database the "request.args"
  is fine while if it is a means of collecting information use a form in "request.form"

- How do you collect data from a URL placeholder parameter using Flask?
  request.args

- How do you collect data from the query string using Flask?
  request.args.get

- How do you collect data from the body of the request using Flask?
  reuest.form

- What is a cookie and what kinds of things are they commonly used for?
  A "cookie" is a name/string value pair stored by the client. The server
  tells the client to save them and the client sends them to the server with each request

- What is the session object in Flask?
  Sessions contain info for the current browser, Are serialized and ¡"signed" so users can't modify the data.

- What does Flask's `jsonify()` do?
  Jsonify turns javascript into JSON
