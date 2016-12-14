INSERT_CITY_SQL = "INSERT INTO municipality (name) VALUES ('{name}')"

SELECT_CITY_SQL = "SELECT municipality_id FROM municipality WHERE name = ('{name}')"

INSERT_HOUSING_TYPE_SQL = ("INSERT INTO housing_type(name) "
                           "VALUES ('{name}')")

SELECT_HOUSING_TYPE_SQL = ("SELECT housing_type_id FROM housing_type "
                           "WHERE name = '{name}'")

INSERT_STATUS_SQL = ("INSERT INTO status(name) "
                     "VALUES ('{name}')")

SELECT_STATUS_SQL = ("SELECT status_id FROM status "
                     "WHERE name = '{name}'")

INSERT_APN_SQL = """
INSERT INTO locations(APN, municipality_id, street_address, unit_number,
                      postal_code, property_size) VALUES (
                        :APN,
                        (SELECT municipality_id FROM municipality
                         WHERE name=:city_name),
                        :street_address, :unit_number,
                        :postal_code, :property_size)
"""

SELECT_APN_SQL = """
SELECT * FROM locations WHERE APN=:APN
    AND municipality_id=(SELECT municipality_id FROM municipality
                         WHERE name=:city_name)
"""

CREATE_PERMIT_SQL = """
INSERT INTO permit_ids(external_id, municipality_id) VALUES(
              :permit_id,
              (SELECT municipality_id FROM municipality
               WHERE name=:city_name))
"""


CREATE_PERMIT_DATA_SQL = """
INSERT INTO permit_info(municipality_id, external_id, permit_id, status_id,
                        project_name, tenure, assistance_programs,
                        request_date, issue_date, completion_date,
                        applicant, approving_authority)
            VALUES((SELECT municipality_id FROM municipality
                    WHERE name=:city_name),
                   :external_id,
                   (SELECT permit_id FROM permit_ids
                    WHERE external_id=:external_id AND
                    municipality_id=(SELECT municipality_id
                                     FROM municipality
                                     WHERE name=:city_name)),
                   (SELECT status_id FROM status WHERE name=:status),
                   :project_name,
                   :tenure,
                   :assistance_programs,
                   :request_date,
                   :issue_date,
                   :completion_date,
                   :applicant,
                   :approving_authority
                  )
"""

SELECT_PERMIT_DATA_SQL = """
SELECT * FROM permit_info WHERE permit_id=(
     SELECT permit_id FROM permit_ids
     WHERE external_id=:external_id AND
           municipality_id=(SELECT municipality_id
                            FROM municipality
                            WHERE name=:city_name)
    )
"""