#!/bin/zsh

fibonacci_dict() {
    local n=$1
    local -A result  # Associate array (dictionary) in zsh
    local -a fib_sequence=(0 1)  # Array initialization in zsh
    
    # Generate Fibonacci sequence up to n
    while [[ ${fib_sequence[-1]} -le $n ]]; do
        local next=$((${fib_sequence[-1]} + ${fib_sequence[-2]}))
        fib_sequence+=($next)
    done
    
    # Fill dictionary for each number from 0 to n
    for ((i=0; i<=n; i++)); do
        result[$i]=''  # Initialize empty string for each key
        # Add only Fibonacci numbers that are less than current key
        for num in ${fib_sequence[@]}; do
            if [[ $num -lt $i ]]; then
                if [[ -z ${result[$i]} ]]; then
                    result[$i]="$num"
                else
                    result[$i]="${result[$i]} $num"
                fi
            fi
        done
    done
    
    # Print result in required format
    echo "{"
    for ((i=0; i<=n; i++)); do
        echo -n "    $i: ["
        if [[ -n ${result[$i]} ]]; then
            echo -n ${result[$i]} | tr ' ' ','
        fi
        echo "]"
        if [[ $i -lt $n ]]; then
            echo -n ","
        fi
        echo
    done
    echo "}"
}

# Example usage:
# fibonacci_dict 5

