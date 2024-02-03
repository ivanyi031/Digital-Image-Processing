#include "mainwindow.h"
#include "ui_mainwindow.h"
#include<QFileDialog>
#include<QtCharts/QtCharts>
#include<string>
#include<stdio.h>
#include <cstdlib>
#include<iostream>
#include <QColorDialog>
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
cv::Mat image;
cv::Mat gray;
cv::Mat channel1,channel2,channel3;
int rows,cols;
int grows,gcols;
QImage QImgIn;
QImage QImgIng;
QImage Qcolorout;
QImage Fakecolor;
cv:: Mat Kdata;
cv:: Mat label;
cv::Mat centers(8, 1, CV_32FC1);
QColor color1,color2,color3;
using namespace std;
int MainWindow::checkvalue(double value)
{
    if(value>255)
        value=255;
    else if(value<0)
        value=0;
    return value;
}
double MainWindow::LAB_hq_func(double q)
{
    double output;
    if (q > 0.008856)
        output = pow(q, 1/3);
    else
        output = 7.787*q + 16/116;
    return output;
}
void MainWindow::pseudoColor(cv::Mat gray,int map[255][3])
{
    Fakecolor=QImage(gray.cols, gray.rows, QImage::Format_RGB32);
    for (int i = 0 ; i < gray.cols ; i++)
    {
        for (int j = 0 ; j < gray.rows ; j++)
        {
            int intensity = gray.at<cv::Vec3b>(j,i)[0];
            int red=map[intensity][2];
            int green = map[intensity][1];
            int blue = map[intensity][0];
            Fakecolor.setPixel(i, j, qRgb(red, green, blue));
        }
    }
    ui->pesudo->setPixmap(QPixmap::fromImage(Fakecolor.scaled(ui->pesudo->width(),ui->pesudo->height(),Qt::KeepAspectRatio)));
}
void MainWindow::on_selectfile_clicked()
{
    QString fileName = QFileDialog::getOpenFileName(this,
                                                    tr("Open Image"), ".",
                                                    tr("Image Files (*.png *.jpg *.jpeg *.bmp"));

    if(fileName != NULL)
    {
        image = cv::imread(fileName.toStdString().data());
        rows = image.rows;
        cols = image.cols;
        //cvtColor(image, image, 4 );  // 4 for original CV_BGR2RGB
        // Qt image
        QImgIn = QImage(cols, rows, QImage::Format_RGB32);
        for (int i = 0 ; i < cols ; i++)
        {
            for (int j = 0 ; j < rows ; j++)
            {
                int B = image.at<cv::Vec3b>(j,i)[0], G = image.at<cv::Vec3b>(j,i)[1], R = image.at<cv::Vec3b>(j,i)[2];
                QImgIn.setPixel(i, j, qRgb(R, G, B));

            }
        }
        ui->label->setPixmap(QPixmap::fromImage(QImgIn.scaled(ui->label->width(),ui->label->height(),Qt::KeepAspectRatio)));   // Scale
    }
}
void MainWindow::on_SelectFile2_clicked()
{
    QString fileName = QFileDialog::getOpenFileName(this,
                                                    tr("Open Image"), ".",
                                                    tr("Image Files (*.png *.jpg *.jpeg *.bmp"));

    if(fileName != NULL)
    {
        gray = cv::imread(fileName.toStdString().data());
        grows = gray.rows;
        gcols = gray.cols;
        //cvtColor(image, image, 4 );  // 4 for original CV_BGR2RGB
        // Qt image
        QImgIng = QImage(gcols, grows, QImage::Format_RGB32);
        for (int i = 0 ; i < gcols ; i++)
        {
            for (int j = 0 ; j < grows ; j++)
            {
                int B = gray.at<cv::Vec3b>(j,i)[0], G = gray.at<cv::Vec3b>(j,i)[1], R = gray.at<cv::Vec3b>(j,i)[2];
                QImgIng.setPixel(i, j, qRgb(R, G, B));

            }
        }
        ui->grayimage->setPixmap(QPixmap::fromImage(QImgIng.scaled(ui->label->width(),ui->label->height(),Qt::KeepAspectRatio)));   // Scale
    }
}

