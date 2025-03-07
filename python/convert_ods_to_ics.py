from odf.opendocument import load
from odf.table import Table, TableRow, TableCell
from odf.text import P
from ics import Calendar, Event
from datetime import datetime

def get_cell_text(cell):
    """Extract text from a table cell in an ODS file."""
    paragraphs = cell.getElementsByType(P)
    return " ".join([p.firstChild.data if p.firstChild else "" for p in paragraphs]).strip()

def read_ods(file_path):
    doc = load(file_path)
    sheet = doc.spreadsheet.getElementsByType(Table)[0]  # Get the first sheet
    rows = sheet.getElementsByType(TableRow)

    if not rows:
        print("No data found in the ODS file.")
        return []

    # Read headers
    headers = [get_cell_text(cell) for cell in rows[0].getElementsByType(TableCell)]
    print(f"Headers: {headers}")  # Debugging: Print headers

    expected_headers = ["Event Name", "Start Date", "End Date", "Location"]
    if headers[:4] != expected_headers:
        print("Warning: Headers do not match expected format. Check the ODS file.")
    
    # Process event data
    events = []
    for row in rows[1:]:  # Skip header row
        cells = row.getElementsByType(TableCell)
        cell_values = [get_cell_text(cell) for cell in cells]

        if len(cell_values) < 4 or not cell_values[0]:  # Skip empty rows
            continue

        event_name, start_date, end_date, location = cell_values[:4]

        try:
            start_dt = datetime.strptime(start_date, "%Y-%m-%d %H:%M")
            end_dt = datetime.strptime(end_date, "%Y-%m-%d %H:%M")
        except ValueError:
            print(f"Skipping event '{event_name}' due to date format error: {start_date}, {end_date}")
            continue

        events.append((event_name, start_dt, end_dt, location))

    print(f"Found {len(events)} events in the ODS file.")  # Debugging
    return events

def create_ics(events, output_file):
    if not events:
        print("No events found to write to the ICS file.")
        return

    calendar = Calendar()
    for name, start, end, location in events:
        e = Event()
        e.name = name
        e.begin = start
        e.end = end
        e.location = location
        calendar.events.add(e)

    with open(output_file, "w") as f:
        f.writelines(calendar)

    print(f"ICS file '{output_file}' created successfully with {len(events)} events.")

# Change the file path to match your ODS file location
ods_file = "your_file.ods"
ics_file = "schedule.ics"

event_data = read_ods(ods_file)
create_ics(event_data, ics_file)
