import { useEffect, useState } from "react"

export default function TableView (props) {
    const {token, setLogged} = props

    const [tableData, setTableData] = useState([])
    const [userAgeGroup, setUserAgeGroup] = useState([])

    const fetchTable = () => {
        fetch('/api/view/get_table', {
            method: 'get',
            headers: new Headers({
              'Authorization': 'Bearer ' + token
            })
        }).then(r => r.json())
        .then(resp => {
            setTableData(JSON.parse(resp.ageGroups))
            setUserAgeGroup(resp.userAgeGroup)
        })
      }

    useEffect(() => {
        fetchTable();
    }, []);

    const handleSignOut = () => {
        setLogged(false)
    }

    return (
        <div>
            <h1>Age Group Distribution</h1>

            <div style={{display: 'flex',  justifyContent:'center', alignItems:'center'}}>
                <table>
                    <thead>
                    <tr>
                        <th>Age Group</th>
                        <th>Count</th>
                    </tr>
                    </thead>
                    <tbody>
                        {
                            tableData.map((item) => (
                                <tr key={item.id}>
                                    {item.ageGroup === userAgeGroup ?
                                    <td bgcolor={'green'}>{item.ageGroup}</td>
                                    :
                                    <td> {item.ageGroup}</td>
                                    }
                                    {item.ageGroup === userAgeGroup ?
                                    <td bgcolor={'green'}>{item.count}</td>
                                    :
                                    <td> {item.count}</td>
                                    }
                                    <td/>
                                </tr>
                            ))
                        }
                    </tbody>
                </table>
            </div>

            <button onClick={handleSignOut}>Sign Out</button>
        </div>
    )
}