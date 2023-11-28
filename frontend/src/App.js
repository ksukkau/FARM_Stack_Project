import React, {useEffect} from 'react';
import Tab from 'react-bootstrap/Tab';
import Tabs from 'react-bootstrap/Tabs';
import SearchApp from './SearchApp'; 
import EditApp from './EditApp';
import axios from 'axios';
import { SharedStateProvider } from './SharedStateContext';

URL = 'https://farm-stack-project.customcloud.ca'

export default function NavTabs () {

  useEffect(() => {
    const fetchData = async () => {
      try {
        // Make a POST request to the backend endpoint
        const response = await axios.post(`${URL}/api/v1/pokemon/reload`);

        // Handle the response as needed
        console.log(response.data.message);

      } catch (error) {
        console.error('Error updating database:', error);
      }
    };

    fetchData(); // Call the async function

    // This effect runs only once after the initial render
  }, []);

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