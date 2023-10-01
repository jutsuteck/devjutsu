import json

from src.core.dependencies.database.database_manager import db_session
from src.models.v1.security_standards.asvs_category import ASVSCategory
from src.models.v1.security_standards.asvs_sub_category import ASVSSubCategory
from src.models.v1.security_standards.asvs_requirement import ASVSRequirement


def seed_data_to_db(json_filepath: str):
    # Note: get_db() is a generator that yields a session.
    db_gen = db_session()
    # Getting the actual session object from the generator
    session = next(db_gen)

    # Check if the database has already been seeded
    existing_records_count = session.query(ASVSCategory).count()
    if existing_records_count > 0:
        print("Database has already been seeded. Skipping...")
        session.close()
        return

    with open(json_filepath, "r") as f:
        data = json.load(f)

    try:
        for category_data in data:
            category = ASVSCategory(
                name=category_data["category"], objective=""
            )
            session.add(category)
            session.commit()

            for sub_cat_data in category_data["sub_category"]:
                sub_category = ASVSSubCategory(
                    name=sub_cat_data["name"], objective="", category_id=category.id
                )
                session.add(sub_category)
                session.commit()

                for req_data in sub_cat_data["requirements"]:
                    requirement = ASVSRequirement(
                        requirement_id=req_data["id"],
                        description=req_data["description"],
                        objective="",
                        value="",
                        sub_category_id=sub_category.id
                    )
                    session.add(requirement)
                    session.commit()
    finally:
        # Make sure to close the session after using it
        session.close()
