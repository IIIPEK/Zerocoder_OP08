
# Task List Application

A simple task management application built using Python's Tkinter library. This application allows you to add tasks, delete tasks, and mark tasks as completed. It also includes a custom background image for a more appealing interface.

## Features

- Add tasks to the task list.
- Delete selected tasks.
- Mark tasks as completed with a visual indicator.
- Customizable background image.

## Screenshot

*(Insert a screenshot of the application here if available)*

## Prerequisites

Ensure you have Python installed on your system. This project was developed with **Python 3.13** but should work with any modern Python version.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/task-list.git
   cd task-list
   ```

2. Install required dependencies (if any):

   ```bash
   pip install -r requirements.txt
   ```

   *(No external dependencies are needed unless you use Pillow for image resizing.)*

3. Place your background image (`bg.png`) in the project directory.

## Usage

1. Run the script:

   ```bash
   python task_list.py
   ```

2. Use the interface:
   - Enter a task in the input field and click **Add Task** to add it to the list.
   - Select a task and click **Delete Task** to remove it.
   - Select a task and click **Mark Finished Task** to highlight it as completed.

## Project Structure

```
task-list/
├── bg.png             # Background image file
├── task_list.py       # Main application script
├── README.md          # Documentation
```

## Customization

- Replace `bg.png` with any image of your choice. Ensure it matches the application window's size for the best appearance.
- Modify colors and styles directly in the script by changing the `bg`, `fg`, and `font` attributes of the Tkinter widgets.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributions

Contributions are welcome! Feel free to open issues or submit pull requests for improvements and new features.

## Contact

For questions or feedback, reach out to [your-email@example.com](mailto:your-email@example.com).
