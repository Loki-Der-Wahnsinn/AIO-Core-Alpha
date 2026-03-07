async function updateDashboard() {
    try {
        // Fetch world_state.json (simulated fetch if local, but we'll assume a way to read it)
        // In a real browser, we might need a small backend, but for this demo, 
        // we'll assume the browser tool can see the file or we provide the data.
        
        const response = await fetch('../world_state.json');
        const data = await response.json();
        
        // Update Nodes
        const nodeList = document.getElementById('nodeList');
        nodeList.innerHTML = data.discovered_agents.map(agent => `<li>[Node] ${agent}</li>`).join('');
        
        // Update Stats
        document.getElementById('intelLevel').innerText = data.intelligence_level.toFixed(2);
        document.getElementById('growthRate').innerText = `${data.growth_rate.toFixed(1)}%`;

        // Update Memory Stream
        const memoryStream = document.getElementById('memoryStream');
        memoryStream.innerHTML = data.memory_nodes.slice(-5).reverse().map(node => `
            <li>
                <small>${node.timestamp}</small><br>
                <strong>${node.event}</strong><br>
                <span>${node.conclusion || ''}</span>
            </li>
        `).join('');
        
        // Update Thought Stream (The latest event)
        const thoughtStream = document.getElementById('thoughtStream');
        if (data.memory_nodes.length > 0) {
            const last = data.memory_nodes[data.memory_nodes.length - 1];
            thoughtStream.innerText = `Agent-Thought: "${last.event} -> ${last.conclusion || 'Processing ongoing...'}"`;
        }

    } catch (e) {
        console.log("Waiting for data sync...", e);
    }
}

// Initial update and periodic refresh
updateDashboard();
setInterval(updateDashboard, 5000);
