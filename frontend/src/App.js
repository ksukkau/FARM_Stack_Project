import React, {useEffect, useState} from 'react';
import Tab from 'react-bootstrap/Tab';
import Tabs from 'react-bootstrap/Tabs';
import SearchApp from './SearchApp'; 
import EditApp from './EditApp';
import axios from 'axios';
import Spinner from 'react-bootstrap/Spinner';
import { SharedStateProvider } from './SharedStateContext';

URL = 'https://farm-stack-project.customcloud.ca'

export default function NavTabs () {
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchData = async () => {
      try {
        // Make a POST request to the backend endpoint
        const response = await axios.post(`${URL}/api/v1/pokemon/reload`);

        // Handle the response as needed
        console.log(response.data.message);

      } catch (error) {
        console.error('Error updating database:', error);
      } finally {
        setLoading(false); // Set loading to false regardless of success or failure
      }
    };

    fetchData(); // Call the async function

    // This effect runs only once after the initial render
  }, []); 

  // Render loading state if data is still being fetched
  if (loading) {
    return <div className='d-flex justify-content-center align-items-center min-vh-100'>
    <Spinner animation="border" variant="success" />
    <p style={{paddingLeft:"1rem"}}>Loading...</p>
  </div>;
  }


  return (
    <div>
      <SharedStateProvider>
      <Tabs
      defaultActiveKey="search"
      id="uncontrolled-tab-example"
      className="mb-3"
    >
      <Tab eventKey="search" title="Search">
        <SearchApp/>
      </Tab>
      <Tab eventKey="edit" title="Edit">
        <EditApp/>
      </Tab>
    </Tabs>
      </SharedStateProvider>
      </div>
  );
};