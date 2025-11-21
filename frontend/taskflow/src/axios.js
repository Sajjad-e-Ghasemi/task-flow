import axios from "axios";

const instance = axios.create({
    baseURL: "http://127.0.0.1:8000/",
    timeout: 10000,
    headers:{
        "Content-Type": "application/json",
    } // Set a timeout of 10 seconds
});
export default instance;