void MainWindow::on_RGB_clicked()
{
    label.release();
    centers.release();
    Kdata = cv::Mat(cols*rows*1, 3, CV_32F);
    for (int i = 0 ; i < rows ; i++)
        for (int j = 0 ; j < cols ; j++)
            for (int k = 0 ; k < 3 ; k++)
                Kdata.at<float>(i + j*rows, k) = image.at<cv::Vec3b>(i,j)[k];
    ui->coloroutput->setPixmap(QPixmap::fromImage(QImgIn.scaled(ui->coloroutput->width(),ui->coloroutput->height(),Qt::KeepAspectRatio)));
    QString Type ="RGB";
    ui->colortype->setText(Type);
}


void MainWindow::on_CMY_clicked()
{
    Kdata = cv::Mat(cols*rows*1, 3, CV_32F);
    label.release();
    centers.release();
    Qcolorout = QImage(cols, rows, QImage::Format_RGB32);
    for (int i = 0 ; i < rows ; i++)
    {
        for (int j = 0 ; j < cols ; j++)
        {
            double B = image.at<cv::Vec3b>(i,j)[0], G = image.at<cv::Vec3b>(i,j)[1], R = image.at<cv::Vec3b>(i,j)[2];
            double C = (255-R), M = (255-G), Y = (255-B);
            Qcolorout.setPixel(j, i, qRgb(C,M,Y));
            // Set Kdata for kmeans algorithm
            Kdata.at<float>(i + j*rows,0) = C;
            Kdata.at<float>(i + j*rows,1) = M;
            Kdata.at<float>(i + j*rows, 2) = Y;
        }
    }
    ui->coloroutput->setPixmap(QPixmap::fromImage(Qcolorout.scaled(ui->coloroutput->width(),ui->coloroutput->height(),Qt::KeepAspectRatio)));
    QString Type ="CMY";
    ui->colortype->setText(Type);
}


void MainWindow::on_HSI_clicked()
{
    Kdata = cv::Mat(cols*rows*1, 3, CV_32F);
    label.release();
    centers.release();

    // Set QImgOut
    Qcolorout = QImage(cols, rows, QImage::Format_RGB32);
    for (int i = 0 ; i < rows ; i++)
    {
        for (int j = 0 ; j < cols ; j++)
        {
            double B = image.at<cv::Vec3b>(i,j)[0], G = image.at<cv::Vec3b>(i,j)[1], R = image.at<cv::Vec3b>(i,j)[2];
            // theta, H, S, I
            double theta, H, S, I;
            theta = acos((0.5*((R-G)+(R-B))) / sqrt((R-G)*(R-G) + (R-B)*(G-B)));
            if (B <= G)
                H = theta;
            else
                H = 360.0 - theta;
            S = 1 - 3/(R+G+B)*min(min(R,G),B);
            I = (R + G + B)/3;
            Qcolorout.setPixel(j, i, qRgb(int(checkvalue(H)), int(checkvalue(S)), int(checkvalue(I))));

            // Set Kdata for kmeans algorithm
            Kdata.at<float>(i + j*rows, 0) = float(checkvalue(H));
            Kdata.at<float>(i + j*rows, 1) = float(checkvalue(S));
            Kdata.at<float>(i + j*rows, 2) = float(checkvalue(I));
        }
    }
    ui->coloroutput->setPixmap(QPixmap::fromImage(Qcolorout.scaled(ui->coloroutput->width(),ui->coloroutput->height(),Qt::KeepAspectRatio)));
    QString Type ="HSI";
    ui->colortype->setText(Type);
}



