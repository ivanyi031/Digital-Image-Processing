#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
#include<opencv2/core/core.hpp>
#include<opencv2/highgui/highgui.hpp>
#include<opencv2/imgproc/imgproc.hpp>
QT_BEGIN_NAMESPACE
namespace Ui { class MainWindow; }
QT_END_NAMESPACE

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    MainWindow(QWidget *parent = nullptr);
    ~MainWindow();

private slots:
    void on_selectfile_clicked();
    int MainWindow::checkvalue(double value);
    void on_RGB_clicked();
    double MainWindow::LAB_hq_func(double q);
    void on_CMY_clicked();
    void MainWindow::pseudoColor(cv::Mat,int map[255][3]);
    void on_HSI_clicked();

    void on_XYZ_clicked();

    void on_Lab_clicked();

    void on_YUV_clicked();

    void on_pushButton_clicked();

    void on_selectcolor1_clicked();

    void on_selectcolor2_clicked();

    void on_selectcolor3_clicked();

    void on_colormap_clicked();

    void on_SelectFile2_clicked();

private:
    Ui::MainWindow *ui;
};
#endif // MAINWINDOW_H
