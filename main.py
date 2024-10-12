import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtGui import QIcon

# Global variables
browser = None
url_bar = None

def navigate_to_url():
    url = url_bar.text()
    browser.setUrl(QUrl('https://' + url))

def navigate_home():
    browser.setUrl(QUrl('https://google.com'))

def update_url(q):
    url_bar.setText(q.toString())

def navigate_Owner_btn():
    browser.setUrl(QUrl('https://github.com/ujjwal1808'))


def main():
    global browser, url_bar
    
    # Create the application
    app = QApplication(sys.argv)
    app.setApplicationName('My Cool Browser')

    # Main window
    window = QMainWindow()
    window.setWindowTitle("UJ's Browser")
    # window.setWindowTitle.setStyleSheet("background-color: #4CAF50;")
    window.showMaximized()

    # WebEngineView (browser)
    browser = QWebEngineView()
    browser.setUrl(QUrl('https://google.com'))
    window.setCentralWidget(browser)

    # Navigation bar (QToolBar)
    navbar = QToolBar()
    window.addToolBar(navbar)

    # Back button
    back_btn = QAction(QIcon('backward.png'), '', window)
    back_btn.triggered.connect(browser.back)
    navbar.addAction(back_btn)

    # Forward button
    forward_btn = QAction(QIcon('forward.png'), '', window)
    forward_btn.triggered.connect(browser.forward)
    navbar.addAction(forward_btn)

    # Reload button
    reload_btn = QAction(QIcon('reload.png'),'', window)
    reload_btn.triggered.connect(browser.reload)
    navbar.addAction(reload_btn)

    # Home button
    home_btn = QAction(QIcon('home.png'), '', window)
    home_btn.triggered.connect(navigate_home)
    navbar.addAction(home_btn)

    Owner_btn = QAction('Owners Github', window)
    Owner_btn.triggered.connect(navigate_Owner_btn)
    navbar.addAction(Owner_btn)

    # URL bar
    url_bar = QLineEdit()
    url_bar.returnPressed.connect(navigate_to_url)
    navbar.addWidget(url_bar)

    # Apply styles to URL bar
    url_bar.setStyleSheet("""
    QLineEdit {
        background-color: white;
        color: black;  /* Optional: Set the text color */
        border-radius: 5px;  /* Optional: Rounded corners */
        padding: 5px;  /* Optional: Add some padding inside the input */
    }
    # setApplicationName{
    #     background-color: #4CAF50;
    # }                      
    #                       """)
    
    navbar.setStyleSheet("""
        background-color: black;
        color: white;  
        border-radius: 5px;
        font-size: 20px;
        padding: 15px;  
""")
   
    
    # Update the URL bar when the browser URL changes
    browser.urlChanged.connect(update_url)

    # Start the application
    window.show()
    window.setStyleSheet("""
        background-color: black;
""")
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
    main.setStyleSheet("""
        background-color: cyan;
""")