// TaskFormModal.js
import React, { useState, useEffect } from 'react';
import { Modal, Button, Form } from 'react-bootstrap';
import axios from 'axios';

const TaskFormModal = ({ show, handleClose, task, refreshTasks }) => {
    const [data, setData] = useState({
        title: '',
        completed: 'Pending'
      });
    useEffect(()=>{
        setData({
            title : task?.title ?? "",
            id : task?.id ?? null,
            completed: task?.completed ?? "Pending"})
    }, [task])

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      if (task) {
        await axios.put(`http://localhost:8000/tasks/${task.id}`, data );
      } else {
        await axios.post('http://localhost:8000/tasks/create-task', data );
      }
      refreshTasks();
      handleClose();
    } catch (error) {
      console.error('Error submitting task:', error);
    }
  };

  return (
    <Modal show={show} onHide={handleClose}>
      <Modal.Header closeButton>
        <Modal.Title>{task ? 'Edit Task' : 'Add Task'}</Modal.Title>
      </Modal.Header>
      <Modal.Body>
        <Form onSubmit={handleSubmit}>
          <Form.Group controlId="taskTitle">
            <Form.Label>Title</Form.Label>
            <Form.Control
              type="text"
              placeholder="Enter task title"
              value={data?.title}
              onChange={(e) => setData((prevState)=>({
                ...prevState,
                title: e.target.value
              }))}
              required
            />
            <Form.Label>status</Form.Label>
            <Form.Control
              as="select"
              value={data?.completed}
              name='completed'
              onChange={(e) => setData((prevState)=>({
                ...prevState,
                completed: e.target.value
              }))}
              required
            >
              <option value="Pending" >Pending</option>
              <option value="In Progress">In Progress</option>
              <option value="Completed">Completed</option>
            </Form.Control>
          </Form.Group>
          <Button variant="primary" type="submit" className="mt-3">
            {task ? 'Update Task' : 'Create Task'}
          </Button>
        </Form>
      </Modal.Body>
    </Modal>
  );
};

export default TaskFormModal;