void MainWindow::on_XYZ_clicked()
{
    Kdata = cv::Mat(cols*rows*1, 3, CV_32F);
    label.release();
    centers.release();

    // Set QImgOut
    Qcolorout = QImage(cols, rows, QImage::Format_RGB32);
    for (int i = 0 ; i < rows ; i++)
    {
        for (int j = 0 ; j < cols ; j++)
        {
            double B = image.at<cv::Vec3b>(i,j)[0], G = image.at<cv::Vec3b>(i,j)[1], R = image.at<cv::Vec3b>(i,j)[2];
            //
            double X, Y, Z;
            X = 0.412453*R + 0.357580*G + 0.180423*B;
            Y = 0.212671*R + 0.715160*G + 0.072169*B;
            Z = 0.019334*R + 0.119193*G + 0.950227*B;
            Qcolorout.setPixel(j, i, qRgb(int(checkvalue(X)), int(checkvalue(Y)), int(checkvalue(Z))));
            // Set Kdata for kmeans algorithm
            Kdata.at<float>(i + j*rows, 0) = float(checkvalue(X));
            Kdata.at<float>(i + j*rows, 1) = float(checkvalue(Y));
            Kdata.at<float>(i + j*rows, 2) = float(checkvalue(Z));

        }
    }
    ui->coloroutput->setPixmap(QPixmap::fromImage(Qcolorout.scaled(ui->coloroutput->width(),ui->coloroutput->height(),Qt::KeepAspectRatio)));
    QString Type ="XYZ";
    ui->colortype->setText(Type);
}


void MainWindow::on_Lab_clicked()
{
    Kdata = cv::Mat(cols*rows*1, 3, CV_32F);
    label.release();
    centers.release();
    Qcolorout = QImage(cols, rows, QImage::Format_RGB32);
    for (int i = 0 ; i < rows ; i++)
    {
        for (int j = 0 ; j < cols ; j++)
        {
            double B = image.at<cv::Vec3b>(i,j)[0], G = image.at<cv::Vec3b>(i,j)[1], R = image.at<cv::Vec3b>(i,j)[2];

            // X, Y, Z
            double X, Y, Z;
            X = (0.412453*R + 0.357580*G + 0.180423*B)/255;
            Y = (0.212671*R + 0.715160*G + 0.072169*B)/255;
            Z = (0.019334*R + 0.119193*G + 0.950227*B)/255;

            // L, A, B (D65 Light Source)
            double L, A, B_;
            L  = 116*LAB_hq_func(Y/100)-16;
            A  = 500*(LAB_hq_func(X/95.21)-LAB_hq_func(Y/100));
            B_ = 200*(LAB_hq_func(Y/100)-LAB_hq_func(Z/99.60));
            Qcolorout.setPixel(j, i, qRgb(int(checkvalue(L*255)), int(checkvalue(A*255)), int(checkvalue(B_*255))));

            // Set Kdata for kmeans algorithm
            Kdata.at<float>(i + j*rows, 0) = float(checkvalue(B_*255));
            Kdata.at<float>(i + j*rows, 1) = float(checkvalue(A*255));
            Kdata.at<float>(i + j*rows, 2) = float(checkvalue(L*255));
        }
    }
    ui->coloroutput->setPixmap(QPixmap::fromImage(Qcolorout.scaled(ui->coloroutput->width(),ui->coloroutput->height(),Qt::KeepAspectRatio)));
    QString Type ="L*a*b";
    ui->colortype->setText(Type);
}


void MainWindow::on_YUV_clicked()
{
    Kdata = cv::Mat(cols*rows*1, 3, CV_32F);
    label.release();
    centers.release();
    Qcolorout = QImage(cols, rows, QImage::Format_RGB32);
    for (int i = 0 ; i < rows ; i++)
    {
        for (int j = 0 ; j < cols ; j++)
        {
            double B = image.at<cv::Vec3b>(i,j)[0], G = image.at<cv::Vec3b>(i,j)[1], R = image.at<cv::Vec3b>(i,j)[2];


            // X, Y, Z
            double Y, U, V;
            Y = R * 0.299 + G * 0.587 + B * 0.114;
            U = R * -0.169 + G * -0.332 + B * 0.500 + 128.0;
            V = R * 0.500 + G * -0.419 + B * -0.0813 + 128.0;
            Qcolorout.setPixel(j, i, qRgb(int(checkvalue(Y)), int(checkvalue(U)), int(checkvalue(V))));
            // Set Kdata for kmeans algorithm
            Kdata.at<float>(i + j*rows, 0) = float(checkvalue(Y));
            Kdata.at<float>(i + j*rows, 1) = float(checkvalue(U));
            Kdata.at<float>(i + j*rows, 2) = float(checkvalue(V));
        }
    }
    // Show Img and data
    ui->coloroutput->setPixmap(QPixmap::fromImage(Qcolorout.scaled(ui->coloroutput->width(),ui->coloroutput->height(),Qt::KeepAspectRatio)));
    QString Type ="YUV";
    ui->colortype->setText(Type);
}


