/****************************************************************************
** Meta object code from reading C++ file 'mainwindow.h'
**
** Created by: The Qt Meta Object Compiler version 67 (Qt 5.15.2)
**
** WARNING! All changes made in this file will be lost!
*****************************************************************************/

#include <memory>
#include "../mainwindow.h"
#include <QtCore/qbytearray.h>
#include <QtCore/qmetatype.h>
#if !defined(Q_MOC_OUTPUT_REVISION)
#error "The header file 'mainwindow.h' doesn't include <QObject>."
#elif Q_MOC_OUTPUT_REVISION != 67
#error "This file was generated using the moc from 5.15.2. It"
#error "cannot be used with the include files from this version of Qt."
#error "(The moc has changed too much.)"
#endif

QT_BEGIN_MOC_NAMESPACE
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
struct qt_meta_stringdata_MainWindow_t {
    QByteArrayData data[24];
    char stringdata0[382];
};
#define QT_MOC_LITERAL(idx, ofs, len) \
    Q_STATIC_BYTE_ARRAY_DATA_HEADER_INITIALIZER_WITH_OFFSET(len, \
    qptrdiff(offsetof(qt_meta_stringdata_MainWindow_t, stringdata0) + ofs \
        - idx * sizeof(QByteArrayData)) \
    )
static const qt_meta_stringdata_MainWindow_t qt_meta_stringdata_MainWindow = {
    {
QT_MOC_LITERAL(0, 0, 10), // "MainWindow"
QT_MOC_LITERAL(1, 11, 21), // "on_SelectFile_clicked"
QT_MOC_LITERAL(2, 33, 0), // ""
QT_MOC_LITERAL(3, 34, 18), // "on_selectA_clicked"
QT_MOC_LITERAL(4, 53, 18), // "on_selectB_clicked"
QT_MOC_LITERAL(5, 72, 30), // "on_verticalSlider_valueChanged"
QT_MOC_LITERAL(6, 103, 5), // "value"
QT_MOC_LITERAL(7, 109, 32), // "on_HistogramEqualization_clicked"
QT_MOC_LITERAL(8, 142, 19), // "on_Contrast_clicked"
QT_MOC_LITERAL(9, 162, 26), // "on_Brightness_valueChanged"
QT_MOC_LITERAL(10, 189, 30), // "on_ContrastSlider_valueChanged"
QT_MOC_LITERAL(11, 220, 20), // "on_grayScale_clicked"
QT_MOC_LITERAL(12, 241, 8), // "PlotHist"
QT_MOC_LITERAL(13, 250, 5), // "int[]"
QT_MOC_LITERAL(14, 256, 4), // "hist"
QT_MOC_LITERAL(15, 261, 11), // "std::string"
QT_MOC_LITERAL(16, 273, 5), // "title"
QT_MOC_LITERAL(17, 279, 25), // "on_Sizevalue_valueChanged"
QT_MOC_LITERAL(18, 305, 4), // "arg1"
QT_MOC_LITERAL(19, 310, 24), // "on_enlargebutton_clicked"
QT_MOC_LITERAL(20, 335, 23), // "on_shrinkbutton_clicked"
QT_MOC_LITERAL(21, 359, 10), // "QImage2Mat"
QT_MOC_LITERAL(22, 370, 7), // "cv::Mat"
QT_MOC_LITERAL(23, 378, 3) // "src"

    },
    "MainWindow\0on_SelectFile_clicked\0\0"
    "on_selectA_clicked\0on_selectB_clicked\0"
    "on_verticalSlider_valueChanged\0value\0"
    "on_HistogramEqualization_clicked\0"
    "on_Contrast_clicked\0on_Brightness_valueChanged\0"
    "on_ContrastSlider_valueChanged\0"
    "on_grayScale_clicked\0PlotHist\0int[]\0"
    "hist\0std::string\0title\0on_Sizevalue_valueChanged\0"
    "arg1\0on_enlargebutton_clicked\0"
    "on_shrinkbutton_clicked\0QImage2Mat\0"
    "cv::Mat\0src"
};
#undef QT_MOC_LITERAL

