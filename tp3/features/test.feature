Feature: Traceur de Courbe Elliptique

  Scenario: Update elliptic curve with valid parameters
    Given we have behave installed
    When we enter valid parameters for a, b, and p
    And we click on "Mettre à jour la courbe"
    Then the plot should be updated with the new elliptic curve

  Scenario: Toggle between points and curve
    Given we have behave installed
    And we have an elliptic curve plotted
    When we click on "Basculer Points/Courbe"
    Then the plot should toggle between showing points and showing the curve
