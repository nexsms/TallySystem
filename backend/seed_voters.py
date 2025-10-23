import csv
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Voter, Tenant
import os


def seed_voters_from_csv(file_path: str):
    """
    Seeds voter data from a CSV file into the database.
    Each row must follow this structure:
    id_number, first_name, middle_name, last_name, phone_number,
    county_code, county_name, constituency_code, constituency_name,
    ward_code, ward_name, polling_station_code, polling_station_name
    """

    if not os.path.exists(file_path):
        print(f"❌ File not found: {file_path}")
        return

    db: Session = SessionLocal()
    added, skipped = 0, 0

    try:
        # Get the first tenant to associate voters with
        tenant = db.query(Tenant).first()
        if not tenant:
            print("❌ No tenants found in the database. Please create a tenant first.")
            return

        with open(file_path, newline="", encoding="latin1") as f:
            sample = f.read(2048)
            f.seek(0)

            try:
                dialect = csv.Sniffer().sniff(sample)
            except csv.Error:
                dialect = csv.excel_tab  # fallback to tab-delimited files

            reader = csv.reader(f, dialect)

            for i, row in enumerate(reader):
                # Ensure correct column length (13 columns)
                if len(row) != 13:
                    skipped += 1
                    continue

                (
                    id_number,
                    first_name,
                    middle_name,
                    last_name,
                    phone_number,
                    county_code,
                    county_name,
                    constituency_code,
                    constituency_name,
                    ward_code,
                    ward_name,
                    polling_station_code,
                    polling_station_name,
                ) = [r.strip() if r else None for r in row]

                # ✅ Clean and normalize fields
                if id_number:
                    id_number = "".join(ch if ch.isdigit() else "0" for ch in id_number)

                # Skip incomplete rows
                if not id_number or not first_name or not last_name or not ward_code:
                    skipped += 1
                    continue

                # Convert numeric fields safely
                try:
                    county_code = int(county_code) if county_code else None
                    constituency_code = (
                        int(constituency_code) if constituency_code else None
                    )
                    ward_code = int(ward_code) if ward_code else None
                except ValueError:
                    skipped += 1
                    continue

                voter = Voter(
                    tenant_id=tenant.id,
                    first_name=first_name.title(),
                    middle_name=middle_name.title() if middle_name else None,
                    last_name=last_name.title(),
                    phone_number=phone_number,
                    county_code=county_code,
                    county_name=county_name.title() if county_name else None,
                    constituency_code=constituency_code,
                    constituency_name=constituency_name.title()
                    if constituency_name
                    else None,
                    ward_code=ward_code,
                    ward_name=ward_name.title() if ward_name else None,
                    polling_station_code=polling_station_code,
                    polling_station_name=polling_station_name.title()
                    if polling_station_name
                    else None,
                )

                db.add(voter)
                added += 1

                if added % 1000 == 0:
                    db.commit()
                    print(f"✅ Committed {added} voters so far...")

            db.commit()
            print(
                f"🎉 Done: Added/Updated {added} voters successfully ({skipped} skipped)."
            )

    except Exception as e:
        db.rollback()
        print(f"❌ Error while seeding voters: {e}")

    finally:
        db.close()


if __name__ == "__main__":
    # Example usage
    seed_voters_from_csv("data/turbo.csv")