static const uint qt_meta_data_MainWindow[] = {

 // content:
       8,       // revision
       0,       // classname
       0,    0, // classinfo
      14,   14, // methods
       0,    0, // properties
       0,    0, // enums/sets
       0,    0, // constructors
       0,       // flags
       0,       // signalCount

 // slots: name, argc, parameters, tag, flags
       1,    0,   84,    2, 0x08 /* Private */,
       3,    0,   85,    2, 0x08 /* Private */,
       4,    0,   86,    2, 0x08 /* Private */,
       5,    1,   87,    2, 0x08 /* Private */,
       7,    0,   90,    2, 0x08 /* Private */,
       8,    0,   91,    2, 0x08 /* Private */,
       9,    1,   92,    2, 0x08 /* Private */,
      10,    1,   95,    2, 0x08 /* Private */,
      11,    0,   98,    2, 0x08 /* Private */,
      12,    2,   99,    2, 0x08 /* Private */,
      17,    1,  104,    2, 0x08 /* Private */,
      19,    0,  107,    2, 0x08 /* Private */,
      20,    0,  108,    2, 0x08 /* Private */,
      21,    1,  109,    2, 0x08 /* Private */,

 // slots: parameters
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void, QMetaType::Int,    6,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void, QMetaType::Int,    6,
    QMetaType::Void, QMetaType::Int,    6,
    QMetaType::Void,
    QMetaType::Void, 0x80000000 | 13, 0x80000000 | 15,   14,   16,
    QMetaType::Void, QMetaType::Int,   18,
    QMetaType::Void,
    QMetaType::Void,
    0x80000000 | 22, QMetaType::QImage,   23,

       0        // eod
};

void MainWindow::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    if (_c == QMetaObject::InvokeMetaMethod) {
        auto *_t = static_cast<MainWindow *>(_o);
        Q_UNUSED(_t)
        switch (_id) {
        case 0: _t->on_SelectFile_clicked(); break;
        case 1: _t->on_selectA_clicked(); break;
        case 2: _t->on_selectB_clicked(); break;
        case 3: _t->on_verticalSlider_valueChanged((*reinterpret_cast< int(*)>(_a[1]))); break;
        case 4: _t->on_HistogramEqualization_clicked(); break;
        case 5: _t->on_Contrast_clicked(); break;
        case 6: _t->on_Brightness_valueChanged((*reinterpret_cast< int(*)>(_a[1]))); break;
        case 7: _t->on_ContrastSlider_valueChanged((*reinterpret_cast< int(*)>(_a[1]))); break;
        case 8: _t->on_grayScale_clicked(); break;
        case 9: _t->PlotHist((*reinterpret_cast< int(*)[]>(_a[1])),(*reinterpret_cast< std::string(*)>(_a[2]))); break;
        case 10: _t->on_Sizevalue_valueChanged((*reinterpret_cast< int(*)>(_a[1]))); break;
        case 11: _t->on_enlargebutton_clicked(); break;
        case 12: _t->on_shrinkbutton_clicked(); break;
        case 13: { cv::Mat _r = _t->QImage2Mat((*reinterpret_cast< const QImage(*)>(_a[1])));
            if (_a[0]) *reinterpret_cast< cv::Mat*>(_a[0]) = std::move(_r); }  break;
        default: ;
        }
    }
}

QT_INIT_METAOBJECT const QMetaObject MainWindow::staticMetaObject = { {
    QMetaObject::SuperData::link<QMainWindow::staticMetaObject>(),
    qt_meta_stringdata_MainWindow.data,
    qt_meta_data_MainWindow,
    qt_static_metacall,
    nullptr,
    nullptr
} };


const QMetaObject *MainWindow::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *MainWindow::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_meta_stringdata_MainWindow.stringdata0))
        return static_cast<void*>(this);
    return QMainWindow::qt_metacast(_clname);
}

int MainWindow::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QMainWindow::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 14)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 14;
    } else if (_c == QMetaObject::RegisterMethodArgumentMetaType) {
        if (_id < 14)
            *reinterpret_cast<int*>(_a[0]) = -1;
        _id -= 14;
    }
    return _id;
}
QT_WARNING_POP
QT_END_MOC_NAMESPACE
