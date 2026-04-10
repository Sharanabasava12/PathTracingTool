Path Tracing Tool (SDN-based)

Project Overview

The **Path Tracing Tool** is a Software Defined Networking (SDN) based project that identifies and displays the path taken by packets between two hosts in a network topology.

This project uses:

* **Mininet** → to emulate the SDN network
* **POX Controller** → to control the switches
* **Python + NetworkX** → to calculate shortest packet path
* **Linux / Ubuntu VM** → execution environment

The tool helps visualize how packets move from source to destination in an SDN network.

---

Objective

To build an SDN-based path tracing system that:

* Creates a custom topology
* Connects multiple switches and hosts
* Finds shortest path between source and destination
* Displays hop-by-hop route
* Counts total hops

---

Technologies Used

* Python 3
* Mininet
* POX Controller
* NetworkX
* Linux / Ubuntu
* OpenFlow

---

Project Structure

text
PathTracingTool/
│── topology.py
│── path_trace.py
│── run.sh
│── README.md
```

---

File Description

1) `topology.py`

This file creates the custom Mininet topology.

Topology Design

```text
h1 --- s1 --- s2 --- s4 --- h2
        \              /
         \--- s3 -----/
```

Devices Used

* 2 Hosts → `h1`, `h2`
* 4 Switches → `s1`, `s2`, `s3`, `s4`

---

2) `path_trace.py`

This file uses **NetworkX graph library** to:

* Build the network graph
* Find shortest path
* Display packet route
* Show hop count

Example Output

```text
PACKET PATH TRACE
Source      : h1
Destination : h2
Path        : h1 -> s1 -> s2 -> s4 -> h2
Hop Count   : 4
```

---

3) `run.sh`

This shell script automates the complete execution.

It performs:

1. Starts Mininet topology
2. Connects to remote POX controller
3. Executes path tracing script

---
Installation Steps

Step 1: Install Mininet

```bash
sudo apt update
sudo apt install mininet -y
```



Step 2: Install Python Library

```bash
pip3 install networkx
```



Step 3: Clone POX Controller

```bash
git clone https://github.com/noxrepo/pox.git
cd pox
```

Run controller:

```bash
./pox.py forwarding.l2_learning
```



How to Run the Project

Step 1: Give permission

```bash
chmod +x run.sh
```

Step 2: Run script

```bash
./run.sh
```

 Working Principle

The project works in the following sequence:

1. Custom topology is created in Mininet
2. POX controller manages switch forwarding
3. Python graph model is built
4. Shortest path algorithm finds packet route
5. Result is displayed with hop count

---

Algorithm Used

The project uses:

**Shortest Path Algorithm**

Implemented using:

```python
nx.shortest_path(graph, src, dst)
```

This finds the minimum-hop route from source to destination.

---

# ✅ Expected Result

The tool successfully displays:

* Source host
* Destination host
* Path followed by packet
* Total number of hops

Example:

```text
h1 -> s1 -> s2 -> s4 -> h2
```

---

Future Enhancements

Possible improvements:

* Real-time packet monitoring
* Dynamic topology updates
* GUI-based topology visualization
* Delay-based best path selection
* Bandwidth-aware routing
* POX event-based live tracing

---

Academic Use

This project is suitable for:

* SDN Mini Projects
* Computer Networks Lab
* Mininet + POX Learning
* Final Year Networking Projects
* Packet Routing Demonstrations

---

Author

**Sharana Basava**
SDN Mini Project – Path Tracing Tool

