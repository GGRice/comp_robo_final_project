# Two Rats in a Maze
#### *A Project on Localization using Scan Matching*
###### The Rats: Gretchen Rice and Siena Okuno  


# Main Idea:  
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
- Hector SLAM: Uses scan alignment to stitch together scan readings as moving through a map  
  - Seems to create map by comparing readings to map, make our own Hector SLAM?
- Extended Kalman filter: standard form of SLAM
- G-Mapping: Another SLAM algorithm, more computationally heavy than Hector, has particle filter in it

# Timeline
Meetings: Wednesdays 7-9, Saturdays 11-1  
11/10: *(11-12) Find algorithms*  
11/13: *(class) Pick the algorithm we want to try first, look into mapping and communication methods, create general code architecture*   
11/14: *(7-9) Start mapping and communication code, make a maze*  
11/16: *(class) Continue working on mapping and communicating, hopefully finish before Thanksgiving break*    
**THANKSGIVING BREAK**    
11/27: *(class) Finish mapping and communication code, have it working. Start work on overlaying code*  
11/28: *(7-9)*  
11/30: *(class) Work on overlaying code*   
12/1: *(11-1)*  
12/4:  *(class) MVP complete*  
12/5: *(7-9)*  
12/7: *(class) Work toward stretch goal, catch up if theings haven't been working*    
12/8: *(11-1)*     
12/12: *(7-9)*  
12/14: *(class) [FINALS PERIOD]* 

# Goals
### Project Goals  
- Working project, the robot successfully completes our mvp  
- Actually understand the code being written  
- Work on something applicable and relevant to the robotics field  

### Team Expectations  
- Transparency in the work being done  
- Pair programming and task division  

# Things to Read
- ICP slides: https://cs.gmu.edu/~kosecka/cs685/cs685-icp.pdf  
- SCD papre: https://igl.ethz.ch/projects/ARAP/svd_rot.pdf  
- Hector SLAM: https://l.messenger.com/l.php?u=https%3A%2F%2Fcdn.fbsbx.com%2Fv%2Ft59.2708-21%2F46969079_258992578304653_6392052041107111936_n.pdf%2F06106777.pdf%3F_nc_cat%3D103%26_nc_ht%3Dcdn.fbsbx.com%26oh%3D8eded0cad0772571a8095c6af2d149ae%26oe%3D5BFF7B4A%26dl%3D1&h=AT17rZz-f7Bt7qCx8DVNq65xxZ1p62S0pOoModQoUmNxQoAxEqOGuWH8IIx4TOmeBAuy9CenW67iCmNgu1FcN25p0U4zCm-dDdATF5jPHPCpVCFcmlR4yj9ZAK0OakYMgtNOI-5Y9QkyKw  

