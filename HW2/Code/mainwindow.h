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
    void on_SelectFile_clicked();

    void on_selectA_clicked();

    void on_selectB_clicked();

    void on_verticalSlider_valueChanged(int value);

    void on_HistogramEqualization_clicked();

    void on_Contrast_clicked();

    void on_Brightness_valueChanged(int value);

    void on_ContrastSlider_valueChanged(int value);
    void on_grayScale_clicked();
    void PlotHist(int hist[] ,std::string title);
    void on_Sizevalue_valueChanged(int arg1);

    void on_enlargebutton_clicked();

    void on_shrinkbutton_clicked();
    cv::Mat QImage2Mat(const QImage& src);

private:
    Ui::MainWindow *ui;
};
#endif // MAINWINDOW_H