void MainWindow::on_pushButton_clicked()
{
    cv::destroyAllWindows();
    int k = ui->Kmeancluster->toPlainText().toInt();
    cv::Mat kmeansResult = cv::Mat(image.size(), image.type());
    if (!Kdata.empty())
    {
        kmeans(Kdata, k, label, cv::TermCriteria(cv::TermCriteria::EPS+cv::TermCriteria::MAX_ITER, 10, 1), 10, cv::KMEANS_RANDOM_CENTERS, centers);
        // Set kmeansResult
        if (!label.empty() && !centers.empty())
        {
            for (int i = 0 ; i < rows ; i++)
            {
                for (int j = 0 ; j < cols ; j++)
                {
                    int index = label.at<int>(i + j*rows, 0);
                    for (int k = 0 ; k < 3 ; k++)
                        kmeansResult.at<cv::Vec3b>(i, j)[k] = centers.at<float>(index, k);
                }
            }
            // Show Img
            imshow("After K-means Algorithm", kmeansResult);
            cv::waitKey();
        }
        else
            cout << "label and center are empty" << endl;
    }
    else
        cout << "Kdata is empty" << endl;
}


void MainWindow::on_selectcolor1_clicked()
{
    color1 = QColorDialog::getColor();
    QVariant variant= color1;
    QString colcode = variant.toString();
    ui->color1->setStyleSheet("QLabel { background-color :"+colcode+" ; }");
}


void MainWindow::on_selectcolor2_clicked()
{
    color2 = QColorDialog::getColor();
    QVariant variant= color2;
    QString colcode = variant.toString();
    ui->color2->setStyleSheet("QLabel { background-color :"+colcode+" ;  }");
}


void MainWindow::on_selectcolor3_clicked()
{
    color3 = QColorDialog::getColor();
    QVariant variant= color3;
    QString colcode = variant.toString();
    ui->color3->setStyleSheet("QLabel { background-color :"+colcode+" ; }");
}



void MainWindow::on_colormap_clicked()
{
    int map[256][3];//BGR
    int colors1[]={color1.blue(),color1.green(),color1.red()};
    int colors2[]={color2.blue(),color2.green(),color2.red()};
    int colors3[]={color3.blue(),color3.green(),color3.red()};
    for(int i=0;i<3;i++)
    {
        map[0][i]=colors1[i];
        map[127][i]=colors2[i];
        map[255][i]=colors3[i];
    }
    for(int i=0;i<256;i++)
    {
        if(i==0||i==255||i==127)
            continue;
        for(int j=0;j<3;j++)
        {
            if(i<127)
                map[i][j]=((128-i)*map[0][j]+i*map[127][j])/128;
            else
                map[i][j]=((256-i)*map[127][j]+(i-128)*map[255][j])/128;
        }
    }
    pseudoColor(gray,map);
    QImage colorBar = QImage(1, 256, QImage::Format_RGB32);
    for(int i=0;i<256;i++)
    {
        colorBar.setPixelColor(0,255-i,qRgb(map[i][2], map[i][1], map[i][0]));
    }
   QSize laSize=ui->colorbar->size();
   QImage image1=colorBar.scaled(laSize,Qt::IgnoreAspectRatio);
   ui->colorbar->setPixmap(QPixmap::fromImage(image1));
}




