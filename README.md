# BorneanBirds

## Step 1: Building a universal bird model.
To do this, pull bird recordings from xeno-canto, an archive of recordings from amateur/hobbysit birders.
Xeno-canto uploaders also tag their sounds with the region from which it was pulled,  so we can sort it and pull recordings only from the country of interest to us - Indonesia

Using the map functionality, we filter for recordings done in the specific part of indoneisian borneo for which we have soundscape data - East Kalimantan, on the island of Borneo.

We then map the id's of recordings here to the ones tagged as indoneian birds, and use just those recordings to build our bornean universal bird model.

1. Perform spectral subtration & remove mean frequencies - this will likely get rid of insect / wind etc noises that are common across recordings.

http://www.xeno-canto.org/498016/download

