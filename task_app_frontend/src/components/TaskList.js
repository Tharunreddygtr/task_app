// TaskList.js
import React, { useState, useEffect } from 'react';
import { Button, Form } from 'react-bootstrap';
import axios from 'axios';
import TaskFormModal from './TaskFormModal';
// import './TaskList.css'; // Import the CSS file

const TaskList = () => {
  const [tasks, setTasks] = useState([]);
  const [filteredTasks, setFilteredTasks] = useState([]);
  const [showModal, setShowModal] = useState(false);
  const [selectedTask, setSelectedTask] = useState(null);
  const [searchTerm, setSearchTerm] = useState('');

  const fetchTasks = async (search = '') => {
    try {
      const response = await axios.get('http://localhost:8000/tasks/', {
        params: { search }
      });
      setTasks(response.data);
      setFilteredTasks(response.data);
    } catch (error) {
      console.error('Error fetching tasks:', error);
    }
  };

  useEffect(() => {
    fetchTasks();
  }, []);

  const handleDelete = async (taskId) => {
    try {
      await axios.delete(`http://localhost:8000/tasks/${taskId}`);
      fetchTasks(searchTerm); // Refresh tasks after deletion
    } catch (error) {
      console.error('Error deleting task:', error);
    }
  };

  const handleShowModal = (task = null) => {
    setSelectedTask(task);
    setShowModal(true);
  };

  const handleCloseModal = () => {
    setShowModal(false);
    setSelectedTask(null);
  };

  const handleSearchChange = (e) => {
    const search = e.target.value;
    setSearchTerm(search);
    fetchTasks(search); 
  };

  const getStatusIcon = (status) => {
    console.log(status)
    switch (status) {
      case 'Pending':
        return <i className="fas fa-hourglass-half" title="Pending" />;
      case 'In Progress':
        return <i className="fas fa-spinner" title="In Progress" />;
      case 'Completed':
        return <i className="fas fa-check-circle" title="Completed" />;
      default:
        return null;
    }
  };


  return (
    <div className="task-list-container">
      <div className='header' style={{display: "flex", justifyContent: "space-between", alignItems: "center"}}>
        <h1>Task List</h1>
        <Button onClick={() => handleShowModal()} className="mb-3">Add Task</Button>
      </div>
      <Form.Group controlId="search">
        <Form.Control
          type="text"
          placeholder="Search by title or ID"
          value={searchTerm}
          onChange={handleSearchChange}
        />
      </Form.Group>
      <ul className='task-list'>
        {filteredTasks.map(task => (
          <li key={task.id} className="task-item">
            <div className="task-title">{task.title}</div>
            <div className="task-buttons">
                {getStatusIcon(task.completed)}
              <Button variant="warning" className="mx-2" onClick={() => handleShowModal(task)}>Edit</Button>
              <Button variant="danger" onClick={() => handleDelete(task.id)}>Delete</Button>
            </div>
          </li>
        ))}
      </ul>
      <TaskFormModal show={showModal} handleClose={handleCloseModal} task={selectedTask} refreshTasks={fetchTasks} />
    </div>
  );
};

export default TaskList;
