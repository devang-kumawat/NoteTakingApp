import React, { useEffect, useState } from "react";

import NoteContainer from "./Components/NoteContainer/NoteContainer";
import Sidebar from "./Components/Sidebar/Sidebar";

import "./App.css";
import { debounce } from "lodash";

import axios from "axios";

function App() {
  const [notes, setNotes] = useState([]);
  // Fetch notes from the server when the component mounts
  // and set the notes state with the fetched data.
  useEffect(() => {
    axios.get("http://localhost:5000/notes")
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
      const res = await axios.post("http://localhost:5000/notes", newNote);
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
      axios.delete(`http://127.0.0.1:5000/notes/${id}`);
    } catch (err) {
      console.error("Error deleting note:", err);
    }
  };

  const debouncedUpdate = debounce(async (note) => {
    try {
      await axios.put(`http://127.0.0.1:5000/notes/${note.id}`, note);
    } catch (err) {
      console.error("Debounced update failed", err);
    }
  }, 100); // wait 500ms after last input

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
