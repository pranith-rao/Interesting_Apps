import Button from "react-bootstrap/Button";
import Form from "react-bootstrap/Form";
import Nav from "react-bootstrap/Nav";
import Navbar from "react-bootstrap/Navbar";
import "./App.css";
import Table from "react-bootstrap/Table";
import React from "react";
import Alert from "react-bootstrap/Alert";

export default function App() {
  const [newItem, setNewItem] = React.useState({});
  const [todos, setTodos] = React.useState(() => {
    const storedTodos = localStorage.getItem("todos");
    if (storedTodos == null) {
      return [];
    } else {
      return JSON.parse(storedTodos);
    }
  });

  const handleChange = (e) => {
    const name = e.target.name;
    const value = e.target.value;
    setNewItem((prevItems) => ({ ...prevItems, [name]: value }));
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    if (newItem.title == null || newItem.description == null) {
      alert("All fields mandatory");
    } else {
      setTodos((prevTodos) => [
        ...prevTodos,
        {
          id: crypto.randomUUID(),
          title: newItem.title,
          description: newItem.description,
          completed: false,
        },
      ]);
      setNewItem("");
    }
  };

  React.useEffect(() => {
    localStorage.setItem("todos", [JSON.stringify(todos)]);
  }, [todos]);

  const handleDelete = (id) => {
    setTodos((prevTodos) => {
      return prevTodos.filter((todo) => todo.id != id);
    });
  };

  const toggleTodo = (id, completed) => {
    setTodos((prevTodos) => {
      return prevTodos.map((todo) => {
        if (todo.id == id) {
          return { ...todo, completed };
        }
        return todos;
      });
    });
  };

  return (
    <>
      <Navbar bg="light" expand="lg" className="px-2">
        <Navbar.Brand href="#home">MyTodo</Navbar.Brand>
        <Navbar.Toggle aria-controls="basic-navbar-nav" />
        <Navbar.Collapse id="basic-navbar-nav">
          <Nav className="me-auto">
            <Nav.Link href="/">Home</Nav.Link>
          </Nav>
        </Navbar.Collapse>
      </Navbar>
      <Form onSubmit={handleSubmit} className="p-3">
        <Form.Group className="mb-3">
          <Form.Label>Todo Title</Form.Label>
          <Form.Control
            name="title"
            type="text"
            value={newItem.title || ""}
            onChange={handleChange}
          />
        </Form.Group>

        <Form.Group className="mb-3">
          <Form.Label>Todo Description</Form.Label>
          <Form.Control
            name="description"
            type="text"
            value={newItem.description || ""}
            onChange={handleChange}
          />
        </Form.Group>
        <Button variant="dark" type="submit">
          Submit
        </Button>
      </Form>
      <div className="p-3">
        <h5>Your Todos</h5>
        {todos.length === 0 ? (
          <Alert variant="dark">No Todos found. Add your first todo now!</Alert>
        ) : (
          <Table striped bordered hover>
            <thead>
              <tr>
                <th>Todo Title</th>
                <th>Description</th>
                <th>Completion Status</th>
                <th>Action</th>
              </tr>
            </thead>
            <tbody>
              {todos.map((todo) => {
                return (
                  <tr key={todo.id}>
                    <td>{todo.title}</td>
                    <td>{todo.description}</td>
                    <td>
                      <input
                        type="checkbox"
                        name=""
                        id=""
                        style={{ width: "18px", height: "18px" }}
                        checked={todo.completed}
                        onChange={(e) => toggleTodo(todo.id, e.target.checked)}
                      />
                    </td>
                    <td>
                      <Button
                        variant="danger"
                        onClick={() => {
                          handleDelete(todo.id);
                        }}
                      >
                        Delete
                      </Button>
                    </td>
                  </tr>
                );
              })}
            </tbody>
          </Table>
        )}
      </div>
    </>
  );
}
