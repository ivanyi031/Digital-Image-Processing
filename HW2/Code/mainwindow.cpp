#include "mainwindow.h"
#include "ui_mainwindow.h"
#include<QFileDialog>
#include<QtCharts/QtCharts>
#include<stdio.h>
#include <cstdlib>
QImage grayA;
QImage grayB;
QImage gray_contrast;
QImage Binary;
int graylevel = 256;
int rows;
int cols;
int SizeofImage = 1;
char whichBinary;
int histA[256];
int histB[256];
int histc[256];
MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);
}

MainWindow::~MainWindow()
{
    delete ui;
}
void MainWindow ::PlotHist(int hist[], std::string title)
{
    QBarSet *setH = new QBarSet("Histogram");
    for(int i=0;i<256;i++)
    {
        *setH << hist[i];
    }
    QString Title = QString::fromStdString(title);
;
    QBarSeries *seriesH = new QBarSeries();
    seriesH->append(setH);
    QChart *chart = new QChart();
    chart->addSeries(seriesH);
    chart->setTitle(Title);
    chart->setAnimationOptions(QChart::SeriesAnimations);
    chart->legend()->setVisible(false);
    chart->legend()->setAlignment(Qt::AlignBottom);


    QValueAxis *xAxis = new QValueAxis();
    xAxis->setTitleText("Gray Levels");
    xAxis->setTickAnchor(0.0);
    xAxis->setTickCount(5);
    chart->addAxis(xAxis, Qt::AlignBottom);
    chart->setTheme(QChart::ChartThemeBlueCerulean);
    seriesH->attachAxis(xAxis);

    QChartView *chartView = new QChartView(chart);
    chartView->setRenderHint(QPainter::Antialiasing);
    while(!ui->adjLayout->isEmpty())
    {
        // Clear the horizontal layout content if there is any
        ui->adjLayout->removeItem(ui->adjLayout->itemAt(0));
    }
    ui->adjLayout->addWidget(chartView);
}

