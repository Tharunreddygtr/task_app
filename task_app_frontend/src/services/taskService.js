import axios from 'axios';

const API_URL = 'http://localhost:8000';
const getTasks = () => {
    return axios.get(`${API_URL}/tasks`);
};

const getTask = (id) => {
    return axios.get(`${API_URL}/tasks/${id}`);
};

const createTask = (task) => {
    return axios.post(`${API_URL}/tasks/create-task`, task);
};

const updateTask = (id, task) => {
    return axios.put(`${API_URL}/tasks/${id}`, task);
};

const deleteTask = (id) => {
    return axios.delete(`${API_URL}/tasks/${id}`);
};

export { getTasks, getTask, createTask, updateTask, deleteTask };
