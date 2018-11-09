
- Outline a rough timeline for the major milestones of your project.  This will mainly be useful to refer back to as we move through the project.  
- What do you view as the biggest risks to you being successful on this project?  
- [This section will be completed in class on 11/9] Given each of your YOGAs, in what ways is this project well-aligned with these goals, and in what ways is it misaligned?  If there are ways in which it is not well-aligned, please provide a potential strategy for bringing the project and your learning goals into better alignment.  There should be an individual section for each person on the team addressing the fit between the YOGA and the project topic.  


# Two Rats in a Maze
#### *A Project on Localization using Scan Matching*
###### The Rats: Gretchen Rice and Siena Okuno  


# Main Idea:  
Picture this: 1 map, 1 maze, 1+1=2, 2 robots, 2+1=3, 3 is a triangle, illuminati.

We will have one physical 3D maze with many sharp corners that is fairly small. Two Neatos will start at different points in the maze with no information as to their location or the other robot's location. From there, they with individually map out their surrounding with lidar and relay the information to one common computing source. After a decent map is constructed by each robot as they move through the maze, they will attempt to locate one another by overlaying the maps.  
Our project will be focusing on the overlaying and comparing of the map scans and not the communication or mapping abilities aspects of the project.  

### MVP
As an MVP, our robots will create individual maps by running through the entire maze one at a time and starting at different locations. The robots will have no prior information about the maze, but will have a rough estimate of where they are starting. This will allow us to focus on the scan matching aspect with a more complete scan at first. We will either try one algorithm and imrove that algorithm, or will try multiple algorithms, depending on how the inital algorithm seems to work.  

### Stretch Goal
Ideally, we would want our robot to be able to create a shared map using two different partial maps. Then this map will be used to find each other. We might try several different algorithms and compare to see which has the best results.


# Algorithms
## Algorithms to Use for Map Overlaying
- Iterative closest point  

## Algorithms to Use for Mapping
- Hector SLAM: Uses scan alignment to stitch together scan readings as moving throug ha map  

# Timeline
Meetings: Wednesdays 7-9, Saturdays 11-1  
11/10 *11-12*  
11/13: *Research into other algorithms, pick the one we want to try first*   
11/14 *7-9*  
11/16: *Pick mapping algorithm and communication method, start work on these. Have general code architecture*  
**THANKSGIVING BREAK**    
11/27: *Finish mapping and communication code, have it working. Start work on overlaying code*  
11/28 *7-9*
11/30: *Work on overlaying code*   
12/1 *11-1*  
12/4:  *MVP complete*  
12/5 *7-9*  
12/7: *Work toward stretch goal, catch up if theings haven't been working*    
12/8 *11-1*     
12/12 *7-9*  
12/14: [FINALS PERIOD] 

# Goals
### Project Goals  
- Working project, the robot successfully completes our mvp  
- Actually understand the code being written  
- Work on something applicable and relevant to the robotics field  

### Team Expectations  
- Transparency in the work being done  
- Pair programming and task division  