void MainWindow::on_SelectFile_clicked()
{
    for(int i=0;i<256;i++)
    {
        histA[i]=0;
        histB[i]=0;
        histc[i]=0;
    }
    QString fileName = QFileDialog::getOpenFileName(this,
                                                    tr("Open Image"), ".",
                                                    tr("Image Files (*.png *.jpg *.jpeg *.bmp"));
    cv::Mat image;
    if(fileName != NULL)
    {
        image = cv::imread(fileName.toStdString().data());
        cvtColor(image, image, 4 );  // 4 for original CV_BGR2RGB
        // Qt image
        QImage img = QImage((const unsigned char*) (image.data),image.cols, image.rows, QImage::Format_RGB888);
        // Resize the label to fit the image
        QSize laSize=ui->label->size();
        QImage image1=img.scaled(laSize,Qt::KeepAspectRatio);
        ui->label->setPixmap(QPixmap::fromImage(image1));
    }
    rows = image.rows;
    cols = image.cols;

    grayA=QImage(image.cols, image.rows, QImage::Format_RGB32);
    grayB=QImage(image.cols, image.rows, QImage::Format_RGB32);
    gray_contrast=QImage(image.cols, image.rows, QImage::Format_RGB32);

    for (int y = 0;y<image.rows;y++){
        for(int x=0;x<image.cols;x++)
        {
            cv::Vec3b pixel = image.at<cv::Vec3b>(y,x);
            int blue = pixel[0];
            int green = pixel[1];
            int red = pixel[2];
            int valA = (blue+green+red)/3;
            int valB = 0.299*red+0.587*green+0.114*blue;
            int valC = abs(valA-valB);
            grayA.setPixel(x,y,qRgb(valA, valA, valA));
            grayB.setPixel(x,y,qRgb(valB,valB,valB));
            gray_contrast.setPixel(x,y,qRgb(valC,valC,valC));
            histA[valA]+=1;
            histB[valB]+=1;
            histc[valC]+=1;
        }
    }
    ui->grayLevel->setText(QString::fromStdString("255"));
}
void MainWindow::on_selectA_clicked()
{
    PlotHist(histA,"GrayA");
    whichBinary='A';
    Binary = grayA.scaled(ui->binaryImage->width(),ui->binaryImage->height(),Qt::KeepAspectRatio);
    ui->binaryImage->setPixmap(QPixmap::fromImage(Binary));
    QImage Adjust = grayA.scaled(ui->AdjustImage->width(),ui->AdjustImage->height(),Qt::KeepAspectRatio);
    ui->AdjustImage->setPixmap(QPixmap::fromImage(Adjust));
}
void MainWindow::on_selectB_clicked()
{
    PlotHist(histB,"GrayB");
    whichBinary='B';
    Binary = grayB.scaled(ui->binaryImage->width(),ui->binaryImage->height(),Qt::KeepAspectRatio);
    ui->binaryImage->setPixmap(QPixmap::fromImage(Binary));
    QImage Adjust = grayB.scaled(ui->AdjustImage->width(),ui->AdjustImage->height(),Qt::KeepAspectRatio);
    ui->AdjustImage->setPixmap(QPixmap::fromImage(Adjust));
}
void MainWindow::on_verticalSlider_valueChanged(int value)
{
    QImage binary1(cols,rows,QImage::Format_RGB32);
    for(int y =0;y<rows;y++)
    {
        for(int x=0;x<cols;x++)
        {
            QRgb pixelValue;
            switch (whichBinary){
                case'A':
                    pixelValue = grayA.pixel(x, y);
                    break;
                case'B':
                    pixelValue = grayB.pixel(x, y);
                    break;
                }
            if(value==255){
                binary1.setPixel(x,y,qRgb(0, 0, 0));
                continue;
            }
            if(qRed(pixelValue)< value)
                binary1.setPixel(x,y,qRgb(0, 0, 0));
            else
                binary1.setPixel(x,y,qRgb(255, 255, 255));
        }
    }
    Binary = binary1.scaled(ui->binaryImage->width(),ui->binaryImage->height(),Qt::KeepAspectRatio);
    ui->binaryImage->setPixmap(QPixmap::fromImage(Binary));
    QString n =QString::fromStdString(std::to_string(value));
    ui->threshold->setText(n);
}
void MainWindow::on_HistogramEqualization_clicked()
{
    int adjust_value[256];
    for(int i=0;i<256;i++)
        adjust_value[i]=0;
    int sum=0;
    int histH[256];
    for (int i=0;i<256;i++)
        histH[i]=0;
    QImage histequal(cols,rows,QImage::Format_RGB32);
    switch (whichBinary){
    case'A':
        for(int i=0;i<256;i++)
        {
            sum+=histA[i];
            adjust_value[i]=255*sum/(cols*rows);
        }
        break;
    case'B':
        for(int i=0;i<256;i++)
        {
            sum+=histB[i];
            adjust_value[i]=sum*255/(cols*rows);
        }
        break;
    }
    for(int y =0;y<rows;y++)
    {
        for(int x=0;x<cols;x++)
        {
            QRgb pixelValue;
            if(whichBinary=='A')
               pixelValue = grayA.pixel(x, y);
            else
              pixelValue = grayB.pixel(x, y);
            int newval=adjust_value[qRed(pixelValue)];
            histequal.setPixel(x,y,qRgb(newval,newval,newval));
            histH[newval]++;
        }
    }
    QImage Adjust = histequal.scaled(ui->AdjustImage->width(),ui->AdjustImage->height(),Qt::KeepAspectRatio);
    ui->AdjustImage->setPixmap(QPixmap::fromImage(Adjust));
    PlotHist(histH,"Histogram Equalization");
}
void MainWindow::on_Contrast_clicked()
{
    QImage Gray3 = gray_contrast.scaled(ui->AdjustImage->width(),ui->AdjustImage->height(),Qt::KeepAspectRatio);
    ui->AdjustImage->setPixmap(QPixmap::fromImage(Gray3));
    PlotHist(histc, "Contrast");
}
void MainWindow::on_Brightness_valueChanged(int value)
{
    QImage brightness = QImage(cols,rows,QImage::Format_RGB32);
    for(int y =0;y<rows;y++)
    {
        for(int x=0;x<cols;x++)
        {
            QRgb pixelValue;
            switch (whichBinary){
            case'A':
               pixelValue = grayA.pixel(x, y);

               break;
            case'B':
               pixelValue = grayB.pixel(x, y);
               break;
            }
            int newValue = qRed(pixelValue)+value;
            if(newValue>255)
               newValue=255;
            else if(newValue<0)
               newValue=0;
            brightness.setPixel(x,y,qRgb(newValue,newValue,newValue));
        }
    }
    QImage Brightness = brightness.scaled(ui->AdjustImage->width(),ui->AdjustImage->height(),Qt::KeepAspectRatio);
    ui->AdjustImage->setPixmap(QPixmap::fromImage(Brightness));

    QString n =QString::fromStdString(std::to_string(value));
    ui->brightness->setText(n);
}


void MainWindow::on_ContrastSlider_valueChanged(int value)
{
    QImage contrast = QImage(cols,rows,QImage::Format_RGB32);
    for(int y =0;y<rows;y++)
    {
        for(int x=0;x<cols;x++)
        {
            QRgb pixelValue;
            switch (whichBinary){
            case'A':
               pixelValue = grayA.pixel(x, y);
               break;
            case'B':
               pixelValue = grayB.pixel(x, y);
               break;
            }
            int newValue = qRed(pixelValue)*(value/10);
            if(newValue>255)
               newValue=255;
            contrast.setPixel(x,y,qRgb(newValue,newValue,newValue));
        }
    }
    QImage Contrast = contrast.scaled(ui->AdjustImage->width(),ui->AdjustImage->height(),Qt::KeepAspectRatio);
    ui->AdjustImage->setPixmap(QPixmap::fromImage(Contrast));
    double v = double(value)/10;
    QString n =QString::fromStdString(std::to_string(v));
    ui->contrastvalue->setText(n);
}

