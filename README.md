# Squirrel Tracker Web Application
THis is a Squirrel Track web app that keeps track of all the known squirrels in Central Park. It is built with functions to import the 2018 Central Park Squirrel Census data and allows adding, updating, and viewing the squirrel data.

## Functions
There are two management commands:
- import_squirrel_data
  * import data (in CSV format) to the database
- export_squirrel_data
  * export data in CSV format
 
## Views
There are five views:
- Map
  * located at: */map*
  * shows a map that displays the location of the squirrel sightings on an OpenStreets map
- List of all sightings
  * located at: */sightings*
  * lists all squirrel sightings with links to edit each and a single link to the “add” sighting view
- Update
  * located at: */sightings/<squirrel_id>*
  * update a particular sighting providing unique-squirrel-id
- Add
  * located at: */sightings*
  * create new sightings
  * fields supported: Fields supported: Latitude, Longitude, Unique Squirrel ID, Shift, Date, Age, Primary Fur Color, Location, Specific Location, Running, Chasing, Climbing, Eating, Foraging, Other Activities, Kuks, Quaas, Moans, Tail flags, Tail twitches, Approaches, Indifferent, Runs from
- Stats
  * located at: */sightings/stats*
  * show general stats about the sightings
   
## Group Name
Project Group 35, Section 1

## UNIs
Unis: [yz3659, xs2321]

## Link to server


    

