# AlertTester

This was built to try and reproduce the issues other people are having with various versions of Appium and functionality surrounding Alerts! :)

There's an iOS app and a simple python script using Appium's client library to tap a button that makes an alert show up, and then tap a button that dismisses the alert.

This is the most basic smoke test for an app that has an alert.

#### AlertTester.app

AlertTester has one button named "Tap!". When you tap it, an alert comes up with a button to dismiss it labeled "Thanks".

#### Usage:

1. Start your Appium server with the path to AlertTester.app in either the server launch arguments or the desired capabilities
2. `python main.py`
3. Watch it go!

#### Alt. Usage:

1. Start your Appium server with the path to AlertTester.app
2. Do what you want