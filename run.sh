#!/bin/bash

echo "Starting topology..."
sudo mn --custom topology.py --topo mypath --controller remote

echo "Running tracer..."
python3 path_trace.py
