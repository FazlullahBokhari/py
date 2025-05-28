from sqlalchemy import create_engine, text

# Database connection string
DB_URL = 'mysql+pymysql://root:1234@localhost/pyDb'
engine = create_engine(DB_URL)

# Insert part records
insert_parts = """
INSERT INTO part (name, category) VALUES
('Battery', 'Power'),
('Screen', 'Display'),
('Speaker', 'Audio'),
('Charger', 'Power'),
('Cable', 'Accessory'),
('Graphics Card', 'Hardware'),
('CPU', 'Hardware'),
('SSD', 'Storage'),
('Hard Disk', 'Storage'),
('RAM', 'Memory'),
('Motherboard', 'Hardware'),
('PSU', 'Power'),
('Fan', 'Cooling'),
('Heatsink', 'Cooling'),
('Trackpad', 'Input'),
('Stylus Pen', 'Input'),
('Display Panel', 'Display'),
('VR Headset', 'Accessory'),
('Gamepad', 'Input'),
('Router', 'Networking'),
('LAN Card', 'Networking');
"""

# Insert product records
insert_products = """
INSERT INTO product (serial_no, part_id, name) VALUES
('SN001', 6, 'GraphicsCardX'),
('SN002', 7, 'IntelCoreI9'),
('SN003', 8, 'SamsungSSD'),
('SN004', 9, 'WDHardDisk'),
('SN005', 10, 'KingstonRAM'),
('SN006', 11, 'ASUSBoard'),
('SN007', 12, 'CoolerMasterPSU'),
('SN008', 13, 'ArcticFan'),
('SN009', 14, 'ThermalSink'),
('SN010', 15, 'TrackProPad'),
('SN011', 16, 'WacomPen'),
('SN012', 17, 'TouchHDDisplay'),
('SN013', 18, 'MetaQuest2'),
('SN014', 19, 'XBoxGamepad'),
('SN015', 20, 'TPLinkRouter'),
('SN016', 21, 'IntelLANCard'),
('SN017', 1, 'BatteryPro'),
('SN018', 2, 'RetinaScreen'),
('SN019', 3, 'JBLMini'),
('SN020', 4, 'QuickChargeX');
"""

#Insert warranty records (related to serial numbers)
insert_warranty = """
INSERT INTO warranty (serial_no, price, expiry_date) VALUES
('SN001', 100.00, '2026-01-01'),
('SN002', 300.00, '2026-01-02'),
('SN003', 120.00, '2026-01-03'),
('SN004', 140.00, '2026-01-04'),
('SN005', 80.00, '2026-01-05'),
('SN006', 200.00, '2026-01-06'),
('SN007', 150.00, '2026-01-07'),
('SN008', 90.00, '2026-01-08'),
('SN009', 70.00, '2026-01-09'),
('SN010', 110.00, '2026-01-10'),
('SN011', 60.00, '2026-01-11'),
('SN012', 180.00, '2026-01-12'),
('SN013', 400.00, '2026-01-13'),
('SN014', 250.00, '2026-01-14'),
('SN015', 90.00, '2026-01-15'),
('SN016', 95.00, '2026-01-16'),
('SN017', 50.00, '2026-01-17'),
('SN018', 160.00, '2026-01-18'),
('SN019', 75.00, '2026-01-19'),
('SN020', 55.00, '2026-01-20');
"""

# Execute the scripts
with engine.connect() as conn:
    # Insert into part table
    conn.execute(text(insert_parts))
    # Insert into product table
    conn.execute(text(insert_products))
    # Insert into warranty table
    conn.execute(text(insert_warranty))
    conn.commit()

print("Tables records inserted successfully.")
