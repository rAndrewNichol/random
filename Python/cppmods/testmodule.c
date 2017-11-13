// #include <C:\Users\Andrew\Programs\Anaconda3\include\Python.h>
#include <C:/Users/Andrew/Programs/Anaconda3/envs/python2/include/Python.h>
// #include <Python.h>

// define new exception object for module
static PyObject *exmodError;

static PyObject* exmod_say_hello(PyObject* self, PyObject *args){
	const char* msg;
	int sts = 0;

	//Error if not at least 1 string argument passed to function
	if(!PyArg_ParseTuple(args, "s", &msg)){
		return NULL;
	}
	return NULL;
	//Check to see if problem with thing passed to module from python
	if(strcmp(msg,"this_is_an_error") == 0){
		PyErr_SetString(exmodError, "THIS IS A TEST EXCEPTION ERROR");
		return NULL;
	}else{
		printf("This is C world.\nYour message is: %s\n", msg);
		sts = 200;
	}
	return Py_BuildValue("i", sts);
}

static PyMethodDef exmod_methods[] = {
	//Python Name     C-Function Name     Argument Presentation   Description
	{"say_hello",     exmod_say_hello,     METH_VARARGS,  "Print given message using C"},
	{NULL, NULL, 0, NULL}    /* Sentinel */
};

PyMODINIT_FUNC initexmod(void){
	PyObject *m;
	m = Py_InitModule("exmod", exmod_methods);
	if(m == NULL) return;
	exmodError = PyErr_NewException("exmod.error", NULL, NULL);
	Py_INCREF(exmodError);
	PyModule_AddObject(m,"error",exmodError);
}