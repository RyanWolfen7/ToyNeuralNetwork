import { useState } from 'react'
import './App.css'

function App() {
  const [network, setNetwork] = useState({
    layers: 1,
    inputs: 2,
    outputs: 1,
    biases: [0,1,2],
    weights: [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6]]
  });

  const updateNetwork = async () => {
    const response = await fetch('/api/network', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(network)
    });

    if (!response.ok) {
      console.error('Failed to update network');
      return;
    }

    const data = await response.json();
    setNetwork(data);
  }

  return (
    <div style={{display: 'grid', gridTemplateColumns: '1fr 1fr'}}>
      <div className='Settings' style={{display: 'grid', gridTemplateColumns: '1fr', gridGap: '1rem', justifyItems: 'start'}}>
        <h1> Nuero Network Settings: </h1>
        <div className='Settings-Inputs' style={{display: 'grid', gridTemplateColumns: '1fr 1fr 1fr 1fr', gridGap: '1rem'}}>
          <label>
            <span>Number of Layers:</span>
            <input
              type="number"
              value={network.layers}
              onChange={(e) => setNetwork({...network, layers: parseInt(e.target.value)})}
            />
          </label>
           <label>
            <span>Number of Inputs:</span>
            <input
              type="number"
              value={network.inputs}
              onChange={(e) => setNetwork({...network, inputs: parseInt(e.target.value)})}
            />
          </label>
          <label>
            <span>Number of Outputs:</span>
            <input
              type="number"
              value={network.outputs}
              onChange={(e) => setNetwork({...network, outputs: parseInt(e.target.value)})}
            />
          </label>
          <button className='Update-Network' onClick={updateNetwork}>
            Update
          </button>
        </div>
        <h2> Current Network: </h2>
        <div className='Current-Nodes' style={{display: 'grid', gridTemplateColumns: '1fr 1fr 1fr 1fr', gridGap: '1rem', justifyItems: 'space-between'}}>
          <label>  <span> Current Biases: {3} </span> </label>
          <label> <span> Current Weights: {6} </span> </label>
        </div>
      </div>
      <div>

      </div>
    </div>
  )
}

export default App
