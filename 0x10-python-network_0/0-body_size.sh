#!/bin/bash
curl -s -I "$1" | grep Content-Length | cut -d: -f2
