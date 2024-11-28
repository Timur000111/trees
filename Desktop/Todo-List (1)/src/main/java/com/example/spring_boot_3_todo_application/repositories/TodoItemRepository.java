package com.example.spring_boot_3_todo_application.repositories;

import com.example.spring_boot_3_todo_application.models.TodoItem;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface TodoItemRepository extends JpaRepository<TodoItem, Long> {

}
