<p align='center'>
  <img src="./img/build_sage_orig.png" width=400/>
</p>

BuildSage
---

BuildSage leverages NLP and AI to bring the most pertinent "lessons learned" to attention from past construction experiences.

## Inspiration

Construction companies are project-based organizations, since much of their knowledge is generated on site, from projects they carry out. In fact, projects are an important source of expert know-how and organizational knowledge, but lessons-learned from them are not systematically incorporated into subsequent projects, evidencing a lack of knowledge management and learning culture in local construction companies. This article describes a research effort that addressed this situation and developed a lessons-learned system to help construction companies to overcome these limitations. 

Implementing proper closeout might reduce the cost of construction consultants and make current contractors more competitive.

## What it does
Uses a combination of NLP and fuzzy search to parse through a database of uploaded lessons learned from past construction experiences. Users can submit new lessons that can be indexed and discovered by other users.

## How I built it
Uses a python backend to search through an collection of construction reports based on the user's query. Escalates the most pertinent reports for the given task up to the user based on a parsed version of the request.

Fields of relevance currently used for consideration of different lessons learned. This could be expanded in future work.

<pre>
  Title: Theme of the lesson
  Description: More detail on the lesson
  Project Type
  Country: Currently just U.S.
  Construction Technology: Materials used, equipment, etc.
  Importance level: low (1), medium (2), high (3)
  Experience Type: Best Practice, Problem, or Both
</pre>

## Challenges I ran into
Gathering data and implementing the NLP/search such that pertinent results could be returned for a query.

## Accomplishments that I'm proud of
It works.

## What I learned
How to deploy an NLP model and connect it to a live, running website.

## What's next for BuildSage
* Release to the public and collect more build reports that can be indexed and returned in search results.

### Running the app
The app requires both the backend (python) server and webserver (react) to be running.

To start the python server:
<pre>
  pip install -r requirements.txt
  python app.py
</pre>

</pre>
To start the web server, use the following command:
<pre>
  yarn && yarn start
</pre>

The web server should now be running on port `3000` (with the backend python server on port `8080`).

### Example Searches
* I'm building a condo for a commercial application
* I'm laying the foundation for a new residence
* etc..

### Useful Links
* https://github.com/explosion/spacy-services/tree/master/displacy
* https://github.com/explosion/spacy-services

### Construction Lesson/Report Resources
* https://www.designingbuildings.co.uk/wiki/Lessons_learned_report_for_building_design_and_construction
* https://www.sciencedirect.com/science/article/pii/S1877042816308783
* http://www.horstconstruction.com/lessons-challenging-construction-project/
* https://pdfs.semanticscholar.org/presentation/862e/cc1f7c6d6d5e7003a4ed4abbb6e7da72dfbc.pdf
* https://www.probuilder.com/home-building-25-lessons-learned
* https://www.qaqc-construction.com/library-lessons-learned.php