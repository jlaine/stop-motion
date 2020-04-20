import QtQuick 2.14
import QtQuick.Controls 2.14
import QtQuick.Layouts 1.14

ApplicationWindow {
    width: 800
    height: 600
    title: "Stop motion"
    visible: true

    header: ToolBar {
        RowLayout {
            anchors.fill: parent

            ToolButton {
                action: capture
            }

            ToolButton {
                action: remove
            }
        }
    }

    ColumnLayout {
        anchors.fill: parent

        Image {
            asynchronous: true
            fillMode: Image.PreserveAspectFit
            source: timeline.items.length ? timeline.items[timeline.items.length - 1].url : ''

            Layout.fillHeight: true
            Layout.fillWidth: true
        }

        TimelineView {
            model: timeline.items

            Layout.fillWidth: true
            Layout.minimumHeight: 200
        }
    }

    Action {
        id: capture

        icon.name: "media-record"
        onTriggered: camera.capture(timeline.nextFilePath)
        shortcut: "Return"
        text: "Capture"
    }

    Action {
        id: remove

        icon.name: "edit-delete"
        onTriggered: timeline.deleteLast()
        shortcut: "Del"
        text: "Delete"
    }
}
