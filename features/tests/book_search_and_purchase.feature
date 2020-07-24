v# Created by zelec at 7/7/2020
Feature: Test For Book Purchase
  # Enter feature description here

  Scenario: Purchase Scenario
    Given LF Open Amazon Main Page
    When LF Search for Fantasy Books
#    Then LF RESULT Verify Amount Of Results Is 23
    Then LF RESULT Verify Bestsellers Are Present
    When LF RESULT Add Each Besteseller To Cart
#    Then LF Click On Cart
#    Then LF CART Verify That All Bestsellers Are Present
