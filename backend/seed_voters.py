import csv
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Voter
import os

def seed_voters_from_csv(file_path: str, tenant_id: int = None):
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return

    db: Session = SessionLocal()
    added, skipped = 0, 0

    try:
        with open(file_path, newline='', encoding='latin1') as f:
            sample = f.read(2048)
            f.seek(0)
            try:
                dialect = csv.Sniffer().sniff(sample)
            except csv.Error:
                dialect = csv.excel_tab  # fallback to tab

            reader = csv.reader(f, dialect)

            for i, row in enumerate(reader):
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
                    county,
                    constituency_code,
                    constituency_name,
                    ward_code,
                    ward_name,
                    polling_station_code,
                    polling_station_name
                ) = [r.strip() if r else None for r in row]

                # Fix weird ID numbers (replace O with 0)
                if id_number:
                    id_number = ''.join(ch if ch.isdigit() else '0' for ch in id_number)

                if not id_number or not first_name or not last_name:
                    skipped += 1
                    continue

                voter = Voter(
                    tenant_id=tenant_id,
                    id_number=id_number,
                    first_name=first_name,
                    middle_name=middle_name,
                    last_name=last_name,
                    phone_number=phone_number,
                    county_code=county_code,
                    county=county,
                    constituency_code=constituency_code,
                    constituency_name=constituency_name,
                    ward_code=ward_code,
                    ward_name=ward_name,
                    polling_station_code=polling_station_code,
                    polling_station_name=polling_station_name,
                )

                db.add(voter)
                added += 1

                if added % 1000 == 0:
                    db.commit()
                    print(f"✅ Committed {added} voters...")

            db.commit()
            print(f"🎉 Done: Added {added} voters successfully ({skipped} skipped).")

    except Exception as e:
        db.rollback()
        print(f" Error while seeding voters: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    seed_voters_from_csv("data/turbo.csv", tenant_id=None)
