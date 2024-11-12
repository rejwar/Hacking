package main

import (
    "context"
    "log"

    "github.com/Davinche/goinsta"
)

func main() {
    // Instantiate a new Instagram instance
    insta := goinsta.New("username", "password")

    // Login to your Instagram account
    err := insta.Login()
    if err != nil {
        log.Fatal(err)
    }

    // Define the username of the user you want to report
    userToReport := "username_to_report"

    // Navigate to the user's profile
    user, err := insta.Profiles.ByName(userToReport)
    if err != nil {
        log.Fatal(err)
    }

    // Report the user for violating Instagram's terms of service
    err = user.Report(context.Background())
    if err != nil {
        log.Fatal(err)
    }

    log.Printf("User %s has been reported for violating Instagram's terms of service.", userToReport)
}
