# Sorting Algorithm Visualizer

## Overview

The **Sorting Algorithm Visualizer** is an educational Python application designed to help users understand and observe the behavior of various sorting algorithms. Utilizing the Tkinter library for graphical representation, this tool allows users to interactively explore how different algorithms handle data and progress toward sorting.

## Features

- **Interactive Visualization:** Watch as the selected sorting algorithm processes the data step-by-step, with real-time visual updates and color changes illustrating each operation.

- **Supported Algorithms:**
  - **Bubble Sort:** Compares and swaps adjacent elements if they are out of order, repeatedly iterating through the list.
  - **Selection Sort:** Finds the smallest element from the unsorted portion of the list and moves it to the end of the sorted portion.
  - **Insertion Sort:** Builds the final sorted array one element at a time, inserting each element into its correct position in the sorted portion.

- **Customizable Settings:**
  - **Array Size:** Adjust the number of elements in the list to see how algorithms perform with varying data sizes.
  - **Visualization Speed:** Control the speed of the sorting process using a slider, allowing for both slow, detailed views and faster overviews.

- **Real-Time Feedback:** Provides immediate visual feedback on the sorting process, enhancing comprehension of how each algorithm functions.

## Program Overview

The visualizer is designed to offer an educational experience by providing clear, visual representations of sorting algorithms in action. The application features:

- **Sorting Algorithms:** Implemented as separate functions, each algorithm updates the visual display of the data array in real-time.

- **GUI Components:** Built using Tkinter, the interface includes sliders for adjusting array size and speed, a dropdown menu for selecting sorting algorithms, and a button to start the visualization. 

- **Visualization Logic:** Central to the application is the `drawData` function, which renders the data array on a canvas, using colors to differentiate between various states (e.g., unsorted, being compared, sorted).

## Key Functions

- **`drawData(data, colorArray)`:** Updates the canvas with the current state of the data array, using rectangles to represent elements and colors to indicate their status.

- **`startAlgorithm()`:** Initiates the sorting process based on the selected algorithm and user settings, calling the appropriate sorting function.

- **`generateData()`:** Creates a random list of integers according to the user's specifications for array size, which is then sorted by the chosen algorithm.

## User Interface

- **Algorithm Dropdown:** Choose the sorting algorithm you wish to visualize.
- **Array Size Slider:** Set the number of elements in the list to observe how algorithms handle different input sizes.
- **Speed Slider:** Adjust the speed of the visualization to view the sorting process in detail or quickly.
- **Start Button:** Begin the sorting visualization with the configured settings.
- **Time Complexity Display:** View theoretical time complexity information for the selected sorting algorithm, providing context alongside the visual representation.

Explore and learn sorting algorithms interactively with the Sorting Algorithm Visualizer!

