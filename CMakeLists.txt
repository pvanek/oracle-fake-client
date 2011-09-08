cmake_minimum_required(VERSION 2.6)

project(oracle-fake-lib)

set(libname clntsh)

add_library(${libname} SHARED oracle-fake-lib.cpp)
set_target_properties ( ${libname} PROPERTIES VERSION 11 SOVERSION 11.1 )

