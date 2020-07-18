# Created by zelec at 7/14/2020
Feature: Test for Cart Hover-over tooltip

  Scenario: User can see a tooltip 
    When LF Open gp/product/B074TBCSC8
    When LF Hover Over New Arrivals
    Then LF Verify That A Tooltip Appears