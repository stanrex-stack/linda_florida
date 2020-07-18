# Created by zelec at 7/3/2020
Feature: Test for Ham Menu Music pop up


  Scenario: User can access 6 item music list
    Given LF Open Amazon Main Page
    When LF Click On Hamburger Menu
    And LF Click On Amazon Music Menu Item
    Then LF 6 Menu Items Are Present