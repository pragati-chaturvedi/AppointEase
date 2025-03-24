# AppointEase - AN AI Appointment Scheduling Chatbot

This repository contains a fully integrated AI-based chatbot system for scheduling appointments using Google Calendar. The project leverages OpenAI's GPT API for conversational interactions, integrates with Google Calendar to manage scheduling events, and allows for function calling to interact with external APIs like Google Calendar and Google Docs. Users can interact with the chatbot through a graphical user interface (GUI), where they can provide event details, and the system will automatically schedule appointments on their Google Calendar or fetch the user's schedule from Google Docs.

## Features
- Google Calendar Integration: Allows users to add events directly to their Google Calendar through the chatbot.
- AI Chatbot: Uses GPT-3.5 for natural language processing to understand and process user inputs.
- Function Calling: Supports dynamic function calls to external services like Google Calendar and Google Docs based on the user's requests. Functions like scheduling an appointment or fetching the schedule are triggered by the AI.
- Appointment Scheduling: Automatically schedules appointments based on user input, including event summary, description, start time, and end time.
- Google Docs Integration: Fetches and displays available schedules stored in Google Docs, assisting users in scheduling without conflicts.

## Requirements
- Python 3.x
- Google Calendar API
- Google Docs API
- OpenAI API Key

## How It Works:
1. User Interaction: The user interacts with the chatbot via a GUI. They can input text to schedule an event or check the availability of the calendar.
2. AI-powered Response with Function Calls: The chatbot uses OpenAI's API to interpret the user's request. It dynamically calls specific functions (e.g., schedule_appointment, print_schedule) based on the conversation's context and executes the corresponding actions.
3. Schedule Appointment: If the user wants to schedule an appointment, the chatbot requests event details (summary, description, start time, and end time) and creates the event on Google Calendar.
4. Schedule Fetching: The chatbot can also fetch the current day's schedule from Google Docs to show available times.

