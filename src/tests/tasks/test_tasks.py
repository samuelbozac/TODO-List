from tests.conftest import client


def test_create_task(setup_db):
    task_data = {"title": "Test Task", "description": "Test Description"}
    response = client.post("/tasks/", json=task_data)
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "Test Task"
    assert data["description"] == "Test Description"
    assert "id" in data
    assert data["completed"] == False


def test_read_task(setup_db):
    # First, create a task
    task_data = {"title": "Test Task", "description": "Test Description"}
    create_response = client.post("/tasks/", json=task_data)
    created_task_id = create_response.json()["id"]

    # Then, read the task
    read_response = client.get(f"/tasks/{created_task_id}")
    assert read_response.status_code == 200
    data = read_response.json()
    assert data["title"] == "Test Task"
    assert data["description"] == "Test Description"
    assert data["id"] == created_task_id
    assert data["completed"] == False

    read_response = client.get("/tasks/99")
    assert read_response.status_code == 404


def test_read_tasks(setup_db):
    client.post("/tasks/", json={"title": "Task 1", "description": "Description 1"})
    client.post("/tasks/", json={"title": "Task 2", "description": "Description 2"})

    read_all_response = client.get("/tasks/")
    assert read_all_response.status_code == 200
    data = read_all_response.json()
    assert len(data) == 2
    assert data[0]["title"] == "Task 1"
    assert data[1]["title"] == "Task 2"


def test_update_task(setup_db):
    # First, create a task
    task_data = {"title": "Test Task", "description": "Test Description"}
    create_response = client.post("/tasks/", json=task_data)
    created_task_id = create_response.json()["id"]

    # Then, update the task
    update_data = {
        "title": "Updated Task",
        "description": "Updated Description",
        "completed": True,
    }
    update_response = client.put(f"/tasks/{created_task_id}", json=update_data)
    assert update_response.status_code == 200
    data = update_response.json()
    assert data["title"] == "Updated Task"
    assert data["description"] == "Updated Description"
    assert data["id"] == created_task_id
    assert data["completed"] == True

    update_response = client.put("/tasks/99", json=update_data)
    assert update_response.status_code == 404


def test_delete_task(setup_db):
    # First, create a task
    task_data = {"title": "Test Task", "description": "Test Description"}
    create_response = client.post("/tasks/", json=task_data)
    created_task_id = create_response.json()["id"]

    # Then, delete the task
    delete_response = client.delete(f"/tasks/{created_task_id}")
    assert delete_response.status_code == 200

    # Check if the task is gone
    read_response = client.get(f"/tasks/{created_task_id}")
    assert read_response.status_code == 404

    delete_response = client.delete("/tasks/99")
    assert delete_response.status_code == 404
