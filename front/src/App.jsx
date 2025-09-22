
import { useEffect, useState } from 'react'
import './App.css'
import API_SERVICE from './serivce.jsx'




function App() {
  
  const [result, setResult] = useState(null)
  
  useEffect(()=>{
    API_SERVICE.get('students').then(res=>setResult(res))
  }, [])

  return (
    <>
    {result?.students &&
      <>
        <h1>Студенты</h1>
        <table>
          <thead>
            <tr>
              <th>ФИО</th>
              <th>Возраст</th>
            </tr>
          </thead>
          <tbody>
            {result.students.map((student, index)=>
              <tr key={index}>
                <td>{student.firstname[0]}.{student.patronymic[0]}. {student.secondname}</td>
                <td>{student.age}</td>
              </tr>)
            }
          </tbody>


        </table>
      </>
      }

    
      
    </>
  )
}

export default App
