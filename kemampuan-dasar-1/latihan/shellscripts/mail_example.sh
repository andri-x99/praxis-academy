#!/bin/bash
Recipient="admin@example.com"
Subject="Greeting"
Message="welcome to our site"
`mail -s $Subject $Recipient <<< $Message`
