Feature: Gestión de usuarios

  Scenario: Crear un usuario correctamente
    Given que la API está disponible
    When envío los datos de un usuario nuevo
    Then la respuesta debe tener código 201
    And la respuesta debe incluir su nombre, correo e identificador
    
