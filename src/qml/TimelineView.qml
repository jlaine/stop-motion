import QtQuick 2.0

ListView {
    orientation: ListView.Horizontal

    delegate: Rectangle {
        color: 'pink'
        height: parent.height
        width: parent.height

        Image {
            anchors.fill: parent
            asynchronous: true
            fillMode: Image.PreserveAspectFit
            source: modelData.url
        }
    }
}
