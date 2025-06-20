from print_queue_manager import PrintQueueManager

def test_visualization_function_exists():
    manager = PrintQueueManager()
    assert hasattr(manager, 'show_status_gui')

