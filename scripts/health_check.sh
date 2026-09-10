#!/bin/bash

URL="http://localhost:8000/health"



HTTP_CODE=$(curl -s -o /dev/null -w "%{http_code}" $URL)

if [ "$HTTP_CODE" -eq 200 ];then
    echo "Application is healthy"
    exit 0
else
    echo "Application is unhealthy. HTTP code: $HTTP_CODE"
    exit 1
fi