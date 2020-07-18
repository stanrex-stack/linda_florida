# Created by zelec at 7/5/2020
Feature: Test for Help Searchbar functionality


  Scenario Outline: User can interact with help menu searchbar
    Examples:
    |search_word|
    |Cancel     |
    |Cancelation|
    When LF Open gp/help/customer/display.html
    And LF Help Search For <search_word>
    Then LF Help Verify <search_word> Has Been Found