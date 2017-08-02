

# unregister the event
Unregister-Event -SourceIdentifier volumeChange

# Register an volume change event
Register-WmiEvent -Class win32_VolumeChangeEvent -SourceIdentifier volumeChange
write-host `n
write-host (get-date -format s) "     Beginning script..."

do{
    # wait for the event
    $newEvent = Wait-Event -SourceIdentifier volumeChange
    # get the event type
    $eventType = $newEvent.SourceEventArgs.NewEvent.EventType
    # set all the event types
    $eventTypeName = switch($eventType) {
        1 {"Configuration changed"}
        2 {"Device arrival"}
        3 {"Device removal"}
        4 {"docking"}
    }

    # if anything changed
    write-host `n
    write-host (get-date -format s) "     Event detected = " $eventTypeName
    # not sure what 'configuration changed' means but will run script if something changes?
    if ($eventType -eq 1) {
        write-host `n
        "Running script in 3 seconds..." 
        start-sleep -seconds 3
        C:\AutoMount\automount.ps1
    }
    # run script and set permissions when new harddrive is plugged in
    if ($eventType -eq 2) {
        write-host `n
        "Running script in 3 seconds..." 
        start-sleep -seconds 3
        C:\AutoMount\automount.ps1
    }
    # run script to update stuff when harddrive is unplugged
    if ($eventType -eq 3) {
        write-host `n
        "Running script in 3 seconds..."
        start-sleep -seconds 3
        C:\AutoMount\automount.ps1
    }
    # not sure what docking means
    if ($eventType -eq 4) {
        write-host `n
        "Running script in 3 seconds..." 
        start-sleep -seconds 3
        C:\AutoMount\automount.ps1
    }
    "Script finished running. Waiting on next event."
    # remove the event since we're done using it
    Remove-Event -SourceIdentifier volumeChange
}
# loop until next event
while (1-eq1)

# unregister the event
Unregister-Event -SourceIdentifier volumeChange