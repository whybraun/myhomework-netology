CREATE TABLE Employees (
  employee_id INT PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  department VARCHAR(100) NOT NULL,
  manager_id INT,
  FOREIGN KEY (manager_id) REFERENCES Employees(employee_id)
);
