import React from 'react';
import Nav from 'react-bootstrap/Nav';
import { SharedStateProvider } from './SharedStateContext';
import SearchApp from './SearchApp'; 
import EditApp from './EditApp';

export default function TabsExample () {
  const [activeTab, setActiveTab] = React.useState('search'); 

  const handleTabSelect = (selectedKey) => {
    setActiveTab(selectedKey);
  };

  return (
    <SharedStateProvider>
    <div>
      <Nav variant="tabs" activeKey={activeTab} onSelect={handleTabSelect}>
        <Nav.Item>
          <Nav.Link eventKey="search">Search</Nav.Link>
        </Nav.Item>
        <Nav.Item>
          <Nav.Link eventKey="Edit">Edit</Nav.Link>
        </Nav.Item>
      </Nav>
      {activeTab === 'search' && <SearchApp />} 
      {activeTab === 'Edit' && <EditApp />}
    </div>
    </SharedStateProvider>
  );
};

