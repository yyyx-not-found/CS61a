SELECT Name FROM records
  WHERE Supervisor="Oliver Warbucks";

SELECT * FROM records
  WHERE Supervisor=Name;

SELECT Name FROM records
  WHERE Salary>5000 ORDER BY Name;



SELECT Day, Time FROM records, meetings
  WHERE records.Division=meetings.Division AND records.Supervisor="Oliver Warbucks";

SELECT a.Name FROM records AS a, records AS b
  WHERE a.Supervisor=b.Name AND a.Division<>b.Division;

SELECT a.Name, b.Name
  FROM records AS a, records AS b, meetings AS a_meeting, meetings AS b_meeting
  WHERE a.Division=a_meeting.Division AND b.Division=b_meeting.Division AND
  a_meeting.Day=b_meeting.Day AND a_meeting.Time=b_meeting.Time AND a.Name<b.Name;



SELECT Supervisor, SUM(Salary) FROM records
  GROUP BY Supervisor;

SELECT Day FROM records, meetings
  WHERE records.Division=meetings.Division
  GROUP BY Day Having COUNT(*)<5;

SELECT a.Division FROM records AS a, records AS b
  WHERE a.Division=b.Division AND a.Name<b.Name
  GROUP BY a.Division Having a.Salary+b.Salary<100000;

  

CREATE TABLE num_taught AS
  SELECT Professor, Course, COUNT(*) AS times FROM courses
  GROUP BY Professor, Course;

SELECT a.Professor, b.Professor, a.Course
  FROM num_taught AS a, num_taught AS b
  WHERE a.Course=b.Course AND a.Professor<b.Professor AND a.times=b.times;

SELECT a.Professor, b.Professor FROM courses AS a, courses AS b
  WHERE a.Professor<b.Professor AND a.Course=b.Course AND a.Semester=b.Semester
  GROUP BY a.Professor, b.Professor Having COUNT(*)>1;