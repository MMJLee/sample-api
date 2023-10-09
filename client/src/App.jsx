import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import IssueService from "./api/IssueService.js";

const [issue, setIssue] = useState(0)

useEffect(() => {
  IssueService.readIssues()
}, [])

function createIssue() {
  IssueService.createIssue(issue)
}

function readIssue() {
  IssueService.readIssue(id)
}

function updateIssue() {
  IssueService.updateIssue(id, issue)
}

function deleteIssue() {
  IssueService.deleteIssue(id, issue)
}
function App() {

  return (
    <div>

    </div>
  )
}

export default App
