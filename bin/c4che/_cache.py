AR = '/usr/bin/ar'
ARFLAGS = 'rcs'
BINDIR = '/usr/local/bin'
BOOST_VERSION = '1_65_1'
BOOST_VERSION_NUMBER = 106501
CC_VERSION = ('6', '0', '0')
CFLAGS = ['-fPIC', '-Wall', '-O2', '-pthread', '-DLOG_LEVEL=4']
CFLAGS_NDN_CXX = ['-pthread', '-pthread']
CFLAGS_PROTOBUF = ['-pthread', '-pthread']
COMPILER_CXX = 'g++'
CPPPATH_ST = '-I%s'
CXX = ['clang++']
CXXFLAGS = ['-fPIC', '-Wall', '-O2', '-pthread', '-DLOG_LEVEL=4', '-std=c++0x']
CXXFLAGS_MACBUNDLE = ['-fPIC']
CXXFLAGS_NDN_CXX = ['-pthread', '-pthread']
CXXFLAGS_PROTOBUF = ['-pthread', '-pthread']
CXXFLAGS_cxxshlib = ['-fPIC']
CXXLNK_SRC_F = []
CXXLNK_TGT_F = ['-o']
CXX_NAME = 'gcc'
CXX_SRC_F = []
CXX_TGT_F = ['-c', '-o']
DEFINES = ['HAVE_PROTOBUF=1', 'HAVE_YAML_CPP=1', 'HAVE_SQLITE3=1', 'HAVE_NDN_CXX=1']
DEFINES_ST = '-D%s'
DEST_BINFMT = 'elf'
DEST_CPU = 'x86_64'
DEST_OS = 'linux'
INCLUDEDIR = '/usr/include'
INCLUDES_BOOST = '/usr/include'
INCLUDES_NDN_CXX = ['/usr/local/include']
LIBDIR = '/usr/lib'
LIBPATH_BOOST = ['/usr/lib/x86_64-linux-gnu']
LIBPATH_NDN_CXX = ['/usr/local/lib']
LIBPATH_ST = '-L%s'
LIB_BOOST = ['boost_system', 'boost_filesystem', 'boost_date_time', 'boost_iostreams', 'boost_thread', 'boost_regex', 'boost_program_options', 'boost_chrono', 'boost_random']
LIB_NDN_CXX = ['ndn-cxx', 'boost_system', 'boost_filesystem', 'boost_date_time', 'boost_iostreams', 'boost_regex', 'boost_program_options', 'boost_chrono', 'boost_random', 'boost_thread', 'boost_log', 'boost_log_setup', 'cryptopp', 'ssl', 'crypto', 'sqlite3', 'rt', 'pthread']
LIB_PROTOBUF = ['protobuf', 'pthread']
LIB_SQLITE3 = ['sqlite3']
LIB_ST = '-l%s'
LIB_YAML-CPP = ['yaml-cpp']
LINKFLAGS = ['-fPIC']
LINKFLAGS_MACBUNDLE = ['-bundle', '-undefined', 'dynamic_lookup']
LINKFLAGS_NDN_CXX = ['-pthread', '-pthread']
LINKFLAGS_PROTOBUF = ['-pthread', '-pthread']
LINKFLAGS_cxxshlib = ['-shared']
LINKFLAGS_cxxstlib = ['-Wl,-Bstatic']
LINK_CXX = ['clang++']
PKGCONFIG = '/usr/bin/pkg-config'
PREFIX = '/usr'
PROTOC = '/usr/bin/protoc'
PROTOC_ST = '-I%s'
RPATH_ST = '-Wl,-rpath,%s'
SHLIB_MARKER = '-Wl,-Bdynamic'
SONAME_ST = '-Wl,-h,%s'
STLIBPATH_ST = '-L%s'
STLIB_MARKER = '-Wl,-Bstatic'
STLIB_ST = '-l%s'
cxxprogram_PATTERN = '%s'
cxxshlib_PATTERN = 'lib%s.so'
cxxstlib_PATTERN = 'lib%s.a'
define_key = ['HAVE_PROTOBUF', 'HAVE_YAML_CPP', 'HAVE_SQLITE3', 'HAVE_NDN_CXX']
macbundle_PATTERN = '%s.bundle'
