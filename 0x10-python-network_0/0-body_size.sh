#!/usr/bin/env bash
# Get the byte size
curl -s "$1" | wc -c
