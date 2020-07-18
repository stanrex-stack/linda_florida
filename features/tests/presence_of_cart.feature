# Created by zelec at 7/3/2020
Feature:  Test for Amazon Cart visibility
  # Enter feature description here

  Scenario: User sees the empty cart text
    Given LF Open Amazon Main Page
    When LF Click On Cart
    Then LF Verify Empty Cart Text Is Present

