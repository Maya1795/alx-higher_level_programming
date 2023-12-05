#include <Python.h>

/**
 * print_python_list_info -print infor. about python
 *
 * @p: object list
 *
 */

void print_python_list_info(PyObject *p)
{
	int s, all, i;
	PyObject *o;

	s = Py_SIZE(p);
	all = ((PyListObject *)p)->allocated;
	printf("[*] Size of the Python List = %d\n", s);
	printf("[*] Allocated = %d\n", all);
	for (i = 0; i < s; i++)
	{
		printf("Element %d: ", i);
		o = PyList_GetItem(p, i);
		printf("%s\n", Py_TYPE(o)->tp_name);
	}
}
