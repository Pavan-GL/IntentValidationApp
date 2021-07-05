Problem Context:
Every statement user speaks that could be each utterance. For example : “Do you know chatbot and show me recent growth statistics of chatbot” the entire sentence is the utterance. An intent is the user intention. For example if the user says “Show me recent growth statistics” the user intent is to retrieve a list of statistical headlines. 
	An entity modifies an intent. For example if user types “show me recent growth statistics of chatbot” the entities are “recent” and “statistics” and entities are sometimes referred to as slots.
	Do you know chatbot and show me recent growth statistics of chatbot-> utterance. 
* Show me ->Intent - something needs to be shown.
* Growth statistics -> Entity that modifies the intent.

Problem statement:
Not every entity serves to identify an intent and ability to identify which one is valid or which one is not valid. This major problem can be solved using chatbots. Hence this task is to create the API’s which a chatbot could easily refer while identifying the entities. 
	We can assume that the validation criteria to be already provided some other service. Our task is to validate the entities based on this criteria. Here we need to validate the entire finite set and  validate a slot with numeric values.






Intention validator:
This project intendes to validates intention composed of entities behind the utterance. It's a basic Django app which has three POST Apis
* validate_finite_entity : https://localhost:8000/validateFiniteEntity
* validate_num_entity: https://localhost:8000/validateNumEntity





Assumptions:


* If pick_first is present, it will simply overide the behaviour of support_multiple key and first value will be picked regardless the entity value is valid or not
* Constraint is considered to be boolean or bad request response is thrown.
* If users enter garbage values or irrelevant  information then our API’s will throw the exceptions  either it will show it as a payload or bad request or data types are incorrect it may be null values or required information is missing.
Run Automated Tests

You can run the already pre-built tests for the API’s to test sanity functions as follows: (It takes around 0.030s to 0.045s)
* ./manage.py test
* python manage.py test



