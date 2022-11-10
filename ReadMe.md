# Graphql Query using Python Flask and Ariadne Libraries

## Solution:

An endpoint /graphql is exposed which returns a Person object (fields: email (string), name (string), address (Address))
and a Address object (fields: number (integer), street (string), city (string), state (GraphQL enum).

Ariadne library is used to implement GraphQL servers using schema-first approach.

An Sqlite database "person.db" is used to hold 2 tables for Person and Address object and filled with dummy data.
Currently the two tables are not linked and will be linked in the future using a foreign key to Address table in 
the Person table.

## Validation

The following query and any modifications of the fields can be used to validate this implementation:

query {

  person {

    email

    name

    address {

      number

      street

      city

      state

    }

  }

}
