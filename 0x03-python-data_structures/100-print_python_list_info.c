#include <Python.h>
#include <stdio.h>
/**
 * print_python_list_info - check the code
 * @p: object
 * Return: Always 0.
 */
void print_python_list_info(PyObject *p)
{
int i;
PyListObject *list = (PyListObject *)p;
printf("[*] Size of the Python List = %ld\n", PyList_Size(p));
printf("[*] Allocated = %ld\n", list->allocated);
for (i = 0; i < PyList_Size(p); i++)
{
printf("Element %d: %s\n", i, list->ob_item[i]->ob_type->tp_name);
}
}
