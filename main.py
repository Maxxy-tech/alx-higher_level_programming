#!/bin/bash

# Check if the PYFILE environment variable is set
if [ -z "$PYFILE" ]; then
    echo "Error: PYFILE environment variable is not set."
        exit 1
        fi

        # Check if the file exists
        if [ ! -f "$PYFILE" ]; then
            echo "Error: File $PYFILE not found."
                exit 1
                fi

                # Run the Python script
                python "0-run"
                
