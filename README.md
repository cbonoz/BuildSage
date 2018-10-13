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
Use NLP to search lessons learned from past construction experiences.

## How I built it
Uses a python backend to search through an indexed collection of construction reports based on the user's query or current task. Escalates the most pertinent reports for the given task up to the user.

Fields of relevance currently used for consideration of different lessons learned
<pre>
  Country
  Project Type
  Client
  Contract Type
  Construction Technology
  Activity
  Importance level
  Experience Type: Best Practice, Problem, or Both
</pre>

## Challenges I ran into
Aggregating the data and implementing the NLP such that pertinent results could be returned for a query.

## Accomplishments that I'm proud of
It works.

## What I learned
How to deploy an NLP model and connect it to a live, running website

## What's next for BuildSage
* Release to the public and collect more build reports that can be indexed and returned in search results.


### Useful Links
* https://www.designingbuildings.co.uk/wiki/Lessons_learned_report_for_building_design_and_construction
* https://www.sciencedirect.com/science/article/pii/S1877042816308783
* http://www.horstconstruction.com/lessons-challenging-construction-project/
* https://pdfs.semanticscholar.org/presentation/862e/cc1f7c6d6d5e7003a4ed4abbb6e7da72dfbc.pdf
* https://www.probuilder.com/home-building-25-lessons-learned
* https://www.qaqc-construction.com/library-lessons-learned.php