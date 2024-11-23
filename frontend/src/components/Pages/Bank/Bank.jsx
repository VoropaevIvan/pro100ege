import "./Bank.css";

import Task from "../../Menu/Task/Task";
import { useEffect, useState } from "react";
import { getAllTasksFromServer } from "../../../server/bank";

const Bank = () => {
  const [tasks, setTasks] = useState([]);

  useEffect(() => {
    async function fetchData() {
      const tasksFromServer = await getAllTasksFromServer();
      setTasks(tasksFromServer);
    }
    fetchData();
  }, []);
  return (
    <div className="tasks">
      {tasks.map((task, i) => {
        return <Task taskData={task} key={task.id} />;
      })}
    </div>
  );
};

export default Bank;