void MainWindow::on_grayScale_clicked()
{
    int histg[256];
    for(int i =0;i<256;i++)
        histg[i]=0;
    int Imagemax=0;
    for(int i=255;i>=0;i--)
    {
        if(whichBinary=='A')
        {
            if (histA[i]!=0)
            {
               Imagemax=i;
                break;
            }
        }
        else
        {
            if (histB[i]!=0)
            {
                Imagemax=i;
                break;
            }
        }
    }
    graylevel = ui->grayLevel->toPlainText().toInt();
    QImage Grayscale = QImage(cols,rows,QImage::Format_RGB32);

    for(int y =0;y<rows;y++)
    {
        for(int x=0;x<cols;x++)
        {
            QRgb pixelValue;
            switch (whichBinary){
            case'A':
               pixelValue = grayA.pixel(x, y);
               break;
            case'B':
               pixelValue = grayB.pixel(x, y);
               break;
            }
            int newValue = int(graylevel*(qRed(pixelValue)+1))/(Imagemax+1);
            newValue*=((Imagemax+1)/graylevel);
            newValue-=1;
            histg[newValue]++;

            Grayscale.setPixel(x,y,qRgb(newValue,newValue,newValue));
        }
    }
    QImage Grayscaled = Grayscale.scaled(ui->AdjustImage->width(),ui->AdjustImage->height(),Qt::KeepAspectRatio);
    ui->AdjustImage->setPixmap(QPixmap::fromImage(Grayscaled));
    PlotHist(histg, "New Gray Level");

}
void MainWindow::on_Sizevalue_valueChanged(int arg1)
{
    SizeofImage=arg1;
}
void MainWindow::on_enlargebutton_clicked()
{
    int histE[256];
    for(int i=0;i<256;i++)
        histE[i]=0;
    QImage Rescaled = QImage(SizeofImage*cols,SizeofImage*rows, QImage::Format_RGB32);
    for(int y =0;y<rows;y++)
    {
        for(int x=0;x<cols;x++)
        {
            QRgb pixelValue;
            switch (whichBinary){
            case'A':
               pixelValue = grayA.pixel(x, y);
               break;
            case'B':
               pixelValue = grayB.pixel(x, y);
               break;
            }
            for(int i = 0;i<SizeofImage;i++){
               for(int j =0 ;j<SizeofImage;j++)
               {
                Rescaled.setPixel(x*SizeofImage+i,y*SizeofImage+j,pixelValue);
                histE[qRed(pixelValue)]++;
               }
            }
        }
    }
    QImage rescaled = Rescaled.scaled(ui->AdjustImage->width(),ui->AdjustImage->height(),Qt::KeepAspectRatio);
    ui->AdjustImage->setPixmap(QPixmap::fromImage(rescaled));
    cv::Mat MatEnlarge = QImage2Mat(Rescaled);
    cv::imshow("Enlarge Image", MatEnlarge);
    cv::waitKey(0);
    cv::destroyAllWindows();
    PlotHist(histE, "Enlarge");
}
void MainWindow::on_shrinkbutton_clicked()
{
    int histS[256];
    for(int i=0;i<256;i++)
        histS[i]=0;
    QImage Rescaled = QImage(cols/SizeofImage, rows/SizeofImage, QImage::Format_RGB32);
    for(int y =0;y<rows;y++)
    {
        for(int x=0;x<cols;x++)
        {
            QRgb pixelValue;
            switch (whichBinary){
            case'A':
               pixelValue = grayA.pixel(x, y);
               break;
            case'B':
               pixelValue = grayB.pixel(x, y);
               break;
            }
            if(x%SizeofImage==0&&y%SizeofImage==0)
            {
               Rescaled.setPixel(x/SizeofImage,y/SizeofImage,pixelValue);
               histS[qRed(pixelValue)]++;
            }

        }
    }
    QImage rescaled = Rescaled.scaled(ui->AdjustImage->width(),ui->AdjustImage->height(),Qt::KeepAspectRatio);
    ui->AdjustImage->setPixmap(QPixmap::fromImage(rescaled));
    PlotHist(histS, "Shrink");
}
cv::Mat MainWindow::QImage2Mat(const QImage& src) // from https://stackoverflow.com/questions/37385254/from-cvmat-to-qimage
{
    cv::Mat mat = cv::Mat(src.height(), src.width(), CV_8UC4, (uchar*)src.bits(), src.bytesPerLine());
    cv::Mat result = cv::Mat(mat.rows, mat.cols, CV_8UC3 );
    int from_to[] = { 0,0,  1,1,  2,2 };
    mixChannels( &mat, 1, &result, 1, from_to, 3 );
    return result;
}
