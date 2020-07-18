# Created by zelec at 6/30/2020
Feature: Test for Amazon search functionality


  Scenario: User can search for a product
    Given LF Open Amazon Main Page
    When LF Select Musical Instruments In Select Menu
    When LF Search for Fender
    Then LF Search result for Fender is shown in header