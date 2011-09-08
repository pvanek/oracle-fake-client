cmake_minimum_required(VERSION 2.6)

project(oracle-fake-client)

set(VERSIONMAJOR 11)
set(VERSIONMINOR 1)
set(VERSION ${VERSIONMAJOR}.${VERSIONMINOR})



# some system (rpm builds) setup LIB_SUFFIX for cmake. If there is no set, try to get it from system
IF (NOT LIB_SUFFIX)
        MESSAGE(STATUS "")
        MESSAGE(STATUS "LIB_SUFFIX variable is not defined. It will be autodetected now.")
        MESSAGE(STATUS "You can set it manually with -DLIB_SUFFIX=<value> (64 for example)")
    MESSAGE(STATUS "CMAKE_SIZEOF_VOID_P=${CMAKE_SIZEOF_VOID_P}")
        IF (NOT APPLE)
                # check 64 bit 
                IF (CMAKE_SIZEOF_VOID_P EQUAL 4)
                        SET (LIB_SUFFIX "")
                ELSE (CMAKE_SIZEOF_VOID_P EQUAL 4)
                        SET (LIB_SUFFIX "64")
                        MESSAGE(STATUS " LIB_SUFFIX is set to '${LIB_SUFFIX}'")
                ENDIF (CMAKE_SIZEOF_VOID_P EQUAL 4)
        ELSE (NOT APPLE)
                SET (LIB_SUFFIX "")
        ENDIF (NOT APPLE)
        # BSD does not use lib64 for 64bit libs
        IF (${CMAKE_SYSTEM_NAME} MATCHES ".*BSD")
                message(STATUS "LIB_SUFFIX is disabled for *BSD: ${CMAKE_SYSTEM_NAME}")
                SET (LIB_SUFFIX "")
        ENDIF()
        #
        MESSAGE(STATUS "")
ENDIF (NOT LIB_SUFFIX)



set(libname clntsh)

add_library(${libname} SHARED oracle-fake-lib.cpp)
set_target_properties ( ${libname} PROPERTIES VERSION ${VERSION} SOVERSION ${VERSIONMINOR} )

install(TARGETS ${libname} DESTINATION ${CMAKE_INSTALL_PREFIX}/lib${LIB_SUFFIX})




# packaging related stuff
string(TOLOWER ${CMAKE_PROJECT_NAME} CPACK_PACKAGE_NAME)
SET(CPACK_PACKAGE_VERSION "${VERSION}")
SET(CPACK_SOURCE_GENERATOR "TBZ2")
SET(CPACK_SOURCE_PACKAGE_FILE_NAME "${CPACK_PACKAGE_NAME}-${CPACK_PACKAGE_VERSION}")
SET(CPACK_IGNORE_FILES "/build/;/release/;/CVS/;/\\\\.git/;/\\\\.svn/;\\\\.swp$;\\\\.#;/#;\\\\.tar.gz$;/CMakeFiles/;CMakeCache.txt;refresh-copyright-and-license.pl")
SET(CPACK_SOURCE_IGNORE_FILES ${CPACK_IGNORE_FILES})
INCLUDE(CPack)
# simulate autotools' "make dist"
add_custom_target(dist COMMAND ${CMAKE_MAKE_PROGRAM} package_source)


