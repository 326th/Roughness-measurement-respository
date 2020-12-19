# Mannual data insertion

You may have your data from other method other than our programs, this is a guide on how to add them to your database

Your data needs Latitude, Longtitude, Roughness, Elevation and your designated Grouping

Replace [Latitude], [Longtitude], [Roughness], [Elevation] and [Grouping] in the following SQL commands

```
INSERT INTO `Acceleration`( `Latitude`, `Longitude`, `Acceleration`, `Grouping`) VALUES ([Latitude], [Longtitude], [Roughness], [Grouping]);
INSERT INTO `Height`(`Latitude`, `Longitude`, `Height`) VALUES ([Latitude], [Longtitude], [Elevation])
```
