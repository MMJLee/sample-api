import axios from "axios";

const apiClient = axios.create({
  baseURL: "http://0.0.0.0:8000/issue",
  withCredentials: true,
  httpsAgent: false,
  headers: {
    Accept: "application/json",
    "Content-Type": "application/json",
  }
});

export default {
  async readIssues() {
    this.response = await apiClient.get("");
    return this.response;
  },
  async readIssue(id) {
    this.response = await apiClient.get(`/${id}`);
    return this.response;
  },
  async createIssue(issue)  {
    this.response = await apiClient.post("", issue);
    return this.response;
  },
  async updateIssue(id, issue) {
    this.response = await apiClient.put(`/${id}`, issue);
    return this.response;
  },
  async deleteIssue(id, issue)  {
    this.response = await apiClient.delete(`/${id}`, issue);
    return this.response;
  }
};