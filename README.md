### Intelligent System Case Study: Smart Traffic Management System Using Adaptive Signal Control

To run the system type:
python trafficlight_gui.py

### Power point presentation 
- Canva Link: https://www.canva.com/design/DAGoN1naHcc/XUfQfC75H0nN_xN2VjRoDQ/edit?utm_content=DAGoN1naHcc&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton

Case Study Explanation: Smart Traffic Light GUI System
Introduction
This case study explores the design and implementation of a Smart Traffic Management System using Python's Tkinter library. The aim is to simulate an adaptive traffic signal controller that can improve traffic flow at intersections by prioritizing directions with the most vehicles.

Objective
To develop a graphical user interface (GUI)-based simulation that mimics a real-world traffic light system. The system should:
Dynamically adjust signal timings.
Visually represent roads and signals.
Use input from users to simulate varying traffic conditions.
Problem Addressed
Traditional traffic light systems work on fixed intervals, which is inefficient during uneven traffic flow. This leads to:
Long waits at empty lanes.
Congestion in busy lanes.
Increased fuel consumption and pollution.
This project addresses the problem by introducing adaptive signal control using real-time vehicle input.

System Design & Features
GUI Interface: Developed using Tkinter with a canvas showing roads and 4-directional traffic lights (North, South, East, West).
Traffic Light Colors: Each signal has three lights — Red, Orange, and Green — simulating real-world behavior.
Vehicle Input: Users input the number of vehicles from each direction.
Dynamic Simulation: Based on the input, the direction with the highest vehicle count gets priority.
Responsive Layout: The interface adapts to window size changes and fills the screen.
Algorithm Explanation
Vehicle counts are taken as input.
Directions are sorted in descending order of vehicle count.
For each direction:
The green light is shown for 2 seconds.
The orange light for 1 second.
Then it returns to red before the next direction gets the green light.
All updates run in a separate thread to keep the UI responsive.

Algorithm Used: Greedy Algorithm
This system uses a greedy approach to prioritize the direction with the highest number of vehicles. It does this by:
Collecting vehicle counts from all four directions.
Selecting the direction with the highest count.
Assigning it the green signal before moving to the next highest.
Greedy algorithms make the optimal choice at each step to find a global optimum — here, it's to reduce wait time for the busiest lane.

Tools & Technologies Used
Python 3
Tkinter for GUI
Canvas widget for drawing roads and lights
Threading for simulation without freezing the GUI

Outcomes
Successfully demonstrates how smart signals could optimize intersection flow.
Easy to use and visually intuitive.
Lays the foundation for more advanced systems using sensors or real-time data sources.

Limitations & Future Work
Does not simulate real-time traffic (e.g., sensor input).
Lights are static in position and do not animate vehicle flow.
Future enhancements:
Add vehicle animations.
Use real-time traffic APIs or sensors.
Introduce pedestrian signals or emergency vehicle priority.
