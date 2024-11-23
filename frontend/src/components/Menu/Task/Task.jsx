import "./Task.css";

const Task = ({ taskData }) => {
  console.log(taskData);
  return (
    <div className="task-container">
      <div className={"task " + ""}>
        <div className="task-header">
          <span className="numberEGE">
            {"№ " + taskData.number_in_exam.name + " ЕГЭ"}
          </span>
          <span className="tags">
            <span className="header-tag">{taskData.difficulty_level.name}</span>
            {/* <span className="header-tag">{taskData.actuallity}</span> */}
            {/* <span className="header-tag">{taskData.difficulty_level}</span> */}
            {/* <span className="header-tag">{taskData.actuallity}</span> */}
          </span>
          <span className="stat">
            <span className="header-tag">{"Решило 125 чел."}</span>
            <span className="header-tag">{"45%"}</span>
          </span>
        </div>
        <div className="task-body">
          <p>{taskData.content}</p>
        </div>

        <div className="task-footer">
          <span className="input-with-but">
            <input placeholder="Введите ответ.."></input>
            <button>Проверить ответ</button>
          </span>
          <span className="author">{taskData.author.name}</span>
        </div>
      </div>
    </div>
  );
};

export default Task;
