# Created by zelec at 7/7/2020
Feature: A Full Register test suite
  # Enter feature description here

  Scenario: Verify All Static Text On Register Page
    When LF Open gp/sign-in.html
    Then LF SIGNIN Verify Create your Amazon account Button Is Clickable
    And LF REGISTER Verify Header Text Is Create account
    And LF REGISTER Verify Name Field Text Is Your name
    And LF REGISTER Verify Email Field Text Is Email
    And LF REGISTER Verify Password Field Text Is Password
    And LF REGISTER Verify Password Input Field Text Is At least 6 characters
    And LF REGISTER Verify Password Disclaimer Icon Is Present
#    And LF REGISTER Verify Password Disclaimer Text Is Passwords must be at least 6 characters.
    And LF REGISTER Verify Re-Enter Password Text Is Re-enter password
    And LF REGISTER Verify That Create Your Amazon Account Button Text Is Create your Amazon account
#    And LF SIGNIN Verify In-Box Conditions Of Use Text Is By creating an account, you agree to Amazon's Conditions of Use and Privacy Notice.
    And LF REGISTER Verify Divider Text Is Already have an account? Sign-In
#    And LF SIGNIN Verify Footer Incorporated Info Is 1996-2020, Amazon.com, Inc. or its affiliates

  Scenario:
    When LF Open gp/sign-in.html
    Then LF SIGNIN Verify Create your Amazon account Button Is Clickable
    Then LF REGISTER Input Name bad_name
    Then LF REGISTER Input Email bad_email
    Then LF REGISTER Input Password bad_password
    Then LF REGISTER Input Reenter Password bad_password
    Then LF REGISTER Click On Create Amazon Account

  Scenario:
    When LF Open gp/sign-in.html
    Then LF SIGNIN Verify Create your Amazon account Button Is Clickable
    Then LF REGISTER Click On Sing In Drop Down


  Scenario:
    When LF Open gp/sign-in.html
    Then LF SIGNIN Verify Create your Amazon account Button Is Clickable
    Then LF SIGNIN Verify That Legal Row Conditions Of Use Is Clickable

  Scenario:
    When LF Open gp/sign-in.html
    Then LF SIGNIN Verify Create your Amazon account Button Is Clickable
    Then LF SIGNIN Verify That Legal Row Privacy Notice Is Clickable

  Scenario:
    When LF Open gp/sign-in.html
    Then LF SIGNIN Verify Create your Amazon account Button Is Clickable
    Then LF SIGNIN Verify Conditions Of Use In Footer Is Clickable

  Scenario:
    When LF Open gp/sign-in.html
    Then LF SIGNIN Verify Create your Amazon account Button Is Clickable
    Then LF SIGNIN Verify Privacy Notice In Footer Is Clickable

  Scenario:
    When LF Open gp/sign-in.html
    Then LF SIGNIN Verify Create your Amazon account Button Is Clickable
    Then LF SIGNIN Verify That Footer Help Button Is Clickable