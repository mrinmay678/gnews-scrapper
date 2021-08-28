import React, { Component } from 'react';
import './App.css';

export default class App extends Component{
  baseURL="http://15.206.75.100:8000/"

  state={
	  data:[]
  }

  componentDidMount() {
	fetch(`${this.baseURL}news/scrap`,{
		method:"GET",
		headers:{
			"Content-Type": "application/json"
		}
	})
	.then(res =>res.json())
	.then(res =>{
    this.setState({data:res.data})
    console.log(this.state.data)
	})
  }

  render() {
    return(
      <div>
        <table>
          <tr>
            <th>Image</th>
            <th>Title</th>
            <th>Published at</th>
          </tr>
        {
          this.state.data.map(data=>
            <tr>
              <td><a href={data['link']}><img src={data['image']} width="50" height="50"/></a></td>
              <td><a href={data['link']}>{data['title']}</a></td>
              <td>{data['time']}</td>
            </tr>
            )
        }
        </table>
      </div>
    );
  }
}