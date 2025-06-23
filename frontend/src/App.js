import React, { useEffect, useState } from "react";

import NoteContainer from "./Components/NoteContainer/NoteContainer";
import Sidebar from "./Components/Sidebar/Sidebar";

import "./App.css";
import { debounce } from "lodash";

import axios from "axios";

import BASE_URL from "./api";



function App() {
  const [notes, setNotes] = useState([]);
  // Fetch notes from the server when the component mounts
  // and set the notes state with the fetched data.
  useEffect(() => {
      axios.get(`${BASE_URL}/notes`)
      .then((res) => {
        setNotes(res.data);
      })
      .catch((err) => {
        console.error("Error fetching notes:", err);
      });
  }, []);


  const addNote = async(color) => {
    // const tempNotes = [...notes];
    const newNote = {
      id: Date.now().toString() + Math.floor(Math.random() * 49),
      text: "",
      time: Date.now(),
      color,
    };
    try{
      const res = await axios.post(`${BASE_URL}/notes`, newNote);

      setNotes([...notes, res.data]);
    } catch (err) {
      console.error("Error adding note:", err);
    }
  };

  const deleteNote = (id) => {
    const tempNotes = [...notes];

    const index = tempNotes.findIndex((item) => item.id === id);
    if (index < 0) return;

    tempNotes.splice(index, 1);
    setNotes(tempNotes);

    // Delete the note from the server
    try {
      axios.delete(`${BASE_URL}/notes/${id}`)
    } catch (err) {
      console.error("Error deleting note:", err);
    }
  };

  const debouncedUpdate = debounce(async (note) => {
    try {
      await axios.put(`${BASE_URL}/notes/${note.id}`, note)
    } catch (err) {
      console.error("Debounced update failed", err);
    }
  }, 100); // wait 100ms after last input

  const updateText = (text,id)=>{
    const tempNotes = [...notes];
    
    const index = tempNotes.findIndex((item) => item.id === id);
    if (index < 0) return;

    tempNotes[index].text = text;
    setNotes(tempNotes);

    // Update the note on the server
    debouncedUpdate(tempNotes[index]);
  }
  return (
    <div className="App">
      <Sidebar addNote={addNote} />
      <NoteContainer 
      notes={notes} 
      deleteNote={deleteNote} 
      updateText = {updateText}
      />
    </div>
  );
}

export default App;
