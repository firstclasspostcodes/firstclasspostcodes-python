from mock import Mock
from firstclasspostcodes.events import Events


class TestEventsClass:
    def test_an_event_can_be_added(self):
        mock_handler = Mock(return_value=None)
        events = Events()
        events.on('test', mock_handler)
        assert 'test' in events.events
        assert mock_handler in events.events['test']

    def test_a_second_event_can_be_added(self):
        first_mock_handler = Mock(return_value=None)
        second_mock_handler = Mock(return_value=None)
        events = Events()
        events.on('test', first_mock_handler)
        events.on('test', second_mock_handler)
        assert 'test' in events.events
        assert first_mock_handler in events.events['test']
        assert second_mock_handler in events.events['test']

    def test_an_event_can_be_removed(self):
        mock_handler = Mock(return_value=None)
        events = Events()
        events.on('test', mock_handler)
        events.off('test', mock_handler)
        assert 'test' in events.events
        assert events.events['test'] == []

    def test_an_event_is_called(self):
        mock_handler = Mock(return_value=None)
        events = Events()
        events.on('test', mock_handler)
        events.emit('test', 123, a=True, b='test')
        mock_handler.assert_called_once_with(123, a=True, b='test')
