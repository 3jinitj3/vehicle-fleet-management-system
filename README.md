# Vehicle Fleet Management System

A Python-based object-oriented fleet management system designed to model vehicles, engines, and fleet operations through inheritance, composition, abstraction, and factory-based object creation.

---

## Features

- Abstract Base Classes (ABC)
- Inheritance and Polymorphism
- Factory Pattern
- Composition
- Encapsulation and Input Validation
- Custom Iterable Fleet Collection
- Engine Inventory Tracking
- Fleet Reporting

---

## Technologies

- Python
- Object-Oriented Programming (OOP)
- Design Patterns
- Data Validation

---

## Project Structure

### Vehicle Hierarchy

```text
Vehicle (Abstract Base Class)
│
├── Car
├── Truck
└── Motorcycle
```

### Engine Hierarchy

```text
Engine (Abstract Base Class)
│
├── Gas
├── Electric
└── Diesel
```

### Supporting Classes

```text
VehicleFactory
Fleet
```

---

## Concepts Demonstrated

### Object-Oriented Programming

- Abstraction
- Encapsulation
- Inheritance
- Polymorphism
- Composition

### Design Patterns

- Factory Pattern

### Python Features

- Iterators (`__iter__`, `__next__`)
- Property Getters and Setters
- Type Hints
- Input Validation

---

## Sample Output

### Fleet Report

screenshots/fleet_report.png

---

### Vehicle Factory Statistics

screenshots/engine_type_summary.png

---

### Engine Inventory

screenshots/engine_inventory.png

---

## Example Scenario

The system can:

1. Create engine objects
2. Create vehicles using a factory pattern
3. Assign engines to vehicles
4. Store vehicles in a fleet
5. Generate fleet reports
6. Track engine inventory statistics

---

## Future Enhancements

- Persistent storage with SQLite or PostgreSQL
- Fleet maintenance scheduling
- Fuel consumption analytics
- Reporting exports
- REST API integration

---

## Author

James J. Jones

Computer Science Graduate Student

Software Engineering | Python | SQL